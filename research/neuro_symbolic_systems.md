**Navigation**: [🏠 Home](../README.md) | [📄 Paper](../paper_main.md) | [🚀 Quick Start](../QUICK_START.md) | [📑 Index](../PROJECT_INDEX.md)

---

# Neuro-Symbolic AI Systems Survey (2023-2025)

## Overview

Neuro-symbolic AI combines neural networks with symbolic reasoning to leverage both data-driven learning and logical inference. Research has grown exponentially from 53 publications in 2020 to 236 in 2023, with continued growth in 2024-2025.

---

## Major Systems and Frameworks

### 1. AlphaGeometry & AlphaGeometry 2 (DeepMind, 2024-2025)

**Architecture**: Neuro-symbolic system combining neural language model with symbolic deduction engine

**Domain**: Euclidean geometry problem solving

**Performance**:
- AlphaGeometry (2024): Solved 25/30 IMO geometry problems (83.3%)
- Human gold medalist average: 25.9/30 problems
- Previous SOTA: 10/30 problems
- AlphaGeometry 2 (2025): Solved 42/50 IMO problems (2000-2024), exceeding gold medalist average of 40.9

**Key Features**:
- Symbolic engine attempts proofs using deductive logic
- Neural LM adds auxiliary constructs (points/lines) when symbolic engine gets stuck
- Trained on 100M synthetic proofs from 500M random diagrams
- AlphaGeometry 2 uses Gemini, trained with 10x more synthetic data
- Symbolic engine is 100x faster than predecessor

**Training**: Self-supervised on synthetic geometry proofs

**Citation**: Nature, January 17, 2024; AlphaGeometry 2 announced February 5, 2025

---

### 2. AlphaProof (DeepMind, 2024)

**Architecture**: Neuro-symbolic combining pre-trained LM with AlphaZero reinforcement learning

**Domain**: Formal mathematical proof generation in Lean

**Performance**:
- 2024 IMO: 28/42 points (silver medal standard)
- Solved 4/6 IMO 2024 problems with AlphaGeometry 2
- First AI to reach medal level at IMO

**Key Features**:
- Translates natural language to formal Lean proof language
- Self-trains on millions of mathematical proofs across difficulty levels
- Continues training during competition with iterative refinement
- Uses formal verification for guaranteed correctness

**Architecture Type**: Interactive - neural generates candidates, symbolic verifier provides feedback

---

### 3. Logic-LM & Logic-LM++ (2023-2024)

**Architecture**: LLM + symbolic solver with iterative refinement

**Domain**: Multi-domain logical reasoning

**Performance**:
- Logic-LM: +39.2% over LLM alone, +18.4% over Chain-of-Thought
- Alternative source: +62.6% over standard prompting, +23.5% over CoT
- Logic-LM++: State-of-the-art on multiple reasoning benchmarks
- LeanReasoner: Near-perfect accuracy on ProofWriter with only 100 examples

**Benchmarks**: ProofWriter, PrOntoQA, FOLIO, LogicalDeduction, AR-LSAT

**Key Features**:
- LLM translates natural language to symbolic formulation
- Symbolic solver performs deterministic inference
- Self-refinement module uses solver error messages to revise formulations
- Logic-LM++ supports multi-step refinement with semantic reversion

**Architecture Type**: Pipeline with feedback loop

**Citation**: EMNLP 2023 (Findings)

---

### 4. Proof of Thought (2024)

**Architecture**: LLM program synthesis + theorem prover verification

**Domain**: Open-ended reasoning with formal verification

**Performance**:
- Improved performance on StrategyQA
- Successfully demonstrated on novel multimodal reasoning tasks
- Provides verifiable and interpretable results

**Key Features**:
- Custom interpreter converts LLM outputs to First Order Logic
- Z3 theorem prover scrutinizes formal constructs
- JSON-based DSL balances logical precision with human readability
- Bridges intuitive LLM reasoning with formal logic verification

**Architecture Type**: Interactive - iterative generation and verification

**Citation**: NeurIPS 2024 Sys2Reasoning Workshop (arXiv:2409.17270)

---

### 5. Logical Neural Networks - LNN (IBM)

**Architecture**: Neurons represent weighted real-valued logic components

