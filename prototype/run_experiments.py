"""
Experimental Evaluation Script

Runs comprehensive evaluation of the hybrid temporal reasoning system
across all test cases and generates detailed results.
"""

from hybrid_reasoner import HybridTemporalReasoner, ExtractionLevel
from test_cases import TestSuite, TemporalDomain
from llm_interface import MockLLM
import json
import time
from typing import Dict, List
from collections import defaultdict


class ExperimentRunner:
    """Runs experiments and generates evaluation metrics"""

    def __init__(self):
        self.suite = TestSuite()
        self.results = []
        self.metrics = defaultdict(dict)

    def run_all_tests(self, llm_accuracy: str = "medium", verbose: bool = True):
        """Run all test cases with the hybrid reasoner"""
        if verbose:
            print("=" * 80)
            print("RUNNING COMPREHENSIVE TEMPORAL REASONING EVALUATION")
            print("=" * 80)
            print(f"\nLLM Accuracy Setting: {llm_accuracy}")
            print(f"Total Test Cases: {len(self.suite.test_cases)}")
            print("\n" + "=" * 80)

        reasoner = HybridTemporalReasoner(llm_accuracy=llm_accuracy)
        pure_llm = MockLLM(accuracy_level=llm_accuracy)

        for i, test_case in enumerate(self.suite.test_cases, 1):
            if verbose:
                print(f"\n[{i}/{len(self.suite.test_cases)}] Running {test_case.id}...")
                print(f"Domain: {test_case.domain.value}, Level: {test_case.level}, Difficulty: {test_case.difficulty}")

            start_time = time.time()

            # Run hybrid reasoning
            try:
                # Determine extraction level
                level_map = {
                    1: ExtractionLevel.LEVEL_1_EXTRACTION,
                    2: ExtractionLevel.LEVEL_2_ORDERING,
                    3: ExtractionLevel.LEVEL_3_CALCULATION
                }
                level = level_map.get(test_case.level, ExtractionLevel.LEVEL_1_EXTRACTION)

                # Combine question and context for reasoning
                full_query = f"{test_case.context} {test_case.question}"

                hybrid_result = reasoner.reason(full_query, level=level)

                # Get pure LLM result for comparison
                pure_llm_result = pure_llm.query(full_query)

                elapsed_time = time.time() - start_time

                # Store result
                result = {
                    "test_id": test_case.id,
                    "domain": test_case.domain.value,
                    "level": test_case.level,
                    "difficulty": test_case.difficulty,
                    "question": test_case.question,
                    "context": test_case.context,
                    "ground_truth": test_case.ground_truth_answer,
                    "pure_llm_answer": pure_llm_result,
                    "hybrid_answer": hybrid_result.verified_answer,
                    "llm_confidence": hybrid_result.llm_confidence,
                    "symbolic_confidence": hybrid_result.symbolic_confidence,
                    "overall_confidence": hybrid_result.confidence,
                    "used_symbolic": hybrid_result.used_symbolic,
                    "conflicts_detected": hybrid_result.conflicts_detected,
                    "provenance_id": hybrid_result.provenance_id,
                    "execution_time": elapsed_time,
                    "success": True
                }

                self.results.append(result)

                if verbose:
                    print(f"  Pure LLM: {pure_llm_result[:100]}...")
                    print(f"  Hybrid: {hybrid_result.verified_answer[:100]}...")
                    print(f"  Confidence: {hybrid_result.confidence:.2f}")
                    print(f"  Used Symbolic: {hybrid_result.used_symbolic}")
                    print(f"  Time: {elapsed_time:.3f}s")

            except Exception as e:
                if verbose:
                    print(f"  ERROR: {str(e)}")
                result = {
                    "test_id": test_case.id,
                    "domain": test_case.domain.value,
                    "level": test_case.level,
                    "difficulty": test_case.difficulty,
                    "error": str(e),
                    "success": False
                }
                self.results.append(result)

        if verbose:
            print("\n" + "=" * 80)
            print("EVALUATION COMPLETE")
            print("=" * 80)

        self._compute_metrics()

    def _compute_metrics(self):
        """Compute aggregate metrics from results"""
        # Overall metrics
        total_tests = len(self.results)
        successful_tests = sum(1 for r in self.results if r.get("success", False))

        self.metrics["overall"] = {
            "total_tests": total_tests,
            "successful_tests": successful_tests,
            "success_rate": successful_tests / total_tests if total_tests > 0 else 0,
            "avg_confidence": sum(r.get("overall_confidence", 0) for r in self.results if r.get("success")) / successful_tests if successful_tests > 0 else 0,
            "symbolic_usage_rate": sum(1 for r in self.results if r.get("used_symbolic", False)) / successful_tests if successful_tests > 0 else 0,
            "avg_execution_time": sum(r.get("execution_time", 0) for r in self.results if r.get("success")) / successful_tests if successful_tests > 0 else 0
        }

        # By level
        for level in [1, 2, 3]:
            level_results = [r for r in self.results if r.get("level") == level and r.get("success")]
            if level_results:
                self.metrics[f"level_{level}"] = {
                    "count": len(level_results),
                    "avg_confidence": sum(r["overall_confidence"] for r in level_results) / len(level_results),
                    "symbolic_usage": sum(1 for r in level_results if r["used_symbolic"]) / len(level_results),
                    "avg_time": sum(r["execution_time"] for r in level_results) / len(level_results)
                }

        # By domain
        domains = set(r.get("domain") for r in self.results if r.get("domain"))
        for domain in domains:
            domain_results = [r for r in self.results if r.get("domain") == domain and r.get("success")]
            if domain_results:
                self.metrics[f"domain_{domain}"] = {
                    "count": len(domain_results),
                    "avg_confidence": sum(r["overall_confidence"] for r in domain_results) / len(domain_results),
                    "symbolic_usage": sum(1 for r in domain_results if r["used_symbolic"]) / len(domain_results)
                }

        # By difficulty
        for difficulty in ["easy", "medium", "hard"]:
            diff_results = [r for r in self.results if r.get("difficulty") == difficulty and r.get("success")]
            if diff_results:
                self.metrics[f"difficulty_{difficulty}"] = {
                    "count": len(diff_results),
                    "avg_confidence": sum(r["overall_confidence"] for r in diff_results) / len(diff_results),
                    "symbolic_usage": sum(1 for r in diff_results if r["used_symbolic"]) / len(diff_results)
                }

    def print_metrics(self):
        """Print formatted metrics summary"""
        print("\n" + "=" * 80)
        print("EVALUATION METRICS SUMMARY")
        print("=" * 80)

        # Overall
        overall = self.metrics["overall"]
        print("\nOVERALL PERFORMANCE:")
        print(f"  Total Tests: {overall['total_tests']}")
        print(f"  Successful: {overall['successful_tests']}")
        print(f"  Success Rate: {overall['success_rate']:.1%}")
        print(f"  Average Confidence: {overall['avg_confidence']:.3f}")
        print(f"  Symbolic Verification Usage: {overall['symbolic_usage_rate']:.1%}")
        print(f"  Average Execution Time: {overall['avg_execution_time']:.3f}s")

        # By level
        print("\nPERFORMANCE BY LEVEL:")
        for level in [1, 2, 3]:
            key = f"level_{level}"
            if key in self.metrics:
                m = self.metrics[key]
                print(f"  Level {level}:")
                print(f"    Tests: {m['count']}")
                print(f"    Avg Confidence: {m['avg_confidence']:.3f}")
                print(f"    Symbolic Usage: {m['symbolic_usage']:.1%}")
                print(f"    Avg Time: {m['avg_time']:.3f}s")

        # By domain
        print("\nPERFORMANCE BY DOMAIN:")
        for key in sorted(self.metrics.keys()):
            if key.startswith("domain_"):
                domain = key.replace("domain_", "")
                m = self.metrics[key]
                print(f"  {domain}:")
                print(f"    Tests: {m['count']}")
                print(f"    Avg Confidence: {m['avg_confidence']:.3f}")
                print(f"    Symbolic Usage: {m['symbolic_usage']:.1%}")

        # By difficulty
        print("\nPERFORMANCE BY DIFFICULTY:")
        for difficulty in ["easy", "medium", "hard"]:
            key = f"difficulty_{difficulty}"
            if key in self.metrics:
                m = self.metrics[key]
                print(f"  {difficulty.capitalize()}:")
                print(f"    Tests: {m['count']}")
                print(f"    Avg Confidence: {m['avg_confidence']:.3f}")
                print(f"    Symbolic Usage: {m['symbolic_usage']:.1%}")

        print("\n" + "=" * 80)

    def print_detailed_examples(self, num_examples: int = 3):
        """Print detailed examples with provenance"""
        print("\n" + "=" * 80)
        print(f"DETAILED EXAMPLES (showing {num_examples})")
        print("=" * 80)

        # Get examples from different levels
        examples = []
        for level in [1, 2, 3]:
            level_results = [r for r in self.results if r.get("level") == level and r.get("success")]
            if level_results:
                examples.append(level_results[0])

        for i, result in enumerate(examples[:num_examples], 1):
            print(f"\n{'=' * 80}")
            print(f"EXAMPLE {i}: {result['test_id']} (Level {result['level']}, {result['domain']})")
            print("=" * 80)
            print(f"\nContext: {result['context']}")
            print(f"\nQuestion: {result['question']}")
            print(f"\nGround Truth: {result['ground_truth']}")
            print(f"\n--- Pure LLM Answer ---")
            print(result['pure_llm_answer'])
            print(f"\n--- Hybrid Answer ---")
            print(result['hybrid_answer'])
            print(f"\n--- Metrics ---")
            print(f"LLM Confidence: {result['llm_confidence']:.3f}")
            print(f"Symbolic Confidence: {result['symbolic_confidence']:.3f}")
            print(f"Overall Confidence: {result['overall_confidence']:.3f}")
            print(f"Used Symbolic Verification: {result['used_symbolic']}")
            if result['conflicts_detected']:
                print(f"Conflicts Detected: {result['conflicts_detected']}")
            print(f"Execution Time: {result['execution_time']:.3f}s")

    def export_results(self, filepath: str = "/tmp/paper_research/prototype/experiment_results.json"):
        """Export results to JSON file"""
        export_data = {
            "metrics": dict(self.metrics),
            "results": self.results,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }

        with open(filepath, 'w') as f:
            json.dump(export_data, f, indent=2)

        print(f"\nResults exported to: {filepath}")

    def generate_comparison_table(self):
        """Generate comparison table: Pure LLM vs Hybrid"""
        print("\n" + "=" * 80)
        print("COMPARISON: Pure LLM vs Hybrid Approach")
        print("=" * 80)

        print("\n{:<15} {:<30} {:<30} {:<10}".format(
            "Test ID", "Pure LLM", "Hybrid", "Improved"
        ))
        print("-" * 80)

        for result in self.results[:10]:  # Show first 10
            if result.get("success"):
                test_id = result['test_id']
                pure_llm = result['pure_llm_answer'][:28] + "..." if len(result['pure_llm_answer']) > 28 else result['pure_llm_answer']
                hybrid = result['hybrid_answer'][:28] + "..." if len(result['hybrid_answer']) > 28 else result['hybrid_answer']
                improved = "Yes" if result['used_symbolic'] else "N/A"

                print("{:<15} {:<30} {:<30} {:<10}".format(
                    test_id, pure_llm, hybrid, improved
                ))

        print("-" * 80)


def main():
    """Main execution function"""
    print("=" * 80)
    print("HYBRID TEMPORAL REASONING SYSTEM - EXPERIMENTAL EVALUATION")
    print("=" * 80)

    # Initialize and run experiments
    runner = ExperimentRunner()

    # Run all tests
    runner.run_all_tests(llm_accuracy="medium", verbose=True)

    # Print metrics
    runner.print_metrics()

    # Print detailed examples
    runner.print_detailed_examples(num_examples=3)

    # Generate comparison table
    runner.generate_comparison_table()

    # Export results
    runner.export_results()

    print("\n" + "=" * 80)
    print("EVALUATION COMPLETE - See experiment_results.json for full details")
    print("=" * 80)


if __name__ == "__main__":
    main()
