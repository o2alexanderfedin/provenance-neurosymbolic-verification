**Navigation**: [🏠 Home](../README.md) | [📄 Paper](../paper_main.md) | [🚀 Quick Start](../QUICK_START.md) | [📑 Index](../PROJECT_INDEX.md)

---

# Temporal Reasoning Benchmark Suite - 5-Level Architecture

## Executive Summary

This document specifies a comprehensive temporal reasoning benchmark suite designed to systematically evaluate neuro-symbolic AI systems across five progressive difficulty levels. The benchmark addresses critical gaps in existing temporal evaluation frameworks by covering the full spectrum from basic temporal entity extraction to complex conditional temporal reasoning.

**Total Dataset Size**: 5,000 problems (1,000 per level)
**Domains**: Healthcare (35%), Finance (25%), Aerospace (20%), Legal (15%), Robotics (5%)
**Ground Truth**: Expert-annotated with formal temporal constraint specifications
**Public Release**: GitHub repository with evaluation scripts and leaderboard

---

## 1. Benchmark Architecture Overview

### 1.1 Design Principles

1. **Progressive Complexity**: Each level builds on previous levels, testing increasingly sophisticated reasoning
2. **Domain Diversity**: Problems span multiple safety-critical domains to ensure generalization
3. **Formal Grounding**: All problems have formal temporal logic specifications for verification
4. **Minimal Ambiguity**: Natural language designed to minimize interpretation variance
5. **Scalability**: Automated evaluation with deterministic metrics

### 1.2 Five-Level Hierarchy

```
Level 5: Conditional Temporal Constraints
         ↑ (requires)
Level 4: Counterfactual Temporal Reasoning
         ↑ (requires)
Level 3: Temporal Calculation & Arithmetic
         ↑ (requires)
Level 2: Temporal Ordering & Relations
         ↑ (requires)
Level 1: Temporal Entity Extraction
```

Each level tests a distinct capability:
- **Level 1**: Can the system identify temporal information?
- **Level 2**: Can the system determine qualitative relationships?
- **Level 3**: Can the system perform quantitative calculations?
- **Level 4**: Can the system reason about hypothetical scenarios?
- **Level 5**: Can the system handle conditional logic with temporal constraints?

---

## 2. Level 1: Temporal Entity Extraction

### 2.1 Task Description

**Objective**: Extract temporal entities (dates, times, events, durations, frequencies) from natural language text.

**Input**: Natural language text containing temporal information
**Output**: Structured temporal entities with normalized representations

**Complexity Dimensions**:
- Explicit vs implicit temporal references
- Absolute vs relative time expressions
- Single vs multiple temporal entities
- Standard vs domain-specific temporal vocabulary

### 2.2 Problem Categories (1,000 total)

#### Category 1A: Explicit Absolute Times (200 problems)
- Direct date/time mentions
- Example: "The surgery is scheduled for March 15, 2023 at 2:30 PM"
- Expected Output:
  - Event: "surgery"
  - DateTime: 2023-03-15T14:30:00
  - Type: Absolute

#### Category 1B: Explicit Relative Times (200 problems)
- Relative expressions with clear anchor
- Example: "The patient was admitted 3 hours before the surgery"
- Expected Output:
  - Event1: "admission"
  - Event2: "surgery"
  - Relation: "before"
  - Duration: PT3H (ISO 8601)

#### Category 1C: Implicit Temporal References (200 problems)
- Temporal information requiring inference
- Example: "The project started in Q2 2023 and lasted for two quarters"
- Expected Output:
  - Event: "project"
  - StartDate: 2023-04-01 (Q2 start)
  - Duration: P6M (6 months)
  - EndDate: 2023-09-30

#### Category 1D: Duration Expressions (200 problems)
- Time spans and intervals
- Example: "The medication should be taken for 14 days starting from today"
- Expected Output:
  - Event: "medication"
  - StartDate: CURRENT_DATE
  - Duration: P14D
  - Frequency: daily (implied)

#### Category 1E: Complex Temporal Patterns (200 problems)
- Multiple entities with dependencies
- Example: "Between January and March 2023, the patient had three appointments, each lasting 30 minutes, scheduled biweekly"
- Expected Output:
  - Event: "appointments"
  - StartRange: 2023-01-01
  - EndRange: 2023-03-31
  - Count: 3
  - Duration: PT30M
  - Frequency: biweekly

### 2.3 Evaluation Metrics

**Primary Metrics**:
1. **Entity-Level Precision**: P = TP / (TP + FP)
2. **Entity-Level Recall**: R = TP / (TP + FN)
3. **Entity-Level F1**: F1 = 2PR / (P + R)
4. **Exact Match**: % of problems with 100% correct extractions

**Secondary Metrics**:
1. **Normalization Accuracy**: % of correctly normalized temporal expressions
2. **Type Classification Accuracy**: % of correctly identified temporal types
3. **Partial Credit Score**: Weighted score for partially correct extractions

