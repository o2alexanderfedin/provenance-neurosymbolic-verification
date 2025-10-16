# Neuro-Symbolic AI Benchmarks and Performance Metrics

## Overview

This document organizes benchmark results by reasoning domain, focusing on quantitative performance metrics from neuro-symbolic systems (2023-2025).

---

## 1. Arithmetic and Mathematical Reasoning

### GSM8K (Grade School Math 8K)

**Dataset**: 1,319 grade school math word problems, 2-8 steps each

**Baseline LLM Performance**:
- Standard prompting: ~50-60% (varies by model)
- Chain-of-Thought: ~65-70%

**Neuro-Symbolic Improvements**:

| Method | Accuracy | Improvement over Baseline |
|--------|----------|--------------------------|
| Chain-of-Thought | ~70% | Baseline |
| Self-Consistency + CoT | 74% | +10-17.9% over CoT |
| Prolog Generation | ~75-80% | +9.5% with data augmentation |
| Logic-LM | ~80-85% | +39.2% over LLM alone |
| RL Models (2024) | 90.8% (7B model) | State-of-the-art |

**Key Findings**:
- Performance degrades significantly (up to 65%) when irrelevant clauses added to problems
- LLMs rely on pattern matching rather than genuine reasoning
- Prolog-based approaches consistently outperform Chain-of-Thought

### MATH Benchmark

**Dataset**: High school competition mathematics, multiple difficulty levels

**Performance**:
- RL-enhanced models (2024): 77.4% on MATH 500 subset (7B parameters)
- Previous SOTA: ~50-60% for similar model sizes

### GSM-Symbolic (2024)

**Dataset**: Apple's symbolic template variant of GSM8K for controlled evaluation

**Key Finding**: All SOTA models show performance degradation when:
- Only numerical values altered
- Seemingly relevant but unnecessary clauses added (up to 65% drop)

**Implication**: Current LLMs lack genuine logical reasoning capability

### BigBench Arithmetic

**Task**: Four basic operations on 5-digit numbers

**Status**: Remains largely unsolved by pure LLM approaches

**Recent Work**: IGC (Integrating a Gated Calculator) - December 2024

### Arithmetic with Tool Augmentation

**Performance Highlights**:
- ReTool on AIME2024: 67.0%
- ReTool on AIME2025: 49.3%
- Training: Only 400 RL steps

---

## 2. Logic and Formal Reasoning

### PrOntoQA

**Dataset**: 500 examples in 5-hop fictional character subset

**Task**: Synthetic relational reasoning, transitivity, set membership

**Performance**:
- LLM Baseline: ~40-50%
- Logic-LM: Significant improvement (part of +39.2% average)
- Near-perfect with proper symbolic formulation

### FOLIO (First-Order Logic)

**Dataset**: 1,430 examples (unique conclusions) paired with 487 premise sets

**Task**: Natural language reasoning with FOL annotations, commonsense scenarios

**Performance**:
- Random guess baseline: 33.33% (true/false/unknown)
- LLaMA-13B (8-shot): 33.63% (barely above random)
- Logic-LM: Substantial improvement (part of +39.2% average)
- qwen2.5:32b (2025): Improved but still challenging

**Key Finding**: Most challenging benchmark for current LLMs

### ProofWriter

**Dataset**: Logical proof generation and verification

**Performance**:
- Logic-LM: Significant improvement over baselines
- LeanReasoner (March 2024): Near-perfect accuracy with only 100 training examples
- Other methods: Require entire training set

**Notable**: Logic-LM and GPT-4 CoT only methods achieving strong performance with limited data

### LogicBench (2024)

**Purpose**: Systematic evaluation of logical reasoning in LLMs

**Findings**: Reveals significant limitations in current models across diverse logical tasks

### ProverQA

**Task**: Logical proof verification

**Status**: Used in 2025 evaluations of neurosymbolic systems

---

## 3. Commonsense Reasoning

### CommonsenseQA

**Performance with Self-Consistency**:
- Chain-of-Thought: Baseline
- Self-Consistency + CoT: +5% improvement

### StrategyQA

**Task**: Multi-hop strategy questions

**Performance**:
- Proof of Thought: Improved performance with formal verification
- Provides interpretable and verifiable results

### AR-LSAT

**Task**: Law school admission test analytical reasoning

**Performance**:
- Logic-LM: Significant improvement (part of multi-benchmark evaluation)

---

## 4. Geometry and Spatial Reasoning

### International Mathematical Olympiad (IMO) - Geometry

**AlphaGeometry Performance**:
- 30 IMO geometry problems
- AlphaGeometry (2024): 25/30 (83.3%)
- Previous SOTA: 10/30 (33.3%)
- Human gold medalist: 25.9/30 (86.3%)
- **Improvement**: +150% over previous SOTA

