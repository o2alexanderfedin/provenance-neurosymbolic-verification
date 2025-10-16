"""
Mock LLM Interface for Temporal Reasoning

Simulates LLM behavior for extracting temporal information from natural language.
Provides realistic responses with intentional errors to demonstrate hybrid system benefits.
"""

import json
import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class ExtractionLevel(Enum):
    """Levels of temporal reasoning complexity"""
    LEVEL_1_EXTRACTION = 1  # Extract events and basic temporal info
    LEVEL_2_ORDERING = 2    # Order events temporally
    LEVEL_3_CALCULATION = 3  # Calculate durations and specific times


@dataclass
class TemporalEvent:
    """Represents an event extracted by the LLM"""
    name: str
    description: str
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    duration: Optional[str] = None
    absolute_time: Optional[str] = None


@dataclass
class TemporalRelation:
    """Represents a temporal relation between events"""
    event1: str
    event2: str
    relation: str
    confidence: float = 1.0


@dataclass
class LLMResponse:
    """Response from LLM with extracted temporal information"""
    events: List[TemporalEvent]
    relations: List[TemporalRelation]
    raw_answer: str
    extraction_level: ExtractionLevel
    metadata: Dict = None

    def to_dict(self):
        return {
            "events": [asdict(e) for e in self.events],
            "relations": [asdict(r) for r in self.relations],
            "raw_answer": self.raw_answer,
            "extraction_level": self.extraction_level.value,
            "metadata": self.metadata or {}
        }


