# Research Gaps Requiring Experimental Validation

## Overview

This document identifies critical gaps in the research landscape that require experimental validation for a comprehensive academic paper on neuro-symbolic AI with LLMs and formal verification. Gaps are categorized by type (theoretical, empirical, practical) and prioritized by impact and feasibility.

---

## PRIORITY 1: CRITICAL GAPS (Must Address for Paper Completeness)

### Gap 1.1: Lack of Standardized Temporal Reasoning Benchmark

**Current State**:
- TempTabQA: Limited to table-based QA, single-hop temporal reasoning
- ChronoSense: Allen's relations only, no duration calculations
- No comprehensive benchmark suite covering extraction → ordering → calculation → counterfactual → conditional reasoning

**Evidence of Gap**:
- TReMu paper: 160% improvement claimed but no standard benchmark comparison
- Different papers use different datasets (not comparable)
- Duration calculation: 13-16% accuracy reported but no unified test set

**Required Validation**:
1. **Temporal Reasoning Benchmark Suite** with 5 levels:
   - **Level 1 (Extraction)**: Identify dates, times, events from natural language
   - **Level 2 (Ordering)**: Determine before/after, Allen's 13 relations
   - **Level 3 (Calculation)**: Compute durations, deadlines, arithmetic
   - **Level 4 (Counterfactual)**: What-if scenarios (if event delayed, cascade effects?)
   - **Level 5 (Conditional)**: If-then temporal constraints (if A before B, then C during D)

2. **Evaluation Metrics**:
   - Extraction: Precision, Recall, F1 (temporal entity recognition)
   - Ordering: Accuracy, temporal consistency (no cyclic before relations)
   - Calculation: Exact match, absolute error, relative error
   - Counterfactual: Correctness (ground truth scenarios)
   - Conditional: Constraint satisfaction rate

3. **Dataset Composition** (proposed):
   - 1000 problems per level (5000 total)
   - Domains: Healthcare (clinical pathways), finance (trading timestamps), aerospace (mission timelines), legal (contract deadlines), robotics (action sequences)
   - Difficulty gradations: Simple (single constraint) → Complex (10+ interacting constraints)

