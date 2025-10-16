"""
Allen's Interval Algebra Implementation for Temporal Reasoning

This module implements Allen's 13 basic temporal relations and provides
constraint propagation and reasoning capabilities.

References:
- Allen, J. F. (1983). "Maintaining knowledge about temporal intervals"
- Communication of the ACM, 26(11), 832-843
"""

from enum import Enum
from typing import Set, Dict, Tuple, List, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
import json


class AllenRelation(Enum):
    """Allen's 13 basic temporal relations between intervals"""
    BEFORE = "before"           # X before Y: X.end < Y.start
    AFTER = "after"            # X after Y: X.start > Y.end
    MEETS = "meets"            # X meets Y: X.end = Y.start
    MET_BY = "met-by"          # X met-by Y: X.start = Y.end
    OVERLAPS = "overlaps"      # X overlaps Y: X.start < Y.start < X.end < Y.end
    OVERLAPPED_BY = "overlapped-by"  # X overlapped-by Y
    DURING = "during"          # X during Y: Y.start < X.start < X.end < Y.end
    CONTAINS = "contains"      # X contains Y: X.start < Y.start < Y.end < X.end
    STARTS = "starts"          # X starts Y: X.start = Y.start, X.end < Y.end
    STARTED_BY = "started-by"  # X started-by Y
    FINISHES = "finishes"      # X finishes Y: X.start > Y.start, X.end = Y.end
    FINISHED_BY = "finished-by"  # X finished-by Y
    EQUALS = "equals"          # X equals Y: X.start = Y.start, X.end = Y.end


@dataclass
class TimeInterval:
    """Represents a temporal interval with start and end times"""
    name: str
    start: Optional[float] = None  # Unix timestamp or relative time
    end: Optional[float] = None
    duration: Optional[float] = None  # Duration in seconds

    def __post_init__(self):
        """Compute missing values if possible"""
        if self.start is not None and self.end is not None:
            self.duration = self.end - self.start
        elif self.start is not None and self.duration is not None:
            self.end = self.start + self.duration
        elif self.end is not None and self.duration is not None:
            self.start = self.end - self.duration

    def is_complete(self) -> bool:
        """Check if interval has all time values"""
        return self.start is not None and self.end is not None

    def __repr__(self):
        return f"TimeInterval({self.name}, start={self.start}, end={self.end}, duration={self.duration})"