class MockLLM:
    """
    Mock LLM that simulates temporal reasoning capabilities.
    Includes realistic patterns of success and failure for different complexity levels.
    """

    def __init__(self, accuracy_level: str = "medium"):
        """
        Initialize mock LLM with different accuracy levels.

        Args:
            accuracy_level: "high", "medium", or "low" - affects error rate
        """
        self.accuracy_level = accuracy_level
        self.error_rates = {
            "high": 0.1,
            "medium": 0.3,
            "low": 0.5
        }
        self.current_error_rate = self.error_rates.get(accuracy_level, 0.3)

        # Pre-defined responses for common temporal reasoning problems
        self.response_templates = self._initialize_templates()

    def _initialize_templates(self) -> Dict[str, dict]:
        """Initialize response templates for common problem types"""
        return {
            "medical_timeline": {
                "pattern": r"patient.*admitted.*discharged|surgery.*recovery|medication.*treatment",
                "handler": self._handle_medical_timeline
            },
            "project_schedule": {
                "pattern": r"project.*deadline|task.*complete|meeting.*scheduled",
                "handler": self._handle_project_schedule
            },
            "event_sequence": {
                "pattern": r"first.*then.*finally|after.*before.*during",
                "handler": self._handle_event_sequence
            },
            "duration_calculation": {
                "pattern": r"how long|duration|lasted.*hours|took.*minutes",
                "handler": self._handle_duration_calculation
            },
            "time_overlap": {
                "pattern": r"overlap|simultaneously|at the same time|concurrent",
                "handler": self._handle_time_overlap
            }
        }

    def extract_temporal_info(self, text: str, level: ExtractionLevel = ExtractionLevel.LEVEL_1_EXTRACTION) -> LLMResponse:
        """
        Extract temporal information from natural language text.

        Args:
            text: Input natural language text
            level: Target extraction level

        Returns:
            LLMResponse with extracted events and relations
        """
        text_lower = text.lower()

        # Find matching template
        for template_name, template_info in self.response_templates.items():
            if re.search(template_info["pattern"], text_lower):
                return template_info["handler"](text, level)

        # Default handler for unknown patterns
        return self._handle_generic(text, level)

    def _handle_medical_timeline(self, text: str, level: ExtractionLevel) -> LLMResponse:
        """Handle medical timeline problems"""
        events = []
        relations = []

        # Extract events using simple pattern matching (simulating LLM)
        if "admitted" in text.lower():
            events.append(TemporalEvent(
                name="admission",
                description="Patient admitted to hospital"
            ))

        if "surgery" in text.lower():
            events.append(TemporalEvent(
                name="surgery",
                description="Surgical procedure"
            ))

        if "discharged" in text.lower():
            events.append(TemporalEvent(
                name="discharge",
                description="Patient discharged"
            ))

        if "medication" in text.lower() or "treatment" in text.lower():
            events.append(TemporalEvent(
                name="treatment",
                description="Medical treatment"
            ))

        # Extract relations
        if len(events) >= 2:
            # Typical medical timeline: admission -> surgery -> discharge
            if any(e.name == "admission" for e in events) and any(e.name == "surgery" for e in events):
                relations.append(TemporalRelation("admission", "surgery", "before", 0.9))

            if any(e.name == "surgery" for e in events) and any(e.name == "discharge" for e in events):
                relations.append(TemporalRelation("surgery", "discharge", "before", 0.9))

        # Simulate LLM reasoning for answer
        raw_answer = self._generate_medical_answer(text, events, relations, level)

        return LLMResponse(
            events=events,
            relations=relations,
            raw_answer=raw_answer,
            extraction_level=level,
            metadata={"domain": "medical", "confidence": 0.85}
        )

    def _handle_project_schedule(self, text: str, level: ExtractionLevel) -> LLMResponse:
        """Handle project scheduling problems"""
        events = []
        relations = []

        # Extract tasks and meetings
        task_pattern = r"(task|meeting|milestone|deadline)\s+(\w+)"
        matches = re.finditer(task_pattern, text.lower())

        for match in matches:
            event_type, event_name = match.groups()
            events.append(TemporalEvent(
                name=event_name,
                description=f"{event_type} {event_name}"
            ))

        # Look for temporal keywords
        if "before" in text.lower():
            words = text.lower().split()
            before_idx = [i for i, w in enumerate(words) if w == "before"]
            for idx in before_idx:
                if idx > 0 and idx < len(words) - 1:
                    # Simple extraction (not perfect, simulating LLM limitations)
                    relations.append(TemporalRelation(
                        words[idx-1], words[idx+1], "before", 0.7
                    ))

        raw_answer = self._generate_project_answer(text, events, relations, level)

        return LLMResponse(
            events=events,
            relations=relations,
            raw_answer=raw_answer,
            extraction_level=level,
            metadata={"domain": "project_management", "confidence": 0.80}
        )

    def _handle_event_sequence(self, text: str, level: ExtractionLevel) -> LLMResponse:
        """Handle general event sequence problems"""
        events = []
        relations = []

        # Extract events from common patterns
        # Pattern: "First X, then Y, finally Z"
        first_pattern = r"first[,\s]+([^,\.]+)"
        then_pattern = r"then[,\s]+([^,\.]+)"
        finally_pattern = r"finally[,\s]+([^,\.]+)"

        first_match = re.search(first_pattern, text.lower())
        then_match = re.search(then_pattern, text.lower())
        finally_match = re.search(finally_pattern, text.lower())

        event_names = []
        if first_match:
            event_name = first_match.group(1).strip()
            events.append(TemporalEvent(name="event_1", description=event_name))
            event_names.append("event_1")

        if then_match:
            event_name = then_match.group(1).strip()
            events.append(TemporalEvent(name="event_2", description=event_name))
            event_names.append("event_2")

        if finally_match:
            event_name = finally_match.group(1).strip()
            events.append(TemporalEvent(name="event_3", description=event_name))
            event_names.append("event_3")

        # Create sequential relations
        for i in range(len(event_names) - 1):
            relations.append(TemporalRelation(
                event_names[i], event_names[i+1], "before", 0.95
            ))

        raw_answer = self._generate_sequence_answer(text, events, relations, level)

        return LLMResponse(
            events=events,
            relations=relations,
            raw_answer=raw_answer,
            extraction_level=level,
            metadata={"domain": "general", "confidence": 0.90}
        )

    def _handle_duration_calculation(self, text: str, level: ExtractionLevel) -> LLMResponse:
        """Handle duration calculation problems (often has errors in pure LLM)"""
        events = []
        relations = []

        # Extract time values
        time_pattern = r"(\d+)\s*(hour|minute|day|week|month)s?"
        time_matches = re.finditer(time_pattern, text.lower())

        durations = []
        for match in time_matches:
            value, unit = match.groups()
            durations.append(f"{value} {unit}s")

        # Simulate LLM attempting calculation (with potential errors at higher levels)
        if level == ExtractionLevel.LEVEL_3_CALCULATION:
            # LLM might make arithmetic errors
            if self._should_introduce_error():
                raw_answer = "Based on the timeline, the total duration is approximately 15 hours."  # Intentional error
                metadata = {"confidence": 0.6, "calculation_attempted": True, "likely_error": True}
            else:
                raw_answer = "The total duration is 12 hours."
                metadata = {"confidence": 0.85, "calculation_attempted": True}
        else:
            raw_answer = f"The events involve durations of {', '.join(durations)}."
            metadata = {"confidence": 0.90, "calculation_attempted": False}

        # Extract basic events
        events.append(TemporalEvent(name="event_main", description="Main event", duration=durations[0] if durations else None))

        return LLMResponse(
            events=events,
            relations=relations,
            raw_answer=raw_answer,
            extraction_level=level,
            metadata=metadata
        )

    def _handle_time_overlap(self, text: str, level: ExtractionLevel) -> LLMResponse:
        """Handle temporal overlap problems"""
        events = []
        relations = []

        # Extract events
        event_pattern = r"([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)"
        matches = re.finditer(event_pattern, text)

        for i, match in enumerate(matches):
            event_name = match.group(1).lower().replace(" ", "_")
            events.append(TemporalEvent(
                name=f"event_{i+1}",
                description=event_name
            ))

        # Look for overlap indicators
        if "overlap" in text.lower() or "simultaneously" in text.lower():
            if len(events) >= 2:
                relations.append(TemporalRelation(
                    events[0].name, events[1].name, "overlaps", 0.85
                ))

        raw_answer = self._generate_overlap_answer(text, events, relations, level)

        return LLMResponse(
            events=events,
            relations=relations,
            raw_answer=raw_answer,
            extraction_level=level,
            metadata={"domain": "temporal_overlap", "confidence": 0.75}
        )

    def _handle_generic(self, text: str, level: ExtractionLevel) -> LLMResponse:
        """Generic handler for unrecognized patterns"""
        events = [
            TemporalEvent(name="event_unknown", description="Extracted event from text")
        ]
        relations = []
        raw_answer = "I identified a temporal event in the text, but need more context for detailed analysis."

        return LLMResponse(
            events=events,
            relations=relations,
            raw_answer=raw_answer,
            extraction_level=level,
            metadata={"domain": "unknown", "confidence": 0.5}
        )

    def _should_introduce_error(self) -> bool:
        """Determine if an error should be introduced based on accuracy level"""
        import random
        return random.random() < self.current_error_rate

    def _generate_medical_answer(self, text: str, events: List[TemporalEvent],
                                 relations: List[TemporalRelation], level: ExtractionLevel) -> str:
        """Generate natural language answer for medical problems"""
        if level == ExtractionLevel.LEVEL_1_EXTRACTION:
            event_names = [e.name for e in events]
            return f"I identified the following medical events: {', '.join(event_names)}."
        elif level == ExtractionLevel.LEVEL_2_ORDERING:
            if relations:
                rel_strs = [f"{r.event1} {r.relation} {r.event2}" for r in relations]
                return f"The temporal sequence is: {', '.join(rel_strs)}."
            return "I identified medical events but the ordering is unclear."
        else:  # LEVEL_3_CALCULATION
            return "Based on the medical timeline, I estimate the total hospital stay was approximately 5 days."

    def _generate_project_answer(self, text: str, events: List[TemporalEvent],
                                 relations: List[TemporalRelation], level: ExtractionLevel) -> str:
        """Generate natural language answer for project problems"""
        if level == ExtractionLevel.LEVEL_1_EXTRACTION:
            return f"I found {len(events)} project-related events."
        elif level == ExtractionLevel.LEVEL_2_ORDERING:
            return "The tasks should be completed in the order specified by their dependencies."
        else:
            return "The project timeline spans approximately 3 weeks."

    def _generate_sequence_answer(self, text: str, events: List[TemporalEvent],
                                  relations: List[TemporalRelation], level: ExtractionLevel) -> str:
        """Generate natural language answer for sequence problems"""
        if events:
            event_list = [e.description for e in events]
            return f"The sequence of events is: {' -> '.join(event_list)}."
        return "The event sequence follows the order described in the text."

    def _generate_overlap_answer(self, text: str, events: List[TemporalEvent],
                                 relations: List[TemporalRelation], level: ExtractionLevel) -> str:
        """Generate natural language answer for overlap problems"""
        if relations and relations[0].relation == "overlaps":
            return f"Events {relations[0].event1} and {relations[0].event2} occur simultaneously or overlap in time."
        return "The events have some temporal relationship."

    def query(self, question: str) -> str:
        """
        Simple question-answering interface.

        Args:
            question: Natural language question

        Returns:
            Natural language answer
        """
        # Determine extraction level from question
        if "how long" in question.lower() or "duration" in question.lower():
            level = ExtractionLevel.LEVEL_3_CALCULATION
        elif "order" in question.lower() or "sequence" in question.lower():
            level = ExtractionLevel.LEVEL_2_ORDERING
        else:
            level = ExtractionLevel.LEVEL_1_EXTRACTION

        response = self.extract_temporal_info(question, level)
        return response.raw_answer


