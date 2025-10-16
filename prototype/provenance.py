"""
Provenance Tracking System for Hybrid Neuro-Symbolic Reasoning

Tracks the reasoning chain from LLM extraction through symbolic processing
to final answer, enabling transparent explanations and debugging.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Any, Optional
from enum import Enum
from datetime import datetime
import json


class ReasoningStep(Enum):
    """Types of reasoning steps in the hybrid system"""
    LLM_EXTRACTION = "llm_extraction"
    LLM_INFERENCE = "llm_inference"
    SYMBOLIC_CONSTRAINT = "symbolic_constraint"
    SYMBOLIC_PROPAGATION = "symbolic_propagation"
    SYMBOLIC_SOLVING = "symbolic_solving"
    VERIFICATION = "verification"
    CONFLICT_RESOLUTION = "conflict_resolution"
    FINAL_ANSWER = "final_answer"


@dataclass
class ProvenanceNode:
    """A single node in the provenance graph representing one reasoning step"""
    step_id: str
    step_type: ReasoningStep
    timestamp: str
    description: str
    input_data: Dict[str, Any]
    output_data: Dict[str, Any]
    confidence: float = 1.0
    parent_ids: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization"""
        return {
            "step_id": self.step_id,
            "step_type": self.step_type.value,
            "timestamp": self.timestamp,
            "description": self.description,
            "input_data": self.input_data,
            "output_data": self.output_data,
            "confidence": self.confidence,
            "parent_ids": self.parent_ids,
            "metadata": self.metadata
        }


@dataclass
class ProvenanceChain:
    """Complete provenance chain for a reasoning task"""
    task_id: str
    task_description: str
    start_time: str
    end_time: Optional[str] = None
    nodes: List[ProvenanceNode] = field(default_factory=list)
    final_answer: Optional[str] = None
    success: bool = True
    error_message: Optional[str] = None

    def add_node(self, node: ProvenanceNode):
        """Add a provenance node to the chain"""
        self.nodes.append(node)

    def get_node(self, step_id: str) -> Optional[ProvenanceNode]:
        """Retrieve a specific node by ID"""
        for node in self.nodes:
            if node.step_id == step_id:
                return node
        return None

    def get_nodes_by_type(self, step_type: ReasoningStep) -> List[ProvenanceNode]:
        """Get all nodes of a specific type"""
        return [node for node in self.nodes if node.step_type == step_type]

    def to_dict(self) -> dict:
        """Convert to dictionary for serialization"""
        return {
            "task_id": self.task_id,
            "task_description": self.task_description,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "nodes": [node.to_dict() for node in self.nodes],
            "final_answer": self.final_answer,
            "success": self.success,
            "error_message": self.error_message
        }

    def to_json(self, indent: int = 2) -> str:
        """Convert to JSON string"""
        return json.dumps(self.to_dict(), indent=indent)