**AlphaGeometry 2 Performance**:
- 50 IMO problems (2000-2024)
- Solved: 42/50 (84%)
- Human gold medalist average: 40.9/50 (81.8%)
- **First AI to exceed human gold medalist average**

### 3D Visual Grounding (2024)

**Approach**: Reformulated as Constraint Satisfaction Problem

**Task**: Zero-shot 3D spatial reasoning

**Results**: Promising but specific metrics not disclosed in search results

---

## 5. Mathematical Theorem Proving

### International Mathematical Olympiad (IMO) - All Problems

**AlphaProof + AlphaGeometry 2 (2024)**:
- Problems solved: 4/6 at IMO 2024
- Total score: 28/42 points
- Medal level: Silver medal standard
- **First AI to achieve medal level at IMO**

**AlphaGeometry 2 Historical Performance (2025)**:
- IMO problems 2000-2024: 42/50 solved
- Exceeds gold medalist average of 40.9

---

## 6. Planning and Problem-Solving

### PDDL Planning Benchmarks

**Task**: Automated planning with Planning Domain Definition Language

**Performance**:
- Neurosymbolic approaches: 66% solve rate
- GPT-4 Chain-of-Thought: 29% solve rate
- **Improvement**: +127% over pure LLM approach

**Failure Modes** (LLM+P system):
- Forgetting action effects
- Attempting impossible actions
- Lacking systematic search
- Invalid PDDL generation: 15% of attempts
- Incomplete specification handling failures

### IPC (International Planning Competition)

**Status**: 2023 competition featured 5 tracks for cutting-edge planning methods

**Integration**: Neurosymbolic methods (Plan-SOFAI, ZeroC) showing promise

### Trust the PRoC3S (2024)

**Domain**: Long-horizon robotics with CSP

**Approach**: LLMs output parameterized functions as Continuous CSP

---

## 7. Multi-Domain Benchmarks

### Big-Bench

**Coverage**: Difficult and diverse tasks for LLMs

**Usage**: Referenced in neurosymbolic AI research for broad capability assessment

**Status**: Specific neurosymbolic performance metrics not widely reported yet

### ScienceQA

**Graph of Thoughts Performance**:
- T5-base baseline: 85.19%
- GoT with T5-base: 87.59%
- **Improvement**: +2.4 absolute percentage points

---

## 8. Visual and Multimodal Reasoning

### NeurASP Applications

**Tasks**: Visual reasoning combining perception with logical rules

**Approach**: Neural network perception + ASP symbolic reasoning

**Key Capability**: Bidirectional improvement (neural helps symbolic, symbolic helps neural)

### Multimodal Entailment Trees (EMNLP 2024)

**Task**: Video reasoning with neurosymbolic approach

**Status**: Active research area, specific benchmarks emerging

---

## 9. Constraint Satisfaction and Optimization

### Constraint Satisfaction Problems (CSP)

**ConstraintLLM**:
- First LLM specifically for constraint programming
- Industrial-level problems
- Specific accuracy metrics pending publication

**3D Visual Grounding as CSP**:
- Zero-shot capability demonstrated
- Objects and spatial relations as variables and constraints

### Continuous CSP (Robotics)

**Trust the PRoC3S**:
- LLM-generated parameterized functions
- Solved through sampling or optimization
- Applied to long-horizon robotics tasks

---

## 10. Knowledge Graph Reasoning

### Knowledge Graph Completion

**Approaches**: Neurosymbolic methods combining embeddings with logical rules

**Performance**: Comparable or superior to pure neural approaches with benefits:
- Better interpretability
- Improved generalization
- Rule-based explainability

### Query Answering on KGs

**Neural-Symbolic Methods**:
- Logically-informed embeddings
- Embedding with logical constraints
- Rule learning approaches

**Advantage**: Handles incomplete KGs better than pure neural methods

---

## 11. Program Synthesis

### Code Generation Benchmarks

**CoNaLa (Natural Language to Code)**:
- RoBERTaMarian: 35.74 BLEU, 13.8% exact match
- LUKE-Marian: 89.34 BLEU, 78.50% exact match

**DJANGO**:
- LUKE-Marian: 89.34 BLEU, 78.50% exact match

### String Transformation (R3NN)

- Single sample: 63% accuracy
- 100 samples: 94% accuracy
- Neural baselines: 42%
- **Improvement**: +50% with single sample, +124% with 100 samples

### Tratto (Oracle Generation)

**Performance**:
- Accuracy: 73%
- Precision: 72%
- F1-Score: 61%
- Best symbolic/neural: 61% accuracy, 62% precision, 37% F1
- **F1 Improvement**: +65% over best alternative

### SmartLabel (Active Learning)

**Success Rate**: 98% of benchmarks
**User Interaction**: <5 rounds average