**Domain**: General-purpose neuro-symbolic reasoning

**Key Features**:
- Every neuron corresponds to a formula component in weighted real-valued logic
- Omnidirectional inference (not limited to predefined targets)
- End-to-end differentiable
- Minimizes novel loss function capturing logical contradiction
- Highly interpretable disentangled representation
- Seamlessly provides both neural learning and symbolic reasoning

**Applications**:
- Neuro-symbolic inductive logic programming
- Natural language understanding
- Extensions for various reasoning tasks

**Status**: Open-source implementation maintained by IBM Research

**Citation**: AAAI 2022; arXiv:2112.03324

---

### 6. LLASP (2024)

**Architecture**: Fine-tuned lightweight LLM for Answer Set Programming

**Domain**: ASP code generation from natural language

**Performance**:
- Outperforms non-fine-tuned models significantly
- Superior to majority of larger LLMs, especially semantically
- Trained on custom dataset covering fundamental ASP patterns

**Key Innovation**:
- First specialized model for declarative ASP formalism
- Addresses gap where general LLMs fail at ASP generation
- Demonstrates that lightweight specialized models outperform large general models for symbolic tasks

**Architecture Type**: Pipeline - natural language to ASP code

**Publication**: KR 2024 (21st International Conference on Principles of Knowledge Representation and Reasoning), Hanoi, November 2-8, 2024

**Code**: https://github.com/EricaCoppolillo/LLASP

**Citation**: arXiv:2407.18723

---

### 7. NeurASP (2023 Update)

**Architecture**: Neural networks integrated into Answer Set Programming

**Domain**: Neurosymbolic perception and reasoning

**Key Features**:
- Treats neural network output as probability distribution over ASP atomic facts
- Can use pre-trained networks in symbolic computation
- Improves neural perception via symbolic reasoning in ASP
- Trains neural networks with ASP rules for semantic constraints
- Bidirectional benefit: neural improves symbolic, symbolic improves neural

**Applications**: Visual reasoning, logic puzzle solving with neural perception

**Status**: Open-source at github.com/azreasoners/NeurASP

**Citation**: IJCAI 2020; Updated arXiv:2307.07700 (July 2023)

---

### 8. DeepProbLog (2018-2024)

**Architecture**: Neural probabilistic logic programming

**Domain**: Probabilistic reasoning with neural components

**Key Features**:
- Extends ProbLog with neural predicates
- Probabilistic facts parameterized by neural networks
- Adapts ProbLog inference and learning techniques for neural integration
- Combines deep learning with probabilistic logic programming

**Status**: Actively maintained
- Version 2.0.5: January 4, 2024
- Version 2.0.6: August 9, 2024

**Implementation**: Python package available via PyPI

**Citation**: NeurIPS 2018; Artificial Intelligence journal 2021

---

### 9. Scallop (2023-2024)

**Architecture**: Declarative neurosymbolic programming language

**Domain**: General neurosymbolic applications

**Key Features**:
- Flexible symbolic representation based on relational data model
- Declarative Datalog-based language with recursion, aggregation, negation
- Automatic differentiable reasoning based on provenance semirings
- Direct PyTorch integration

**Performance**:
- Comparable or superior accuracy to SOTA models
- Superior runtime and data efficiency
- Enhanced interpretability and generalizability

**Publications**:
- PLDI 2023 (June)
- Monograph: "Neurosymbolic Programming in Scallop: Principles and Practice" (2024)

**Citation**: arXiv:2304.04812

---

### 10. ConstraintLLM (October 2024)

**Architecture**: LLM + constraint programming framework

**Domain**: Industrial-level constraint optimization problems

**Key Features**:
- First LLM specifically designed for CP modeling
- Automatically generates formal PDDL models for constraint optimization
- CARM (retrieval-augmented mechanism) provides in-context exemplars
- Aims for zero-shot and few-shot CP modeling
- Trustworthy neuro-symbolic AI with symbolic solver verification

**Architecture Type**: Pipeline with retrieval augmentation

**Citation**: arXiv:2510.05774

---

### 11. s(CASP) - Constraint Answer Set Programming

**Architecture**: Goal-directed constraint ASP without grounding

**Domain**: Constraint satisfaction with commonsense reasoning

