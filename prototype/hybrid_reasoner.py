"""
Hybrid Neuro-Symbolic Temporal Reasoner

Combines LLM-based extraction with symbolic Allen's Interval Algebra reasoning
to provide accurate, verifiable temporal reasoning with provenance tracking.
"""

from typing import Dict, List, Tuple, Optional, Set
from dataclasses import dataclass
import re
import json

from temporal_core import (
    AllenAlgebra, AllenRelation, TimeInterval,
    TemporalConstraintSolver, parse_relative_time
)
from llm_interface import MockLLM, ExtractionLevel, LLMResponse, TemporalEvent, TemporalRelation
from provenance import ProvenanceTracker, ReasoningStep


@dataclass
class HybridResult:
    """Result from hybrid reasoning combining LLM and symbolic outputs"""
    question: str
    llm_answer: str
    symbolic_answer: Optional[str]
    verified_answer: str
    confidence: float
    llm_confidence: float
    symbolic_confidence: float
    used_symbolic: bool
    conflicts_detected: List[str]
    explanation: str
    provenance_id: str


class HybridTemporalReasoner:
    """
    Main hybrid reasoning system that:
    1. Uses LLM to extract temporal information from natural language
    2. Converts to symbolic constraints (Allen's Interval Algebra)
    3. Verifies and solves using symbolic reasoner
    4. Resolves conflicts between LLM and symbolic reasoning
    5. Tracks full provenance for explainability
    """

    def __init__(self, llm_accuracy: str = "medium"):
        """
        Initialize hybrid reasoner.

        Args:
            llm_accuracy: "high", "medium", or "low" - affects LLM error rate
        """
        self.llm = MockLLM(accuracy_level=llm_accuracy)
        self.algebra = AllenAlgebra()
        self.provenance = ProvenanceTracker()
        self.task_counter = 0

    def reason(self, question: str, level: ExtractionLevel = None) -> HybridResult:
        """
        Main reasoning pipeline: LLM extraction -> Symbolic verification -> Answer

        Args:
            question: Natural language temporal reasoning question
            level: Target extraction level (auto-detected if None)

        Returns:
            HybridResult with answer and provenance
        """
        # Auto-detect level if not specified
        if level is None:
            level = self._detect_reasoning_level(question)

        # Generate unique task ID
        self.task_counter += 1
        task_id = f"task_{self.task_counter:04d}"

        # Start provenance tracking
        self.provenance.start_task(task_id, question)

        try:
            # Step 1: LLM Extraction
            llm_response = self._llm_extraction_step(question, level)

            # Step 2: Convert to symbolic representation
            solver, conversion_step_id = self._symbolic_conversion_step(llm_response)

            # Step 3: Symbolic reasoning and verification
            symbolic_result = self._symbolic_reasoning_step(solver, question, level)

            # Step 4: Compare and verify
            verified_answer, conflicts = self._verification_step(
                llm_response, symbolic_result, question, level
            )

            # Step 5: Generate final answer with confidence
            final_result = self._generate_final_answer(
                question, llm_response, symbolic_result,
                verified_answer, conflicts, task_id
            )

            # Complete provenance
            self.provenance.end_task(task_id, final_result.verified_answer, success=True)

            return final_result

        except Exception as e:
            # Record error in provenance
            error_msg = f"Error in reasoning: {str(e)}"
            self.provenance.end_task(task_id, "", success=False, error_message=error_msg)

            # Return error result
            return HybridResult(
                question=question,
                llm_answer="Error occurred",
                symbolic_answer=None,
                verified_answer=f"Could not determine answer: {error_msg}",
                confidence=0.0,
                llm_confidence=0.0,
                symbolic_confidence=0.0,
                used_symbolic=False,
                conflicts_detected=[error_msg],
                explanation=error_msg,
                provenance_id=task_id
            )

    def _detect_reasoning_level(self, question: str) -> ExtractionLevel:
        """Detect the required reasoning level from the question"""
        question_lower = question.lower()

        # Level 3: Calculations
        if any(word in question_lower for word in ["how long", "duration", "calculate", "total time"]):
            return ExtractionLevel.LEVEL_3_CALCULATION

        # Level 2: Ordering
        if any(word in question_lower for word in ["order", "sequence", "before", "after", "when"]):
            return ExtractionLevel.LEVEL_2_ORDERING

        # Level 1: Extraction
        return ExtractionLevel.LEVEL_1_EXTRACTION

    def _llm_extraction_step(self, question: str, level: ExtractionLevel) -> LLMResponse:
        """Step 1: Extract temporal information using LLM"""
        llm_response = self.llm.extract_temporal_info(question, level)

        # Record in provenance
        events_data = [
            {
                "name": e.name,
                "description": e.description,
                "start_time": e.start_time,
                "end_time": e.end_time,
                "duration": e.duration
            }
            for e in llm_response.events
        ]

        relations_data = [
            {
                "event1": r.event1,
                "event2": r.event2,
                "relation": r.relation,
                "confidence": r.confidence
            }
            for r in llm_response.relations
        ]

        self.provenance.record_llm_extraction(
            query=question,
            events=events_data,
            relations=relations_data,
            confidence=llm_response.metadata.get("confidence", 0.8) if llm_response.metadata else 0.8,
            metadata={
                "level": level.value,
                "raw_answer": llm_response.raw_answer
            }
        )

        return llm_response

    def _symbolic_conversion_step(self, llm_response: LLMResponse) -> Tuple[TemporalConstraintSolver, str]:
        """Step 2: Convert LLM output to symbolic constraints"""
        solver = TemporalConstraintSolver()

        # Add intervals
        for event in llm_response.events:
            interval = self._convert_event_to_interval(event)
            solver.add_interval(interval)

        # Add constraints
        for relation in llm_response.relations:
            allen_relation = self._convert_to_allen_relation(relation.relation)
            if allen_relation:
                solver.add_single_relation(relation.event1, relation.event2, allen_relation)

        # Record in provenance
        step_id = self.provenance.record_symbolic_constraint(
            constraint_desc=f"Converted {len(llm_response.relations)} LLM relations to Allen's algebra",
            constraint_data={
                "num_intervals": len(solver.intervals),
                "num_constraints": len(solver.constraints)
            },
            confidence=1.0
        )

        return solver, step_id

    def _symbolic_reasoning_step(self, solver: TemporalConstraintSolver,
                                 question: str, level: ExtractionLevel) -> Dict:
        """Step 3: Perform symbolic reasoning"""
        # Check consistency
        is_consistent = solver.propagate_constraints()

        # Compute interval values if possible
        if is_consistent:
            intervals = solver.compute_interval_values()
        else:
            intervals = solver.intervals

        # Build result
        result = {
            "consistent": is_consistent,
            "intervals": {name: {
                "start": i.start,
                "end": i.end,
                "duration": i.duration
            } for name, i in intervals.items()},
            "answer": self._compute_symbolic_answer(solver, question, level, is_consistent)
        }

        # Record in provenance
        self.provenance.record_symbolic_solving(
            problem_desc=f"Symbolic temporal reasoning (level {level.value})",
            solution=result,
            success=is_consistent
        )

        return result

    def _verification_step(self, llm_response: LLMResponse, symbolic_result: Dict,
                          question: str, level: ExtractionLevel) -> Tuple[str, List[str]]:
        """Step 4: Verify LLM answer against symbolic reasoning"""
        conflicts = []

        # Check for inconsistencies
        if not symbolic_result["consistent"]:
            conflicts.append("Symbolic constraints are inconsistent - LLM may have extracted conflicting information")

        # Check if LLM answer aligns with symbolic result
        llm_answer = llm_response.raw_answer
        symbolic_answer = symbolic_result["answer"]

        # Simple verification: check if key numbers match
        llm_numbers = set(re.findall(r'\d+', llm_answer))
        symbolic_numbers = set(re.findall(r'\d+', symbolic_answer))

        if llm_numbers and symbolic_numbers and llm_numbers != symbolic_numbers:
            conflicts.append(f"Numerical mismatch: LLM found {llm_numbers}, symbolic found {symbolic_numbers}")

        # Record verification
        verified = len(conflicts) == 0
        self.provenance.record_verification(
            verification_desc="Compare LLM and symbolic answers",
            verified=verified,
            details={
                "llm_answer": llm_answer,
                "symbolic_answer": symbolic_answer,
                "conflicts": conflicts
            }
        )

        # Determine verified answer
        if verified:
            verified_answer = symbolic_answer if symbolic_result["consistent"] else llm_answer
        else:
            # Prefer symbolic if consistent
            if symbolic_result["consistent"]:
                verified_answer = symbolic_answer
                self.provenance.record_conflict_resolution(
                    conflict_desc="Resolved using symbolic reasoning (more reliable)",
                    resolution={"chosen": "symbolic", "reason": "Symbolic constraints are consistent"}
                )
            else:
                verified_answer = llm_answer
                self.provenance.record_conflict_resolution(
                    conflict_desc="Using LLM answer (symbolic inconsistent)",
                    resolution={"chosen": "llm", "reason": "Symbolic constraints inconsistent"}
                )

        return verified_answer, conflicts

    def _generate_final_answer(self, question: str, llm_response: LLMResponse,
                               symbolic_result: Dict, verified_answer: str,
                               conflicts: List[str], task_id: str) -> HybridResult:
        """Step 5: Generate final result with confidence scores"""
        # Calculate confidence scores
        llm_confidence = llm_response.metadata.get("confidence", 0.8) if llm_response.metadata else 0.8
        symbolic_confidence = 1.0 if symbolic_result["consistent"] else 0.5

        # Overall confidence
        if len(conflicts) == 0 and symbolic_result["consistent"]:
            overall_confidence = max(llm_confidence, symbolic_confidence)
        elif symbolic_result["consistent"]:
            overall_confidence = symbolic_confidence
        else:
            overall_confidence = llm_confidence * 0.7  # Penalize if no symbolic verification

        # Determine if symbolic reasoning was used
        used_symbolic = symbolic_result["consistent"]

        # Generate explanation
        explanation = self.provenance.generate_explanation(task_id)

        return HybridResult(
            question=question,
            llm_answer=llm_response.raw_answer,
            symbolic_answer=symbolic_result["answer"],
            verified_answer=verified_answer,
            confidence=overall_confidence,
            llm_confidence=llm_confidence,
            symbolic_confidence=symbolic_confidence,
            used_symbolic=used_symbolic,
            conflicts_detected=conflicts,
            explanation=explanation,
            provenance_id=task_id
        )

    def _convert_event_to_interval(self, event: TemporalEvent) -> TimeInterval:
        """Convert LLM-extracted event to TimeInterval"""
        # Try to parse time values
        start = self._parse_time_value(event.start_time) if event.start_time else None
        end = self._parse_time_value(event.end_time) if event.end_time else None
        duration = self._parse_duration(event.duration) if event.duration else None

        return TimeInterval(
            name=event.name,
            start=start,
            end=end,
            duration=duration
        )

    def _parse_time_value(self, time_str: str) -> Optional[float]:
        """Parse time value from string"""
        if not time_str:
            return None

        # Try to extract number
        numbers = re.findall(r'\d+(?:\.\d+)?', time_str)
        if numbers:
            return float(numbers[0])

        # Try day names (map to simple values)
        days = {
            "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
            "friday": 4, "saturday": 5, "sunday": 6
        }
        for day, value in days.items():
            if day in time_str.lower():
                return float(value)

        return None

    def _parse_duration(self, duration_str: str) -> Optional[float]:
        """Parse duration from string (in seconds)"""
        if not duration_str:
            return None

        # Extract number and unit
        match = re.search(r'(\d+(?:\.\d+)?)\s*(hour|minute|day|week|second)s?', duration_str.lower())
        if match:
            value, unit = match.groups()
            value = float(value)

            # Convert to seconds
            conversions = {
                "second": 1,
                "minute": 60,
                "hour": 3600,
                "day": 86400,
                "week": 604800
            }
            return value * conversions.get(unit, 1)

        # Try to extract just a number (assume hours)
        numbers = re.findall(r'\d+(?:\.\d+)?', duration_str)
        if numbers:
            return float(numbers[0]) * 3600  # Assume hours

        return None

    def _convert_to_allen_relation(self, relation_str: str) -> Optional[AllenRelation]:
        """Convert LLM relation string to Allen relation"""
        relation_str = relation_str.lower().strip()

        mapping = {
            "before": AllenRelation.BEFORE,
            "after": AllenRelation.AFTER,
            "meets": AllenRelation.MEETS,
            "met-by": AllenRelation.MET_BY,
            "met_by": AllenRelation.MET_BY,
            "overlaps": AllenRelation.OVERLAPS,
            "overlapped-by": AllenRelation.OVERLAPPED_BY,
            "overlapped_by": AllenRelation.OVERLAPPED_BY,
            "during": AllenRelation.DURING,
            "contains": AllenRelation.CONTAINS,
            "starts": AllenRelation.STARTS,
            "started-by": AllenRelation.STARTED_BY,
            "started_by": AllenRelation.STARTED_BY,
            "finishes": AllenRelation.FINISHES,
            "finished-by": AllenRelation.FINISHED_BY,
            "finished_by": AllenRelation.FINISHED_BY,
            "equals": AllenRelation.EQUALS,
        }

        return mapping.get(relation_str)

    def _compute_symbolic_answer(self, solver: TemporalConstraintSolver,
                                 question: str, level: ExtractionLevel,
                                 is_consistent: bool) -> str:
        """Generate natural language answer from symbolic reasoning result"""
        if not is_consistent:
            return "The temporal constraints are inconsistent."

        question_lower = question.lower()

        # For duration questions
        if "how long" in question_lower or "duration" in question_lower:
            # Find the relevant interval
            for name, interval in solver.intervals.items():
                if interval.duration is not None:
                    hours = interval.duration / 3600
                    if hours < 1:
                        minutes = interval.duration / 60
                        return f"The duration is {minutes:.0f} minutes."
                    elif hours < 24:
                        return f"The duration is {hours:.1f} hours."
                    else:
                        days = hours / 24
                        return f"The duration is {days:.1f} days."

        # For ordering questions
        if "order" in question_lower or "sequence" in question_lower:
            intervals = list(solver.intervals.keys())
            return f"The temporal sequence involves: {', '.join(intervals)}."

        # For when questions
        if "when" in question_lower:
            for name, interval in solver.intervals.items():
                if interval.start is not None:
                    return f"{name} starts at time {interval.start}."

        # Default
        return "Symbolic reasoning completed successfully."

    def compare_with_pure_llm(self, question: str) -> Dict:
        """
        Compare hybrid approach with pure LLM approach.
        Returns comparison metrics.
        """
        # Get hybrid result
        hybrid_result = self.reason(question)

        # Get pure LLM result
        pure_llm_answer = self.llm.query(question)

        # Compare
        comparison = {
            "question": question,
            "pure_llm_answer": pure_llm_answer,
            "hybrid_answer": hybrid_result.verified_answer,
            "hybrid_confidence": hybrid_result.confidence,
            "used_symbolic_verification": hybrid_result.used_symbolic,
            "conflicts_found": len(hybrid_result.conflicts_detected),
            "improvement": "Yes" if hybrid_result.used_symbolic else "No verification available"
        }

        return comparison


