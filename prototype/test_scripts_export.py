"""
The two runnable scripts must finish and leave their JSON next to themselves.

Each script runs from a throwaway copy of this directory, so the tracked
test_cases.json is never touched. Run from this directory:
    python3 -m unittest test_scripts_export
"""

import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))


class ScriptExportTest(unittest.TestCase):

    def run_copy(self, script, output, **env_overrides):
        with tempfile.TemporaryDirectory() as tmp:
            for path in glob.glob(os.path.join(HERE, "*.py")):
                shutil.copy(path, tmp)
            env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", **env_overrides)
            # Run from somewhere else, so a path relative to the working
            # directory would not land in the copy either.
            done = subprocess.run(
                [sys.executable, os.path.join(tmp, script)],
                cwd=tempfile.gettempdir(),
                env=env,
                capture_output=True,
                text=True,
            )
            self.assertEqual(done.returncode, 0, done.stderr[-2000:])
            with open(os.path.join(tmp, output)) as f:
                return json.load(f)

    def test_test_cases_script_exports_the_suite(self):
        data = self.run_copy("test_cases.py", "test_cases.json")
        self.assertEqual(len(data["tests"]), 20)

    def test_run_experiments_script_exports_results(self):
        data = self.run_copy("run_experiments.py", "experiment_results.json")
        self.assertEqual(len(data["results"]), 20)

    def test_run_experiments_gives_the_same_results_every_run(self):
        # Wall-clock fields differ between runs by nature; everything else,
        # including the mock LLM's answers, must be reproducible.
        timing = {"execution_time", "avg_execution_time", "avg_time", "timestamp"}

        def without_timing(value):
            if isinstance(value, dict):
                return {k: without_timing(v) for k, v in value.items() if k not in timing}
            if isinstance(value, list):
                return [without_timing(v) for v in value]
            return value

        # Different hash seeds, so anything that depends on set order shows up.
        first = self.run_copy("run_experiments.py", "experiment_results.json",
                              PYTHONHASHSEED="1")
        second = self.run_copy("run_experiments.py", "experiment_results.json",
                               PYTHONHASHSEED="2")
        self.assertEqual(len(first["results"]), 20)
        self.assertEqual(without_timing(first), without_timing(second))


if __name__ == "__main__":
    unittest.main()
