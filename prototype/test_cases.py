"""
Comprehensive Test Cases for Hybrid Temporal Reasoning System

Covers 20 test cases across different temporal reasoning levels and domains:
- Level 1: Temporal extraction
- Level 2: Event ordering and relations
- Level 3: Duration calculations

Domains: Medical, Financial, Project Management, General Events
"""

from dataclasses import dataclass
from typing import List, Optional
from enum import Enum
import json


class TemporalDomain(Enum):
    """Domain categories for test cases"""
    MEDICAL = "medical"
    FINANCIAL = "financial"
    PROJECT = "project_management"
    GENERAL = "general"
    TRAVEL = "travel"
    ACADEMIC = "academic"


@dataclass
class TestCase:
    """A single temporal reasoning test case"""
    id: str
    domain: TemporalDomain
    level: int  # 1, 2, or 3
    question: str
    context: str
    ground_truth_answer: str
    ground_truth_events: List[str]
    ground_truth_relations: List[tuple]  # (event1, relation, event2)
    expected_duration: Optional[float] = None  # In seconds, for level 3
    difficulty: str = "medium"  # easy, medium, hard
    notes: str = ""

    def to_dict(self):
        return {
            "id": self.id,
            "domain": self.domain.value,
            "level": self.level,
            "question": self.question,
            "context": self.context,
            "ground_truth_answer": self.ground_truth_answer,
            "ground_truth_events": self.ground_truth_events,
            "ground_truth_relations": self.ground_truth_relations,
            "expected_duration": self.expected_duration,
            "difficulty": self.difficulty,
            "notes": self.notes
        }