---

## 12. Temporal and Causal Reasoning

### Causal Inference Benchmarks

**CausalProbe 2024**:
- Significant performance drop compared to earlier causal Q&A benchmarks
- LLMs show level-1 (shallow) causal reasoning only
- Cannot make meaningful deductions from counterfactuals

**Key Limitation**: LLMs infer causality from temporal/spatial sequence, not true causal understanding

### Temporal Reasoning (ACL 2024)

**Finding**: "Large Language Models Can Learn Temporal Reasoning"

**Challenge**: Joint temporal and causal reasoning remains difficult

**Status**: Active research area with emerging benchmarks

---

## 13. Answer Set Programming Tasks

### ASP Generation Quality

**LLASP**:
- Significantly outperforms non-fine-tuned models
- Beats larger general-purpose LLMs
- Especially superior in semantic correctness

**ASP with LLM Integration**:
- Natural language logic puzzles → ASP programs
- Answer Set Networks: First to fine-tune LLMs with Deep Probabilistic Logic

### Logic Puzzle Solving

**Approach**: LLM generates ASP program, ASP solver finds solutions

**Advantages**:
- Deterministic solving
- Guaranteed correctness
- Explainable results

---

## 14. Scientific Reasoning

### SciAgent Benchmark (2024)

**Coverage**: Multiple scientific domains

**Task**: Tool-augmented scientific reasoning

**Status**: First benchmark for fine-tuned tool-augmented LLMs in science

---

## Performance Summary by Domain

| Domain | Best System | Performance | vs LLM Baseline |
|--------|-------------|-------------|-----------------|
| Geometry | AlphaGeometry 2 | 84% (IMO) | +150% vs prev SOTA |
| Math Proofs | AlphaProof | 67% (4/6 IMO) | First medal level |
| Multi-Logic | Logic-LM | +39.2% | Over LLM alone |
| Arithmetic | RL Models | 90.8% (GSM8K) | +20-30% vs CoT |
| Planning | Neurosymbolic | 66% solve | +127% vs GPT-4 |
| Strings | R3NN | 94% (100-shot) | +124% vs neural |
| Oracle Gen | Tratto | 61% F1 | +65% vs alternatives |
| Spatial QA | GoT | 87.59% | +2.4% vs CoT |

---

## Key Findings Across Benchmarks

### What Works

1. **Symbolic Solver Integration**: Consistent 20-60% improvements
2. **Self-Consistency**: 10-25% gains across reasoning tasks
3. **Iterative Refinement**: Crucial for complex problems
4. **Domain-Specific Fine-tuning**: Smaller specialized models beat large general ones
5. **Synthetic Data**: Enables superhuman performance (AlphaGeometry)
6. **Formal Verification**: Guarantees correctness, enables trust

### What Doesn't Work Well

1. **Pure LLM on Formal Logic**: Near-random on FOLIO
2. **LLM Arithmetic**: Fails on 5-digit calculations
3. **Causal Reasoning**: Only shallow (level-1) capabilities
4. **Novel Operators**: Performance degrades on unseen logical structures
5. **Irrelevant Context**: Up to 65% accuracy drop with distractors

### Failure Modes

1. **Hallucination**: LLMs generate invalid formal syntax (15% in PDDL)
2. **Incomplete Reasoning**: Forget constraints/effects in planning
3. **Pattern Matching**: Rely on training data patterns, not true reasoning
4. **Numerical Errors**: Cannot reliably perform basic arithmetic
5. **Robustness**: Sensitive to problem formulation and irrelevant details

---

## Trends in Benchmark Development (2024-2025)

1. **Controlled Variants**: GSM-Symbolic to isolate reasoning from memorization
2. **Formal Annotations**: FOLIO, ProofWriter with FOL ground truth
3. **Multi-Modal**: Video reasoning, 3D spatial tasks
4. **Stress Testing**: CausalProbe revealing shallow reasoning
5. **Tool-Use Evaluation**: SciAgent, AutoPlanBench for tool-augmented systems
6. **Efficiency Metrics**: Runtime, data efficiency, not just accuracy
7. **Explainability Assessment**: Measuring interpretability of reasoning traces

---

## Research Priorities Based on Benchmark Results

1. **Improve Causal Reasoning**: Move beyond level-1 (shallow) to level-2 (deep)
2. **Robust Arithmetic**: Reliable multi-digit calculation without tools
3. **Generalization**: Transfer to out-of-distribution problems
4. **Efficiency**: Reduce computational cost of self-consistency approaches
5. **Formal Correctness**: Higher success rate in generating valid syntax
6. **Distractor Resistance**: Maintain performance with irrelevant information
7. **Meta-Cognition**: Know when to use tools vs. internal reasoning

---

## References

See references_neurosymbolic.md for complete citations and URLs.