class ProvenanceTracker:
    """
    Manages provenance tracking for hybrid reasoning sessions.
    Provides methods to record steps, generate explanations, and debug reasoning chains.
    """

    def __init__(self):
        self.chains: Dict[str, ProvenanceChain] = {}
        self.current_chain: Optional[ProvenanceChain] = None
        self.step_counter = 0

    def start_task(self, task_id: str, task_description: str) -> ProvenanceChain:
        """Start tracking a new reasoning task"""
        chain = ProvenanceChain(
            task_id=task_id,
            task_description=task_description,
            start_time=datetime.now().isoformat()
        )
        self.chains[task_id] = chain
        self.current_chain = chain
        self.step_counter = 0
        return chain

    def end_task(self, task_id: str, final_answer: str, success: bool = True, error_message: Optional[str] = None):
        """Complete a reasoning task"""
        if task_id in self.chains:
            chain = self.chains[task_id]
            chain.end_time = datetime.now().isoformat()
            chain.final_answer = final_answer
            chain.success = success
            chain.error_message = error_message

    def record_step(self,
                   step_type: ReasoningStep,
                   description: str,
                   input_data: Dict[str, Any],
                   output_data: Dict[str, Any],
                   confidence: float = 1.0,
                   parent_ids: List[str] = None,
                   metadata: Dict[str, Any] = None) -> str:
        """
        Record a reasoning step in the current chain.

        Args:
            step_type: Type of reasoning step
            description: Human-readable description
            input_data: Input data for this step
            output_data: Output/result data
            confidence: Confidence score (0-1)
            parent_ids: IDs of parent steps this depends on
            metadata: Additional metadata

        Returns:
            step_id: Unique identifier for this step
        """
        if not self.current_chain:
            raise RuntimeError("No active task. Call start_task() first.")

        self.step_counter += 1
        step_id = f"{self.current_chain.task_id}_step_{self.step_counter}"

        node = ProvenanceNode(
            step_id=step_id,
            step_type=step_type,
            timestamp=datetime.now().isoformat(),
            description=description,
            input_data=input_data,
            output_data=output_data,
            confidence=confidence,
            parent_ids=parent_ids or [],
            metadata=metadata or {}
        )

        self.current_chain.add_node(node)
        return step_id

    def record_llm_extraction(self, query: str, events: List[dict], relations: List[dict],
                             confidence: float = 0.8, metadata: Dict[str, Any] = None) -> str:
        """Record LLM extraction step"""
        return self.record_step(
            step_type=ReasoningStep.LLM_EXTRACTION,
            description=f"LLM extracted {len(events)} events and {len(relations)} relations",
            input_data={"query": query},
            output_data={"events": events, "relations": relations},
            confidence=confidence,
            metadata=metadata or {}
        )

    def record_symbolic_constraint(self, constraint_desc: str, constraint_data: dict,
                                   parent_ids: List[str] = None, confidence: float = 1.0) -> str:
        """Record symbolic constraint addition"""
        return self.record_step(
            step_type=ReasoningStep.SYMBOLIC_CONSTRAINT,
            description=f"Added symbolic constraint: {constraint_desc}",
            input_data={"constraint_description": constraint_desc},
            output_data={"constraint": constraint_data},
            confidence=confidence,
            parent_ids=parent_ids or []
        )

    def record_symbolic_solving(self, problem_desc: str, solution: dict,
                               parent_ids: List[str] = None, success: bool = True) -> str:
        """Record symbolic solving step"""
        return self.record_step(
            step_type=ReasoningStep.SYMBOLIC_SOLVING,
            description=f"Solved symbolic constraints: {problem_desc}",
            input_data={"problem": problem_desc},
            output_data={"solution": solution, "success": success},
            confidence=1.0 if success else 0.0,
            parent_ids=parent_ids or []
        )

    def record_verification(self, verification_desc: str, verified: bool,
                           details: dict, parent_ids: List[str] = None) -> str:
        """Record verification step"""
        return self.record_step(
            step_type=ReasoningStep.VERIFICATION,
            description=f"Verification: {verification_desc}",
            input_data={"verification_type": verification_desc},
            output_data={"verified": verified, "details": details},
            confidence=1.0 if verified else 0.5,
            parent_ids=parent_ids or []
        )

    def record_conflict_resolution(self, conflict_desc: str, resolution: dict,
                                   parent_ids: List[str] = None) -> str:
        """Record conflict resolution step"""
        return self.record_step(
            step_type=ReasoningStep.CONFLICT_RESOLUTION,
            description=f"Resolved conflict: {conflict_desc}",
            input_data={"conflict": conflict_desc},
            output_data={"resolution": resolution},
            confidence=0.9,
            parent_ids=parent_ids or []
        )

    def generate_explanation(self, task_id: str, format: str = "text") -> str:
        """
        Generate a human-readable explanation of the reasoning process.

        Args:
            task_id: ID of the task to explain
            format: "text" or "html"

        Returns:
            Formatted explanation
        """
        if task_id not in self.chains:
            return f"No provenance found for task {task_id}"

        chain = self.chains[task_id]

        if format == "html":
            return self._generate_html_explanation(chain)
        else:
            return self._generate_text_explanation(chain)

    def _generate_text_explanation(self, chain: ProvenanceChain) -> str:
        """Generate text-based explanation"""
        lines = []
        lines.append("=" * 80)
        lines.append(f"REASONING EXPLANATION: {chain.task_description}")
        lines.append("=" * 80)
        lines.append(f"Task ID: {chain.task_id}")
        lines.append(f"Started: {chain.start_time}")
        lines.append(f"Completed: {chain.end_time or 'In Progress'}")
        lines.append(f"Status: {'SUCCESS' if chain.success else 'FAILED'}")
        if chain.error_message:
            lines.append(f"Error: {chain.error_message}")
        lines.append("")

        # Group steps by type for better readability
        lines.append("REASONING STEPS:")
        lines.append("-" * 80)

        for i, node in enumerate(chain.nodes, 1):
            lines.append(f"\n{i}. {node.step_type.value.upper().replace('_', ' ')}")
            lines.append(f"   ID: {node.step_id}")
            lines.append(f"   Description: {node.description}")
            lines.append(f"   Confidence: {node.confidence:.2f}")
            if node.parent_ids:
                lines.append(f"   Depends on: {', '.join(node.parent_ids)}")

            # Show key input/output
            if node.input_data:
                input_summary = self._summarize_data(node.input_data)
                lines.append(f"   Input: {input_summary}")
            if node.output_data:
                output_summary = self._summarize_data(node.output_data)
                lines.append(f"   Output: {output_summary}")

        lines.append("")
        lines.append("-" * 80)
        lines.append(f"FINAL ANSWER: {chain.final_answer or 'Not yet determined'}")
        lines.append("=" * 80)

        return "\n".join(lines)

    def _generate_html_explanation(self, chain: ProvenanceChain) -> str:
        """Generate HTML-based explanation"""
        html = []
        html.append("<div class='provenance-explanation'>")
        html.append(f"<h2>Reasoning Explanation: {chain.task_description}</h2>")
        html.append(f"<p><strong>Task ID:</strong> {chain.task_id}</p>")
        html.append(f"<p><strong>Status:</strong> {'SUCCESS' if chain.success else 'FAILED'}</p>")

        html.append("<div class='reasoning-steps'>")
        html.append("<h3>Reasoning Steps</h3>")
        html.append("<ol>")

        for node in chain.nodes:
            confidence_class = "high" if node.confidence > 0.8 else "medium" if node.confidence > 0.5 else "low"
            html.append(f"<li class='step step-{node.step_type.value}'>")
            html.append(f"<h4>{node.step_type.value.replace('_', ' ').title()}</h4>")
            html.append(f"<p>{node.description}</p>")
            html.append(f"<p class='confidence confidence-{confidence_class}'>Confidence: {node.confidence:.2f}</p>")
            html.append("</li>")

        html.append("</ol>")
        html.append("</div>")

        html.append(f"<div class='final-answer'>")
        html.append(f"<h3>Final Answer</h3>")
        html.append(f"<p>{chain.final_answer or 'Not yet determined'}</p>")
        html.append("</div>")

        html.append("</div>")
        return "\n".join(html)

    def _summarize_data(self, data: Dict[str, Any], max_length: int = 100) -> str:
        """Summarize data dictionary for display"""
        summary = json.dumps(data, indent=None)
        if len(summary) > max_length:
            summary = summary[:max_length] + "..."
        return summary

    def get_confidence_score(self, task_id: str) -> float:
        """
        Calculate overall confidence score for a task based on all steps.
        Uses weighted average based on step importance.
        """
        if task_id not in self.chains:
            return 0.0

        chain = self.chains[task_id]
        if not chain.nodes:
            return 0.0

        # Weight critical steps more heavily
        weights = {
            ReasoningStep.LLM_EXTRACTION: 0.3,
            ReasoningStep.SYMBOLIC_CONSTRAINT: 0.2,
            ReasoningStep.SYMBOLIC_SOLVING: 0.3,
            ReasoningStep.VERIFICATION: 0.2,
        }

        total_weight = 0.0
        weighted_confidence = 0.0

        for node in chain.nodes:
            weight = weights.get(node.step_type, 0.1)
            weighted_confidence += node.confidence * weight
            total_weight += weight

        if total_weight == 0:
            return 0.0

        return weighted_confidence / total_weight

    def get_reasoning_path(self, task_id: str, step_id: str) -> List[ProvenanceNode]:
        """
        Get the complete reasoning path leading to a specific step.
        Traces back through parent dependencies.
        """
        if task_id not in self.chains:
            return []

        chain = self.chains[task_id]
        target_node = chain.get_node(step_id)

        if not target_node:
            return []

        path = [target_node]
        to_process = list(target_node.parent_ids)

        while to_process:
            parent_id = to_process.pop(0)
            parent_node = chain.get_node(parent_id)
            if parent_node and parent_node not in path:
                path.append(parent_node)
                to_process.extend(parent_node.parent_ids)

        # Reverse to get chronological order
        path.reverse()
        return path

    def export_chain(self, task_id: str, filepath: str):
        """Export provenance chain to JSON file"""
        if task_id not in self.chains:
            raise ValueError(f"No chain found for task {task_id}")

        with open(filepath, 'w') as f:
            json.dump(self.chains[task_id].to_dict(), f, indent=2)

    def import_chain(self, filepath: str) -> str:
        """Import provenance chain from JSON file"""
        with open(filepath, 'r') as f:
            data = json.load(f)

        # Reconstruct chain (simplified - full version would reconstruct all objects)
        task_id = data['task_id']
        self.chains[task_id] = data
        return task_id


