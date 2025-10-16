# Comprehensive Experimental Validation Methodology

## Executive Summary

This document provides the complete experimental validation architecture for the neuro-symbolic AI paper, integrating all components: temporal reasoning benchmark, multi-DSL fine-tuning, provenance quality evaluation, and uncertainty-aware verification. The methodology addresses all critical research gaps identified in research_gaps.md and aligns with the evaluation section requirements from paper_outline.md.

**Total Experimental Scope**:
- 4 major experiments (Gaps 1.1-1.4)
- 5,000-problem temporal benchmark
- 5,000-example multi-DSL training dataset
- 45-participant user study
- 1,000-problem verification dataset
- Estimated timeline: 17-24 weeks (4-6 months)
- Estimated budget: $30K-55K (compute + annotation + user study)

---

## 1. Experimental Overview and Structure

### 1.1 Research Questions

**RQ1 (Temporal Reasoning - Gap 1.1)**:
*Can hybrid neuro-symbolic systems dramatically improve temporal reasoning performance compared to pure LLMs, especially on quantitative calculations?*

**Hypothesis**: Hybrid systems with LLM extraction + Allen's IA + STN solvers will achieve 80-90% performance across all temporal reasoning levels, vs 40-50% for pure LLMs, with most dramatic improvement (+500%) on duration calculations.

**RQ2 (Multi-DSL Fine-Tuning - Gap 1.2)**:
*Does multi-DSL curriculum learning enable transfer learning effects, achieving comparable performance to single-DSL fine-tuning with 1 model instead of 5?*

**Hypothesis**: Multi-DSL curriculum fine-tuning will achieve 80-85% Pass@1 (only 2-5% below single-DSL), with positive transfer learning effects (+10-20%) between similar DSLs (Prolog ↔ ASP).

**RQ3 (Provenance Quality - Gap 1.3)**:
*Do provenance-based explanations provide superior faithfulness, actionability, and trust calibration compared to LLM post-hoc explanations and attention visualization?*

**Hypothesis**: Provenance-based methods will achieve >95% faithfulness (vs ~65% for LLM post-hoc) and better trust calibration (r>0.75 vs r~0.50), validated through user study with 45 domain experts.

**RQ4 (Uncertainty-Aware Verification - Gap 1.4)**:
*Can uncertainty quantification with selective verification reduce false negatives from 18% to <5% while maintaining >70% automation rate?*

**Hypothesis**: Fusion of three uncertainty signals (LLM confidence, multi-sample agreement, parse-and-regenerate) with threshold θ=0.80-0.90 will achieve 2-5% false negative rate with 35-50% abstention, enabling safety-critical deployment.

### 1.2 Experimental Dependencies

```
Experiment Flow:
1. Temporal Benchmark (Gap 1.1) - INDEPENDENT
2. Multi-DSL Fine-Tuning (Gap 1.2) - INDEPENDENT
3. Provenance Quality (Gap 1.3) - Depends on 1, 2 (uses their outputs)
4. Uncertainty Verification (Gap 1.4) - Depends on 2 (uses fine-tuned model)

Parallel Track:
- Experiments 1 and 2 can run concurrently
- Experiments 3 and 4 can run concurrently (after 1, 2 complete)

Total Timeline:
- Phase 1 (Exp 1 & 2): Weeks 1-12
- Phase 2 (Exp 3 & 4): Weeks 13-21
- Phase 3 (Analysis & Writing): Weeks 22-24
```

### 1.3 Resource Requirements Summary

**Computational Resources**:
- Fine-tuning: 3× RTX A6000 or equivalent (40-60 GPU-hours, $240-540 cloud cost)
- Inference: GPT-4 API access ($500-1000 for experiments)
- Baseline systems: Open-source (SWI-Prolog, Clingo, Z3, GQR) - free

**Human Resources**:
- Dataset construction: 500 expert hours ($25K-50K at $50-100/hour)
- User study: 45 participants × $75 = $3,375
- Experiment execution: 100-150 hours (research team)

**Data Requirements**:
- Temporal benchmark: 5,000 problems (create + curate)
- Multi-DSL dataset: 5,000 training + 500 test (create)
- Verification dataset: 1,000 problems with ground truth (curate + create)
- User study materials: 50 problems (subset)

**Total Budget**: $30K-55K (one-time investment, datasets publicly released)

---

## 2. Experiment 1: Temporal Reasoning Benchmark (Gap 1.1)

### 2.1 Objectives

1. **Create comprehensive temporal reasoning benchmark** covering 5 levels: extraction → ordering → calculation → counterfactual → conditional
2. **Quantify LLM failure modes**, especially on temporal calculations (expected 12-18% accuracy)
3. **Demonstrate hybrid advantage** with 120-160% overall improvement
4. **Establish baseline** for future temporal reasoning research

### 2.2 Experimental Design

#### 2.2.1 Dataset Specification

See `./benchmark_design.md` for complete specification.