class AllenAlgebra:
    """
    Implements Allen's Interval Algebra reasoning system with:
    - Composition table for constraint propagation
    - Inverse relations
    - Constraint satisfaction checking
    """

    # Composition table: composition_table[R1][R2] = set of possible relations
    COMPOSITION_TABLE = {
        AllenRelation.BEFORE: {
            AllenRelation.BEFORE: {AllenRelation.BEFORE},
            AllenRelation.AFTER: {AllenRelation.BEFORE, AllenRelation.AFTER, AllenRelation.OVERLAPS,
                                 AllenRelation.OVERLAPPED_BY, AllenRelation.MEETS, AllenRelation.MET_BY,
                                 AllenRelation.DURING, AllenRelation.CONTAINS, AllenRelation.STARTS,
                                 AllenRelation.STARTED_BY, AllenRelation.FINISHES, AllenRelation.FINISHED_BY,
                                 AllenRelation.EQUALS},
            AllenRelation.MEETS: {AllenRelation.BEFORE},
            AllenRelation.OVERLAPS: {AllenRelation.BEFORE},
            AllenRelation.DURING: {AllenRelation.BEFORE},
            AllenRelation.STARTS: {AllenRelation.BEFORE},
            AllenRelation.FINISHES: {AllenRelation.BEFORE},
        },
        AllenRelation.AFTER: {
            AllenRelation.BEFORE: {AllenRelation.BEFORE, AllenRelation.AFTER, AllenRelation.OVERLAPS,
                                  AllenRelation.OVERLAPPED_BY, AllenRelation.MEETS, AllenRelation.MET_BY,
                                  AllenRelation.DURING, AllenRelation.CONTAINS, AllenRelation.STARTS,
                                  AllenRelation.STARTED_BY, AllenRelation.FINISHES, AllenRelation.FINISHED_BY,
                                  AllenRelation.EQUALS},
            AllenRelation.AFTER: {AllenRelation.AFTER},
            AllenRelation.MET_BY: {AllenRelation.AFTER},
            AllenRelation.OVERLAPPED_BY: {AllenRelation.AFTER},
            AllenRelation.CONTAINS: {AllenRelation.AFTER},
            AllenRelation.FINISHED_BY: {AllenRelation.AFTER},
            AllenRelation.STARTED_BY: {AllenRelation.AFTER},
        },
        AllenRelation.MEETS: {
            AllenRelation.BEFORE: {AllenRelation.BEFORE},
            AllenRelation.MEETS: {AllenRelation.BEFORE},
            AllenRelation.OVERLAPS: {AllenRelation.BEFORE},
            AllenRelation.DURING: {AllenRelation.BEFORE},
            AllenRelation.STARTS: {AllenRelation.BEFORE},
            AllenRelation.MET_BY: {AllenRelation.EQUALS},
            AllenRelation.AFTER: {AllenRelation.AFTER},
            AllenRelation.OVERLAPPED_BY: {AllenRelation.AFTER},
            AllenRelation.CONTAINS: {AllenRelation.OVERLAPPED_BY, AllenRelation.AFTER, AllenRelation.CONTAINS,
                                    AllenRelation.FINISHED_BY, AllenRelation.STARTED_BY},
            AllenRelation.STARTED_BY: {AllenRelation.STARTED_BY},
            AllenRelation.FINISHED_BY: {AllenRelation.AFTER},
            AllenRelation.FINISHES: {AllenRelation.BEFORE},
        },
        AllenRelation.EQUALS: {
            AllenRelation.BEFORE: {AllenRelation.BEFORE},
            AllenRelation.AFTER: {AllenRelation.AFTER},
            AllenRelation.MEETS: {AllenRelation.MEETS},
            AllenRelation.MET_BY: {AllenRelation.MET_BY},
            AllenRelation.OVERLAPS: {AllenRelation.OVERLAPS},
            AllenRelation.OVERLAPPED_BY: {AllenRelation.OVERLAPPED_BY},
            AllenRelation.DURING: {AllenRelation.DURING},
            AllenRelation.CONTAINS: {AllenRelation.CONTAINS},
            AllenRelation.STARTS: {AllenRelation.STARTS},
            AllenRelation.STARTED_BY: {AllenRelation.STARTED_BY},
            AllenRelation.FINISHES: {AllenRelation.FINISHES},
            AllenRelation.FINISHED_BY: {AllenRelation.FINISHED_BY},
            AllenRelation.EQUALS: {AllenRelation.EQUALS},
        }
    }

    # Inverse relations
    INVERSE = {
        AllenRelation.BEFORE: AllenRelation.AFTER,
        AllenRelation.AFTER: AllenRelation.BEFORE,
        AllenRelation.MEETS: AllenRelation.MET_BY,
        AllenRelation.MET_BY: AllenRelation.MEETS,
        AllenRelation.OVERLAPS: AllenRelation.OVERLAPPED_BY,
        AllenRelation.OVERLAPPED_BY: AllenRelation.OVERLAPS,
        AllenRelation.DURING: AllenRelation.CONTAINS,
        AllenRelation.CONTAINS: AllenRelation.DURING,
        AllenRelation.STARTS: AllenRelation.STARTED_BY,
        AllenRelation.STARTED_BY: AllenRelation.STARTS,
        AllenRelation.FINISHES: AllenRelation.FINISHED_BY,
        AllenRelation.FINISHED_BY: AllenRelation.FINISHES,
        AllenRelation.EQUALS: AllenRelation.EQUALS,
    }

    @staticmethod
    def determine_relation(interval1: TimeInterval, interval2: TimeInterval) -> Optional[AllenRelation]:
        """
        Determine the Allen relation between two complete intervals.
        Returns None if intervals are incomplete.
        """
        if not (interval1.is_complete() and interval2.is_complete()):
            return None

        x_start, x_end = interval1.start, interval1.end
        y_start, y_end = interval2.start, interval2.end

        epsilon = 1e-6  # Tolerance for floating point comparison

        if abs(x_start - y_start) < epsilon and abs(x_end - y_end) < epsilon:
            return AllenRelation.EQUALS
        elif x_end < y_start - epsilon:
            return AllenRelation.BEFORE
        elif x_start > y_end + epsilon:
            return AllenRelation.AFTER
        elif abs(x_end - y_start) < epsilon:
            return AllenRelation.MEETS
        elif abs(x_start - y_end) < epsilon:
            return AllenRelation.MET_BY
        elif x_start < y_start - epsilon and y_start < x_end - epsilon and x_end < y_end - epsilon:
            return AllenRelation.OVERLAPS
        elif y_start < x_start - epsilon and x_start < y_end - epsilon and y_end < x_end - epsilon:
            return AllenRelation.OVERLAPPED_BY
        elif y_start < x_start - epsilon and x_end < y_end - epsilon:
            return AllenRelation.DURING
        elif x_start < y_start - epsilon and y_end < x_end - epsilon:
            return AllenRelation.CONTAINS
        elif abs(x_start - y_start) < epsilon and x_end < y_end - epsilon:
            return AllenRelation.STARTS
        elif abs(x_start - y_start) < epsilon and y_end < x_end - epsilon:
            return AllenRelation.STARTED_BY
        elif x_start > y_start + epsilon and abs(x_end - y_end) < epsilon:
            return AllenRelation.FINISHES
        elif y_start > x_start + epsilon and abs(x_end - y_end) < epsilon:
            return AllenRelation.FINISHED_BY

        return None

    @staticmethod
    def compose(rel1: AllenRelation, rel2: AllenRelation) -> Set[AllenRelation]:
        """
        Compose two relations: if X rel1 Y and Y rel2 Z, what are possible relations X ? Z
        Returns a set of possible relations.
        """
        # Use simplified composition - in full implementation would use complete table
        if rel1 in AllenAlgebra.COMPOSITION_TABLE and rel2 in AllenAlgebra.COMPOSITION_TABLE[rel1]:
            return AllenAlgebra.COMPOSITION_TABLE[rel1][rel2]

        # Default: return all relations (conservative)
        return set(AllenRelation)

    @staticmethod
    def inverse(rel: AllenRelation) -> AllenRelation:
        """Get the inverse of a relation"""
        return AllenAlgebra.INVERSE[rel]

    @staticmethod
    def is_consistent(constraints: Dict[Tuple[str, str], Set[AllenRelation]]) -> bool:
        """
        Check if a set of temporal constraints is consistent using path consistency.
        constraints: dict mapping (interval1, interval2) to set of possible relations
        """
        # Simplified consistency check using path consistency algorithm
        # Full implementation would use algebraic closure

        intervals = set()
        for (i1, i2) in constraints.keys():
            intervals.add(i1)
            intervals.add(i2)

        intervals = list(intervals)

        # Path consistency: for all triples (i, j, k), check i-j-k path
        changed = True
        iterations = 0
        max_iterations = 100

        while changed and iterations < max_iterations:
            changed = False
            iterations += 1

            for i in intervals:
                for j in intervals:
                    if i == j:
                        continue

                    for k in intervals:
                        if k == i or k == j:
                            continue

                        # Get constraints
                        ij_key = (i, j) if (i, j) in constraints else (j, i)
                        jk_key = (j, k) if (j, k) in constraints else (k, j)
                        ik_key = (i, k) if (i, k) in constraints else (k, i)

                        if ij_key not in constraints or jk_key not in constraints:
                            continue

                        # Handle inverse if needed
                        ij_rels = constraints[ij_key] if ij_key[0] == i else {AllenAlgebra.inverse(r) for r in constraints[ij_key]}
                        jk_rels = constraints[jk_key] if jk_key[0] == j else {AllenAlgebra.inverse(r) for r in constraints[jk_key]}

                        # Compose i->j->k
                        composed = set()
                        for r1 in ij_rels:
                            for r2 in jk_rels:
                                composed.update(AllenAlgebra.compose(r1, r2))

                        # Intersect with existing constraint
                        if ik_key in constraints:
                            old_rels = constraints[ik_key] if ik_key[0] == i else {AllenAlgebra.inverse(r) for r in constraints[ik_key]}
                            new_rels = old_rels.intersection(composed)

                            if len(new_rels) == 0:
                                return False  # Inconsistent

                            if len(new_rels) < len(old_rels):
                                constraints[ik_key] = new_rels if ik_key[0] == i else {AllenAlgebra.inverse(r) for r in new_rels}
                                changed = True

        return True