**Key Features**:
- Top-down goal-directed search (unlike traditional ground-and-solve ASP)
- Supports negation as failure (NAF) and classical negation
- Variables kept during execution and in answer sets (similar to CLP)
- Can solve problems that cannot be grounded
- Suitable for commonsense reasoning requiring answer justification

**Related Systems**: Multiple CASP solvers including acsolver, clingcon, ezcsp, idp, inca, dingo, mingo, aspmt, clingo[l,dl], ezsmt

**Community**: Active ASPOCP workshop series (2023, 2024, 2025)

**Implementation**: Available as SWI-Prolog library

**Citations**: Cambridge Core - Theory and Practice of Logic Programming (2021); arXiv:2107.08252

---

### 12. xASP (Explanation-based ASP)

**Architecture**: Answer Set Programming with explanation generation

**Domain**: Explainable ASP reasoning

**Key Features**:
- Generates explanations for why atoms belong/don't belong to answer sets
- Computes minimal assumption sets, explanation sequences, explanation DAGs
- Interactive xASP navigator for visual exploration
- Focus on explainable AI needs

**Recent Integration**: Combined with LLMs to translate natural language logic puzzles to ASP

**Citation**: NSF publication 10462534

---

### 13. Tool-Augmented LLM Frameworks (2024)

#### ReTool (April 2025)
- Tool-augmented RL framework for mathematical reasoning
- Code interpreter integration during RL
- Performance: 67.0% on AIME2024, 49.3% on AIME2025 (400 training steps)

#### ARTIST (April 2025)
- Agentic reasoning with autonomous tool selection
- Multi-turn reasoning with tool results feedback
- Supports self-correction and iterative refinement

#### SciAgent (February 2024)
- First fine-tuned tool-augmented LLM for scientific reasoning
- Benchmark covering multiple scientific domains

---

### 14. SAT/SMT Solver Integration Systems (2024)

#### SatLM
- Combines LLMs with automated theorem provers
- State-of-the-art on multiple datasets

#### DiLA (Differential Logic Layer)
- LLM parses problems into SAT specifications
- Differential logic layer provides formal solving

#### Counterexample-Guided Synthesis
- Combines LLM generation with Z3 SMT solver verification
- Iterative refinement using counterexamples
- Implementations with GPT-4, GPT-3.5 Turbo

#### MCP Solver (2025)
- Bridges LLMs with symbolic solvers via Model Context Protocol
- Multi-paradigm solving capability

---

### 15. PDDL Planning Systems (2024)

#### Planning Copilot
- Automated planner selection (classical vs numeric)
- Syntactic domain validation
- LLM-assisted planning

#### Plan2Evolve
- LLM-based PDDL generation and optimization
- Generates symbolic planning domains as data generators
- Transforms plans into chain-of-thought traces

#### PDDLLM
- First complete planning domain generation from scratch
- No predefined predicates or actions
- Autonomously derives logical structures from LLM knowledge

**Performance**: 66% solve rate vs 29% for GPT-4 with CoT prompting

---

### 16. Prompting-Based Approaches (2024)

#### Tree of Thoughts (ToT)
- Models reasoning as tree exploration
- Significant improvement over linear chain-of-thought

#### Graph of Thoughts (GoT)
- Non-sequential thought representation as graphs
- +2.4% accuracy improvement (85.19% to 87.59%) on ScienceQA with T5-base

#### Chain-of-Thought with Self-Consistency
- Samples multiple reasoning paths, selects most consistent
- Performance improvements:
  - GSM8K: +17.9% (up to 74% total)
  - SVAMP: +11.0% to +14%
  - MultiArith: +24%
  - CommonsenseQA: +5%
  - ARC: +4-5%

#### Confidence-Improved Self-Consistency (CISC) (2024)
- 46% reduction in computational costs
- Maintains or improves accuracy

---

### 17. Prolog-Based Systems (2024)

#### Thought-Like-Pro
- LLMs generate Prolog code for logical reasoning
- Prolog engine validates reasoning trajectories
- Outperforms Chain-of-Thought on arithmetic reasoning

**GSM8K-Prolog Dataset**: Curated for Prolog code generation evaluation