**Experimental Plan**:
- Baseline: GPT-4, Claude 3.5, DeepSeek-V3 (pure LLM)
- Hybrid: TReMu-style (LLM + Allen's IA + STN solver)
- Symbolic: Pure Allen's IA + STN (requires manual extraction)
- Evaluate on all 5 levels, report per-level and overall performance

**Expected Outcome**:
- Pure LLM: Strong on Level 1 (70-80%), weak on Levels 3-5 (15-40%)
- Hybrid: Strong across all levels (60-80% overall)
- Symbolic: Perfect on Levels 2-5 given correct extraction (but requires manual setup)

**Paper Contribution**:
- First comprehensive temporal reasoning benchmark
- Public dataset release for future research
- Establishes baseline performance for hybrid approaches

**Feasibility**: Medium (requires dataset construction, ~2-4 weeks)

---

### Gap 1.2: Multi-DSL Fine-Tuning Transfer Learning

**Current State**:
- LLASP: Fine-tuned for ASP only
- ConstraintLLM: Fine-tuned for MiniZinc only
- GPT-4o: Zero-shot Prolog 74% Pass@1 (suggests general capability)
- No systematic evaluation of multi-DSL fine-tuning or transfer learning

**Hypothesis**:
- Fine-tuning on ASP improves Prolog generation (shared logic programming structure)
- Fine-tuning on Prolog + ASP + SMT-LIB improves all three (transfer learning)
- Curriculum learning (simple DSL first) may outperform simultaneous multi-DSL training

**Required Validation**:
1. **Dataset Construction**:
   - Same problem translated to multiple DSLs:
     - Prolog (declarative logic programming)
     - ASP (non-monotonic reasoning)
     - SMT-LIB (quantifier-free theories)
     - PDDL (planning)
     - Datalog (restricted logic programming)
   - 500-1000 problems with ground truth solutions
   - Domains: Constraint satisfaction, planning, combinatorial optimization, graph problems

2. **Training Strategies**:
   - **Baseline**: No fine-tuning (GPT-4, Claude zero-shot)
   - **Single-DSL**: Fine-tune on ASP only, Prolog only, etc. (5 models)
   - **Multi-DSL Simultaneous**: Train on all DSLs simultaneously (1 model)
   - **Multi-DSL Curriculum**: Train on Datalog → Prolog → ASP → SMT-LIB → PDDL (order: simple to complex)
   - **Transfer Learning**: Fine-tune on ASP, then transfer to Prolog (evaluate cross-DSL improvement)

3. **Evaluation Metrics**:
   - Pass@1, Pass@10 (execution correctness)
   - Syntax error rate (compilation success)
   - Semantic correctness (test suite pass rate)
   - Generation time, model size

**Experimental Plan**:
- Base model: Llama 3.1 8B or similar (open-source for controlled experiments)
- Fine-tuning: QLoRA (parameter-efficient, 3× RTX A6000 or equivalent)
- Training data: 5000 examples (1000 per DSL)
- Test data: 500 held-out problems (100 per DSL)
- Report: Per-DSL performance, cross-DSL transfer effects, curriculum impact

**Expected Outcome**:
- Single-DSL fine-tuning: 30-50% improvement over baseline (confirms LLASP/ConstraintLLM findings)
- Multi-DSL simultaneous: 20-40% improvement (slightly worse than single-DSL due to task interference)
- Multi-DSL curriculum: 25-45% improvement (better than simultaneous, close to single-DSL)
- Transfer learning: ASP fine-tuning → +15-25% Prolog improvement (confirms hypothesis)

**Paper Contribution**:
- First multi-DSL fine-tuning study
- Transfer learning results guide cost-effective deployment (train once, use for multiple DSLs)
- Curriculum learning insights for formal language training

**Feasibility**: High (dataset construction intensive, but training manageable with QLoRA)

---

### Gap 1.3: Provenance Quality Metrics and User Study

**Current State**:
- s(CASP) generates explanations but no quantitative quality metrics
- xASP explanations evaluated qualitatively
- ProvSQL correctness proven mathematically but user comprehension unstudied
- No standardized metrics for explanation quality across systems

**Required Validation**:
1. **Explanation Quality Metrics** (objective):
   - **Faithfulness**: Provenance polynomial correctly captures derivation?
     - Metric: Verification rate (independent checker confirms explanation matches computation)
     - Test: Generate explanation, verify via provenance polynomial evaluation
   - **Minimality**: Is explanation minimal sufficient?
     - Metric: Proof size (number of steps), graph complexity (nodes, edges)
     - Baseline: Brute-force all derivations, compare to explanation size
   - **Completeness**: Are all derivations captured?
     - Metric: Coverage (% of alternative derivations shown)
     - Test: Enumerate all proofs (if tractable), measure explanation coverage

2. **Explanation Quality Metrics** (subjective - user study):
   - **Comprehensibility**: Can domain experts understand explanation?
     - Metric: Time-to-understand (seconds to grasp key points)
     - Metric: Correctness quiz (after reading explanation, answer questions)
   - **Actionability**: Can user fix errors based on explanation?
     - Metric: Debugging success rate (given wrong program + explanation, can user fix?)
     - Metric: Time-to-fix (how long to resolve error)
   - **Trust Calibration**: Do users appropriately trust/distrust results?
     - Metric: Trust rating (Likert scale 1-7) vs actual correctness
     - Metric: Over-trust rate (trust incorrect result), under-trust rate (distrust correct result)

3. **User Study Design**:
   - **Participants**: 30-60 domain experts (10-20 per domain: legal, medical, financial)
   - **Systems Compared**:
     - Provenance polynomials (Scallop/ProvSQL visualization)
     - s(CASP) justification trees with NL templates
     - xASP explanation graphs
     - LLM post-hoc explanations (GPT-4 asked "explain your reasoning")
     - Attention visualization (baseline)
   - **Tasks**:
     - Comprehension: Read explanation, answer questions
     - Debugging: Given wrong program, use explanation to fix
     - Trust: Evaluate explanation, predict correctness
   - **Metrics**: Time-to-understand, quiz accuracy, debugging success, trust calibration

**Experimental Plan**:
- Recruit domain experts (legal professionals, medical practitioners, financial analysts)
- Present 10 problems per participant (2 per explanation type, randomized order)
- Measure all metrics, analyze via ANOVA (explanation type as independent variable)
- Qualitative feedback: Interviews about preference, usability

**Expected Outcome**:
- **Faithfulness**: Provenance 95-100% (mathematically guaranteed), LLM post-hoc 60-80%, attention 40-60%
- **Comprehensibility**: s(CASP) NL highest (domain experts), provenance polynomials lower (requires math background), attention lowest
- **Actionability**: Provenance + s(CASP) highest (structural information), LLM post-hoc variable, attention lowest
- **Trust Calibration**: Provenance best (explicit uncertainty), LLM post-hoc worst (over-confidence)

**Paper Contribution**:
- First quantitative comparison of explanation methods for logic programs
- User study validates provenance-based explanation superiority
- Design guidelines for explanation interfaces

**Feasibility**: Medium (user recruitment challenging, but essential for impact)

---

### Gap 1.4: Hybrid Architecture End-to-End Verification

**Current State**:
- Symbolic components verified (Z3 proofs, Lean kernel)
- LLM components unverified (black-box)
- No formal verification of LLM → DSL translation correctness
- **Formalization Gap**: LLM may generate wrong spec → symbolic solver correctly verifies wrong spec

**Evidence**:
- ArXiv 2505.20047: Uncertainty-based selective verification reduces errors 14-100%
- But: No formal guarantee, only empirical improvement

**Required Validation**:
1. **Verified Neuro-Symbolic Pipeline Components**:
   - **LLM Output Constraints**: Formal specification of valid DSL outputs
     - Example: Prolog syntax grammar (BNF)
     - Example: ASP well-formedness constraints (stratification, safety)
   - **Uncertainty Quantification**: Confidence scores for LLM generations
     - Method 1: Softmax probability over token sequences
     - Method 2: Multiple sample agreement (self-consistency)
     - Method 3: Parse-and-regenerate consistency
   - **Selective Verification**: Abstain when uncertainty exceeds threshold
     - Threshold optimization: Minimize (false_negatives + abstention_rate)
   - **Property-Based Testing**: Generated specs must satisfy sanity checks
     - Example: Prolog predicates used must be defined
     - Example: ASP programs must be safe (all variables in positive literals)

2. **Formal Guarantees** (what can be proven?):
   - **Soundness of Symbolic Component**: Already proven (Z3, Lean kernels)
   - **Abstention Correctness**: If abstain, no false negative (trivial: no answer given)
   - **Selective Verification Soundness**: If verify (don't abstain), probability of error < ε
     - Requires: Empirical calibration of uncertainty thresholds
     - Probabilistic guarantee (not deterministic)
   - **End-to-End Bound**: P(error) ≤ P(LLM_error) × (1 - abstention_rate) + P(symbolic_error)
     - P(symbolic_error) ≈ 0 (verified components)
     - P(LLM_error) depends on uncertainty threshold
     - Trade-off: Lower threshold → higher abstention, lower P(error)

3. **Certified Proof Checkers**:
   - ArXiv 2405.10611: Formal proof of neural network verification algorithm soundness
   - Extend to LLM-generated specifications:
     - Proof: If verification succeeds, spec satisfies properties
     - Imandra theorem prover (or Coq/Lean) for soundness proof

**Experimental Plan**:
- Dataset: 1000 problems with ground-truth specifications (NL description + correct formal spec)
- LLM generation: GPT-4 with uncertainty quantification (3 methods above)
- Varying uncertainty thresholds: 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99
- Measure: Abstention rate, false negative rate (generated wrong spec), false positive rate (abstained on correct spec)
- Plot: ROC curve (false negative vs abstention rate), select optimal threshold

**Expected Outcome**:
- Threshold 0.5: Low abstention (10-20%), high false negatives (20-40%)
- Threshold 0.9: Medium abstention (30-50%), low false negatives (2-5%)
- Threshold 0.95: High abstention (50-70%), very low false negatives (<1%)
- Optimal: Threshold 0.85-0.9 (30-40% abstention, 2-5% false negatives)
- Safety-critical systems: Choose 0.95+ (prioritize correctness over coverage)

**Paper Contribution**:
- Formal framework for hybrid system verification
- Probabilistic soundness guarantees
- Abstention strategy for safety-critical deployment
- First end-to-end verified neuro-symbolic pipeline (with probabilistic bounds)

**Feasibility**: Medium-High (theoretical framework + empirical validation)

---

## PRIORITY 2: HIGH-VALUE GAPS (Strengthen Paper, Not Critical)

### Gap 2.1: Real-Time Provenance for Streaming Data

**Current State**:
- ProvSQL: Batch processing (PostgreSQL queries)
- Scallop: Static programs (no incremental updates)
- No system for real-time provenance computation on streaming data

**Application Domains**:
- Aerospace: Sensor data streams (real-time anomaly detection with explanation)
- Financial: Trading data (millisecond-latency provenance for regulatory compliance)
- Healthcare: Continuous patient monitoring (explain alert triggers)

**Required Validation**:
- Incremental provenance computation algorithms
- Benchmark: Latency (time to explanation), throughput (events/second)
- Comparison: Batch recomputation vs incremental vs approximate (provenance sketches)

**Feasibility**: Low (substantial implementation effort, specialized expertise)

**Paper Impact**: High (enables real-world deployment in time-critical systems)

**Recommendation**: Future work section (acknowledge gap, propose approach, leave implementation for follow-on research)

---

### Gap 2.2: Federated Provenance with Privacy Preservation

**Current State**:
- Provenance assumes centralized computation
- No framework for federated learning with provenance tracking
- Privacy concerns: Provenance may reveal sensitive data lineage

**Application Domains**:
- Healthcare: Multi-hospital federated learning (HIPAA compliance requires audit trails)
- Financial: Cross-institution fraud detection (provenance without revealing proprietary data)

**Required Validation**:
- Cryptographic provenance protocols (secure multi-party computation)
- Differential privacy for provenance (ε-DP guarantees)
- Benchmark: Privacy-utility tradeoff

**Feasibility**: Very Low (cryptography expertise, significant implementation)

**Paper Impact**: Medium-High (emerging area, but niche)

**Recommendation**: Future work section

---

### Gap 2.3: Scalable Provenance for Web-Scale Systems

**Current State**:
- ProvSQL: Tested on database queries (thousands to millions of facts)
- Scallop: Small to medium programs
- No evaluation at web scale (billions of facts, millions of rules)

**Bottleneck**:
- Provenance polynomials grow exponentially for complex derivations
- Storage overhead (polynomial size)
- Computation overhead (polynomial evaluation)

**Required Validation**:
- Provenance sketches (approximate, bounded error)
- Hierarchical provenance (summary at different granularities)
- Lazy provenance computation (on-demand, only for queried facts)
- Benchmark: Scalability (time, space complexity) vs accuracy

**Feasibility**: Medium (algorithmic, requires implementation)

**Paper Impact**: Medium (practical deployment, but not core contribution)

**Recommendation**: Future work or optional experiment (if time permits)

---

## PRIORITY 3: EXPLORATORY GAPS (Nice-to-Have, Time Permitting)

### Gap 3.1: LLM Meta-Cognition for DSL Selection

**Current State**:
- Human expert chooses DSL based on problem characteristics
- No system for automatic DSL selection (Prolog vs ASP vs SMT vs PDDL vs Lean?)

**Hypothesis**:
- LLM can classify problems and suggest appropriate DSL
- Features: Problem structure, constraints, domain, required guarantees

**Required Validation**:
- Dataset: 500 problems with expert-labeled "best DSL"
- LLM classifier: GPT-4 with few-shot examples
- Evaluation: Accuracy of DSL selection
- Ablation: What problem features most predictive?

**Feasibility**: Medium (dataset construction, classification straightforward)

**Paper Impact**: Low-Medium (interesting, but not critical)

**Recommendation**: Optional (if space in discussion section)

---

### Gap 3.2: Provenance Compression Techniques

**Current State**:
- Provenance polynomials can be very large (exponential in derivation depth)
- No systematic study of compression techniques

**Potential Techniques**:
- Polynomial factorization (share common subexpressions)
- Provenance sketches (probabilistic data structures)
- Hierarchical summarization (details on-demand)

**Required Validation**:
- Benchmark: Size reduction (compression ratio) vs information loss
- Metrics: Exact provenance recovery, approximate bounds

**Feasibility**: Low-Medium (algorithmic, requires theory + implementation)

**Paper Impact**: Low (optimization, not core contribution)

**Recommendation**: Future work

---

### Gap 3.3: Cross-System Provenance Interoperability

**Current State**:
- Each system has own provenance format (ProvSQL, Scallop, s(CASP))
- No standard interchange format

**Proposed**:
- Universal provenance format (extending SMT-LIB or W3C PROV?)
- Provenance exchange protocol
- Converters between formats

**Feasibility**: Low (standardization effort, community buy-in)

**Paper Impact**: Low (infrastructure, not research contribution)

**Recommendation**: Future work (mention as open challenge)

---

## PRIORITY 4: NEGATIVE RESULTS (Important to Document)

### Gap 4.1: When Does Pure LLM Outperform Hybrid?

**Current State**:
- Paper focuses on hybrid superiority (40-160% improvements)
- But: Are there domains where pure LLM is sufficient or better?

**Hypothesis**:
- Simple problems: Pure LLM faster (no symbolic overhead)
- Ambiguous problems: Pure LLM more flexible (symbolic may fail on ill-defined specs)
- Open-ended tasks: Pure LLM creative (symbolic too rigid)

**Required Validation**:
- Identify domains where hybrid underperforms
- Measure: Latency (pure vs hybrid), accuracy, user satisfaction
- Example domains: Creative writing (LLM better), simple arithmetic (hybrid overkill), exploratory analysis (LLM flexibility needed)

**Expected Outcome**:
- Simple problems (<3 constraints): Pure LLM comparable or faster
- Complex problems (10+ constraints): Hybrid dramatically better
- Ambiguous problems: Pure LLM may be preferable (symbolic fails on vague specs)

**Paper Impact**: High (honesty about limitations, guide practitioners)

**Recommendation**: Include in discussion section (when NOT to use hybrid approach)

---

### Gap 4.2: Failure Modes of Hybrid Systems

**Current State**:
- Success stories well-documented (AlphaGeometry, TReMu, etc.)
- Failure modes less studied

**Potential Failure Modes**:
1. **LLM Parsing Errors Propagate**: Wrong DSL generation → symbolic solver verifies wrong spec
2. **Symbolic Solver Timeouts**: LLM generates valid but unsolvable problem
3. **Explanation Complexity**: Provenance polynomial too large for human understanding
4. **Iteration Divergence**: Refinement loop doesn't converge (Logic-LM++ semantic reversion addresses this)

**Required Validation**:
- Collect failure cases from experiments
- Categorize failure modes
- Measure frequency of each mode
- Propose mitigation strategies

**Paper Impact**: High (practical deployment guidance)

**Recommendation**: Include in evaluation section (error analysis subsection)

---

## SUMMARY: PRIORITIZED EXPERIMENTAL PLAN

### Must-Do (Critical for Paper Completeness)

1. **Temporal Reasoning Benchmark** (Gap 1.1)
   - 5-level benchmark suite (extraction → ordering → calculation → counterfactual → conditional)
   - Dataset: 1000 problems per level (5000 total)
   - Evaluate: Pure LLM vs Hybrid vs Symbolic
   - Timeline: 3-4 weeks (dataset construction + experiments)

2. **Multi-DSL Fine-Tuning** (Gap 1.2)
   - Dataset: 1000 problems × 5 DSLs (Prolog, ASP, SMT, PDDL, Datalog)
   - Training: Single-DSL, Multi-DSL Simultaneous, Curriculum, Transfer Learning
   - Evaluate: Pass@1, syntax errors, semantic correctness
   - Timeline: 4-6 weeks (dataset + training + evaluation)

3. **Provenance Quality User Study** (Gap 1.3)
   - Participants: 30-60 domain experts
   - Systems: Provenance polynomials, s(CASP), xASP, LLM post-hoc, Attention
   - Metrics: Faithfulness, comprehensibility, actionability, trust calibration
   - Timeline: 6-8 weeks (recruitment + study + analysis)

4. **Hybrid Verification Framework** (Gap 1.4)
   - Uncertainty quantification (3 methods)
   - Selective verification (threshold optimization)
   - Dataset: 1000 problems with ground truth
   - Measure: Abstention rate, false negative/positive rates
   - Timeline: 2-3 weeks (implementation + experiments)

**Total Timeline**: 15-21 weeks (3.5-5 months) for critical experiments

### Should-Do (Strengthen Paper)

5. **Failure Mode Analysis** (Gap 4.2)
   - Collect failures from all experiments
   - Categorize and measure frequency
   - Timeline: Concurrent with above (analysis during experiments)

6. **Pure LLM vs Hybrid Boundaries** (Gap 4.1)
   - Identify when pure LLM sufficient
   - Timeline: 1-2 weeks (analysis + small experiments)

**Total Timeline**: +2-3 weeks

### Nice-to-Have (Time Permitting)

7. **Scalable Provenance** (Gap 2.3) - If time permits
8. **LLM Meta-Cognition** (Gap 3.1) - If space in discussion

---

## RESOURCE REQUIREMENTS

### Computational
- **Fine-tuning**: 3× RTX A6000 GPUs (or equivalent cloud rental: ~$2-5K)
- **Experiments**: Standard workstation (GPT-4 API access: ~$500-1000)
- **Total Compute Budget**: $3-6K

### Human Resources
- **Dataset Construction**: 100-200 hours (problem creation, DSL translations, ground truth)
- **User Study**: 60-120 hours (recruitment, study sessions, analysis)
- **Experiments**: 80-120 hours (implementation, running, analysis)
- **Total Effort**: 240-440 hours (3-5.5 months full-time, or 6-11 months part-time)

### Data Requirements
- **Temporal Benchmark**: 5000 problems (create or curate)
- **Multi-DSL Dataset**: 5000 problem-DSL pairs (create)
- **Verification Dataset**: 1000 NL-formal spec pairs (curate from existing benchmarks + create)
- **User Study Materials**: 50 problems (subset of above)

---

## CONCLUSION

**Critical Gaps (Must Address)**:
1. Temporal reasoning benchmark (no standard evaluation)
2. Multi-DSL fine-tuning (unknown transfer learning effects)
3. Provenance quality metrics (no quantitative comparison)
4. Hybrid verification framework (formalization gap)

**High-Value Gaps (Strengthen Paper)**:
5. Failure mode analysis (practical guidance)
6. Pure LLM vs hybrid boundaries (honest limitations)

**Exploratory Gaps (Nice-to-Have)**:
7. Real-time, federated, web-scale provenance (future work)
8. LLM meta-cognition, compression, interoperability (future work)

**Experimental Plan**: Focus on Gaps 1.1-1.4 + 4.1-4.2 (6 experiments, 17-24 weeks)

**Expected Outcome**: Comprehensive paper with novel benchmarks, quantitative provenance evaluation, multi-DSL fine-tuning insights, and verified hybrid framework - advancing neuro-symbolic AI from research prototype to deployable technology for safety-critical systems.
