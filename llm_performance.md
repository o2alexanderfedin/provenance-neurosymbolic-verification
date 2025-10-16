# LLM Code Generation Performance Matrix

## Executive Summary

Modern LLMs have achieved near-human performance on standard code generation benchmarks, with top models exceeding 90% accuracy on HumanEval. However, formal code generation (theorem proving) remains significantly more challenging, with success rates typically below 50% on competition-level mathematics. This document synthesizes performance data across general-purpose code generation, formal verification, and specialized models.

---

## 1. General Code Generation Performance (2024-2025)

### 1.1 HumanEval Benchmark Performance

**HumanEval**: 164 Python programming problems evaluating functional correctness. Industry-standard benchmark since 2021.

| Model | HumanEval Pass@1 | Year | Notes |
|-------|-----------------|------|-------|
| **Gemini 2.5 Pro** | ~99% | 2025 | Highest reported performance |
| **Claude 3.5 Sonnet** | 92% | 2024 | Leading anthropic model |
| **GPT-4o** | 90.2% | 2024 | OpenAI's multimodal flagship |
| **DeepSeek-V3** | ~90% | 2024 | Open-source competitive model |
| **Gemini Ultra** | 74.4% | 2023 | Previous generation |
| **Claude 2** | 71.2% | 2023 | Previous generation |
| **GPT-4** | ~67% | 2023 | Earlier GPT-4 version |
| **Llama 3.1 405B** | ~65-70% | 2024 | Largest open-source model |
| **DeepSeek-V2.5** | ~65-70% | 2024 | Earlier DeepSeek version |

**Key Findings**:
- Top proprietary models exceed 90%, approaching human-level performance
- Open-source models (Llama 3.1, DeepSeek) narrowing gap to GPT-4o
- 20+ percentage point improvement from 2023 to 2025 for leading models

### 1.2 MBPP Benchmark Performance

**MBPP (Mostly Basic Python Problems)**: 1,000 crowd-sourced Python programming problems, more diverse than HumanEval.

| Model | MBPP Pass@1 | Context |
|-------|-------------|---------|
| **GPT-4** | 75-80% | Leading performance tier |
| **Claude 3.5** | 70-75% | Competitive with GPT-4 |
| **DeepSeek-V3** | 70-75% | Strong open-source showing |
| **Smaller models (<10B)** | 30-50% | Significant performance gap |

**Observations**:
- MBPP proves more challenging than HumanEval due to greater diversity
- 10-15% absolute performance gap between top models and MBPP vs. HumanEval
- Problem diversity exposes weaknesses in pattern matching

### 1.3 SWE-bench: Real-World Software Engineering

**SWE-bench**: Real-world GitHub issues from popular Python repositories. Tests end-to-end software engineering capabilities.

| Model | SWE-bench Score | Significance |
|-------|----------------|--------------|
| **Claude 3.7 Sonnet** | 70.3% | Record-breaking performance |
| **OpenAI o1** | ~49% | Second-tier performance |
| **GPT-4o** | ~35-40% | Substantial gap to Claude |
| **Open-source models** | <30% | Significant performance gap |

**Critical Insights**:
- Real-world engineering tasks remain far more challenging than synthetic benchmarks
- 21+ percentage point gap between Claude 3.7 and OpenAI o1
- SWE-bench correlates better with practical coding assistance utility
- Reasoning-focused models (o1) don't automatically translate to SWE-bench success

---

## 2. Formal Code Generation & Theorem Proving

### 2.1 Theorem Proving Benchmarks

**Key Benchmarks**:
- **miniF2F**: 244 formalized mathematics problems from MATH dataset and competitions
- **PUTNAMBENCH**: First benchmark including Lean 4, Isabelle, and Coq simultaneously
- **ProofNet**: Curated formal proofs for evaluation
- **MathComp/AFP**: Real-world mathematical libraries

### 2.2 Formal Verification Performance (2024-2025)

| System | Backend | Benchmark | Success Rate | Notes |
|--------|---------|-----------|--------------|-------|
| **AlphaProof** | Lean | IMO 2024 | Silver Medal | 4/6 problems solved |
| **AlphaGeometry 2** | Symbolic | IMO Geometry | 83% (25yr) | 200x faster symbolic engine |
| **DeepSeek-Prover-v2-671B** | Lean | miniF2F | ~35-40% | Largest reasoning model |
| **DeepSeek-Prover-v2-7B** | Lean | miniF2F | ~25-30% | Efficient smaller model |
| **LeanDojo/ReProver** | Lean | mathlib | ~30-35% | Retrieval-augmented prover |
| **CoqPilot** | Coq | Plugin tests | ~20-30% | LLM-based proof generation |
| **Copra** | Lean/Coq | Multi-language | ~15-25% | First multi-language system |