**Summary**:
- **Total**: 5,000 problems (1,000 per level)
- **Domains**: Healthcare (35%), Finance (25%), Aerospace (20%), Legal (15%), Robotics (5%)
- **Difficulty**: Easy (30%), Medium (50%), Hard (20%)
- **Annotations**: Natural language + formal temporal logic specs (Allen's IA + STN)

**Construction Timeline**:
- Weeks 1-4: Data source collection (MIMIC-III, 10-K, NASA, contracts)
- Weeks 5-8: Expert annotation (2 annotators per domain)
- Weeks 9-10: Inter-annotator agreement checking (κ ≥ 0.85)
- Weeks 11-12: Formal specification generation and consistency verification

#### 2.2.2 Systems Under Test

**Baseline Systems**:
1. **Pure LLM (Zero-Shot)**
   - GPT-4 Turbo (gpt-4-turbo-2024-04-09)
   - Claude 3.5 Sonnet (claude-3-5-sonnet-20241022)
   - DeepSeek-V3
   - Prompting: Chain-of-Thought (CoT) with temporal reasoning instructions

2. **Pure LLM (Few-Shot)**
   - Same models as above
   - 5-shot examples per level (25 total examples)

3. **Specialized Temporal Systems**
   - TReMu (if available)
   - TempGraph-LLM
   - CRONKGQA (for temporal KG problems)

**Our Hybrid System**:
1. **LLM Component**
   - Fine-tuned Llama 3.1 8B (from Experiment 2)
   - Temporal entity extraction
   - Constraint extraction (qualitative + quantitative)

2. **Symbolic Components**
   - Allen's Interval Algebra: GQR (General Qualitative Reasoner)
   - STN Solver: Custom implementation (Floyd-Warshall path consistency)
   - CSTN Solver: For conditional temporal networks (Level 5)

3. **Temporal Provenance**
   - Custom temporal semiring implementation
   - Provenance polynomial construction
   - Dependency tracking

**Ablation Variants** (to isolate component contributions):
- LLM only (baseline)
- LLM + Extraction tools (SUTime, HeidelTime)
- LLM + Allen's IA
- LLM + Allen's IA + STN
- LLM + Allen's IA + STN + Provenance (full system)

#### 2.2.3 Evaluation Protocol

**Automated Evaluation**:
- Evaluation scripts: Python with JSON I/O
- Per-level metrics (see `./evaluation_metrics.md`)
- Statistical tests: Paired t-tests, ANOVA, Bonferroni correction
- Cross-validation: 5-fold for generalization testing

**Execution Plan**:
1. Run all systems on all 5,000 problems
2. Record: Predictions, confidence scores, processing time, errors
3. Compute metrics per level and overall
4. Error analysis: Categorize failure modes
5. Statistical significance testing

**Expected Execution Time**:
- Pure LLM: ~3-5 seconds per problem × 5,000 = 4-7 hours per system
- Hybrid: ~5-10 seconds per problem × 5,000 = 7-14 hours
- Total: ~50-100 hours (parallel execution)

#### 2.2.4 Expected Results

See `./evaluation_metrics.md` Section 1 for complete metrics.

**Key Expected Findings**:
1. **Level 3 (Calculation)**: Pure LLM catastrophic failure (12-18% EM), Hybrid 85-92% (+529%)
2. **Level 2 (Ordering)**: Pure LLM 65%, Hybrid 92% (+42%)
3. **Overall**: Pure LLM 47%, Hybrid 84% (+79%)
4. **Domain Variance**: Healthcare (86%), Finance (91%), Aerospace (88%), Legal (79%), Robotics (82%)

**Statistical Power Analysis**:
- Effect size: Cohen's d ≈ 1.5-3.5 (large effects expected)
- Sample size: N=5,000 (1,000 per level)
- Power: 1-β > 0.99 (highly powered)
- Significance: α = 0.05 (with Bonferroni correction for 15 comparisons: α_adj = 0.003)

### 2.3 Dataset Release

**Public Release Components**:
1. Full dataset (5,000 problems with annotations) - GitHub repository
2. Evaluation scripts - Python, MIT license
3. Baseline results - JSON with all metrics
4. Documentation - README, examples, tutorials
5. Leaderboard template - For community submissions

**License**: CC-BY 4.0 (data), MIT (code)

**Citation Requirements**: Paper reference + dataset DOI

### 2.4 Potential Challenges and Mitigations

**Challenge 1: Inter-Annotator Agreement <0.85**
- Mitigation: Third expert adjudication, clearer annotation guidelines, pilot annotation

**Challenge 2: Baseline System Unavailability (TReMu, etc.)**
- Mitigation: Focus on GPT-4, Claude, DeepSeek (widely available), cite published results for others

**Challenge 3: Execution Time Too Long**
- Mitigation: Parallel execution, subset sampling (representative 1,000-problem subset), caching

**Challenge 4: Domain Imbalance**
- Mitigation: Stratified sampling, weighted metrics, per-domain reporting

---

## 3. Experiment 2: Multi-DSL Fine-Tuning (Gap 1.2)

### 3.1 Objectives

1. **Evaluate transfer learning** across multiple DSLs (Prolog, ASP, SMT-LIB, PDDL, Datalog)
2. **Compare training strategies**: Single-DSL vs Multi-DSL Simultaneous vs Multi-DSL Curriculum
3. **Quantify practical trade-offs**: Performance vs deployment cost (1 model vs 5)
4. **Demonstrate cost-effective deployment** with minimal performance loss

### 3.2 Experimental Design

#### 3.2.1 Dataset Construction

**DSLs Included**:
1. **Datalog**: Restricted logic programming (polynomial-time guarantees)
2. **Prolog**: General-purpose logic programming (SLD resolution)
3. **ASP**: Answer Set Programming (non-monotonic reasoning)
4. **SMT-LIB**: Satisfiability Modulo Theories (quantifier-free logics)
5. **PDDL**: Planning Domain Definition Language (classical planning)

**Dataset Size**:
- Training: 1,000 examples per DSL (5,000 total)
- Validation: 100 examples per DSL (500 total)
- Test: 100 examples per DSL (500 total)

**Data Sources**:
- Existing benchmarks: HumanEval (adapted), APPS, CodeContests
- Logic programming tasks: Family trees, graph problems, constraint satisfaction
- Planning problems: Blocksworld, Logistics, Grid navigation
- Verification problems: Bit-vector puzzles, array reasoning

**Example Format**:
```json
{
  "problem_id": "datalog_001",
  "domain": "graph",
  "description": "Find all nodes reachable from node 'a' in the graph.",
  "graph": {"edges": [["a","b"], ["b","c"], ["c","d"]]},
  "expected_output": ["a", "b", "c", "d"],
  "dsl": "datalog",
  "solution": "reachable(X, Y) :- edge(X, Y).\nreachable(X, Z) :- edge(X, Y), reachable(Y, Z).\n?- reachable(a, X).",
  "test_cases": [
    {"input": "a", "expected": ["a","b","c","d"]},
    {"input": "b", "expected": ["b","c","d"]}
  ],
  "difficulty": "easy"
}
```

**Construction Timeline**:
- Weeks 1-6: Data collection and adaptation from existing benchmarks
- Weeks 7-10: DSL translation by experts (1 expert per DSL)
- Weeks 11-12: Test case generation and validation

#### 3.2.2 Training Strategies

**Strategy 1: No Fine-Tuning (Baseline)**
- GPT-4, Claude 3.5, DeepSeek-V3 (zero-shot, few-shot)

**Strategy 2: Single-DSL Fine-Tuning**
- Train 5 separate models (1 per DSL)
- Base model: Llama 3.1 8B
- Training data: 1,000 examples per DSL
- QLoRA configuration: rank=16, alpha=32, dropout=0.1
- Epochs: 3-5 per DSL
- Learning rate: 1e-4 with cosine decay
- Batch size: 32 (gradient accumulation)

**Strategy 3: Multi-DSL Simultaneous**
- Train 1 model on all DSLs simultaneously
- Training data: 5,000 examples (mixed)
- Shuffled batches (random DSL per example)
- Same hyperparameters as Strategy 2

**Strategy 4: Multi-DSL Curriculum (Our Approach)**
- Train 1 model with sequential DSL introduction
- Curriculum order: Datalog → Prolog → ASP → SMT-LIB → PDDL
- Rationale: Simple to complex, restricted to general
- Each stage: 1,000 new examples + 200 review from previous stages
- Prevents catastrophic forgetting

**Strategy 5: Transfer Learning Study**
- Pre-train on DSL A (e.g., ASP)
- Fine-tune on DSL B (e.g., Prolog)
- Measure transfer effect: Performance(B | pre-trained on A) - Performance(B | baseline)

**Constrained Generation**:
- All strategies use grammar-based constrained generation
- BNF grammars for each DSL (eliminates syntax errors)
- Implemented via guided decoding (e.g., Outlines library)

#### 3.2.3 Training Infrastructure

**Hardware**:
- 3× RTX A6000 (48GB VRAM each) or equivalent cloud GPUs
- Estimated time: 40-60 hours total
- Cost estimate: $240-540 (cloud rental)

**Software Stack**:
- Base model: Llama 3.1 8B (HuggingFace)
- Fine-tuning: QLoRA (bitsandbytes + PEFT)
- Framework: PyTorch, Transformers, Accelerate
- Evaluation: Custom test harness with DSL execution engines

**Hyperparameters** (optimized on validation set):
- Learning rate: 1e-4 (cosine decay)
- Batch size: 32 (effective, via gradient accumulation)
- LoRA rank: 16
- LoRA alpha: 32
- Dropout: 0.1
- Warmup steps: 100
- Max gradient norm: 1.0
- Weight decay: 0.01

#### 3.2.4 Evaluation Protocol

**Metrics** (see `./evaluation_metrics.md` Section 2):
- Pass@1: % programs passing all test cases
- Pass@10: Best of 10 samples
- Syntax error rate: % invalid DSL programs
- Semantic correctness: % valid programs passing tests
- Generation time: Inference latency

**Execution Plan**:
1. Train all strategies (Weeks 1-8)
2. Evaluate on held-out test set (500 problems per strategy)
3. Ablation studies: Vary training data size, curriculum order
4. Transfer learning experiments: All DSL pairs (5×4 = 20 experiments)
5. Statistical analysis: ANOVA with post-hoc tests

**Expected Execution Time**:
- Training: 40-60 hours (one-time cost)
- Evaluation: ~5-10 seconds per problem × 500 × 5 strategies = 3-7 hours

#### 3.2.5 Expected Results

**Primary Results**:
| Strategy | Avg Pass@1 | Training Cost | Models | Deployment Cost |
|----------|------------|---------------|--------|-----------------|
| No FT (GPT-4) | 64% | $0 | N/A | $0.027/problem |
| Single-DSL | 84% | $1,200-2,700 | 5 | $0.015/problem × 5 |
| Multi-DSL Simultaneous | 79% | $240-540 | 1 | $0.015/problem |
| **Multi-DSL Curriculum** | **82%** | **$240-540** | **1** | **$0.015/problem** |

**Key Expected Findings**:
1. Single-DSL best per-DSL (84%) but requires 5 models
2. Curriculum (82%) only 2% below single-DSL, 1 model
3. Positive transfer: ASP ↔ Prolog (+6-8%), Datalog → Prolog (+4-6%)
4. Constrained generation: 0% syntax errors (vs 12-20% without)

**Transfer Learning Matrix** (expected):
```
Pre-train →  | Datalog | Prolog | ASP | SMT | PDDL
Fine-tune ↓  |         |        |     |     |
-------------|---------|--------|-----|-----|-----
Datalog      | -       | +5%    | +3% | +1% | +2%
Prolog       | +4%     | -      | +7% | +2% | +3%
ASP          | +3%     | +8%    | -   | +2% | +4%
SMT-LIB      | +1%     | +2%    | +2% | -   | +1%
PDDL         | +2%     | +3%    | +4% | +1% | -

Interpretation: Pre-training on ASP, then fine-tuning on Prolog → +8% vs training Prolog from scratch
```

### 3.3 Ablation Studies

**Ablation 1: Training Data Size**
- Vary: 100, 500, 1000, 2000 examples per DSL
- Expected: Diminishing returns after 1000 examples

**Ablation 2: Curriculum Order**
- Test alternative orderings (e.g., Prolog → Datalog → ASP)
- Expected: Our order (simple to complex) best

**Ablation 3: Constrained vs Unconstrained Generation**
- With grammar: 0% syntax errors, 82% Pass@1
- Without grammar: 15-20% syntax errors, 68-72% Pass@1

### 3.4 Potential Challenges and Mitigations

**Challenge 1: Catastrophic Forgetting (Multi-DSL)**
- Mitigation: Review examples from previous stages, replay buffer, elastic weight consolidation

**Challenge 2: GPU Memory Constraints**
- Mitigation: QLoRA (4-bit quantization), gradient checkpointing, smaller batch sizes

**Challenge 3: Negative Transfer**
- Mitigation: Careful curriculum design, monitor per-DSL performance, early stopping if degradation

**Challenge 4: Benchmark Contamination (GPT-4, Claude)**
- Mitigation: Create original problems, verify test set held-out from public corpora

---

## 4. Experiment 3: Provenance Quality User Study (Gap 1.3)

### 4.1 Objectives

1. **Quantify explanation quality** across multiple dimensions: faithfulness, comprehensibility, actionability, trust calibration
2. **Compare explanation methods**: Provenance polynomials, s(CASP), xASP, LLM post-hoc, Attention
3. **Validate hypothesis** that provenance-based methods achieve >95% faithfulness and better trust calibration
4. **Inform explanation design** for deployed systems

### 4.2 Experimental Design

#### 4.2.1 Participant Recruitment

**Target**: 45 domain experts (9 per domain)

**Domains**:
1. Legal (9): Lawyers, legal scholars, paralegals
2. Medical (9): Physicians, nurses, medical informaticists
3. Financial (9): Financial analysts, traders, compliance officers
4. Engineering (9): Software engineers, systems engineers
5. Scientific (9): Researchers using computational methods

**Recruitment Strategy**:
- Professional networks (LinkedIn, domain-specific forums)
- Conference attendees (AAAI, IJCAI, domain conferences)
- University contacts (collaborators, alumni)
- Paid advertisements (professional communities)

**Compensation**: $75 per participant (30-60 minute session)

**Inclusion Criteria**:
- 3+ years professional experience in domain
- Familiarity with computational reasoning (basic programming or formal methods)
- English proficiency (study conducted in English)

**Exclusion Criteria**:
- AI/ML researchers (to avoid bias)
- Prior exposure to study materials

#### 4.2.2 Study Materials

**Problem Set**: 50 problems (10 per domain)
- Sourced from Experiments 1 and 2
- Complexity: Medium difficulty (representative)
- Diversity: Mix of temporal, logic, constraint problems

**Explanation Methods** (5 systems):
1. **Provenance Polynomials**: ℕ[X] semiring with custom visualization
2. **s(CASP) Justification Trees**: ASP with NL templates
3. **xASP Explanation Graphs**: Argument-based graphs
4. **LLM Post-Hoc**: GPT-4 asked "explain your reasoning"
5. **Attention Visualization**: Token-level attention heatmaps

**Per-Problem Materials**:
- Problem statement (natural language)
- Result (answer computed by system)
- Explanation (in one of 5 formats above)
- Comprehension quiz (3 multiple-choice questions)
- Debugging task (for subset of problems)
- Trust rating (Likert scale 1-7)

**Randomization**:
- Each participant sees 10 problems (2 per explanation method)
- Problem-method pairing randomized across participants (Latin square design)
- Avoids order effects and learning effects

#### 4.2.3 Study Protocol

**Session Structure** (40-45 minutes):

1. **Consent and Demographics** (5 minutes)
   - Informed consent
   - Background questionnaire (domain, years experience, familiarity with AI)

2. **Training** (5 minutes)
   - Overview of explanation methods (1 minute each)
   - Example problem (not used in main study)
   - Practice tasks

3. **Main Study** (30 minutes)
   - 10 problems (3 minutes each)
   - Per problem:
     a. Read problem statement and explanation (timed)
     b. Answer comprehension quiz (3 questions)
     c. Debugging task (if applicable): Identify and fix error
     d. Rate confidence in result (1-7 Likert)
     e. Ground truth revealed after rating

4. **Post-Study Questionnaire** (5 minutes)
   - Ranking of explanation methods (preferences)
   - Qualitative feedback (open-ended)
   - Which method would you trust in your domain?

**Data Collection**:
- Automated web interface (custom React app)
- All interactions logged (timing, responses, confidence ratings)
- Video recording (optional, for qualitative analysis)

#### 4.2.4 Metrics

See `./evaluation_metrics.md` Section 3 for complete specification.

**Primary Metrics**:
1. **Faithfulness** (objective): % explanations verified correct via provenance checker
2. **Comprehensibility** (subjective): % correct quiz answers
3. **Time-to-Understand** (objective): Seconds to complete comprehension task
4. **Debugging Success** (objective): % participants who correctly fixed error
5. **Time-to-Fix** (objective): Minutes to resolve bug
6. **Trust Calibration** (objective): Pearson correlation between confidence rating and actual correctness

**Secondary Metrics**:
- User preferences (ranking)
- Qualitative themes (thematic analysis of feedback)
- Domain-specific effects (interaction: domain × explanation method)

#### 4.2.5 Statistical Analysis

**Primary Analysis**: Mixed ANOVA
- Within-subjects factor: Explanation method (5 levels)
- Between-subjects factor: Domain (5 levels)
- Dependent variables: Comprehensibility, Time-to-Understand, Debugging Success, Time-to-Fix, Trust Calibration

**Post-Hoc Tests**: Tukey HSD for pairwise comparisons

**Effect Size**: Cohen's d for pairwise differences

**Significance Level**: α = 0.05 (with Bonferroni correction for multiple comparisons)

**Power Analysis**:
- Expected effect size: d = 0.6-1.0 (medium to large)
- Sample size: N = 45
- Power: 1-β = 0.80-0.95 (adequate)

**Reliability**: Cronbach's α for comprehension quiz internal consistency

#### 4.2.6 Expected Results

See `./evaluation_metrics.md` Section 3.4 for complete results table.

**Key Expected Findings**:
1. **Faithfulness**: Provenance (97%) > s(CASP) (95%) > xASP (93%) >> LLM (68%) > Attention (52%)
2. **Comprehensibility**: s(CASP) (84%) > Provenance (78%) > LLM (76%) > xASP (72%) > Attention (58%)
3. **Debugging**: s(CASP) (88%) > Provenance (82%) > xASP (76%) > LLM (64%) > Attention (42%)
4. **Trust Calibration**: s(CASP) (r=0.82) > Provenance (r=0.78) > xASP (r=0.74) > LLM (r=0.52) > Attention (r=0.38)

**Statistical Significance** (expected):
- All pairwise comparisons (Provenance vs LLM, s(CASP) vs Attention, etc.): p < 0.001
- Domain effects: Medical highest comprehensibility (technical training), Legal lowest (legal jargon)

### 4.3 Execution Plan

**Timeline**:
- Weeks 13-14: Material preparation (problem selection, explanation generation)
- Weeks 15-16: Web interface development and pilot testing (N=5)
- Weeks 17-19: Participant recruitment and scheduling
- Weeks 20-21: Main study (15-20 participants per week)
- Week 22: Data analysis and reporting

**Pilot Testing** (N=5):
- Test protocol clarity
- Calibrate task difficulty (target: 60-80% comprehension accuracy)
- Identify technical issues with web interface
- Adjust based on feedback

### 4.4 Ethical Considerations

**IRB Approval**: Required for human subjects research
- Submit protocol to Institutional Review Board
- Informed consent procedures
- Data privacy (anonymization, secure storage)

**Participant Safety**:
- No deception (purpose clearly stated)
- Voluntary participation (can withdraw anytime)
- Debriefing (results shared after publication)

**Data Privacy**:
- De-identification (remove personally identifiable information)
- Secure storage (encrypted, access-controlled)
- Retention: 5 years (standard for research data)

### 4.5 Potential Challenges and Mitigations

**Challenge 1: Recruitment Difficulty**
- Mitigation: Higher compensation ($100 instead of $75), flexible scheduling, remote participation

**Challenge 2: Low Engagement**
- Mitigation: Engaging materials, clear instructions, progress indicators, short sessions (40 min)

**Challenge 3: Domain Expertise Variability**
- Mitigation: Stratified analysis by experience level, control for expertise in analysis

**Challenge 4: Explanation Method Unfamiliarity**
- Mitigation: Training phase, practice problems, clear documentation

---

## 5. Experiment 4: Uncertainty-Aware Verification (Gap 1.4)

### 5.1 Objectives

1. **Develop formal framework** for uncertainty quantification in hybrid systems
2. **Optimize abstention threshold** for different domains (general, medical, aerospace)
3. **Demonstrate probabilistic soundness bounds**: P(error) ≤ 6% (general), ≤1% (safety-critical)
4. **Validate two-tier deployment strategy**: 87% automation with <1% error

### 5.2 Experimental Design

#### 5.2.1 Dataset Construction

**Size**: 1,000 problems with ground-truth specifications

**Sources**:
- Subset of Experiment 1 (temporal problems): 400 problems
- Subset of Experiment 2 (DSL translation): 400 problems
- New problems from real-world applications: 200 problems

**Ground Truth Requirements**:
- Natural language problem statement
- Correct formal specification (verified by experts)
- Test cases for validation
- Domain label (general, medical, financial, aerospace, legal)

**Annotation**:
- Two experts per problem (independent specifications)
- Adjudication if disagreement (third expert)
- Inter-annotator agreement: κ ≥ 0.90 (higher than Experiment 1 due to critical importance)

**Construction Timeline**:
- Weeks 1-2: Problem selection and curation
- Weeks 3-4: Expert annotation (2 annotators × 1000 problems ÷ 40 hours = 50 hours per annotator)
- Week 5: Adjudication and final verification

#### 5.2.2 Uncertainty Quantification Methods

**Method 1: LLM Confidence Scores**
- Extract token-level log probabilities during generation
- Aggregate: `conf = exp(mean(log_prob_i))`
- Range: [0, 1], higher is more confident

**Method 2: Multi-Sample Agreement**
- Generate N=5 independent samples
- Compare outputs: `agree = (# samples matching majority) / N`
- Range: [0.2, 1.0], higher is more agreement

**Method 3: Parse-and-Regenerate Consistency**
- DSL → NL description (LLM generates natural language explanation of program)
- NL → DSL' (LLM regenerates program from explanation)
- Check semantic equivalence: `consistent = 1` if DSL ≡ DSL', else `0`

**Fusion Strategy** (lightweight weighted combination):
```
Uncertainty = w1 × (1 - conf) + w2 × (1 - agree) + w3 × (1 - consistent)

Weights (optimized on validation set, 200 problems):
- w1 = 0.3 (LLM confidence)
- w2 = 0.5 (multi-sample agreement, most reliable)
- w3 = 0.2 (consistency check)

Abstention Decision:
If Uncertainty > θ, abstain (provide certificate)
Else, proceed to verification
```

#### 5.2.3 Threshold Optimization

**Approach**: ROC analysis varying θ ∈ [0.5, 0.55, 0.60, ..., 0.95]

**For each threshold θ**:
1. Run uncertainty quantification on all 1,000 problems
2. Classify: Abstain if U > θ, Proceed if U ≤ θ
3. Execute proceeded problems through symbolic verification
4. Measure:
   - Abstention Rate (AR): % problems abstained
   - False Negative Rate (FNR): % wrong specs generated without abstention
   - False Positive Rate (FPR): % correct specs abstained
   - End-to-End Error: P(error) = FNR × (1 - AR)

**Optimization Criteria**:
- **General Use**: Minimize `Cost = 3×FNR + AR` (moderate error penalty)
- **High-Stakes**: Minimize `Cost = 10×FNR + AR` (strong error penalty)
- **Safety-Critical**: Minimize `Cost = 100×FNR + AR` (extreme error penalty)

**Validation**:
- 5-fold cross-validation on 1,000-problem dataset
- Report mean and standard deviation across folds
- Select threshold maximizing cost function on validation set
- Test on held-out test set (if available) or report cross-validation results

#### 5.2.4 Probabilistic Soundness Framework

**Formal Guarantee**:
```
P(error) ≤ P(LLM_error | U ≤ θ) × (1 - AR) + P(symbolic_error)

Where:
- P(LLM_error | U ≤ θ): Conditional error probability (low uncertainty but still wrong)
- AR: Abstention rate (% of problems abstained, no answer given)
- P(symbolic_error): Error rate of symbolic components ≈ 0 (verified)

Simplified: P(error) ≈ FNR × (1 - AR)

Example (θ = 0.90):
- FNR = 3%
- AR = 47%
- P(error) = 0.03 × (1 - 0.47) = 0.016 = 1.6%
```

**Empirical Calibration**:
- Measure FNR for each threshold on validation set
- Verify: Does empirical P(error) match predicted bound?
- Adjust weights (w1, w2, w3) if calibration poor

#### 5.2.5 Evaluation Protocol

**Systems Under Test**:
1. **Pure LLM (No Abstention)**: Baseline, always generates answer
2. **LLM + Confidence Only**: Abstain based on Method 1 only
3. **LLM + Agreement Only**: Abstain based on Method 2 only
4. **LLM + Consistency Only**: Abstain based on Method 3 only
5. **Our Fusion**: Weighted combination of all 3 methods

**Execution Plan**:
1. Run all systems on 1,000-problem dataset
2. Vary threshold θ for systems 2-5 (10 thresholds × 5 systems = 50 configurations)
3. Compute metrics (AR, FNR, FPR, P(error)) for each configuration
4. Plot ROC curves: AR (x-axis) vs FNR (y-axis)
5. Identify optimal thresholds for different domains
6. Validate two-tier strategy (Tier 1: θ=0.70, Tier 2: θ=0.95)

**Expected Execution Time**:
- Uncertainty quantification: ~10-15 seconds per problem × 1,000 = 3-4 hours
- Symbolic verification: ~5 seconds per problem × (1-AR) × 1,000 = 1-3 hours
- Total: ~10-20 hours (all configurations)

#### 5.2.6 Expected Results

See `./evaluation_metrics.md` Section 4.4 for complete results table.

**Key Expected Findings**:

**ROC Curve** (AR vs FNR):
```
θ     | AR   | FNR  | FPR  | P(error) | Recommended Domain
------|------|------|------|----------|-------------------
0.50  | 12%  | 18%  | 3%   | 16%      | Low-stakes
0.60  | 19%  | 13%  | 5%   | 11%      | General (low priority)
0.70  | 28%  | 8%   | 7%   | 6%       | General use
0.80  | 38%  | 5%   | 10%  | 3%       | Financial, legal
0.90  | 47%  | 3%   | 12%  | 2%       | Medical (high-stakes)
0.95  | 63%  | 1%   | 15%  | 0.6%     | Aerospace (safety-critical)
```

**System Comparison** (at θ=0.80):
```
System                | AR   | FNR  | P(error)
----------------------|------|------|----------
Pure LLM (baseline)   | 0%   | 18%  | 18%
Confidence Only       | 30%  | 10%  | 7%
Agreement Only        | 35%  | 6%   | 4%
Consistency Only      | 25%  | 12%  | 9%
Our Fusion            | 38%  | 5%   | 3%
```

**Two-Tier Strategy** (Tier 1: θ=0.70, Tier 2: θ=0.95):
```
Tier 1 (θ=0.70):
  - Automation: 72% (100% - 28% AR)
  - Error rate: 6%

Tier 2 (θ=0.95) on Tier 1 abstentions:
  - Additional automation: 15% (of original 28%)
  - Error rate on Tier 2: <1%

Human Review:
  - Remaining: 13% (abstained at both tiers)

Overall:
  - Automation: 87% (72% + 15%)
  - Error rate: <1% (weighted average)
  - Human review: 13%
```

**Probabilistic Guarantee Validation**:
- Predicted P(error) from formula vs actual empirical error rate
- Expected: Match within 1-2% (e.g., predicted 2%, actual 1.5-2.5%)

### 5.3 Ablation Studies

**Ablation 1: Weight Sensitivity**
- Vary weights (w1, w2, w3) in range [0, 1] (constrained: w1+w2+w3=1)
- Expected: w2 (agreement) most important, w3 (consistency) least
- Optimal weights close to (0.3, 0.5, 0.2)

**Ablation 2: Number of Samples (N)**
- Vary N ∈ {3, 5, 10, 20} for multi-sample agreement
- Expected: Diminishing returns after N=5, trade-off with cost

**Ablation 3: Domain-Specific Thresholds**
- Optimize thresholds separately for each domain
- Expected: Medical/Aerospace require higher θ (0.90-0.95), General lower (0.70)

### 5.4 Potential Challenges and Mitigations

**Challenge 1: Ground Truth Annotation Errors**
- Mitigation: Two independent annotators, adjudication, high κ requirement (≥0.90)

**Challenge 2: Semantic Equivalence Checking (Method 3)**
- Mitigation: Use SMT solver for equivalence when possible, heuristics otherwise, accept false negatives (conservative)

**Challenge 3: Calibration Failure (Predicted ≠ Actual Error)**
- Mitigation: Re-optimize weights on larger validation set, domain-specific calibration

**Challenge 4: High Abstention Rate Unacceptable**
- Mitigation: Two-tier strategy reduces effective AR from 47% to 13% (human review only)

---

## 6. Integration and Cross-Experiment Analysis

### 6.1 Combined System Evaluation

**Objective**: Evaluate fully integrated system with all components:
1. Multi-DSL fine-tuned LLM (Experiment 2)
2. Temporal reasoning module (Experiment 1)
3. Provenance-based explanation (Experiment 3)
4. Uncertainty-aware verification (Experiment 4)

**Evaluation Dataset**: 100 end-to-end problems requiring all components

**Example Problem**:
```
Problem: Clinical Sepsis Protocol (Healthcare Domain)

Input: "Patient presents with suspected sepsis at 10:00 AM. Protocol requires:
- Blood culture within 3 hours of presentation
- Antibiotics within 1 hour of blood culture
- Lab results available 24-48 hours after culture
- Antibiotic adjustment within 4 hours of lab results

If blood culture delayed by 1 hour, when is the latest antibiotic adjustment deadline?"

System Components Used:
1. LLM: Extract temporal entities and constraints
2. Temporal: Allen's IA + STN solver for timeline computation
3. Uncertainty: Quantify confidence, abstain if uncertain
4. Provenance: Track dependencies, explain cascade effects
5. Verification: Formal checking of timeline consistency

Expected Output:
- Answer: 54 hours after presentation (10:00 + 4h + 48h + 4h)
- Explanation: Provenance polynomial showing cascade
- Confidence: 0.92 (high confidence, proceed)
- Verification: Timeline verified consistent
```

**Metrics**:
- End-to-end correctness: % problems solved correctly
- Component contribution: Ablation removing each component
- Explanation quality: User validation (subset of 20 problems, N=10 participants)
- Uncertainty calibration: Predicted vs actual error rate

### 6.2 Failure Mode Analysis

**Objective**: Categorize and quantify failure modes across all experiments

**Failure Categories**:
1. **LLM Parsing Errors**: Wrong specification generated
2. **Symbolic Solver Timeouts**: Valid spec but unsolvable
3. **Explanation Complexity**: Provenance too large for understanding
4. **Iteration Divergence**: Refinement doesn't converge
5. **Abstention False Positives**: Correct spec abstained

**Data Collection**:
- Record all failures across all experiments
- Manual categorization by two annotators (κ ≥ 0.80)
- Measure frequency, severity, domain distribution

**Mitigation Strategies**:
- Per failure mode, propose and test mitigation
- Example: LLM parsing errors → uncertainty-aware abstention (Experiment 4)
- Example: Solver timeouts → timeout certificates (future work)

**Expected Findings**:
| Failure Mode | Frequency | Severity | Primary Mitigation |
|--------------|-----------|----------|--------------------|
| LLM Parsing | 6-12% | High | Uncertainty abstention (reduces to 1-3%) |
| Solver Timeout | 2-5% | Medium | Timeout detection, alternative encoding |
| Explanation Complexity | 3-8% | Low | Hierarchical summarization, factorization |
| Iteration Divergence | 5-10% | Medium | Iteration limit (max 3), semantic reversion |
| Abstention FP | 10-15% | Low | Threshold tuning, domain-specific thresholds |

### 6.3 Performance vs Cost Trade-off Analysis

**Objective**: Guide deployment decisions based on performance-cost-accuracy trade-offs

**Dimensions**:
- Performance: Overall accuracy/correctness
- Cost: Computational cost ($ per problem)
- Coverage: % problems automated (1 - abstention rate)
- Safety: Error rate (false negatives)

**Configurations Compared**:
1. **Pure LLM (GPT-4)**: High cost ($0.027/problem), moderate performance (64-70%)
2. **Fine-Tuned Multi-DSL**: Low cost ($0.015/problem), high performance (82%)
3. **Hybrid (No Abstention)**: Medium cost ($0.020/problem), very high performance (84%), 6-18% error
4. **Hybrid + Uncertainty (θ=0.70)**: Medium cost, high performance, 72% coverage, 6% error
5. **Hybrid + Uncertainty (θ=0.90)**: Medium cost, high performance, 53% coverage, 2% error
6. **Hybrid + Two-Tier**: Medium cost, high performance, 87% coverage, <1% error (optimal)

**Recommendation Matrix**:
| Use Case | Configuration | Rationale |
|----------|---------------|-----------|
| Low-stakes (exploratory) | Pure LLM or Config 2 | Speed over accuracy, cost-effective |
| General use | Config 6 (Two-Tier) | Balance: 87% automation, <1% error, moderate cost |
| High-stakes (financial) | Config 5 (θ=0.90) | Prioritize safety: 2% error acceptable, 53% coverage |
| Safety-critical (medical, aerospace) | Config 5 (θ=0.95) | Maximum safety: <1% error, 37% coverage, high human review |

---

## 7. Timeline and Resource Allocation

### 7.1 Detailed Timeline (24 Weeks Total)

**Phase 1: Dataset Construction and Setup (Weeks 1-4)**
- Week 1: Infrastructure setup (GPUs, software, web interface)
- Weeks 2-4: Temporal benchmark construction (Exp 1)
- Weeks 2-4: Multi-DSL dataset construction (Exp 2) [Parallel]

**Phase 2: Training and Evaluation (Weeks 5-12)**
- Weeks 5-8: Multi-DSL fine-tuning (Exp 2)
- Weeks 9-12: Temporal benchmark evaluation (Exp 1)
- Weeks 9-12: Verification dataset construction (Exp 4) [Parallel]

**Phase 3: User Study and Uncertainty (Weeks 13-21)**
- Weeks 13-14: User study material preparation (Exp 3)
- Weeks 15-16: Pilot testing (Exp 3)
- Weeks 17-19: Main user study (Exp 3)
- Weeks 17-21: Uncertainty-aware verification (Exp 4) [Parallel]

**Phase 4: Analysis and Integration (Weeks 22-24)**
- Week 22: User study analysis (Exp 3)
- Week 22: Cross-experiment integration (Section 6)
- Week 23: Failure mode analysis (Section 6.2)
- Week 24: Final report preparation, dataset release preparation

**Critical Path**: Exp 1 and Exp 2 must complete before Exp 3 and Exp 4 can start (dependencies on their outputs).

### 7.2 Resource Allocation

**Computational**:
- Fine-tuning (Exp 2): 40-60 GPU-hours on 3× RTX A6000 ($240-540 cloud)
- Inference (All): GPT-4 API ($500-1000 total across all experiments)
- Symbolic solvers: Open-source, free

**Human Annotation**:
- Temporal benchmark (Exp 1): 350 hours × $75/hr = $26,250
- Multi-DSL dataset (Exp 2): 100 hours × $75/hr = $7,500
- Verification dataset (Exp 4): 50 hours × $75/hr = $3,750
- User study participants (Exp 3): 45 × $75 = $3,375

**Personnel**:
- Research team: 100-150 hours (experiment execution, analysis)
- Assumed: In-house research team (no additional cost)

**Total Budget**: $30K-55K (one-time, datasets publicly released)

### 7.3 Risk Management

**Risk 1: Timeline Overrun**
- Mitigation: Buffer weeks (24-week plan allows 2-4 week buffer before typical conference deadlines)
- Contingency: Prioritize Experiments 1 and 2 (core contributions), defer 3 and 4 to follow-up work

**Risk 2: Budget Overrun**
- Mitigation: Negotiate bulk discounts for user study (professional recruitment services)
- Contingency: Reduce user study sample size (45 → 30, still adequate power)

**Risk 3: Technical Failures (GPU unavailability, API outages)**
- Mitigation: Backup cloud providers (AWS, GCP, Azure), pre-purchase API credits
- Contingency: Extend timeline, use smaller models (Llama 3.1 8B → 3B)

**Risk 4: Participant No-Shows (User Study)**
- Mitigation: Over-recruit (60 participants scheduled, target 45 completions)
- Contingency: Extended recruitment period (3 weeks → 5 weeks)

---

## 8. Reproducibility and Open Science

### 8.1 Data Release

**Datasets** (all public, CC-BY 4.0 license):
1. **Temporal Reasoning Benchmark** (5,000 problems)
   - JSON format with natural language, formal specs, ground truth
   - GitHub repository: github.com/[org]/temporal-reasoning-benchmark
   - DOI: Zenodo archive for permanent citation

2. **Multi-DSL Training/Test Set** (6,000 examples total)
   - JSON format with problem, DSL solution, test cases
   - GitHub repository: github.com/[org]/multi-dsl-dataset
   - DOI: Zenodo archive

3. **Verification Dataset** (1,000 problems)
   - JSON format with NL, ground truth spec, domain labels
   - GitHub repository: github.com/[org]/uncertainty-verification-dataset
   - DOI: Zenodo archive

**Evaluation Scripts**:
- Python scripts for all metrics
- GitHub repository: github.com/[org]/neurosymbolic-evaluation
- MIT license
- Documentation: README, tutorials, examples

### 8.2 Model Release

**Fine-Tuned Models** (HuggingFace, Apache 2.0 license):
1. Multi-DSL Curriculum Model (Llama 3.1 8B + QLoRA adapters)
   - HuggingFace: huggingface.co/[org]/llama3.1-8b-multi-dsl
   - Model card: Architecture, training data, performance, limitations

**Baseline Systems**:
- Links to public implementations (SWI-Prolog, Clingo, Z3, GQR)
- Custom components: Temporal provenance engine (open-source, MIT license)

### 8.3 Experimental Protocols

**Documentation**:
- Detailed protocols for each experiment (this document)
- Hyperparameters, random seeds, software versions
- Statistical analysis code (Jupyter notebooks)

**Replication Package**:
- Docker container with all dependencies
- Makefile for reproducing all experiments
- Estimated runtime: 100-150 hours (user study excluded)

### 8.4 Pre-Registration

**Optional but Recommended**:
- Pre-register experiments (e.g., Open Science Framework)
- Commit to analysis plan before data collection
- Prevents p-hacking, increases credibility

---

## 9. Ethical Considerations

### 9.1 Human Subjects Research (User Study)

**IRB Approval**:
- Submit protocol to Institutional Review Board
- Informed consent procedures (written consent form)
- Data privacy plan (de-identification, secure storage)
- Participant rights (voluntary, withdraw anytime, debriefing)

**Vulnerable Populations**:
- None targeted (adult professionals only)
- No deception (purpose clearly stated)

### 9.2 Dataset Construction

**Data Sources**:
- MIMIC-III: De-identified clinical notes (already IRB-approved)
- 10-K filings: Public financial reports (no privacy concerns)
- Legal contracts: Anonymized (remove personally identifiable information)
- NASA logs: Public archives (no privacy concerns)

**Bias Considerations**:
- Domain balance: Ensure no single domain dominates (35% max)
- Difficulty balance: Easy (30%), Medium (50%), Hard (20%)
- Cultural bias: Examples from diverse contexts (US, EU, Asia if applicable)

### 9.3 Deployment Considerations

**Safety-Critical Warnings**:
- Documentation: Clearly state limitations (probabilistic guarantees, not deterministic)
- Recommended thresholds by domain (with error rates)
- Human-in-the-loop recommended for safety-critical (medical, aerospace)

**Misuse Prevention**:
- Model release: Include model card with intended use, limitations
- Licensing: Non-commercial clause for safety-critical applications (optional)

### 9.4 Environmental Impact

**Carbon Footprint**:
- Fine-tuning: ~40-60 GPU-hours on A6000 (≈25 kg CO2 estimated)
- Inference: API calls (carbon offset by providers like OpenAI)
- Mitigation: Use energy-efficient hardware, carbon offset programs

---

## 10. Expected Contributions and Impact

### 10.1 Novel Contributions

1. **First Comprehensive Temporal Reasoning Benchmark** (5,000 problems, 5 levels)
   - Addresses Gap 1.1
   - Public dataset enables future research
   - Quantifies LLM catastrophic failures (12-18% on calculations)

2. **Multi-DSL Fine-Tuning with Transfer Learning** (first systematic study)
   - Addresses Gap 1.2
   - Demonstrates 1 model achieves 98% of 5-model performance
   - Quantifies transfer effects (+6-8% Prolog ↔ ASP)

3. **Provenance Quality Validation** (first user study comparing methods)
   - Addresses Gap 1.3
   - Shows provenance-based >95% faithfulness vs ~65% LLM
   - Design guidelines: Combine provenance (faithfulness) + NL templates (comprehensibility)

4. **Uncertainty-Aware Verification Framework** (probabilistic soundness bounds)
   - Addresses Gap 1.4
   - Formal framework with P(error) ≤ 6% (general), ≤1% (safety-critical)
   - Two-tier strategy: 87% automation with <1% error

### 10.2 Practical Impact

**Deployment in Safety-Critical Domains**:
- Healthcare: Clinical pathway verification (FDA compliance)
- Finance: SEC Rule 613 timestamp verification (regulatory compliance)
- Aerospace: Mission timeline verification (DO-178C compliance)
- Legal: Contract deadline analysis (GDPR Article 22 compliance)

**Cost Reduction**:
- Multi-DSL: 5× deployment simplification (1 model vs 5)
- Fine-tuning: $240-540 one-time cost, saves $0.012 per problem at scale
- Automation: 87% automation reduces human review burden 7× (vs 100% manual)

**Research Enablement**:
- Public benchmarks enable fair comparison
- Baselines established for future work
- Open-source tools accelerate research

### 10.3 Academic Impact

**Expected Publications**:
1. Main paper (AAAI/IJCAI/NeurIPS 2026): Comprehensive system + evaluation
2. Benchmark paper (Datasets track): Temporal reasoning benchmark
3. Follow-up papers: Multi-DSL curriculum learning, Provenance quality metrics

**Citations**:
- Benchmark: Expected high citation (cf. GSM8K, FOLIO, etc.)
- System: Cited by future neuro-symbolic work

**Community Engagement**:
- Annual workshop (AAAI, IJCAI)
- Benchmark challenges with prizes
- Collaborative dataset extensions (multilingual, additional domains)

---

## 11. Conclusion and Next Steps

This experimental design provides a comprehensive validation framework for the neuro-symbolic AI paper, addressing all critical research gaps identified. The methodology is rigorous, reproducible, and ethically sound.

**Key Strengths**:
1. **Comprehensive**: Covers all critical gaps (1.1-1.4) with 4 major experiments
2. **Rigorous**: Statistical power analysis, multiple baselines, ablation studies
3. **Reproducible**: Public datasets, open-source code, detailed protocols
4. **Impactful**: Enables safety-critical deployment, establishes benchmarks

**Immediate Next Steps**:
1. **Week 1-4**: Infrastructure setup, dataset construction initiation
2. **IRB Submission**: User study protocol (Week 1)
3. **GPU Rental**: Secure compute resources (Week 1)
4. **Recruitment**: Begin user study participant outreach (Week 13)

**Success Criteria**:
- All 4 experiments completed within 24 weeks
- Statistical significance achieved (p<0.05 with appropriate corrections)
- Datasets and code publicly released
- Paper accepted at top-tier venue (AAAI, IJCAI, NeurIPS 2026)

**Fallback Plan**:
- If timeline compressed: Prioritize Experiments 1 and 2 (core contributions)
- If budget constrained: Reduce user study sample size (45 → 30)
- If compute constrained: Use smaller models (8B → 3B)

This experimental validation will advance neuro-symbolic AI from research prototypes to deployable technology for safety-critical applications with mathematical guarantees.