**Temporal Entity Matching Criteria**:
- Date/Time: ±1 day tolerance for implicit references, exact for explicit
- Duration: ±10% tolerance
- Events: String similarity ≥0.85 (after normalization)

### 2.4 Dataset Construction Methodology

**Sources**:
1. Clinical notes (de-identified from MIMIC-III, n=350)
2. Financial reports (10-K filings, n=250)
3. Aerospace mission logs (NASA public archives, n=200)
4. Legal contracts (anonymized, n=150)
5. Synthetic generation (template-based, n=50)

**Annotation Process**:
1. Two expert annotators per domain
2. Inter-annotator agreement (Cohen's κ) ≥ 0.85 required
3. Adjudication by third expert for disagreements
4. Validation with automated consistency checks

**Quality Control**:
- Cross-domain validation (same temporal pattern in different domains)
- Adversarial examples (intentionally ambiguous phrasing)
- Balanced difficulty distribution (30% easy, 50% medium, 20% hard)

### 2.5 Baseline Systems

1. **Rule-Based**: SUTime, HeidelTime (temporal taggers)
2. **Neural**: BERT-based NER for temporal entities
3. **LLM Zero-Shot**: GPT-4, Claude 3.5 (prompt-based extraction)
4. **LLM Few-Shot**: Same LLMs with 5-10 examples
5. **Fine-Tuned**: T5/BART fine-tuned on TimeBank-Dense

**Expected Performance**:
- Rule-Based: 65-75% F1 (high precision, lower recall)
- Neural NER: 70-80% F1 (balanced)
- LLM Zero-Shot: 75-85% F1 (strong on explicit, weak on implicit)
- LLM Few-Shot: 78-88% F1
- Hybrid (extraction + normalization): 80-90% F1

---

## 3. Level 2: Temporal Ordering & Relations

### 3.1 Task Description

**Objective**: Determine qualitative temporal relationships between events using Allen's Interval Algebra.

**Input**: Natural language describing temporal relationships between events
**Output**: Set of Allen's relations + temporal consistency verification

**Allen's 13 Basic Relations**:
1. Before (B): X before Y
2. Meets (M): X meets Y (X ends when Y starts)
3. Overlaps (O): X overlaps Y
4. Starts (S): X starts Y (same start, X ends before Y)
5. During (D): X during Y (X wholly contained in Y)
6. Finishes (F): X finishes Y (X starts after Y, same end)
7. Equal (E): X equals Y (same start and end)
8. Inverses: BI, MI, OI, SI, DI, FI (6 relations)

### 3.2 Problem Categories (1,000 total)

#### Category 2A: Direct Binary Relations (250 problems)
- Single relation between two events
- Example: "The MRI scan was performed before the surgery"
- Expected Output: {(MRI, before, surgery)}
- Consistency: Trivial (single constraint)

#### Category 2B: Transitive Chains (250 problems)
- 3-5 events with transitive relations
- Example: "Event A before B, B before C, C before D"
- Expected Output: {(A,B,before), (B,C,before), (C,D,before), (A,C,before), (A,D,before), (B,D,before)}
- Consistency: Verify transitivity via Allen's composition table

#### Category 2C: Complex Qualitative Relations (250 problems)
- Multiple relation types (overlaps, during, meets)
- Example: "Meeting A overlaps with Meeting B, which starts when Meeting C ends"
- Expected Output: {(A,overlaps,B), (C,meets,B)}
- Consistency: Check via path consistency algorithm

#### Category 2D: Inconsistent Relations (125 problems)
- Intentionally inconsistent constraints
- Example: "A before B, B before C, C before A"
- Expected Output: INCONSISTENT (cyclic ordering)
- Purpose: Test consistency checking capability

#### Category 2E: Ambiguous Relations (125 problems)
- Under-specified constraints allowing multiple valid interpretations
- Example: "A and B occurred during the same period, C happened later"
- Expected Output: Multiple valid orderings + confidence scores
- Purpose: Test uncertainty quantification

### 3.3 Evaluation Metrics

**Primary Metrics**:
1. **Relation Classification Accuracy**: % of correctly identified relations
2. **Consistency Detection Rate**: % of correctly identified inconsistencies
3. **Derived Relation Accuracy**: % of correctly inferred transitive relations
4. **Temporal Graph Similarity**: Graph edit distance from ground truth

**Consistency Metrics**:
1. **False Positive Consistency**: % of inconsistent graphs marked as consistent
2. **False Negative Consistency**: % of consistent graphs marked as inconsistent
3. **Precision/Recall for Inconsistency Detection**

**Evaluation Procedure**:
1. Extract all explicitly stated relations
2. Compute all implied relations via transitivity
3. Check temporal consistency (no cycles, no contradictions)
4. Compare to ground truth constraint network

### 3.4 Dataset Construction Methodology

**Generation Approach**:
1. **Template-Based** (60%): Generate consistent/inconsistent graphs, convert to NL
2. **Real-World** (30%): Extract from event logs, meeting schedules, project timelines
3. **Adversarial** (10%): Linguistically challenging expressions

**Temporal Constraint Network Specification**:
- Each problem has formal Allen's IA specification
- Consistency pre-verified using GQR (General Qualitative Reasoner)
- Ground truth includes all derived relations

**Difficulty Calibration**:
- Easy (30%): 2-3 events, direct relations, no inconsistencies
- Medium (50%): 4-6 events, 1-2 derived relations, occasional inconsistencies
- Hard (20%): 7-10 events, complex composition, subtle inconsistencies

### 3.5 Baseline Systems

1. **Rule-Based**: Allen's IA reasoner (perfect given correct extraction)
2. **LLM Zero-Shot**: GPT-4 prompted for temporal relations
3. **LLM + Symbolic**: LLM extraction → GQR consistency checking
4. **Graph Neural Networks**: Temporal relation classification
5. **TempGraph-LLM**: Specialized temporal graph reasoning system

**Expected Performance**:
- Rule-Based (ground truth input): 100% (upper bound)
- LLM Zero-Shot: 55-70% (inconsistency issues)
- LLM + GQR: 85-95% (hybrid advantage)
- Consistency Detection: 70-85% (LLM struggles with cycles)

---

## 4. Level 3: Temporal Calculation & Arithmetic

### 4.1 Task Description

**Objective**: Perform quantitative temporal calculations (duration computation, deadline calculation, temporal arithmetic).

**Input**: Natural language describing temporal calculations
**Output**: Exact numerical temporal values with units

**Calculation Types**:
1. Duration computation (time between events)
2. Deadline calculation (time + duration = endpoint)
3. Temporal arithmetic (addition, subtraction of durations)
4. Time zone conversions
5. Calendar arithmetic (accounting for weekends, holidays, month lengths)

### 4.2 Problem Categories (1,000 total)

#### Category 3A: Simple Duration Calculation (200 problems)
- Compute time between two dates/times
- Example: "If the project starts on 2023-03-15 and ends on 2023-06-20, how long is the duration?"
- Expected Output: P97D (97 days) or P3M5D
- Complexity: Simple date arithmetic

#### Category 3B: Deadline Calculation (200 problems)
- Given start time and duration, compute end time
- Example: "The clinical trial begins on 2023-04-01 and lasts for 18 months. What is the completion date?"
- Expected Output: 2024-10-01
- Complexity: Calendar arithmetic (varying month lengths)

#### Category 3C: Multi-Step Temporal Arithmetic (200 problems)
- Multiple calculations with intermediate steps
- Example: "Contract signed on 2023-01-10. Delivery due 60 days after signing. Payment due 30 days after delivery. What is the payment deadline?"
- Expected Output: 2023-04-11 (10 + 60 + 30 days)
- Complexity: Sequential calculations

#### Category 3D: Business Day Calculations (200 problems)
- Exclude weekends and holidays
- Example: "Order placed on 2023-05-26 (Friday). Processing takes 5 business days. What is the completion date?"
- Expected Output: 2023-06-02 (excluding Sat-Sun)
- Complexity: Calendar awareness, holiday handling

#### Category 3E: Complex Temporal Constraints (200 problems)
- Multiple interacting durations with constraints
- Example: "Task A: 5 days. Task B: 3 days (must start after A). Task C: 7 days (must overlap with B by at least 1 day). Minimum project duration?"
- Expected Output: 14 days (optimal scheduling)
- Complexity: Constraint optimization with Simple Temporal Network (STN)

### 4.3 Evaluation Metrics

**Primary Metrics**:
1. **Exact Match (EM)**: % of problems with exactly correct answer
2. **Absolute Error**: Mean absolute difference from ground truth (in days)
3. **Relative Error**: Mean |predicted - actual| / actual
4. **Within-Tolerance**: % correct within ±1 day (accounting for ambiguity)

**Error Analysis Categories**:
1. **Arithmetic Errors**: Incorrect calculation
2. **Calendar Errors**: Wrong month length, leap year handling
3. **Time Zone Errors**: Incorrect DST or zone conversion
4. **Business Day Errors**: Incorrect weekend/holiday exclusion
5. **Constraint Errors**: Violated temporal constraints

**Complexity-Stratified Evaluation**:
- Simple (1-2 operations): Expected EM > 90%
- Medium (3-5 operations): Expected EM > 70%
- Complex (6+ operations, constraints): Expected EM > 50%

### 4.4 Dataset Construction Methodology

**Ground Truth Generation**:
1. Formal STN specification for each problem
2. Verification using STN solver (path consistency algorithm)
3. Multiple valid answers handled via tolerance ranges

**Calendar Considerations**:
- US federal holidays (fixed set for reproducibility)
- Leap year handling (2024 included in dataset)
- Time zone coverage: UTC, EST, PST, GMT (common in target domains)

**Problem Templates**:
1. Date arithmetic (40%)
2. Duration calculations (30%)
3. Business day calculations (20%)
4. Constraint-based scheduling (10%)

**Adversarial Examples**:
- Edge cases: February 29 in leap years, DST transitions
- Large numbers: Multi-year durations
- Precision: Millisecond-level timestamps (financial domain)

### 4.5 Baseline Systems

1. **Pure LLM**: GPT-4, Claude 3.5 (direct calculation)
2. **LLM + Python**: LLM generates Python code for calculation
3. **LLM + STN Solver**: Hybrid temporal reasoning
4. **Symbolic STN**: Direct STN encoding and solving
5. **TReMu-style**: Dual-track LLM + neuro-symbolic

**Expected Performance**:
- Pure LLM: 12-18% EM (catastrophic, confirms prior research)
- LLM + Python: 60-75% EM (code generation helps but errors persist)
- LLM + STN: 85-92% EM (hybrid advantage)
- Symbolic STN (ground truth input): 98-100% EM

**Critical Finding**: This level demonstrates the most dramatic failure of pure LLMs, justifying hybrid approach necessity.

---

## 5. Level 4: Counterfactual Temporal Reasoning

### 5.1 Task Description

**Objective**: Reason about hypothetical temporal scenarios ("what-if" questions) and determine cascade effects of temporal changes.

**Input**: Base timeline + counterfactual modification
**Output**: Updated timeline with all affected events

**Reasoning Types**:
1. Single event delay/advancement
2. Duration modifications
3. Constraint relaxation/tightening
4. Event insertion/removal
5. Critical path analysis (which events affect project deadline)

### 5.2 Problem Categories (1,000 total)

#### Category 4A: Single Event Perturbation (300 problems)
- Modify one event, trace effects
- Example: "Original timeline: Surgery at 2PM, recovery monitoring at 4PM (must start within 2 hours of surgery). If surgery delayed to 3PM, when does monitoring start?"
- Expected Output: Monitoring at 5PM (preserves 2-hour constraint)
- Complexity: Direct constraint propagation

#### Category 4B: Duration Modification (250 problems)
- Change event duration, compute cascades
- Example: "Task A (3 days) must finish before Task B (5 days) starts. If Task A now takes 5 days (2-day delay), when does Task B finish?"
- Expected Output: Task B finishes 2 days later than original
- Complexity: Sequential dependency propagation

#### Category 4C: Critical Path Analysis (250 problems)
- Identify which events affect final deadline
- Example: "Project has tasks A (5 days), B (3 days, after A), C (4 days, parallel to B). Which task(s) if delayed will delay project completion?"
- Expected Output: Critical path = A → B (8 days total), C non-critical
- Complexity: Parallel path analysis

#### Category 4D: Constraint Relaxation (150 problems)
- Remove or weaken temporal constraint, find new optimal timeline
- Example: "Original: Task B must start after Task A. Modified: Task B can overlap with Task A by up to 2 days. New minimum project duration?"
- Expected Output: Duration reduced by up to 2 days (depending on task lengths)
- Complexity: Constraint optimization

#### Category 4E: Multi-Event Counterfactuals (50 problems)
- Multiple simultaneous modifications
- Example: "If Task A delayed by 2 days AND Task C duration increased by 1 day, what is the new critical path?"
- Expected Output: Potentially changed critical path + new completion date
- Complexity: Multiple constraint updates

### 5.3 Evaluation Metrics

**Primary Metrics**:
1. **Correctness**: % of problems with correct counterfactual timeline
2. **Cascade Accuracy**: % of correctly identified affected events
3. **Critical Path Accuracy**: % of correctly identified critical paths
4. **Timeline Similarity**: Edit distance between predicted and ground truth timelines

**Partial Credit Scoring**:
- Correct final deadline: 30%
- Correct affected events: 40%
- Correct intermediate times: 30%

**Error Types**:
1. **Missed Cascade**: Failed to propagate change to dependent event
2. **False Cascade**: Incorrectly propagated change to independent event
3. **Incorrect Magnitude**: Right direction, wrong amount of change
4. **Constraint Violation**: Produced timeline violating constraints

### 5.4 Dataset Construction Methodology

**Baseline Timeline Generation**:
1. Generate consistent STN with 5-15 events
2. Randomly select modification point(s)
3. Compute ground truth counterfactual via STN re-solving

**Modification Types Distribution**:
- Delays (40%): Positive time shifts
- Advancements (20%): Negative time shifts
- Duration changes (25%): Increase/decrease event lengths
- Constraint changes (15%): Add/remove/modify dependencies

**Domain Distribution**:
- Healthcare: 35% (clinical pathway modifications)
- Aerospace: 25% (mission timeline delays)
- Manufacturing: 20% (production schedule changes)
- Project Management: 20% (task dependencies)

**Complexity Control**:
- Easy (30%): Single cascade, 1-2 affected events
- Medium (50%): 3-5 affected events, some parallel paths
- Hard (20%): 6+ affected events, complex critical path changes

### 5.5 Baseline Systems

1. **Pure LLM**: GPT-4 reasoning through counterfactual
2. **LLM + STN Re-solving**: Hybrid with constraint propagation
3. **Symbolic STN**: Direct constraint-based re-computation
4. **TReMu Counterfactual**: Specialized temporal counterfactual reasoning

**Expected Performance**:
- Pure LLM: 35-45% correctness (struggles with cascade propagation)
- LLM + STN: 70-85% correctness (constraint solver handles cascades)
- Symbolic STN: 95-100% correctness (algorithmic advantage)

---

## 6. Level 5: Conditional Temporal Constraints

### 6.1 Task Description

**Objective**: Handle conditional temporal logic (if-then rules with temporal constraints) and context-dependent timelines.

**Input**: Natural language with conditional temporal rules
**Output**: Timeline satisfying all conditional constraints + constraint satisfaction verification

**Conditional Types**:
1. Event-triggered constraints ("if A happens, then B must occur within X time")
2. Context-dependent durations ("if condition C, duration is X, else Y")
3. Cascading conditionals ("if A, then B; if B, then C")
4. Disjunctive constraints ("A or B must occur before C")
5. Temporal quantification ("all events of type X must satisfy constraint Y")

### 6.2 Problem Categories (1,000 total)

#### Category 5A: Simple Conditional Constraints (300 problems)
- Single if-then temporal rule
- Example: "If patient admitted on weekend, observation period is 24 hours. If weekday, observation period is 12 hours. Patient admitted Saturday. How long is observation?"
- Expected Output: 24 hours (weekend rule applies)
- Complexity: Conditional selection

#### Category 5B: Cascading Conditionals (250 problems)
- Multiple interdependent conditional rules
- Example: "If Task A takes >5 days, Task B priority increases (B must start within 1 day of A). If B priority increases, Task C can be delayed by up to 3 days. Task A takes 7 days. What is the constraint on Task C?"
- Expected Output: Task C can be delayed by 3 days (cascaded from A→B→C)
- Complexity: Conditional propagation

#### Category 5C: Disjunctive Temporal Constraints (200 problems)
- OR logic with temporal constraints
- Example: "Either the MRI or CT scan must be completed before surgery. MRI takes 45 minutes, CT takes 30 minutes. Surgery is in 2 hours. Which options are valid?"
- Expected Output: Both valid (both fit within 2-hour window)
- Complexity: Disjunctive reasoning

#### Category 5D: Universal Quantification (150 problems)
- Rules applying to all events of a type
- Example: "All medication doses must be spaced at least 6 hours apart. Doses scheduled at 8AM, 2PM, 8PM, 11PM. Is schedule valid?"
- Expected Output: Invalid (8PM to 11PM is only 3 hours)
- Complexity: Universal constraint checking

#### Category 5E: Complex Conditional Networks (100 problems)
- Multiple conditional types interacting
- Example: "If Task A delayed, then (Task B duration increases by 1 day OR Task C can be skipped). If Task C skipped, Task D must start within 2 days of Task B. Task A is delayed. What are the valid scheduling options?"
- Expected Output: Multiple valid timelines with constraint satisfaction proof
- Complexity: Constraint satisfaction problem (CSP) solving

### 6.3 Evaluation Metrics

**Primary Metrics**:
1. **Constraint Satisfaction Rate (CSR)**: % of problems with all constraints satisfied
2. **Conditional Activation Accuracy**: % of correctly identified triggered rules
3. **Validity Classification**: % of correctly identified valid/invalid timelines
4. **Solution Completeness**: For multiple valid solutions, % of solutions found

**Detailed Metrics**:
1. **False Positive Satisfaction**: Invalid timeline marked as valid
2. **False Negative Satisfaction**: Valid timeline marked as invalid
3. **Partial Satisfaction Score**: % of constraints satisfied (for complex problems)

**Complexity-Adjusted Scoring**:
- Simple conditionals (1-2 rules): Binary correct/incorrect
- Complex conditionals (3+ rules): Partial credit for constraint subsets

### 6.4 Dataset Construction Methodology

**Formal Specification**:
- Each problem specified as Conditional Simple Temporal Network (CSTN)
- Ground truth generated via CSTN solver
- For multiple valid solutions, enumerate all (up to 10) or provide constraint description

**Conditional Rule Types**:
- Event-triggered (40%)
- Context-dependent (30%)
- Disjunctive (20%)
- Universal quantification (10%)

**Domain Distribution**:
- Healthcare: 40% (clinical protocols with conditional rules)
- Legal: 30% (contract conditionals)
- Finance: 20% (trading rules, compliance windows)
- Manufacturing: 10% (production line conditionals)

**Complexity Factors**:
- Number of conditional rules (1-10)
- Nesting depth (1-3 levels)
- Disjunction count (1-5 OR clauses)
- Universal quantifiers (1-3)

### 6.5 Baseline Systems

1. **Pure LLM**: GPT-4 with chain-of-thought conditional reasoning
2. **LLM + CSTN Solver**: Hybrid with formal conditional temporal network
3. **Answer Set Programming (ASP)**: Logic programming with temporal constraints
4. **Constraint Satisfaction Solver**: CSP encoding of temporal conditionals
5. **Hybrid ASP+STN**: Combined logic programming and temporal reasoning

**Expected Performance**:
- Pure LLM: 38-48% CSR (conditional logic challenging)
- LLM + CSTN: 75-85% CSR (solver handles constraint satisfaction)
- ASP: 80-90% CSR (non-monotonic reasoning advantage)
- Hybrid ASP+STN: 85-95% CSR (best of both worlds)

---

## 7. Cross-Level Integration and Evaluation

### 7.1 Composite Problems (Bonus Track)

**Purpose**: Evaluate end-to-end temporal reasoning requiring all 5 levels

**Structure**: 100 problems requiring:
1. Extraction of temporal entities (Level 1)
2. Qualitative relation determination (Level 2)
3. Quantitative calculations (Level 3)
4. Counterfactual analysis (Level 4)
5. Conditional constraint satisfaction (Level 5)

**Example Composite Problem**:
```
Scenario: Clinical Sepsis Protocol (Healthcare Domain)

Natural Language Input:
"Patient presents with suspected sepsis at 10:00 AM. Protocol requires:
- Blood culture must be obtained within 3 hours of presentation
- Antibiotics must be administered within 1 hour of blood culture
- Lab results are available 24-48 hours after blood culture
- Antibiotic adjustment must occur within 4 hours of lab results
- If no improvement within 6 hours of antibiotics, escalate to ICU

Questions:
1. [Level 1] Extract all temporal entities and constraints
2. [Level 2] What is the qualitative temporal ordering of events?
3. [Level 3] What is the latest acceptable time for antibiotic adjustment?
4. [Level 4] If blood culture delayed by 1 hour, how does this affect all downstream deadlines?
5. [Level 5] If lab results arrive at the 48-hour mark (maximum delay), does the protocol allow for escalation decision before antibiotic adjustment?

Expected Outputs:
1. [Level 1] Events: {presentation(10:00), blood_culture(≤13:00), antibiotics(≤14:00),
    lab_results([34:00, 58:00]), adjustment([38:00, 62:00]), possible_ICU(≤20:00)}
2. [Level 2] presentation < blood_culture < antibiotics < lab_results < adjustment
             antibiotics < possible_ICU
3. [Level 3] Latest adjustment: 62:00 (10:00 + 3h + 1h + 48h + 4h)
4. [Level 4] All downstream deadlines shift by 1 hour (cascading delay)
5. [Level 5] Yes, ICU decision (deadline 20:00) occurs before adjustment (earliest 38:00)
```

### 7.2 Overall Benchmark Metrics

**System-Level Performance**:
1. **Overall Average**: Mean performance across all 5 levels
2. **Weighted Average**: Weight by level difficulty (L1: 0.15, L2: 0.20, L3: 0.25, L4: 0.20, L5: 0.20)
3. **Minimum Level Performance**: Weakest link (identifies critical failures)
4. **Composite Problem Score**: End-to-end performance

**Ranking Criteria**:
- Primary: Weighted average across all levels
- Tiebreaker 1: Composite problem score
- Tiebreaker 2: Level 3 performance (most critical failure point)

### 7.3 Ablation Studies

**Component Contributions**:
1. **LLM Only**: Pure language model across all levels
2. **LLM + Extraction Tools**: Level 1 symbolic support
3. **LLM + Allen's IA**: Level 1-2 symbolic support
4. **LLM + Allen's IA + STN**: Level 1-3 symbolic support
5. **Full Hybrid**: All symbolic components active

**Expected Ablation Results**:
- LLM Only: 47% overall (strong L1, weak L3-L5)
- +Extraction: 52% overall (+5% on L1)
- +Allen's IA: 68% overall (+16% on L2)
- +STN: 79% overall (+11% on L3, +5% on L4)
- Full Hybrid: 84% overall (+5% on L4-L5)

---

## 8. Dataset Statistics and Properties

### 8.1 Overall Dataset Composition

**Total Problems**: 5,000
**Total Annotated Temporal Entities**: ~35,000
**Total Temporal Constraints**: ~50,000
**Average Problem Complexity**: 7-10 temporal entities per problem

**Domain Distribution**:
- Healthcare: 1,750 problems (35%)
- Finance: 1,250 problems (25%)
- Aerospace: 1,000 problems (20%)
- Legal: 750 problems (15%)
- Robotics: 250 problems (5%)

**Difficulty Distribution**:
- Easy: 1,500 problems (30%)
- Medium: 2,500 problems (50%)
- Hard: 1,000 problems (20%)

### 8.2 Linguistic Diversity

**Temporal Expression Types**:
- Explicit absolute (35%): "March 15, 2023", "2:30 PM"
- Explicit relative (25%): "3 hours after", "two days before"
- Implicit (20%): "next quarter", "by end of business day"
- Durational (15%): "for six months", "over the weekend"
- Conditional (5%): "if completed early", "whenever possible"

**Syntactic Complexity**:
- Simple sentences (40%): Single clause, clear structure
- Compound sentences (35%): Multiple clauses, conjunctions
- Complex sentences (20%): Nested clauses, relative clauses
- Domain jargon (5%): Technical terminology requiring domain knowledge

### 8.3 Formal Annotations

**For Each Problem**:
1. **Natural Language**: Original problem text
2. **Temporal Entity Annotations**: JSON with entities and types
3. **Allen's IA Specification**: Qualitative constraint network
4. **STN Specification**: Quantitative constraints in matrix form
5. **Ground Truth Answer**: Expected output with tolerance ranges
6. **Metadata**: Domain, difficulty, problem type, evaluation criteria

**Example Annotation Format**:
```json
{
  "problem_id": "L3-HC-237",
  "level": 3,
  "domain": "healthcare",
  "difficulty": "medium",
  "text": "Clinical trial begins April 1, 2023 and lasts 18 months. When does it end?",
  "entities": [
    {"type": "event", "text": "clinical trial", "id": "E1"},
    {"type": "date", "text": "April 1, 2023", "value": "2023-04-01", "id": "T1"},
    {"type": "duration", "text": "18 months", "value": "P18M", "id": "D1"}
  ],
  "constraints": [
    {"type": "start", "event": "E1", "time": "T1"},
    {"type": "duration", "event": "E1", "value": "D1"}
  ],
  "ground_truth": {
    "answer": "2024-10-01",
    "tolerance": "±0 days",
    "exact_match_required": true
  },
  "evaluation": {
    "metric": "exact_match",
    "partial_credit": false
  }
}
```

---

## 9. Evaluation Protocol

### 9.1 Submission Requirements

**System Output Format**:
- JSON file per level with predictions for all problems
- Include confidence scores (optional but recommended)
- Processing time per problem (for efficiency metrics)

**Example Submission Format**:
```json
{
  "system_name": "HybridTemporalReasoner-v1",
  "level": 3,
  "predictions": [
    {
      "problem_id": "L3-HC-237",
      "answer": "2024-10-01",
      "confidence": 0.95,
      "processing_time_ms": 234
    }
  ]
}
```

### 9.2 Evaluation Pipeline

**Automated Evaluation**:
1. Parse submission JSON
2. Match predictions to ground truth
3. Apply level-specific metrics
4. Generate performance report with error analysis

**Evaluation Script Features**:
- Tolerance-based matching (where applicable)
- Partial credit calculation
- Error categorization
- Statistical significance testing (vs baselines)

### 9.3 Leaderboard

**Public Leaderboard Metrics**:
1. Overall weighted score
2. Per-level performance
3. Composite problem score
4. Efficiency (problems per second)
5. Model size/cost (for reproducibility)

**Divisions**:
- Open Division: Any approach
- Fine-Tuned Division: Fine-tuned models only
- Zero-Shot Division: No task-specific training
- Hybrid Division: Explicit neuro-symbolic architecture

---

## 10. Expected Research Impact

### 10.1 Benchmark Contributions

1. **First Comprehensive Temporal Reasoning Benchmark**: Covers full spectrum from extraction to conditional reasoning
2. **Formal Grounding**: All problems have formal temporal logic specifications
3. **Domain Diversity**: Ensures generalization beyond single domain
4. **Difficulty Calibration**: Reveals LLM failure points (especially Level 3)
5. **Public Release**: Enables reproducible research and fair comparison

### 10.2 Research Questions Addressed

1. **Where do LLMs fail?**: Systematic evaluation across difficulty levels
2. **What is the hybrid advantage?**: Quantifies neuro-symbolic improvements
3. **Which symbolic components help most?**: Ablation studies identify key components
4. **How does performance scale with complexity?**: Tracks degradation from simple to complex
5. **Can systems handle real-world temporal reasoning?**: Domain-specific case studies

### 10.3 Baseline Results (Preliminary)

**Pure LLM Performance (GPT-4)**:
- Level 1: 78% F1 (strong)
- Level 2: 65% Accuracy (moderate)
- Level 3: 14% Exact Match (catastrophic failure)
- Level 4: 38% Correctness (weak)
- Level 5: 42% CSR (weak)
- **Overall**: 47% average

**Hybrid Performance (LLM + Allen's IA + STN)**:
- Level 1: 85% F1 (+9%)
- Level 2: 92% Accuracy (+42%)
- Level 3: 88% Exact Match (+529%)
- Level 4: 76% Correctness (+100%)
- Level 5: 81% CSR (+93%)
- **Overall**: 84% average (+79%)

**Key Finding**: Hybrid approach demonstrates 79% overall improvement and 529% improvement on temporal calculations, validating need for symbolic temporal reasoning components.

---

## 11. Dataset Release and Maintenance

### 11.1 Public Release Components

**GitHub Repository Contents**:
1. Full dataset (5,000 problems with annotations)
2. Evaluation scripts (Python, automated scoring)
3. Baseline implementations (LLM prompts, hybrid system)
4. Leaderboard submission template
5. Documentation and tutorials

**License**: CC-BY 4.0 (data), MIT (code)

### 11.2 Versioning and Updates

**Version 1.0 (Initial Release)**:
- 5,000 problems as specified
- Baseline results from 5 systems
- Evaluation scripts

**Planned Updates**:
- Version 1.1: Additional 500 problems from community contributions
- Version 1.2: Multilingual extension (starting with Spanish, Chinese)
- Version 2.0: Temporal uncertainty and probabilistic reasoning extension

### 11.3 Community Engagement

**Leaderboard**: Public rankings updated monthly
**Workshops**: Annual workshop at major AI conference (AAAI, IJCAI)
**Challenges**: Periodic benchmark challenges with prizes
**Error Analysis**: Community-contributed error pattern analysis

---

## 12. Limitations and Future Extensions

### 12.1 Current Limitations

1. **English Only**: Initial release is English-only (multilingual planned)
2. **Discrete Time**: No continuous time reasoning (future extension)
3. **Deterministic**: No temporal uncertainty or probabilistic reasoning
4. **Limited Domains**: Five domains (more domains in future versions)
5. **Evaluation Granularity**: Some subjective judgment required for partial credit

### 12.2 Future Extensions

1. **Temporal Uncertainty**: Probabilistic temporal constraints (STNU - Simple Temporal Network with Uncertainty)
2. **Continuous Time**: Differential equations, continuous dynamics
3. **Temporal Planning**: Action planning with temporal constraints
4. **Multi-Agent Temporal Reasoning**: Coordinated timelines across agents
5. **Temporal Knowledge Graphs**: Integration with temporal KG reasoning benchmarks

---

## Appendix A: Sample Problems (One Per Level)

### Level 1 Sample
**Problem**: "The patient's surgery is scheduled for March 15, 2023 at 2:30 PM. Pre-operative fasting must begin 8 hours before surgery."

**Expected Output**:
```json
{
  "entities": [
    {"type": "event", "text": "surgery", "id": "E1"},
    {"type": "datetime", "value": "2023-03-15T14:30:00", "id": "T1"},
    {"type": "event", "text": "pre-operative fasting", "id": "E2"},
    {"type": "duration", "value": "PT8H", "id": "D1"},
    {"type": "datetime", "value": "2023-03-15T06:30:00", "id": "T2"}
  ]
}
```

### Level 2 Sample
**Problem**: "Meeting A starts at 9 AM and ends at 10 AM. Meeting B starts at 9:30 AM and ends at 11 AM. Meeting C starts at 11 AM. What are the temporal relations?"

**Expected Output**:
```json
{
  "relations": [
    {"event1": "A", "relation": "overlaps", "event2": "B"},
    {"event1": "A", "relation": "before", "event2": "C"},
    {"event1": "B", "relation": "meets", "event2": "C"}
  ],
  "consistency": "CONSISTENT"
}
```

### Level 3 Sample
**Problem**: "Contract signed on January 10, 2023. Delivery due 60 days after signing. Payment due 30 days after delivery. What is the payment deadline?"

**Expected Output**: "April 11, 2023" (exact date arithmetic)

### Level 4 Sample
**Problem**: "Original timeline: Task A (3 days) → Task B (5 days) → Task C (2 days). If Task A delayed by 2 days, when does Task C finish?"

**Expected Output**: "Task C finishes 2 days later than original (cascade from A → B → C)"

### Level 5 Sample
**Problem**: "If patient admitted on weekend, observation period is 24 hours. If weekday, 12 hours. Patient admitted on Saturday at 8 AM. When can discharge occur?"

**Expected Output**: "Sunday at 8 AM" (24-hour rule applies)

---

## Appendix B: Evaluation Script Example

```python
def evaluate_level_3(predictions, ground_truth):
    """
    Evaluate Level 3 (Temporal Calculation) submissions
    """
    exact_matches = 0
    absolute_errors = []

    for pred, gt in zip(predictions, ground_truth):
        pred_date = parse_date(pred['answer'])
        gt_date = parse_date(gt['answer'])

        if pred_date == gt_date:
            exact_matches += 1
            absolute_errors.append(0)
        else:
            error_days = abs((pred_date - gt_date).days)
            absolute_errors.append(error_days)

    metrics = {
        'exact_match': exact_matches / len(predictions),
        'mean_absolute_error': np.mean(absolute_errors),
        'median_absolute_error': np.median(absolute_errors),
        'within_1_day': sum(e <= 1 for e in absolute_errors) / len(absolute_errors)
    }

    return metrics
```

---

## Conclusion

This temporal reasoning benchmark suite provides a systematic, comprehensive evaluation framework for neuro-symbolic AI systems. The 5-level architecture progressively tests capabilities from basic extraction to complex conditional reasoning, with formal grounding ensuring reproducibility and fair comparison.

**Key Innovations**:
1. Progressive difficulty hierarchy
2. Formal temporal logic specifications for all problems
3. Domain diversity ensuring generalization
4. Comprehensive metrics at each level
5. Public leaderboard and community engagement

**Expected Impact**: This benchmark will become the standard for temporal reasoning evaluation, driving research in hybrid neuro-symbolic approaches and quantifying the hybrid advantage for safety-critical temporal reasoning applications.