**Key Observations**:
- IMO silver medal achievement (AlphaProof) marks major milestone
- Competition-level mathematics remains challenging (35-40% success rate)
- Multi-language support (Lean, Coq, Isabelle) still immature
- Retrieval augmentation provides 10-15% performance boost

### 2.3 Proof Search Limitations

**Data Scarcity**:
- Proof Pile dataset: Only 500MB of formal proofs across 6 languages
- Orders of magnitude smaller than code generation training data
- Manual curation remains laborious bottleneck

**Theorem Proving Challenges**:
- Search space exponentially larger than code generation
- Requires deep mathematical reasoning, not pattern matching
- Limited training data compared to general programming
- Proof tactics and strategies hard to learn from examples alone

---

## 3. Specialized Models & Domain-Specific Performance

### 3.1 Logic Programming Generation (Prolog, ASP)

**Prolog Generation** (Yang, Chen, Tam 2024):
- **GPT-4o**: 74% Pass@1 on GSM8K-Prolog
- **DeepSeek-V3**: 80% accuracy on FinQA financial reasoning (vs. 63-76% CoT)
- **Llama2/CodeLlama/Mistral**: Outperformed Chain-of-Thought with Prolog generation

**Answer Set Programming (ASP)**:
- **LLASP** (fine-tuned): Substantially outperformed larger general LLMs on semantic correctness
- **GPT-4**: Moderate success with few-shot ASP generation, frequent errors
- **ASPBench 2025**: LLMs struggle most with answer set computation (core solving)
- **DeepSeek-R1, o4-mini, Gemini-2.5-flash-thinking**: Poor performance on ASP entailment

**Key Insight**: Domain-specific fine-tuning (LLASP) trumps scale for formal languages. Specialized training on 1-10B parameter models beats 100B+ general models.

### 3.2 Constraint Programming Generation

**ConstraintLLM** (2024):
- Fine-tuned on Qwen2.5-Coder-32B with QLoRA (3x NVIDIA A6000 GPUs)
- Competed with GPT-4o and DeepSeek-V3-685B on industrial CP benchmarks
- Cost-effective specialized training matches massive general models

**GenCP** (Constrained Text Generation):
- Faster than Beam Search
- 100% constraint satisfaction guarantee
- LLM domain prediction + CP search integration

**Logic.py** (ZebraLogicBench):
- 65% absolute improvement over baseline LLMs
- Domain-specific language + constraint solver architecture

### 3.3 Neuro-Symbolic Integration Performance

| System | Architecture | Benchmark | Improvement | Year |
|--------|--------------|-----------|-------------|------|
| **TReMu** | LLM + Python temporal code | GPT-4o temporal reasoning | 29.83 → 77.67 (160%) | 2024 |
| **CRONKGQA** | Transformer + Temporal KG | CronQuestions | 120% vs. next best | 2024 |
| **CLMASP** | LLM + ASP planning | bAbI, StepGame, CLUTRR | 90%+ execution rate | 2023 |
| **AlphaGeometry 2** | Gemini + symbolic deduction | IMO geometry 25yr | 53% → 83% | 2024 |
| **Proof of Thought** | LLM + Z3 SMT | Mathematical reasoning | 40% error reduction | 2023 |

**Pattern**: Hybrid architectures combining LLMs for understanding with symbolic systems for reasoning show 40-160% improvements over pure neural approaches.

---

## 4. Performance Factors & Tradeoffs

### 4.1 Model Size vs. Specialization

**Scale Effects**:
- General pattern: Larger models (100B+) show better raw performance
- **Exception**: Domain-specific fine-tuning on smaller models (1-32B) can outperform 100B+ general models on specialized tasks
- **ConstraintLLM**: 32B specialized ≈ 685B general (DeepSeek-V3)
- **LLASP**: Lightweight specialized >> 175B+ general for ASP