class TemporalConstraintSolver:
    """
    Solves temporal constraint satisfaction problems using Allen's Interval Algebra
    and constraint propagation.
    """

    def __init__(self):
        self.intervals: Dict[str, TimeInterval] = {}
        self.constraints: Dict[Tuple[str, str], Set[AllenRelation]] = {}
        self.algebra = AllenAlgebra()

    def add_interval(self, interval: TimeInterval):
        """Add a time interval to the problem"""
        self.intervals[interval.name] = interval

    def add_constraint(self, interval1: str, interval2: str, relations: Set[AllenRelation]):
        """Add a temporal constraint between two intervals"""
        key = (interval1, interval2)
        if key in self.constraints:
            # Intersect with existing constraint
            self.constraints[key] = self.constraints[key].intersection(relations)
        else:
            self.constraints[key] = relations

    def add_single_relation(self, interval1: str, interval2: str, relation: AllenRelation):
        """Add a single relation constraint"""
        self.add_constraint(interval1, interval2, {relation})

    def propagate_constraints(self) -> bool:
        """
        Propagate constraints to derive new relations and check consistency.
        Returns True if consistent, False otherwise.
        """
        return self.algebra.is_consistent(self.constraints)

    def get_relation(self, interval1: str, interval2: str) -> Optional[Set[AllenRelation]]:
        """Get possible relations between two intervals"""
        if (interval1, interval2) in self.constraints:
            return self.constraints[(interval1, interval2)]
        elif (interval2, interval1) in self.constraints:
            # Return inverse relations
            return {self.algebra.inverse(r) for r in self.constraints[(interval2, interval1)]}
        return None

    def compute_interval_values(self) -> Dict[str, TimeInterval]:
        """
        Compute concrete time values for intervals using constraints.
        This is a simplified version - full implementation would use CSP solver.
        """
        # Start with intervals that have concrete values
        complete = {name: interval for name, interval in self.intervals.items() if interval.is_complete()}
        incomplete = {name: interval for name, interval in self.intervals.items() if not interval.is_complete()}

        changed = True
        iterations = 0
        max_iterations = 50

        while changed and incomplete and iterations < max_iterations:
            changed = False
            iterations += 1

            for name, interval in list(incomplete.items()):
                # Try to infer values from constraints with complete intervals
                for complete_name, complete_interval in complete.items():
                    if name == complete_name:
                        continue

                    rel_set = self.get_relation(name, complete_name)
                    if not rel_set or len(rel_set) != 1:
                        continue

                    rel = list(rel_set)[0]

                    # Try to infer time values based on relation
                    if rel == AllenRelation.BEFORE:
                        if interval.end is None:
                            interval.end = complete_interval.start - 1
                            if interval.duration is not None:
                                interval.start = interval.end - interval.duration
                                changed = True
                    elif rel == AllenRelation.AFTER:
                        if interval.start is None:
                            interval.start = complete_interval.end + 1
                            if interval.duration is not None:
                                interval.end = interval.start + interval.duration
                                changed = True
                    elif rel == AllenRelation.MEETS:
                        if interval.end is None:
                            interval.end = complete_interval.start
                            if interval.duration is not None:
                                interval.start = interval.end - interval.duration
                                changed = True
                    elif rel == AllenRelation.MET_BY:
                        if interval.start is None:
                            interval.start = complete_interval.end
                            if interval.duration is not None:
                                interval.end = interval.start + interval.duration
                                changed = True

                    if interval.is_complete():
                        complete[name] = interval
                        del incomplete[name]
                        changed = True
                        break

        return self.intervals

    def to_dict(self) -> dict:
        """Export solver state to dictionary"""
        return {
            "intervals": {name: {"name": i.name, "start": i.start, "end": i.end, "duration": i.duration}
                         for name, i in self.intervals.items()},
            "constraints": {f"{k[0]}-{k[1]}": [r.value for r in v]
                          for k, v in self.constraints.items()}
        }