if __name__ == "__main__":
    # Example usage
    print("=" * 80)
    print("Provenance Tracking System - Example")
    print("=" * 80)

    tracker = ProvenanceTracker()

    # Start a task
    task_id = "medical_timeline_001"
    tracker.start_task(task_id, "Determine patient hospital stay duration")

    # Record LLM extraction
    llm_step = tracker.record_llm_extraction(
        query="Patient admitted Monday, surgery Tuesday, discharged Friday",
        events=[
            {"name": "admission", "day": "Monday"},
            {"name": "surgery", "day": "Tuesday"},
            {"name": "discharge", "day": "Friday"}
        ],
        relations=[
            {"event1": "admission", "event2": "surgery", "relation": "before"},
            {"event1": "surgery", "event2": "discharge", "relation": "before"}
        ],
        confidence=0.9
    )

    # Record symbolic constraints
    constraint_step = tracker.record_symbolic_constraint(
        constraint_desc="admission before surgery",
        constraint_data={"interval1": "admission", "interval2": "surgery", "relation": "before"},
        parent_ids=[llm_step],
        confidence=1.0
    )

    # Record solving
    solving_step = tracker.record_symbolic_solving(
        problem_desc="Compute total duration",
        solution={"duration": "4 days", "start": "Monday", "end": "Friday"},
        parent_ids=[llm_step, constraint_step],
        success=True
    )

    # Record verification
    verif_step = tracker.record_verification(
        verification_desc="Verify temporal consistency",
        verified=True,
        details={"consistent": True, "conflicts": []},
        parent_ids=[solving_step]
    )

    # End task
    tracker.end_task(task_id, "The patient stayed in hospital for 4 days.", success=True)

    # Generate explanation
    print("\n" + tracker.generate_explanation(task_id))

    # Show confidence score
    print(f"\nOverall Confidence Score: {tracker.get_confidence_score(task_id):.2f}")

    print("\n" + "=" * 80)