**Optimal Strategy**:
- Use 100B+ frontier models for general code generation
- Fine-tune 7-32B models for domain-specific formal languages
- Cost-performance tradeoff favors specialized models for repeated formal tasks

### 4.2 Quantifier Handling

**Performance by Logic Complexity**:
- **Quantifier-free first-order logic**: 70-90% success (well-supported by SMT solvers)
- **First-order logic with quantifiers**: 40-60% success (heuristic approaches)
- **Higher-order logic**: 20-40% success (theorem provers required)
- **Recursive definitions**: 50-70% success (better with logic programming)

**Key Observation**: LLMs struggle with quantifier reasoning, performing 20-30% worse than quantifier-free equivalents.

### 4.3 Training Data Leakage Effects

**Recent Analysis** (2024):
- ~37% of model behavior on established benchmarks attributable to solution leakage
- Models memorize solutions from training data contamination
- Novel, unpublished test cases show 15-25% lower performance
- Overestimation of true generalization capabilities

**Implications**:
- Published benchmark scores likely overestimate real-world performance
- Need for continuously refreshed evaluation datasets
- Private evaluation sets critical for accurate assessment

---

## 5. Temporal & Quantitative Reasoning Performance

### 5.1 Temporal Reasoning Benchmarks (2024-2025)

**TempTabQA** (11,454 QA pairs):
- **Top LLMs**: Lag humans by 13.5+ F1 points
- **Challenge areas**: Multi-step reasoning, implicit constraints, temporal aggregation

**Test of Time (ToT)** - Google Research:
- **Gemini 1.5 Pro**: 88.72% (AWE graphs) vs. 51.07% (Complete graphs)
- **37+ percentage point gap** based on graph structure alone
- **Duration questions**: 13-16% accuracy across ALL models (abysmal)
- **Timezone questions**: 74-90% accuracy (pattern matching, not reasoning)

**TIME Benchmark** (38,522 QA pairs):
- Level 1 (extraction): 70-80% accuracy
- Level 2 (ordering): 50-65% accuracy
- Level 3 (counterfactual): 30-45% accuracy

**ComplexTempQA** (100M+ QA pairs):
- Large-scale training improves basic temporal extraction
- Does NOT solve compositional temporal reasoning
- Quantity ≠ quality for temporal understanding

### 5.2 Allen's Interval Algebra Performance

**ChronoSense Benchmark** (16 Allen relation tasks):
- LLMs handle Allen relations **inconsistently, even symmetrical ones**
- Symbolic reasoners (GQR, SparQ, QSRlib): Efficient within tractable subsets
- LLMs fail to reliably apply formal temporal logic rules

**Key Finding**: LLMs lack formal temporal reasoning capabilities. Hybrid approaches combining LLM extraction with symbolic temporal reasoners achieve 40-160% improvements.

---

## 6. Error Rates by Problem Type

### 6.1 Syntax vs. Semantic Error Distribution

**Based on 557 incorrect solutions across HumanEval** (2024 study):

| Error Category | CodeGen-16B | InCoder-1.3B | ChatGPT | Average |
|----------------|-------------|--------------|---------|---------|
| **Code Block Error** | 53.2% | 60.0% | 43.2% | 52.1% |
| **Garbage Code** | 27.3% | 38.1% | 22.4% | 29.3% |
| **Condition Error** | 15-20% | 15-20% | 15-20% | ~17% |
| **Constant Value Error** | 10-15% | 10-15% | 10-15% | ~12% |
| **Other Semantic** | 5-10% | 5-10% | 5-10% | ~7% |

**Semantic Error Breakdown**:
- **Garbage Code**: Only comments, meaningless snippets, wrong logical direction
- **Condition Errors**: Missing or incorrect conditionals
- **Constant Value Errors**: Wrong values in function arguments, assignments

**Syntactic Error Breakdown**:
- **Code Block Errors**: Missing blocks, incorrect structure, indentation issues
- Attributed to misinterpreting task requirements

### 6.2 Error Patterns Across Model Families

**Universal Issues** (all LLMs exhibit):
- Incorrect conditions in complex logic
- Wrong logical direction (reversing intended flow)
- Struggles with multi-line, multi-location errors

**Size-Independent Issues**:
- Complex logic condition handling poor across all model sizes
- No clear correlation between parameter count and logical reasoning quality
- Suggests fundamental architecture limitations, not just scale

---

## 7. Pass@K Metrics & Sampling Strategies