# Level 1: Temporal Extraction Test Cases
TEST_CASES = [
    # Test 1: Simple medical timeline
    TestCase(
        id="L1_MED_001",
        domain=TemporalDomain.MEDICAL,
        level=1,
        question="What medical events occurred in this patient's timeline?",
        context="Patient was admitted to the emergency room on Monday morning, received initial treatment, underwent surgery on Tuesday, and was discharged on Friday afternoon.",
        ground_truth_answer="The medical events are: admission, initial treatment, surgery, and discharge.",
        ground_truth_events=["admission", "treatment", "surgery", "discharge"],
        ground_truth_relations=[],
        difficulty="easy",
        notes="Basic event extraction from medical narrative"
    ),

    # Test 2: Financial transaction sequence
    TestCase(
        id="L1_FIN_001",
        domain=TemporalDomain.FINANCIAL,
        level=1,
        question="Identify all financial events in the transaction history.",
        context="The account was opened on January 1st. First deposit made on January 5th. Stock purchase executed on January 10th. Dividend received on January 15th.",
        ground_truth_answer="Financial events: account opening, deposit, stock purchase, dividend receipt.",
        ground_truth_events=["account_opening", "deposit", "stock_purchase", "dividend_receipt"],
        ground_truth_relations=[],
        difficulty="easy",
        notes="Extracting financial events from timeline"
    ),

    # Test 3: Project milestones
    TestCase(
        id="L1_PRJ_001",
        domain=TemporalDomain.PROJECT,
        level=1,
        question="What are the key project milestones?",
        context="Project kickoff happened in Q1. Requirements gathering was completed. Design phase followed. Development started in Q2. Testing is ongoing.",
        ground_truth_answer="Milestones: kickoff, requirements gathering, design, development start, testing.",
        ground_truth_events=["kickoff", "requirements", "design", "development", "testing"],
        ground_truth_relations=[],
        difficulty="easy",
        notes="Identifying project phases and milestones"
    ),

    # Test 4: Travel itinerary
    TestCase(
        id="L1_TRV_001",
        domain=TemporalDomain.TRAVEL,
        level=1,
        question="List all events in the travel itinerary.",
        context="Departure from home at 6 AM. Airport check-in at 7 AM. Flight departure at 9 AM. Arrival at destination at 2 PM. Hotel check-in at 3 PM.",
        ground_truth_answer="Travel events: home departure, airport check-in, flight departure, arrival, hotel check-in.",
        ground_truth_events=["home_departure", "airport_checkin", "flight_departure", "arrival", "hotel_checkin"],
        ground_truth_relations=[],
        difficulty="easy",
        notes="Extracting travel-related events"
    ),

    # Level 2: Temporal Ordering Test Cases
    # Test 5: Medical procedure ordering
    TestCase(
        id="L2_MED_001",
        domain=TemporalDomain.MEDICAL,
        level=2,
        question="What is the correct temporal sequence of medical procedures?",
        context="The patient was admitted on Monday, underwent surgery on Tuesday, spent two days in recovery, and was discharged on Friday.",
        ground_truth_answer="Sequence: admission (Monday) → surgery (Tuesday) → recovery (Wed-Thu) → discharge (Friday).",
        ground_truth_events=["admission", "surgery", "recovery", "discharge"],
        ground_truth_relations=[
            ("admission", "before", "surgery"),
            ("surgery", "before", "recovery"),
            ("recovery", "before", "discharge")
        ],
        difficulty="medium",
        notes="Ordering medical events with explicit temporal markers"
    ),

    # Test 6: Financial transaction ordering
    TestCase(
        id="L2_FIN_001",
        domain=TemporalDomain.FINANCIAL,
        level=2,
        question="In what order did the financial transactions occur?",
        context="Before investing in stocks, the client opened a brokerage account. After the account was funded, the first trade was executed. The dividend payment came after the trade.",
        ground_truth_answer="Order: account opening → funding → trade execution → dividend payment.",
        ground_truth_events=["account_opening", "funding", "trade", "dividend"],
        ground_truth_relations=[
            ("account_opening", "before", "funding"),
            ("funding", "before", "trade"),
            ("trade", "before", "dividend")
        ],
        difficulty="medium",
        notes="Ordering with explicit before/after indicators"
    ),

    # Test 7: Project task dependencies
    TestCase(
        id="L2_PRJ_001",
        domain=TemporalDomain.PROJECT,
        level=2,
        question="What is the dependency order of project tasks?",
        context="Task A must be completed before Task B can start. Task B and Task C can run concurrently. Task D requires both B and C to be finished first.",
        ground_truth_answer="Dependencies: A before B, A before C, B before D, C before D. B and C can overlap.",
        ground_truth_events=["task_A", "task_B", "task_C", "task_D"],
        ground_truth_relations=[
            ("task_A", "before", "task_B"),
            ("task_A", "before", "task_C"),
            ("task_B", "before", "task_D"),
            ("task_C", "before", "task_D")
        ],
        difficulty="hard",
        notes="Complex dependencies with concurrent tasks"
    ),

    # Test 8: Event overlap
    TestCase(
        id="L2_GEN_001",
        domain=TemporalDomain.GENERAL,
        level=2,
        question="Which events overlap in time?",
        context="The conference started at 9 AM. The keynote speech began at 9:30 AM during the conference. The networking session started at 11 AM while the conference was still ongoing.",
        ground_truth_answer="The keynote overlaps with the conference. The networking session overlaps with the conference.",
        ground_truth_events=["conference", "keynote", "networking"],
        ground_truth_relations=[
            ("keynote", "during", "conference"),
            ("networking", "during", "conference")
        ],
        difficulty="medium",
        notes="Identifying temporal overlaps"
    ),

    # Test 9: Sequential with gaps
    TestCase(
        id="L2_MED_002",
        domain=TemporalDomain.MEDICAL,
        level=2,
        question="Describe the temporal relationships in the treatment plan.",
        context="The patient completed the first round of chemotherapy. After a two-week break, the second round began. The patient was in remission between rounds.",
        ground_truth_answer="First chemotherapy → break/remission → second chemotherapy.",
        ground_truth_events=["chemo_round1", "break", "chemo_round2"],
        ground_truth_relations=[
            ("chemo_round1", "before", "break"),
            ("break", "before", "chemo_round2")
        ],
        difficulty="medium",
        notes="Sequential events with explicit gaps"
    ),

    # Test 10: Complex meeting schedule
    TestCase(
        id="L2_PRJ_002",
        domain=TemporalDomain.PROJECT,
        level=2,
        question="How are the meetings scheduled relative to each other?",
        context="The planning meeting happens first thing Monday morning. The design review is scheduled for Tuesday, after the planning is complete. The client presentation is on Friday, but only after both planning and design review are done.",
        ground_truth_answer="Planning (Monday) → Design Review (Tuesday) → Client Presentation (Friday).",
        ground_truth_events=["planning", "design_review", "client_presentation"],
        ground_truth_relations=[
            ("planning", "before", "design_review"),
            ("design_review", "before", "client_presentation")
        ],
        difficulty="medium",
        notes="Meeting scheduling with dependencies"
    ),

    # Level 3: Duration Calculation Test Cases
    # Test 11: Hospital stay duration
    TestCase(
        id="L3_MED_001",
        domain=TemporalDomain.MEDICAL,
        level=3,
        question="How long was the patient's hospital stay?",
        context="Patient was admitted on Monday at 8 AM and discharged on Friday at 2 PM.",
        ground_truth_answer="The hospital stay was 4 days and 6 hours (102 hours total).",
        ground_truth_events=["admission", "discharge"],
        ground_truth_relations=[("admission", "before", "discharge")],
        expected_duration=367200,  # 4.25 days in seconds
        difficulty="medium",
        notes="Calculate duration between two timepoints"
    ),

    # Test 12: Meeting total time
    TestCase(
        id="L3_PRJ_001",
        domain=TemporalDomain.PROJECT,
        level=3,
        question="What was the total meeting time?",
        context="The meeting had three parts: a 45-minute presentation, a 30-minute Q&A session, and a 15-minute wrap-up.",
        ground_truth_answer="The total meeting time was 90 minutes (1.5 hours).",
        ground_truth_events=["presentation", "qa_session", "wrapup"],
        ground_truth_relations=[
            ("presentation", "before", "qa_session"),
            ("qa_session", "before", "wrapup")
        ],
        expected_duration=5400,  # 90 minutes in seconds
        difficulty="easy",
        notes="Sum of sequential durations"
    ),

    # Test 13: Treatment duration
    TestCase(
        id="L3_MED_002",
        domain=TemporalDomain.MEDICAL,
        level=3,
        question="How long does the complete treatment take?",
        context="The treatment protocol consists of a 2-hour infusion, followed by a 1-hour observation period, and then a 30-minute consultation.",
        ground_truth_answer="The complete treatment takes 3.5 hours (210 minutes).",
        ground_truth_events=["infusion", "observation", "consultation"],
        ground_truth_relations=[
            ("infusion", "before", "observation"),
            ("observation", "before", "consultation")
        ],
        expected_duration=12600,  # 3.5 hours in seconds
        difficulty="easy",
        notes="Sequential medical procedure durations"
    ),

    # Test 14: Project timeline
    TestCase(
        id="L3_PRJ_002",
        domain=TemporalDomain.PROJECT,
        level=3,
        question="What is the total project duration?",
        context="The project has four phases: planning (2 weeks), design (3 weeks), development (8 weeks), and testing (2 weeks).",
        ground_truth_answer="The total project duration is 15 weeks.",
        ground_truth_events=["planning", "design", "development", "testing"],
        ground_truth_relations=[
            ("planning", "before", "design"),
            ("design", "before", "development"),
            ("development", "before", "testing")
        ],
        expected_duration=9072000,  # 15 weeks in seconds
        difficulty="medium",
        notes="Multi-phase project duration"
    ),

    # Test 15: Travel time calculation
    TestCase(
        id="L3_TRV_001",
        domain=TemporalDomain.TRAVEL,
        level=3,
        question="How long is the entire journey?",
        context="The journey consists of a 3-hour flight, a 45-minute layover, and then a 2-hour connecting flight.",
        ground_truth_answer="The total journey time is 5 hours and 45 minutes.",
        ground_truth_events=["first_flight", "layover", "second_flight"],
        ground_truth_relations=[
            ("first_flight", "before", "layover"),
            ("layover", "before", "second_flight")
        ],
        expected_duration=20700,  # 5.75 hours in seconds
        difficulty="easy",
        notes="Multi-leg journey duration"
    ),

    # Test 16: Academic semester duration
    TestCase(
        id="L3_ACD_001",
        domain=TemporalDomain.ACADEMIC,
        level=3,
        question="How long is the academic semester?",
        context="Classes start on September 1st and run for 14 weeks. Then there's a 1-week break, followed by a 2-week exam period.",
        ground_truth_answer="The semester is 17 weeks long.",
        ground_truth_events=["classes", "break", "exams"],
        ground_truth_relations=[
            ("classes", "before", "break"),
            ("break", "before", "exams")
        ],
        expected_duration=10281600,  # 17 weeks in seconds
        difficulty="medium",
        notes="Academic timeline calculation"
    ),

    # Test 17: Complex financial hold period
    TestCase(
        id="L3_FIN_001",
        domain=TemporalDomain.FINANCIAL,
        level=3,
        question="When can the funds be withdrawn?",
        context="Funds deposited today have a 3-day processing period, followed by a 5-day hold period before they can be withdrawn.",
        ground_truth_answer="Funds can be withdrawn after 8 days.",
        ground_truth_events=["deposit", "processing", "hold", "withdrawal"],
        ground_truth_relations=[
            ("deposit", "before", "processing"),
            ("processing", "before", "hold"),
            ("hold", "before", "withdrawal")
        ],
        expected_duration=691200,  # 8 days in seconds
        difficulty="medium",
        notes="Sequential waiting periods"
    ),

    # Mixed Complexity Test Cases
    # Test 18: Medical with overlapping treatments
    TestCase(
        id="L2_MED_003",
        domain=TemporalDomain.MEDICAL,
        level=2,
        question="How do the treatments relate temporally?",
        context="Physical therapy started on Week 1. Medication was prescribed during Week 2 while PT continued. Both treatments ended simultaneously after Week 6.",
        ground_truth_answer="PT starts first, medication starts during PT, both finish together.",
        ground_truth_events=["physical_therapy", "medication"],
        ground_truth_relations=[
            ("physical_therapy", "started-by", "medication"),
            ("physical_therapy", "finished-by", "medication")
        ],
        difficulty="hard",
        notes="Complex overlapping treatments"
    ),

    # Test 19: Project with parallel tasks
    TestCase(
        id="L3_PRJ_003",
        domain=TemporalDomain.PROJECT,
        level=3,
        question="What is the critical path duration?",
        context="Task A takes 5 days. Tasks B and C can start after A and run in parallel - B takes 3 days, C takes 4 days. Task D requires both B and C to complete and takes 2 days.",
        ground_truth_answer="Critical path is A(5) → C(4) → D(2) = 11 days.",
        ground_truth_events=["task_A", "task_B", "task_C", "task_D"],
        ground_truth_relations=[
            ("task_A", "before", "task_B"),
            ("task_A", "before", "task_C"),
            ("task_B", "before", "task_D"),
            ("task_C", "before", "task_D")
        ],
        expected_duration=950400,  # 11 days in seconds
        difficulty="hard",
        notes="Parallel tasks with critical path"
    ),

    # Test 20: Complex medical case
    TestCase(
        id="L3_MED_003",
        domain=TemporalDomain.MEDICAL,
        level=3,
        question="What is the total treatment time from start to finish?",
        context="Initial consultation lasted 30 minutes. Lab tests were ordered and took 2 hours to process. Doctor reviewed results for 15 minutes. Treatment session was 1 hour. Follow-up appointment scheduled after 1 week.",
        ground_truth_answer="Immediate treatment: 3 hours 45 minutes. Total timeline including follow-up: 1 week and 3 hours 45 minutes.",
        ground_truth_events=["consultation", "lab_tests", "review", "treatment", "followup"],
        ground_truth_relations=[
            ("consultation", "before", "lab_tests"),
            ("lab_tests", "before", "review"),
            ("review", "before", "treatment"),
            ("treatment", "before", "followup")
        ],
        expected_duration=13500,  # 3.75 hours for immediate treatment (seconds)
        difficulty="hard",
        notes="Multi-stage medical process with delays"
    ),
]