**Performance**: +9.5% and +4.0% accuracy with permuted samples for data augmentation

**Rationale**: Prolog's declarative nature easier for LLMs than imperative control flow

---

### 18. Other Notable Systems

#### Answer Set Networks (ASN) (December 2024)
- Graph Neural Network-based scalable ASP
- First to show LLM fine-tuning with Deep Probabilistic Logic Programming
- GPU batching and parallelization

#### LLM-ARC
- LLM Actor generates declarative logic programs
- Automated Reasoning Critic evaluates and provides feedback
- Neurosymbolic framework for enhanced logical reasoning

#### Dolphin
- Programmable framework for scalable neurosymbolic learning
- Focus on efficiency and scalability

#### RECOVER
- Framework for failure detection and recovery
- Addresses robustness in neurosymbolic systems

#### LOOP
- Plug-and-play framework for enhanced planning in autonomous systems

---

## System Comparison Summary

| System | Domain | Architecture Type | Key Strength | Performance Highlight |
|--------|--------|------------------|--------------|---------------------|
| AlphaGeometry 2 | Geometry | Interactive | Synthetic data generation | 84% IMO problem solve rate |
| AlphaProof | Math proofs | Interactive | Formal verification | Silver medal at IMO 2024 |
| Logic-LM++ | Multi-domain logic | Pipeline + feedback | Multi-step refinement | +39.2% over LLM alone |
| Proof of Thought | General reasoning | Interactive | Interpretability | Verifiable formal proofs |
| LLASP | ASP generation | Pipeline | Domain specialization | Beats general LLMs |
| Scallop | General | Embedded DSL | Data efficiency | Superior interpretability |
| ConstraintLLM | Optimization | Pipeline | Industrial applicability | First CP-specific LLM |
| ReTool | Math reasoning | Tool-augmented | RL integration | 67% on AIME2024 |
| Self-Consistency | Multi-domain | Ensemble | Robustness | +17.9% on GSM8K |

---

## Architecture Patterns

### 1. Pipeline Architecture
- Neural → Symbolic (one-way): Logic-LM, LLASP, ConstraintLLM
- Symbolic → Neural (one-way): Knowledge graph embeddings
- Neural ↔ Symbolic (feedback): Logic-LM++, AlphaProof

### 2. Interactive/Integrated Architecture
- Tight coupling: LNN, Scallop, DeepProbLog, NeurASP
- Alternating: AlphaGeometry, AlphaProof, Proof of Thought
- Parallel ensemble: Self-Consistency, Graph of Thoughts

### 3. Tool-Augmented Architecture
- Code execution: ReTool, PAL, PoT
- Symbolic solvers: Logic-LM, SatLM, DiLA
- Specialized reasoners: PDDL planners, Prolog engines

---

## Training Approaches

### Self-Supervised on Synthetic Data
- AlphaGeometry: 100M proofs from synthetic diagrams
- AlphaProof: Millions of mathematical problems
- DeepProbLog: Probabilistic program learning

### Fine-tuning on Domain Data
- LLASP: Specialized ASP dataset
- SciAgent: Scientific reasoning tasks
- ReTool: RL with tool integration

### In-Context Learning
- Logic-LM: Few-shot prompting with solver feedback
- ConstraintLLM: Retrieval-augmented exemplars
- Tool-augmented systems: Dynamic tool selection

---

## Key Trends (2023-2025)

1. **Formal Verification**: Increased use of theorem provers and type systems for guaranteed correctness
2. **Synthetic Data**: Self-supervised training on programmatically generated problems
3. **Lightweight Specialization**: Smaller specialized models outperforming large general models
4. **Iterative Refinement**: Feedback loops between neural and symbolic components
5. **Tool Integration**: LLMs as coordinators for specialized symbolic tools
6. **Multimodal Integration**: Extending beyond text to geometry, visual reasoning
7. **Production Systems**: Moving from research prototypes to industrial applications

---

## Research Gaps Identified

According to the 2024 systematic review:
- Meta-cognition capabilities remain limited
- Trustworthiness and reliability need improvement
- Seamless integration between neural and symbolic remains challenging
- Explainability needs further development
- Computational efficiency for real-time applications

---

## References

See references_neurosymbolic.md for complete citation list with URLs.