if __name__ == "__main__":
    # Test the mock LLM
    print("=" * 60)
    print("Mock LLM Interface - Test Cases")
    print("=" * 60)

    llm = MockLLM(accuracy_level="medium")

    # Test Case 1: Medical timeline
    print("\n1. Medical Timeline:")
    print("-" * 60)
    medical_text = "The patient was admitted on Monday, underwent surgery on Tuesday, and was discharged on Friday."
    response = llm.extract_temporal_info(medical_text, ExtractionLevel.LEVEL_2_ORDERING)
    print(f"Input: {medical_text}")
    print(f"Events: {[e.name for e in response.events]}")
    print(f"Relations: {[(r.event1, r.relation, r.event2) for r in response.relations]}")
    print(f"Answer: {response.raw_answer}")

    # Test Case 2: Project schedule
    print("\n2. Project Schedule:")
    print("-" * 60)
    project_text = "Task A must be completed before Task B. Task B should finish before the deadline."
    response = llm.extract_temporal_info(project_text, ExtractionLevel.LEVEL_2_ORDERING)
    print(f"Input: {project_text}")
    print(f"Events: {[e.name for e in response.events]}")
    print(f"Relations: {[(r.event1, r.relation, r.event2) for r in response.relations]}")
    print(f"Answer: {response.raw_answer}")

    # Test Case 3: Duration calculation
    print("\n3. Duration Calculation:")
    print("-" * 60)
    duration_text = "The meeting lasted 2 hours, followed by a 30 minute break, then a 1 hour workshop."
    response = llm.extract_temporal_info(duration_text, ExtractionLevel.LEVEL_3_CALCULATION)
    print(f"Input: {duration_text}")
    print(f"Answer: {response.raw_answer}")
    print(f"Metadata: {response.metadata}")

    # Test Case 4: Event sequence
    print("\n4. Event Sequence:")
    print("-" * 60)
    sequence_text = "First, we prepared the materials. Then, we conducted the experiment. Finally, we analyzed the results."
    response = llm.extract_temporal_info(sequence_text, ExtractionLevel.LEVEL_2_ORDERING)
    print(f"Input: {sequence_text}")
    print(f"Events: {[(e.name, e.description) for e in response.events]}")
    print(f"Relations: {[(r.event1, r.relation, r.event2) for r in response.relations]}")
    print(f"Answer: {response.raw_answer}")

    print("\n" + "=" * 60)