### 7.1 Pass@K Definition

**Pass@1**: Probability of generating correct solution on first attempt (most important metric)

**Pass@K**: Probability of generating at least one correct solution in K attempts

**Typical Results**:
- Pass@1: 70-90% (top models, HumanEval)
- Pass@10: 85-95% (substantial improvement)
- Pass@100: 90-98% (diminishing returns)

**Practical Implications**:
- Self-correction with multiple sampling provides 10-20% improvement
- Cost-performance tradeoff: Pass@10 offers good balance
- Pass@100 rarely worth computational cost

### 7.2 Sampling Temperature Effects

**Temperature Settings**:
- **T=0.0** (deterministic): Best for well-defined problems, single correct solution
- **T=0.3-0.5**: Balanced exploration, recommended for code generation
- **T=0.8-1.0**: High diversity, useful for creative solutions but higher error rate

**Pass@K Performance by Temperature**:
- Low temperature (0.0-0.3): Best Pass@1, moderate Pass@K improvement
- Medium temperature (0.4-0.6): Balanced Pass@1 and Pass@K
- High temperature (0.7+): Worse Pass@1, best Pass@K diversity

---

## 8. Comparative Analysis: LLMs vs. Specialized Systems

### 8.1 SMT Solver Performance

**Z3 Performance** (2024 benchmarks):
- **QF_BV** (bit-vectors): 95%+ success on 10,000+ constraint problems
- **QF_LIA** (linear integer arithmetic): 90%+ success
- **Quantified formulas**: 40-60% success (heuristic E-matching)
- **15x speedup** over Yices on specific integer problems
- **6x average speedup** over Choco/MINION constraint solvers

**SMT vs. LLM Code Generation**:
- SMT: 100% correctness when solution found (proof-based)
- LLM: 70-90% correctness (statistical, no guarantees)
- SMT: Limited to formal specifications
- LLM: Natural language to code, broader applicability

### 8.2 ASP Solver Performance

**ASP Performance** (CLASP, recent benchmarks):
- **9x geomean speedup** over SMT-based approaches for Datalog synthesis
- Non-hallucination property: Everything in answer set has justification
- Stable model semantics prevents circular reasoning

**ASP vs. LLM Logic Generation**:
- ASP solvers: Guaranteed correctness for valid programs
- LLM-generated ASP: 30-74% syntactic correctness (LLASP)
- LLM-generated ASP: Lower semantic correctness without fine-tuning
- Hybrid approach: LLM generates, ASP solver verifies and executes

### 8.3 Constraint Logic Programming (CLP)

**CLP(FD) Performance**:
- Faster than SMT for small finite domains (<1000 values)
- Competitive with dedicated constraint solvers (Gecode, Choco)
- Global constraints (all_different, cumulative) provide domain-specific optimization

**SMT vs. CLP Performance Crossover**:
- **SMT faster**: Large domains (>1000 values), theory combination, mostly-ground problems
- **CLP faster**: Small finite domains, logical structure, recursive definitions
- **No universal winner**: Problem structure determines optimal tool

---

## 9. Synthesis: Performance Landscape Summary

### 9.1 Current State of the Art (2025)

**General Code Generation**:
- Top models (Gemini 2.5 Pro, Claude 3.5 Sonnet, GPT-4o): 90-99% HumanEval
- Real-world engineering (SWE-bench): 70% best performance (Claude 3.7)
- Gap between synthetic benchmarks and real-world tasks remains substantial

**Formal Code Generation**:
- Theorem proving (miniF2F): 35-40% success rate (DeepSeek-Prover-v2-671B)
- Competition mathematics (IMO): Silver medal achieved (AlphaProof)
- Multi-language formal systems: 15-30% success rate
- Significant room for improvement; human-level formal reasoning not achieved

**Specialized Formal Languages**:
- Domain-specific fine-tuning essential for >70% accuracy
- Hybrid neuro-symbolic approaches: 40-160% improvement over pure neural
- Logic programming generation: 70-80% with proper prompting/fine-tuning
- Constraint programming: Competitive with frontier models using specialized 32B models

### 9.2 Key Performance Predictors