if __name__ == "__main__":
    # Example usage
    print("=" * 80)
    print("Hybrid Neuro-Symbolic Temporal Reasoner - Example")
    print("=" * 80)

    reasoner = HybridTemporalReasoner(llm_accuracy="medium")

    # Test case 1: Medical timeline
    print("\nTest 1: Medical Timeline")
    print("-" * 80)
    question1 = "A patient was admitted to the hospital on Monday, underwent surgery on Tuesday, and was discharged on Friday. How long was the hospital stay?"

    result1 = reasoner.reason(question1)
    print(f"Question: {question1}")
    print(f"\nLLM Answer: {result1.llm_answer}")
    print(f"Symbolic Answer: {result1.symbolic_answer}")
    print(f"Verified Answer: {result1.verified_answer}")
    print(f"Confidence: {result1.confidence:.2f}")
    print(f"Used Symbolic: {result1.used_symbolic}")
    if result1.conflicts_detected:
        print(f"Conflicts: {result1.conflicts_detected}")

    # Test case 2: Event ordering
    print("\n\nTest 2: Event Ordering")
    print("-" * 80)
    question2 = "First, the team prepared the presentation. Then, they held the meeting. Finally, they sent the follow-up email. What is the order of events?"

    result2 = reasoner.reason(question2)
    print(f"Question: {question2}")
    print(f"\nLLM Answer: {result2.llm_answer}")
    print(f"Symbolic Answer: {result2.symbolic_answer}")
    print(f"Verified Answer: {result2.verified_answer}")
    print(f"Confidence: {result2.confidence:.2f}")

    # Test case 3: Comparison with pure LLM
    print("\n\nTest 3: Comparison with Pure LLM")
    print("-" * 80)
    question3 = "The meeting lasted 2 hours, followed by a 30 minute break, then a 1 hour workshop. What was the total time?"

    comparison = reasoner.compare_with_pure_llm(question3)
    print(f"Question: {comparison['question']}")
    print(f"\nPure LLM Answer: {comparison['pure_llm_answer']}")
    print(f"Hybrid Answer: {comparison['hybrid_answer']}")
    print(f"Hybrid Confidence: {comparison['hybrid_confidence']:.2f}")
    print(f"Improvement: {comparison['improvement']}")

    print("\n" + "=" * 80)
