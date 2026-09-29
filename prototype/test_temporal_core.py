"""
Tests for the Allen interval algebra in temporal_core.

Run from this directory:  python3 -m unittest test_temporal_core
"""

import itertools
import unittest

from temporal_core import (
    AllenAlgebra,
    AllenRelation as R,
    TemporalConstraintSolver,
)


def allen_relation(x, y):
    """Classify two intervals (start, end) straight from Allen's endpoint definitions.

    Written independently of AllenAlgebra.determine_relation so the test does not
    check the production code against itself.
    """
    xs, xe = x
    ys, ye = y
    if xe < ys:
        return R.BEFORE
    if ye < xs:
        return R.AFTER
    if xe == ys:
        return R.MEETS
    if ye == xs:
        return R.MET_BY
    if xs == ys and xe == ye:
        return R.EQUALS
    if xs == ys:
        return R.STARTS if xe < ye else R.STARTED_BY
    if xe == ye:
        return R.FINISHES if xs > ys else R.FINISHED_BY
    if xs < ys:
        return R.OVERLAPS if xe < ye else R.CONTAINS
    return R.DURING if xe < ye else R.OVERLAPPED_BY


def true_composition_table():
    """Every (X rel1 Y, Y rel2 Z) -> set of possible X ? Z, by enumeration.

    Three intervals have at most six distinct endpoints, so integer endpoints in
    range(6) realise every possible configuration.
    """
    intervals = [(s, e) for s, e in itertools.combinations(range(6), 2)]
    table = {}
    for x, y, z in itertools.product(intervals, repeat=3):
        key = (allen_relation(x, y), allen_relation(y, z))
        table.setdefault(key, set()).add(allen_relation(x, z))
    return table


class CompositionTableTest(unittest.TestCase):

    def test_every_cell_is_listed_and_matches_allens_definitions(self):
        truth = true_composition_table()
        self.assertEqual(len(truth), 13 * 13)
        checked = 0
        for rel1, rel2 in itertools.product(R, repeat=2):
            with self.subTest(x_y=rel1.value, y_z=rel2.value):
                listed = AllenAlgebra.COMPOSITION_TABLE.get(rel1, {}).get(rel2)
                self.assertIsNotNone(listed, "cell missing from the table")
                self.assertEqual(
                    {r.value for r in listed},
                    {r.value for r in truth[(rel1, rel2)]},
                )
                self.assertEqual(AllenAlgebra.compose(rel1, rel2), listed)
                checked += 1
        self.assertEqual(checked, 13 * 13)


class ConsistencyTest(unittest.TestCase):

    def test_satisfiable_scenario_is_reported_consistent(self):
        # A = [5, 10], B = [10, 15], C = [0, 10]: A meets B, C meets B,
        # and A finishes C. All three hold at once.
        solver = TemporalConstraintSolver()
        solver.add_single_relation("A", "B", R.MEETS)
        solver.add_single_relation("C", "B", R.MEETS)
        solver.add_single_relation("A", "C", R.FINISHES)

        self.assertTrue(solver.propagate_constraints())
        self.assertEqual(solver.get_relation("A", "C"), {R.FINISHES})

    def test_contradictory_scenario_is_reported_inconsistent(self):
        # If A overlaps B and B overlaps C, then A starts first and B's start
        # lies inside A, so A cannot lie strictly inside C.
        solver = TemporalConstraintSolver()
        solver.add_single_relation("A", "B", R.OVERLAPS)
        solver.add_single_relation("B", "C", R.OVERLAPS)
        solver.add_single_relation("A", "C", R.DURING)

        self.assertFalse(solver.propagate_constraints())

    def test_every_three_interval_network_matches_brute_force(self):
        # For three intervals with one base relation per pair, path
        # consistency decides satisfiability exactly, so the solver must agree
        # with enumeration on all 13**3 networks.
        truth = true_composition_table()
        wrong = []
        for ab, bc, ac in itertools.product(R, repeat=3):
            solver = TemporalConstraintSolver()
            solver.add_single_relation("A", "B", ab)
            solver.add_single_relation("B", "C", bc)
            solver.add_single_relation("A", "C", ac)
            if solver.propagate_constraints() != (ac in truth[(ab, bc)]):
                wrong.append((ab.value, bc.value, ac.value))
        self.assertEqual(wrong, [])


if __name__ == "__main__":
    unittest.main()