**Factors Positively Correlating with Success**:
1. **Problem structure clarity**: Well-defined problems yield 20-30% better results
2. **Domain-specific fine-tuning**: 15-40% improvement over general models
3. **Hybrid neuro-symbolic approaches**: 40-160% improvement
4. **Retrieval augmentation**: 10-15% improvement (theorem proving)
5. **Multiple sampling (Pass@K)**: 10-20% improvement (K=10 vs. K=1)

**Factors Negatively Correlating with Performance**:
1. **Quantifier complexity**: 20-30% performance drop per quantifier level
2. **Temporal reasoning depth**: 15-35% accuracy drop from Level 1 to Level 3
3. **Multi-step logical dependencies**: 10-25% accuracy drop
4. **Novel problem types** (no training data): 15-25% accuracy drop
5. **Semantic vs. syntactic challenges**: Semantic errors 2-3x harder to avoid

### 9.3 Practical Recommendations

**For General Code Generation**:
- Use frontier models (GPT-4o, Claude 3.5 Sonnet, Gemini 2.5 Pro)
- Expect 90%+ accuracy on well-defined problems
- Apply self-correction (Pass@10) for critical code

**For Formal Verification**:
- Use specialized systems (AlphaProof, DeepSeek-Prover-v2) for theorem proving
- Expect 35-40% success rate; always verify outputs
- Consider hybrid approaches combining LLM + symbolic reasoners

**For Domain-Specific Formal Languages**:
- Fine-tune 7-32B models on domain-specific data (LLASP approach)
- Use constrained generation (JSON Schema, grammar prompting)
- Employ external interpreters/verifiers (Prolog, ASP solvers)
- Expect 70-80% accuracy with proper domain adaptation

**For Temporal Reasoning**:
- Never rely on pure LLM temporal reasoning (13-16% duration accuracy)
- Use hybrid approaches: LLM extraction + symbolic temporal reasoners
- Expect 40-160% improvement with proper integration
- Allen's algebra and STN/STNU solvers essential for verification

---

## 10. Future Performance Projections

### 10.1 Near-Term Trajectory (2025-2026)

**Expected Improvements**:
- General code generation: 95%+ HumanEval (marginal improvements)
- SWE-bench: 75-80% (more significant potential)
- Theorem proving: 45-55% miniF2F (active research area)
- Temporal reasoning: 60-70% with hybrid approaches (currently 30-45% Level 3)

**Bottlenecks**:
- Training data quality plateau for general coding
- Formal proof data scarcity (500MB vs. TB for general code)
- Compositional reasoning remains challenging
- Multi-step logical inference not scaling with parameter count

### 10.2 Long-Term Challenges (2027+)

**Fundamental Limitations**:
- Statistical learning cannot guarantee formal correctness
- Quantifier reasoning requires architectural changes
- Temporal reasoning needs explicit symbolic integration
- Explainability demands hybrid neuro-symbolic approaches

**Research Directions**:
- Integrated neuro-symbolic architectures (not post-hoc combinations)
- Provenance-aware LLM training for explainable reasoning
- Specialized tokenization for formal languages
- Curriculum learning for compositional reasoning

### 10.3 The 74% Pass@1 Milestone

**From Papers Directory** (compass_artifact reference):
- **GPT-4o**: 74% Pass@1 accuracy on Prolog generation (financial reasoning)
- **Context**: GSM8K-Prolog dataset with external interpreter
- **Significance**: Domain-specific generation crossing 70% threshold
- **Comparison**: Pure CoT approaches at 63-76%

**Interpretation**:
- 74% represents state-of-the-art for specialized formal language generation
- External interpreter validation essential for formal correctness
- Declarative target languages (Prolog, ASP) more amenable to LLM generation
- 10-15% gap from general code generation performance (85-90% HumanEval)

---

## Conclusion

LLM code generation has achieved impressive performance on general programming tasks (90-99% HumanEval) but formal code generation remains challenging (35-40% theorem proving, 74% specialized formal languages). The key insight: **hybrid neuro-symbolic approaches combining LLM understanding with symbolic reasoning and verification provide 40-160% improvements** over pure neural methods.

For formal code generation and verification, specialized models with domain-specific training and external verification (SMT solvers, ASP solvers, theorem provers) represent the state of the art, outperforming pure LLM approaches while maintaining formal correctness guarantees.

**Critical Takeaway**: Frontier LLMs excel at code generation pattern matching but lack formal reasoning capabilities. Applications requiring correctness guarantees must integrate symbolic verification systems, not rely on LLMs alone.