def parse_relative_time(time_str: str, reference: float = 0) -> float:
    """
    Parse relative time expressions like '2 hours', '30 minutes', '1 day'
    Returns time in seconds relative to reference point.
    """
    time_str = time_str.lower().strip()

    units = {
        'second': 1, 'seconds': 1, 'sec': 1, 's': 1,
        'minute': 60, 'minutes': 60, 'min': 60, 'm': 60,
        'hour': 3600, 'hours': 3600, 'hr': 3600, 'h': 3600,
        'day': 86400, 'days': 86400, 'd': 86400,
        'week': 604800, 'weeks': 604800, 'w': 604800,
        'month': 2592000, 'months': 2592000,  # Approximate 30 days
        'year': 31536000, 'years': 31536000, 'y': 31536000
    }

    parts = time_str.split()
    if len(parts) >= 2:
        try:
            value = float(parts[0])
            unit = parts[1].rstrip('s')  # Remove trailing 's' if present
            if unit in units:
                return reference + value * units[unit]
        except ValueError:
            pass

    return reference


if __name__ == "__main__":
    # Example usage
    print("=" * 60)
    print("Allen's Interval Algebra - Example Demonstrations")
    print("=" * 60)

    # Example 1: Determine relation between two intervals
    print("\n1. Determining relations between intervals:")
    print("-" * 60)

    meeting = TimeInterval("meeting", start=9.0, end=10.0)
    lunch = TimeInterval("lunch", start=12.0, end=13.0)

    relation = AllenAlgebra.determine_relation(meeting, lunch)
    print(f"{meeting.name} {relation.value} {lunch.name}")
    print(f"Meeting: {meeting.start} - {meeting.end}")
    print(f"Lunch: {lunch.start} - {lunch.end}")

    # Example 2: Constraint solving
    print("\n2. Temporal constraint solving:")
    print("-" * 60)

    solver = TemporalConstraintSolver()

    # Add intervals
    solver.add_interval(TimeInterval("event_A", start=0, end=10))
    solver.add_interval(TimeInterval("event_B", duration=5))
    solver.add_interval(TimeInterval("event_C", duration=3))

    # Add constraints
    solver.add_single_relation("event_A", "event_B", AllenRelation.BEFORE)
    solver.add_single_relation("event_B", "event_C", AllenRelation.MEETS)

    print("Constraints:")
    print("- event_A before event_B")
    print("- event_B meets event_C")

    # Check consistency
    is_consistent = solver.propagate_constraints()
    print(f"\nConstraints consistent: {is_consistent}")

    # Compute interval values
    result = solver.compute_interval_values()
    print("\nComputed intervals:")
    for name, interval in result.items():
        print(f"  {name}: start={interval.start}, end={interval.end}, duration={interval.duration}")

    # Example 3: Composition
    print("\n3. Relation composition:")
    print("-" * 60)
    print("If A before B and B meets C, then A ? C:")
    composed = AllenAlgebra.compose(AllenRelation.BEFORE, AllenRelation.MEETS)
    print(f"Possible relations: {[r.value for r in composed]}")

    print("\n" + "=" * 60)