class TestSuite:
    """Manages and runs temporal reasoning test cases"""

    def __init__(self):
        self.test_cases = TEST_CASES

    def get_test_by_id(self, test_id: str) -> Optional[TestCase]:
        """Retrieve a specific test case by ID"""
        for test in self.test_cases:
            if test.id == test_id:
                return test
        return None

    def get_tests_by_level(self, level: int) -> List[TestCase]:
        """Get all tests for a specific level"""
        return [test for test in self.test_cases if test.level == level]

    def get_tests_by_domain(self, domain: TemporalDomain) -> List[TestCase]:
        """Get all tests for a specific domain"""
        return [test for test in self.test_cases if test.domain == domain]

    def get_tests_by_difficulty(self, difficulty: str) -> List[TestCase]:
        """Get all tests of a specific difficulty"""
        return [test for test in self.test_cases if test.difficulty == difficulty]

    def export_to_json(self, filepath: str):
        """Export all test cases to JSON file"""
        data = {
            "test_suite": "Temporal Reasoning Test Cases",
            "version": "1.0",
            "total_tests": len(self.test_cases),
            "tests": [test.to_dict() for test in self.test_cases]
        }
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def summary(self) -> str:
        """Generate a summary of the test suite"""
        level_counts = {}
        domain_counts = {}
        difficulty_counts = {}

        for test in self.test_cases:
            level_counts[test.level] = level_counts.get(test.level, 0) + 1
            domain_counts[test.domain.value] = domain_counts.get(test.domain.value, 0) + 1
            difficulty_counts[test.difficulty] = difficulty_counts.get(test.difficulty, 0) + 1

        summary = []
        summary.append("=" * 80)
        summary.append("TEMPORAL REASONING TEST SUITE SUMMARY")
        summary.append("=" * 80)
        summary.append(f"Total Test Cases: {len(self.test_cases)}")
        summary.append("")
        summary.append("By Level:")
        for level in sorted(level_counts.keys()):
            summary.append(f"  Level {level}: {level_counts[level]} tests")
        summary.append("")
        summary.append("By Domain:")
        for domain in sorted(domain_counts.keys()):
            summary.append(f"  {domain}: {domain_counts[domain]} tests")
        summary.append("")
        summary.append("By Difficulty:")
        for difficulty in sorted(difficulty_counts.keys()):
            summary.append(f"  {difficulty}: {difficulty_counts[difficulty]} tests")
        summary.append("=" * 80)

        return "\n".join(summary)


if __name__ == "__main__":
    # Display test suite summary
    suite = TestSuite()
    print(suite.summary())

    # Display sample test cases
    print("\n\nSAMPLE TEST CASES:")
    print("=" * 80)

    # Show one from each level
    for level in [1, 2, 3]:
        tests = suite.get_tests_by_level(level)
        if tests:
            test = tests[0]
            print(f"\nLevel {level} Example - {test.id} ({test.domain.value}):")
            print(f"Question: {test.question}")
            print(f"Context: {test.context}")
            print(f"Ground Truth: {test.ground_truth_answer}")
            print(f"Events: {test.ground_truth_events}")
            if test.ground_truth_relations:
                print(f"Relations: {test.ground_truth_relations}")
            if test.expected_duration:
                print(f"Expected Duration: {test.expected_duration} seconds")
            print("-" * 80)

    # Export to JSON
    print("\n\nExporting test cases to JSON...")
    suite.export_to_json("/tmp/paper_research/prototype/test_cases.json")
    print("Exported to: /tmp/paper_research/prototype/test_cases.json")
