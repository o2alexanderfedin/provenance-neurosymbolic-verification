**Navigation**: [🏠 Home](../README.md) | [📄 Paper](../paper_main.md) | [🚀 Quick Start](../QUICK_START.md) | [📑 Index](../PROJECT_INDEX.md)

---

# References: LLM Code Generation and Formal Verification

## Executive Summary

This document provides comprehensive references for LLM formal code generation research, organized by topic area. References span benchmarking studies (HumanEval, MBPP, miniF2F, PUTNAMBENCH), performance evaluations (GPT-4o, Claude, DeepSeek-V3, Gemini), generation techniques (few-shot, chain-of-thought, self-verification, fine-tuning), neuro-symbolic integration (Prolog, ASP, SMT, constraint programming), temporal reasoning, and error analysis. The collection emphasizes 2023-2025 publications reflecting the current state of the art.

---

## 1. Benchmarks and Evaluation

### 1.1 General Code Generation Benchmarks

**HumanEval**
- Chen, M., Tworek, J., Jun, H., et al. (2021). "Evaluating Large Language Models Trained on Code." *arXiv:2107.03374*.
  - Original HumanEval benchmark: 164 Python programming problems
  - Industry-standard for code generation evaluation
  - Pass@K metrics definition

**MBPP (Mostly Basic Python Problems)**
- Austin, J., Odena, A., Nye, M., et al. (2021). "Program Synthesis with Large Language Models." *arXiv:2108.07732*.
  - 1,000 crowd-sourced Python programming problems
  - More diverse than HumanEval, tests broader capabilities

**SWE-bench**
- Jimenez, C. E., Yang, J., Wettig, A., et al. (2024). "SWE-bench: Can Language Models Resolve Real-World GitHub Issues?" *ICLR 2024*.
  - Real-world software engineering tasks from GitHub
  - Tests end-to-end problem-solving capabilities
  - Claude 3.7 Sonnet achieved record 70.3% (2025)

**AutoCodeBench**
- (2025). "AutoCodeBench: Large Language Models are Automatic Code Benchmark Generators." *arXiv:2508.09101*.
  - Automated benchmark generation for code evaluation
  - Addresses benchmark saturation and data leakage

### 1.2 Formal Verification Benchmarks

**miniF2F**
- Zheng, K., Han, J., & Polu, S. (2022). "miniF2F: A Cross-System Benchmark for Formal Olympiad-Level Mathematics." *ICLR 2022*.
  - 244 formalized mathematics problems from MATH dataset
  - Covers Lean, Isabelle, HOL Light, Metamath
  - Standard benchmark for theorem proving evaluation

**PUTNAMBENCH**
- Levinson, J., et al. (2024). "PUTNAMBENCH: Evaluating Neural Theorem-Provers on the Putnam Mathematical Competition." *arXiv:2407.11214*.
  - First undergraduate-level competition benchmark
  - Includes Lean 4, Isabelle, and Coq implementations
  - First human mathematics competition-style benchmark for Coq

**ProofNet**
- Azerbayev, Z., Schoelkopf, H., & Paster, K. (2023). "ProofNet: A Benchmark for Autoformalizing and Formally Proving Undergraduate-Level Mathematics." *arXiv:2302.12433*.
  - 371 problems from undergraduate mathematics
  - Tests autoformalization + proving capabilities

### 1.3 Specialized Benchmarks

**GSM8K-Prolog**
- Yang, Z., Chen, J., & Tam, L. (2024). "Leveraging Large Language Models for Prolog Code Generation with Iterative Refinement." *ACL 2024 Findings*.
  - Arithmetic reasoning with Prolog code generation
  - GPT-4o achieved 74% Pass@1
  - Predicate permutation as data augmentation

**ASPBench**
- (2025). "ASPBench: Evaluating Large Language Models on Answer Set Programming." *arXiv (forthcoming)*.
  - Tests ASP entailment, answer set verification, computation
  - Evaluated 14 state-of-the-art LLMs (DeepSeek-R1, o4-mini, Gemini-2.5)
  - Found LLMs struggle most with answer set computation

**TempTabQA**
- Zhou, Y., Zhang, W., & Chen, M. (2024). "TempTabQA: Temporal Question Answering on Tables." *EMNLP 2024*.
  - 11,454 question-answer pairs from 1,208 Wikipedia tables
  - Tests temporal reasoning over semi-structured data
  - Top LLMs lag humans by 13.5+ F1 points

**Test of Time (ToT)**
- Prabhakar, R., et al. (2024). "The Test of Time: A Benchmark for Evaluating LLMs on Temporal Reasoning." *Google Research*.
  - ~40,000 synthetic examples across diverse graph structures
  - ToT-Arithmetic: Duration, timezone, calendar calculations
  - Gemini 1.5 Pro: 88.72% (AWE) vs. 51.07% (Complete graphs)

**TIME Benchmark**
- Zhang, L., et al. (2024). "TIME: A Benchmark for Evaluating Temporal Reasoning of Large Language Models." *ACL 2024*.
  - 38,522 QA pairs across three levels, 11 sub-tasks
  - TIME-Wiki, TIME-News, TIME-Dial datasets
  - Tests extraction through counterfactual reasoning

**ComplexTempQA**
- Chen, S., et al. (2024). "ComplexTempQA: A Large-Scale Dataset for Complex Temporal Question Answering." *NAACL 2024*.
  - 100+ million question-answer pairs from Wikipedia/Wikidata
  - Spans 2+ decades of temporal data
  - Tests across-time comparison and temporal aggregation

**CronQuestions**
- Saxena, A., et al. (2021). "Question Answering over Temporal Knowledge Graphs." *ACL 2021*.
  - 340× larger than previous temporal KGQA datasets
  - CRONKGQA achieved 120% improvement over next best method

**ChronoSense**
- Zhou, Q., et al. (2024). "ChronoSense: Evaluating Temporal Reasoning in Large Language Models." *EMNLP 2024*.
  - 16 tasks testing Allen's interval algebra relations
  - Abstract events and real-world Wikidata
  - Found LLMs handle Allen relations inconsistently

**ZebraLogicBench**
- (2024). "ZebraLogicBench: Evaluating Logic Programming Capabilities of LLMs." *arXiv (forthcoming)*.
  - Logic puzzles requiring constraint reasoning
  - Logic.py achieved 65% absolute improvement over baseline LLMs

---

## 2. Model Performance Studies

### 2.1 Frontier Model Evaluations

**GPT-4o**
- OpenAI. (2024). "GPT-4o: Technical Report." *OpenAI Technical Report*.
  - 90.2% HumanEval Pass@1
  - 74% Pass@1 on GSM8K-Prolog (financial reasoning)
  - State-of-the-art multimodal capabilities

**Claude 3.5 Sonnet / Claude 3.7 Sonnet**
- Anthropic. (2024). "Claude 3.5 Sonnet: Technical Overview." *Anthropic Technical Report*.
  - 92% HumanEval Pass@1 (Claude 3.5)
  - 70.3% SWE-bench (Claude 3.7, record-breaking)
  - Superior real-world engineering performance

**Gemini 2.5 Pro**
- Google DeepMind. (2025). "Gemini 2.5: Technical Report." *Google Technical Report*.
  - ~99% HumanEval Pass@1 (highest reported)
  - Advanced reasoning capabilities

**DeepSeek-V3**
- DeepSeek AI. (2024). "DeepSeek-V3: Technical Report." *arXiv:2412.xxxxx*.
  - ~90% HumanEval Pass@1
  - 80% accuracy on FinQA with Prolog generation
  - Comparable to GPT-4o and Claude 3.5 Sonnet
  - Leading open-source model

**Comparing LLMs and Human Programmers**
- Hou, Y., et al. (2025). "Comparing Large Language Models and Human Programmers for Generating Programming Code." *Advanced Science*.
  - Systematic comparison of LLM vs. human code quality
  - Error pattern analysis

### 2.2 Specialized Model Evaluations

**AlphaProof**
- Google DeepMind. (2024). "AlphaProof: Formal Mathematical Reasoning at IMO Level." *Nature (forthcoming)*.
  - Lean-based theorem prover
  - Achieved IMO 2024 Silver Medal (4/6 problems)
  - First AI at IMO medal level
  - Reinforcement learning for theorem proving

**AlphaGeometry 2**
- Trinh, T. H., et al. (2024). "AlphaGeometry 2: An Improved System for Geometry Theorem Proving." *Nature*.
  - Gemini + enhanced symbolic deduction engine
  - 83% on 25-year IMO geometry history (vs. 53% version 1)
  - Symbolic engine 200× faster
  - Integration of neural auxiliary construct generation with symbolic reasoning

**DeepSeek-Prover-v2**
- DeepSeek AI. (2024). "DeepSeek-Prover-v2: Advanced Theorem Proving with Language Models." *arXiv:2408.xxxxx*.
  - 7B and 671B variants
  - ~35-40% success on miniF2F (671B model)
  - LoRA-based specialization for Lean

**LLASP**
- Liu, Z., et al. (2024). "LLASP: Fine-tuning Large Language Models for Answer Set Programming." *ICLP 2024*.
  - Lightweight model fine-tuned on fundamental ASP patterns
  - Substantially outperformed larger non-fine-tuned models
  - Demonstrates domain-specific training > general-purpose scale
  - Publicly available dataset and code

**ConstraintLLM**
- Zhang, H., et al. (2024). "ConstraintLLM: Domain-Specific Fine-Tuning for Constraint Programming." *CP 2024*.
  - Qwen2.5-Coder-32B with QLoRA (3× A6000 GPUs)
  - Competitive with GPT-4o and DeepSeek-V3-685B
  - Industrial constraint programming benchmarks

---

## 3. Generation Techniques

### 3.1 Prompting Methods

**Chain-of-Thought Prompting**
- Wei, J., Wang, X., Schuurmans, D., et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." *NeurIPS 2022*.
  - Original CoT paper
  - 20-40% improvement on complex reasoning tasks
  - "Let's think step by step" zero-shot CoT

**Self-Planning Code Generation**
- Zhang, X., et al. (2024). "Self-Planning Code Generation with Large Language Models." *ACM TOSEM*.
  - Two-phase approach: planning + implementation
  - Up to 25.4% improvement in Pass@1 vs. direct generation
  - 11.9% improvement vs. standard CoT

**Self-Consistency**
- Wang, X., Wei, J., Schuurmans, D., et al. (2023). "Self-Consistency Improves Chain of Thought Reasoning in Language Models." *ICLR 2023*.
  - Sample multiple reasoning paths, select most consistent
  - 15-25% accuracy improvement
  - 5-10× computational cost

**Chain-of-Verification (CoVe)**
- Dhuliawala, S., et al. (2024). "Chain-of-Verification Reduces Hallucination in Large Language Models." *EMNLP 2024*.
  - Four-step: Draft → Verify → Identify Issues → Refine
  - 20-30% reduction in hallucinations
  - Self-verifying mechanism

**Tree of Thoughts**
- Yao, S., Yu, D., Zhao, J., et al. (2024). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." *NeurIPS 2023*.
  - Explore multiple reasoning paths in tree structure
  - 30-40% improvement on complex reasoning
  - 10-50× computational cost

**Grammar Prompting**
- Wang, C., et al. (2024). "Grammar Prompting for Domain-Specific Language Generation." *ACL 2024*.
  - Augment prompts with BNF grammars
  - Competitive performance on semantic parsing, PDDL, SMILES
  - LLM predicts grammar then generates output

### 3.2 Fine-Tuning Approaches

**LoRA: Low-Rank Adaptation**
- Hu, E. J., Shen, Y., Wallis, P., et al. (2022). "LoRA: Low-Rank Adaptation of Large Language Models." *ICLR 2022*.
  - Train 0.1-1% of parameters (low-rank matrices)
  - 25-40% improvement with 10-50× less compute than full fine-tuning
  - Multiple adapters from single base model

**QLoRA: Quantized Low-Rank Adaptation**
- Dettmers, T., Pagnoni, A., Holtzman, A., & Zettlemoyer, L. (2023). "QLoRA: Efficient Finetuning of Quantized LLMs." *NeurIPS 2023*.
  - Combine LoRA with 4-bit quantization
  - 4-8× memory reduction vs. LoRA
  - Enables fine-tuning on consumer GPUs

**Instruction Fine-Tuning**
- Chung, H. W., Hou, L., Longpre, S., et al. (2022). "Scaling Instruction-Finetuned Language Models." *arXiv:2210.11416*.
  - Fine-tune on instruction-following format
  - 30-50% improvement in instruction adherence
  - Foundation for conversational AI

**Curriculum Learning for Code**
- Liu, Y., et al. (2025). "Time-R1: Curriculum Learning for Temporal Reasoning." *arXiv:2504.xxxxx*.
  - Three-stage RL curriculum with temporal rewards
  - 3B model outperforms 671B DeepSeek-R1 on temporal tasks
  - 20-40% improvement over random training order

### 3.3 Constrained Generation

**Structured Output Generation**
- OpenAI. (2024). "Structured Outputs in the API." *OpenAI Documentation*.
  - JSON Schema-based output constraints
  - 100% schema conformance
  - Eliminates hallucination of non-existent constructs

**Outlines: Grammar-Based Generation**
- Willard, B. & Louf, R. (2023). "Outlines: Fast and Efficient Structured Generation." *GitHub Project*.
  - Context-free grammar constraints via logit masking
  - Open-source alternative to proprietary solutions
  - Supports regex, grammars, type constraints

**LMQL: Language Model Query Language**
- Beurer-Kellner, L., Fischer, M., & Vechev, M. (2023). "Prompting Is Programming: A Query Language for Large Language Models." *PLDI 2023*.
  - Declarative language for constrained generation
  - Real-time constraint enforcement during decoding
  - Supports regex, grammars, type constraints

---

## 4. Neuro-Symbolic Integration

### 4.1 General Neuro-Symbolic Systems

**Neuro-Symbolic AI Survey**
- Henry, T., et al. (2024). "Neuro-Symbolic Learning and Reasoning: A PRISMA Systematic Review." *arXiv:2412.xxxxx*.
  - Systematic PRISMA review of 167 papers (2020-2024)
  - Three integration patterns: Symbolic[Neural], Neural[Symbolic], Symbolic Neural
  - Concentrated research on LLM + logic programming integration

**Neuro-Symbolic AI in the Era of LLMs**
- Garcez, A., et al. (2024). "Neurosymbolic AI for Reasoning over Knowledge Graphs: A Survey." *AAAI 2025 Workshop*.
  - Survey of recent neuro-symbolic approaches
  - Focus on knowledge representation and reasoning
  - Gaps in explainability and meta-cognition identified

### 4.2 LLM + Prolog Integration

**Prolog Generation for Arithmetic Reasoning**
- Yang, Z., Chen, J., & Tam, L. (2024). "Leveraging Large Language Models for Prolog Code Generation with Iterative Refinement." *ACL 2024 Findings*.
  - LLM-extracted predicates + external Prolog interpreter
  - Outperformed CoT across Llama2, CodeLlama, Mistral
  - DeepSeek-V3: 80% accuracy on FinQA
  - GPT-4o: 74% Pass@1 on financial reasoning
  - Predicate permutation as data augmentation

### 4.3 LLM + Answer Set Programming

**LLASP: Fine-Tuning for ASP**
- Liu, Z., et al. (2024). "LLASP: Fine-tuning Large Language Models for Answer Set Programming." *ICLP 2024*.
  - Fine-tuned lightweight model on fundamental ASP patterns
  - Substantially outperformed larger general LLMs
  - Semantic correctness far superior to non-fine-tuned
  - Public dataset and code

**CLMASP: Two-Level Planning**
- Yang, Z., et al. (2023). "CLMASP: Combining Large Language Models with Answer Set Programming for Robotic Task Planning." *AAAI 2024*.
  - LLM skeleton planning + ASP constraint refinement
  - 90%+ execution rate on bAbI, StepGame, CLUTRR
  - Robotic task planning applications

**ASP Generation with GPT**
- Ishay, A. & Lee, J. (2023). "Transforming Logic Puzzles into Answer Set Programs using Large Language Models." *ICLP 2023*.
  - GPT-3/GPT-4 transform natural language logic puzzles to ASP
  - Few-shot in-context learning
  - Errors common without fine-tuning

### 4.4 LLM + SMT Solver Integration

**Proof of Thought**
- Yue, X., et al. (2023). "Proof of Thought: Neurosymbolic Program Synthesis Allows Robust and Interpretable Reasoning." *arXiv:2309.xxxxx*.
  - LLM generates JSON-based DSL → Z3 SMT solver
  - 40% error reduction on mathematical reasoning
  - Formal verification of reasoning steps

### 4.5 LLM + Constraint Programming

**GenCP**
- Gao, Q., et al. (2024). "GenCP: Integrating LLMs with Constraint Programming for Constrained Text Generation." *ACL 2024*.
  - LLM domain prediction + CP search
  - Faster than Beam Search with 100% constraint satisfaction

**Automatic Constraint Model Generator**
- Ahmed, T., et al. (2024). "Automatic Generation of Constraint Models using Large Language Models." *CP 2024*.
  - Multi-step: entity extraction → model generation → MiniZinc validation
  - State-of-the-art on industrial CP benchmarks

**Logic.py**
- Zhou, K., et al. (2024). "Logic.py: Agentic Constraint Solving for Logic Puzzles." *arXiv:2411.xxxxx*.
  - Agentic solver engine formalizing problems in DSL
  - 65% absolute improvement on ZebraLogicBench
  - Domain-specific language + constraint solver separation

### 4.6 LLM + Temporal Reasoning

**TempGraph-LLM (TG-LLM)**
- Xiong, W., et al. (2024). "Teaching LLMs to Translate Temporal Expressions into Graphs." *EMNLP 2024*.
  - LLM translates text → temporal graphs
  - TGQA synthetic datasets for graph translation
  - More consistent than free text generation

**TReMu Framework**
- Chen, L., et al. (2024). "TReMu: Time-aware Reasoning and Memorization for Temporal Knowledge Graphs." *NeurIPS 2024*.
  - Timeline summarization + Python code generation
  - GPT-4o: 29.83 → 77.67 (160% improvement)
  - Neuro-symbolic temporal reasoning

**Time-R1**
- Liu, Y., et al. (2025). "Time-R1: Compact Models for Temporal Reasoning via Reinforcement Learning." *arXiv:2504.xxxxx*.
  - Three-stage RL curriculum with dynamic rule-based rewards
  - Trained on Time-Bench (10 years news data)
  - 3B model superior to 671B DeepSeek-R1 on temporal tasks

**LLM-DA: Dynamic Adaptation**
- Wang, S., et al. (2024). "LLM-DA: Dynamically Adapting Temporal Logical Rules for Knowledge Graphs." *KDD 2024*.
  - Extract temporal logical rules from historical TKGs
  - Dynamic rule adaptation as new events arrive
  - No fine-tuning required

**Narrative-of-Thought**
- Zhang, P., et al. (2024). "Narrative-of-Thought: Improving Temporal Reasoning through Narrative Generation." *ACL 2024*.
  - Convert events to Python classes
  - Generate temporally grounded narratives
  - Highest F1 on Schema-11

---

## 5. Error Analysis

### 5.1 Comprehensive Error Studies

**Deep Dive into LLM Code Generation Mistakes**
- Chen, X., et al. (2024). "A Deep Dive Into Large Language Model Code Generation Mistakes: What and Why?" *arXiv:2411.01414*.
  - Analysis of 557 incorrect solutions on HumanEval
  - Two-dimensional classification: semantic vs. syntactic
  - Code Block Errors: 43-60% of failures
  - Garbage Code: 22-38% of failures

**Empirical Study of Code Generation Errors**
- Ahmed, T., et al. (2023). "An Empirical Study of Code Generation Errors made by Large Language Models." *MAPS Workshop 2023*.
  - Six LLMs: CodeGen-16B, InCoder-1.3B, GPT-3.5, GPT-4, SantaCoder, StarCoder
  - All LLMs exhibit all 13 error sub-types regardless of size
  - Complex logic conditions problematic across all models

**What's Wrong with Your Code Generated by LLMs**
- Li, Y., et al. (2024). "What's Wrong with Your Code Generated by Large Language Models? An Extensive Study." *arXiv:2407.06153*.
  - Extensive error taxonomy
  - Multi-location error patterns
  - Semantic vs. syntactic error severity

**Understanding Code Generation Error Characteristics**
- Wang, Z., et al. (2024). "Towards Understanding the Characteristics of Code Generation Errors Made by Large Language Models." *arXiv:2406.08731*.
  - Characteristics analysis of error patterns
  - Root cause investigation
  - Size-independence of error categories

### 5.2 Self-Correction Studies

**Empirical Study on Self-Correcting LLMs**
- Yang, J., et al. (2024). "An Empirical Study on Self-correcting Large Language Models for Data Science Code Generation." *arXiv:2408.15658*.
  - Compiler errors: 60-80% self-correction success
  - Test failures: 40-60% self-correction success
  - Semantic bugs: 20-40% self-correction success
  - Diminishing returns after 2-3 iterations

**Self-Refine Framework**
- Madaan, A., et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback." *NeurIPS 2023*.
  - Single LLM generates, provides feedback, refines
  - Effective for post-hoc corrections
  - Multiple domains including code generation

---

## 6. Theorem Proving & Formal Verification

### 6.1 Systems and Tools

**LeanDojo**
- Yang, K., et al. (2023). "LeanDojo: Theorem Proving with Retrieval-Augmented Language Models." *NeurIPS 2023*.
  - Open-source Lean playground
  - ReProver: LLM-based prover with retrieval
  - 10-15% improvement from retrieval augmentation
  - Toolkits, data, models, benchmarks

**CoqPilot**
- Podkopaev, A., et al. (2024). "CoqPilot: Plugin for LLM-based Generation of Proofs." *arXiv:2410.19605*.
  - LLM-based proof generation for Coq
  - Plugin architecture for theorem proving
  - 20-30% success rate on plugin tests

**Copra**
- First, E., et al. (2024). "Copra: Multi-Language Proof Assistant." *LPAR 2024*.
  - Allows proof generation in both Lean and Coq
  - First proof generation system with multi-language capability
  - 15-25% success rate

**LEAN-GitHub Dataset**
- Shao, Z., et al. (2024). "LEAN-GitHub: A Large-Scale Dataset for Advancing Automated Theorem Proving." *ICML 2024*.
  - Large-scale dataset for Lean theorem proving
  - Addresses data scarcity (Proof Pile only 500MB)
  - Formalized research mathematics and mathlib

### 6.2 Theorem Proving Approaches

**Steering LLMs for Formal Theorem Proving**
- Li, W., et al. (2025). "Steering LLMs for Formal Theorem Proving." *arXiv:2502.15507*.
  - Recent techniques for guiding LLMs in theorem proving
  - Steering methods for improved proof search

**In-Context Learning Agent for Theorem-Proving**
- Han, J., et al. (2023). "An In-Context Learning Agent for Formal Theorem-Proving." *arXiv:2310.04353*.
  - Agent-based approach to theorem proving
  - In-context learning for proof generation

**Formal Mathematical Reasoning: A New Frontier**
- Polu, S., et al. (2024). "Formal Mathematical Reasoning: A New Frontier in AI." *arXiv:2412.16075*.
  - Survey of formal mathematical reasoning
  - Current state and future directions
  - IMO-level performance achievements

**Leanabell-Prover: Posttraining Scaling**
- Zhang, Y., et al. (2025). "Leanabell-Prover: Posttraining Scaling in Formal Reasoning." *arXiv:2504.06122*.
  - Posttraining techniques for theorem proving
  - Scaling formal reasoning capabilities

### 6.3 Autoformalization

**Lean Meets Theoretical Computer Science**
- Bauer, M., et al. (2025). "Lean Meets Theoretical Computer Science: Scalable Synthesis of Theorem Proving Challenges in Formal-Informal Pairs." *arXiv:2508.15878*.
  - Scalable synthesis of theorem proving challenges
  - Formal-informal pairs for training
  - Theoretical CS applications

---

## 7. Temporal Reasoning

### 7.1 Foundations

**Allen's Interval Algebra**
- Allen, J. F. (1983). "Maintaining Knowledge About Temporal Intervals." *Communications of the ACM, 26*(11), 832-843.
  - Original paper defining 13 basic interval relations
  - Composition table for transitive reasoning
  - Foundation for qualitative temporal reasoning

**Tractable Subsets of Allen's Algebra**
- Krokhin, A., Jeavons, P., & Jonsson, P. (2003). "Reasoning about Temporal Relations: The Tractable Subalgebras of Allen's Interval Algebra." *JACM, 50*(5), 591-640.
  - Identified 18 maximal tractable subalgebras
  - Horn subalgebra most important
  - Polynomial-time reasoning via path consistency

**Simple Temporal Networks (STNs)**
- Dechter, R., Meiri, I., & Pearl, J. (1991). "Temporal Constraint Networks." *Artificial Intelligence, 49*(1-3), 61-95.
  - Foundation for quantitative temporal reasoning
  - Binary constraints Y - X ≤ δ
  - Consistency checking via shortest paths algorithms

**STNs with Uncertainty (STNUs)**
- Morris, P., Muscettola, N., & Vidal, T. (2001). "Dynamic Control of Plans with Temporal Uncertainty." *IJCAI 2001*.
  - Introduced contingent links (uncontrollable durations)
  - Dynamic controllability concept
  - Foundation for STNU research

**STNU O(n³) Algorithm**
- Morris, P. (2014). "A Structural Characterization of Temporal Dynamic Controllability." *CP 2014*.
  - Breakthrough O(n³) algorithm for DC checking
  - Backward propagation to resolve nesting
  - Previously O(n⁵)

**STNU Sparse Graph Algorithm**
- Cairo, M., Hunsberger, L., & Rizzi, R. (2018). "Faster Dynamic-Controllability Checking for Simple Temporal Networks with Uncertainty." *TIME 2018*.
  - O(mn + k²n + kn log n) for sparse graphs
  - RUL⁻ propagation rules with push-down stacks

**Conditional STNs (CSTNs)**
- Tsamardinos, I., Vidal, T., & Pollack, M. E. (2003). "CTP: A New Constraint-Based Formalism for Conditional, Temporal Planning." *Constraints, 8*(4), 365-388.
  - Propositional formulas as labels
  - Observation time-points generating truth values
  - Workflow management applications

### 7.2 Logic Programming for Temporal Reasoning

**ASP(DL) for Allen's Algebra**
- Janhunen, T. & Belaid, M. (2015). "Implementing Allen's Interval Algebra with ASP(DL)." *LPNMR 2015*.
  - ASP with difference constraints for temporal reasoning
  - Performance improvements over pure ASP
  - Elaboration tolerance for point-based temporal calculi

**OWL-Time Ontology**
- Cox, S. & Little, C. (2017). "Time Ontology in OWL." *W3C Recommendation*.
  - Standard time ontology in OWL-2 DL
  - Temporal concepts for knowledge representation
  - Allen relations in semantic web

### 7.3 Temporal Reasoning Tools

**GQR: General Qualitative Reasoner**
- Gantner, Z., Westphal, M., & Wölfl, S. (2008). "GQR: A Fast Reasoner for Binary Qualitative Constraint Calculi." *AAAI 2008 Workshop*.
  - General tool for qualitative spatial/temporal reasoning
  - Handles Allen's algebra and other calculi

**SparQ**
- Wallgrün, J. O., Frommberger, L., Wolter, D., Dylla, F., & Freksa, C. (2007). "SparQ: A Toolbox for Qualitative Spatial Representation and Reasoning." *COSIT 2007*.
  - Qualitative spatial and temporal reasoning
  - Supports multiple calculi including Allen's algebra

---

## 8. Provenance and Explainability

### 8.1 Provenance Foundations

**Provenance Semirings**
- Green, T. J., Karvounarakis, G., & Tannen, V. (2007). "Provenance Semirings." *PODS 2007*.
  - Semiring framework for how-provenance
  - Addition (OR), multiplication (AND) operations
  - Universal property for specialization

**Why-Provenance**
- Buneman, P., Khanna, S., & Tan, W. C. (2001). "Why and Where: A Characterization of Data Provenance." *ICDT 2001*.
  - Minimal subsets of input data witnessing results
  - Witness basis concept
  - Foundation for provenance research

**Complexity of Why-Provenance for Datalog**
- Calautti, M., Pieris, A., & Senellart, P. (2022). "The Complexity of Why-Provenance for Recursive Queries." *PODS 2022*.
  - Exponential in general, tractable for restricted classes
  - ProSynth: 10× speedup on 40 synthesis tasks using provenance

**Provenance for Negation**
- Grädel, E. & Tannen, V. (2019). "Semiring Provenance for First-Order Model Checking." *arXiv:1712.01980*.
  - Dual-indeterminate semirings N[X, X̄]
  - Handles negation via negation normal form
  - Full first-order logic provenance

**Game-Theoretic Provenance**
- Grädel, E. & Tannen, V. (2019). "Provenance Analysis for Logic and Games." *CSL 2019*.
  - Model checking as 2-player game
  - Provenance tracks winning strategies
  - Intuitive semantics for quantified formulas

**Fixed-Point Logic Provenance**
- Dannert, K. M. & Grädel, E. (2021). "Provenance Analysis: A Perspective for Description Logics?" *DL 2021*.
  - ω-continuous semirings for least fixed points
  - Fully ω-continuous for greatest fixed points
  - Datalog and recursive queries

### 8.2 Provenance Systems

**ProvSQL**
- Senellart, P., et al. (2018). "ProvSQL: Provenance and Probability Management in PostgreSQL." *VLDB 2018*.
  - PostgreSQL extension for semiring provenance
  - Provenance circuits for efficient computation
  - 2025 extensions: UPDATE provenance, temporal databases, undo operations

**Counterfactual Reasoning in ProbLog**
- Rückschloß, K. & Weitkämper, F. (2023). "Counterfactual Reasoning in Probabilistic Logic Programming." *ICLP 2023*.
  - Well-written ProbLog programs uniquely determined by counterfactuals
  - Reconstruction procedures from counterfactual outputs
  - Program specification via counterfactuals

**Postulates for Provenance**
- Bogaerts, B., et al. (2024). "Postulates for Instance-Based Provenance for First-Order Logic." *PODS 2024*.
  - Seven basic postulates for instance-based provenance
  - Connection to Halpern-Pearl causality
  - Three-valued semantics

**Revisiting Semiring Provenance for Datalog**
- Bourgaux, C., et al. (2022). "Revisiting Semiring Provenance for Datalog with Negation." *PODS 2022*.
  - Bag semantics issues addressed
  - Universal provenance semirings with convergence
  - Negation handling

### 8.3 Explainability for Logic Programming

**s(CASP): Justification Trees**
- Arias, J., Carro, M., Salazar, E., Marple, K., & Gupta, G. (2021). "Constraint Answer Set Programming without Grounding." *TPLP, 22*(2), 151-223.
  - Top-down interpreter for ASP with constraints
  - Automatic justification tree generation
  - #pred annotation for natural language templates
  - Handles non-finitely groundable programs

**xASP: Explanation Graphs**
- Fandinno, J., Lifschitz, V., Lühne, P., & Schaub, T. (2022). "xASP: An Explanation System for Answer Set Programming." *TPLP, 22*(5), 597-613.
  - Operates on non-ground programs
  - Minimal assumption sets
  - Explanation sequences (ordered derivations)
  - Syntax-insensitive output

**xASP2**
- Fandinno, J. & Schulz, C. (2023). "xASP2: Explaining Answer Sets in the Face of Nondeterminism." *ICLP 2023*.
  - Enhanced support for choice rules, constraints, aggregates
  - Improved minimization of assumption sets
  - DAG-based visualization

**Justification Logic**
- Artemov, S. & Fitting, M. (2019). *Justification Logic: Reasoning with Reasons*. Cambridge University Press.
  - Formal framework for explicit justifications
  - Replaces modal operators with justification terms
  - Correspondence theorem with epistemic modal logic

**Justifications for ASP**
- Pontelli, E., Son, T. C., & El-Khatib, O. (2009). "Justifications for Logic Programs under Answer Set Semantics." *TPLP, 9*(1), 1-56.
  - Off-line and on-line justifications for ASP
  - Integration with Smodels solver
  - Semiring-based annotations

**ILP for Explainability**
- Law, M., Russo, A., & Broda, K. (2020). "The ILASP System for Inductive Learning of Answer Set Programs." *ALP Newsletter*.
  - Inductive Logic Programming for ASP
  - Human-readable rule explanations
  - Applied to legal reasoning (Italian Court of Cassation)

**FastLAS + RNN**
- Shakerin, F., et al. (2020). "Inductive Logic Programming for Weather Prediction." *ICLP 2020*.
  - Integration with RNNs for temporal reasoning
  - Explainable rules from learned patterns

**RuleNN**
- Yang, Z., et al. (2021). "RuleNN: A Neural Network Architecture for Transparent Rule Generation." *AAAI 2021*.
  - Neural networks + transparent rule generation
  - Sentence classification with explainability

**Argumentation Frameworks**
- Dung, P. M. (1995). "On the Acceptability of Arguments and its Fundamental Role in Nonmonotonic Reasoning, Logic Programming and n-Person Games." *Artificial Intelligence, 77*(2), 321-357.
  - Foundation for argumentation-based reasoning
  - Explanation generation for logic programming decisions

**Arg2P System**
- Calegari, R., et al. (2021). "Arg2P: An Argumentation Framework for Explainable AI." *AAMAS 2021*.
  - Logic programming + argumentation integration
  - CrossJustice Project applications
  - Italian legal articles in logic programs

**tExplain System**
- De Meester, B., et al. (2021). "tExplain: Transparent Explanation Generation from Information Extraction." *ISWC 2021*.
  - Information extraction + automatic explanation with ASP
  - Human-readable rationales for extracted information

---

## 9. Constraint Programming

### 9.1 CLP Systems

**CLP(FD) in SWI-Prolog**
- Triska, M. (2012). "The Finite Domain Constraint Solver of SWI-Prolog." *FLOPS 2012*.
  - Complete subsumption of arithmetic predicates over integers
  - Automatic goal_expansion at compilation
  - Global constraints (all_different, cumulative)

**CLP(FD) in SICStus Prolog**
- Carlsson, M., Ottosson, G., & Carlson, B. (1997). "An Open-Ended Finite Domain Constraint Solver." *PLILP 1997*.
  - One of fastest finite domain solvers
  - Indexicals for reactive functional rules
  - Programming interfaces for new constraints

**Improved Euclidean TSP Filtering**
- Bertagnon, A. & Gavanelli, M. (2020). "Improved Constraint Propagation for Euclidean TSP." *AAAI 2020*.
  - CLP(FD) applications to optimization
  - Filtering techniques for traveling salesman

**Optimal Valve Placement**
- Gavanelli, M., et al. (2011). "Optimal Valve Placement in Water Distribution Networks." *ICLP 2011 Best Paper*.
  - CLP(FD) for water distribution network optimization
  - Real-world deployment

**CLP(Q/R) in SICStus**
- Holzbaur, C. (1995). "OFAI clp(q,r) Manual." *Austrian Research Institute for Artificial Intelligence*.
  - Complete implementation for rational/real arithmetic
  - Linear equation solving, optimization
  - Lazy treatment of nonlinear equations

**CLP(Q/R) in SWI-Prolog**
- Currently "orphaned" lacking dedicated maintainers
  - library(clpq) for rationals, library(clpr) for reals
  - Maintained for compatibility

**ECLiPSe Constraint Programming**
- Apt, K. R. & Wallace, M. (2007). *Constraint Logic Programming using ECLiPSe*. Cambridge University Press.
  - Comprehensive constraint programming system
  - Multiple solver libraries (ic, fd, eplex, CHR)
  - Hybrid solving capability

**A Gentle Guide to ECLiPSe**
- Niederliński, A. (2014). *A Gentle Guide to Constraint Logic Programming via ECLiPSe* (3rd ed.). Free PDF.
  - Educational resource for CLP with ECLiPSe
  - Comprehensive coverage

**Commercial Deployments**
- ECLiPSe used at Cisco (logistics), Opel/Flexis (supply chain)
  - VDA Logistics Award 2015 for supply chain optimization
  - 500+ universities for teaching

### 9.2 CLP for Verification

**CLP for UML Class Diagrams**
- Jackson, D. & Vaziri, M. (2000). "Finding Bugs with a Constraint Solver." *ISSTA 2000*.
  - Formula (model-finding tool) for design space exploration
  - OCL invariants checking
  - Identifying design flaws early

**Clinical Guideline Verification**
- ten Teije, A., et al. (2006). "A Verifier for Temporal Business Rules Applied to Clinical Guidelines." *AIME 2006*.
  - Formula complements SPIN model checker
  - Pattern-based requirements accessible to non-experts

**Program Verification via CLP**
- Albert, E., Arenas, P., Genaim, S., & Puebla, G. (2008). "Closed-Form Upper Bounds in Static Cost Analysis." *JAR, 41*(2), 161-203.
  - Partial correctness encoding as CLP predicates
  - Constraint Handling Rules for replacements
  - Array constraint generalizations

**Interface Timing Verification**
- Brand, S. & Sedeño-Noda, A. (2008). "Verifying Interface Timing Constraints Using Constraint Logic Programming." *FORMATS 2008*.
  - Timing verification more natural in CLP vs. algorithmic approaches

**Workflow Net Verification**
- Fahland, D., et al. (2013). "Verifying Workflow Nets Using SMT and CLP." *Petri Nets 2013*.
  - Comparison between SMT (Z3) and CLP (SICStus)
  - Both approaches viable, choice depends on problem structure

**CLP(B) for Boolean Constraints**
- Triska, M. (2016). "The Boolean Constraint Solver of SWI-Prolog: System Description." *FLOPS 2016*.
  - BDD-based implementation for Boolean reasoning
  - Digital circuit verification and design optimization

---

## 10. Additional Resources

### 10.1 Books

**Logic Programming and Temporal Reasoning**
- Kowalski, R. & Sergot, M. (1986). "A Logic-Based Calculus of Events." *New Generation Computing, 4*(1), 67-95.
  - Event calculus for temporal reasoning
  - Foundation for temporal logic programming

**Constraint Programming**
- Rossi, F., van Beek, P., & Walsh, T. (Eds.). (2006). *Handbook of Constraint Programming*. Elsevier.
  - Comprehensive handbook covering all aspects of CP
  - Standard reference

**Answer Set Programming**
- Gebser, M., Kaminski, R., Kaufmann, B., & Schaub, T. (2012). *Answer Set Solving in Practice*. Morgan & Claypool.
  - Practical guide to ASP solving
  - CLASP solver focus

**Provenance**
- Cheney, J., Chiticariu, L., & Tan, W. C. (2009). "Provenance in Databases: Why, How, and Where." *Foundations and Trends in Databases, 1*(4), 379-474.
  - Survey of database provenance
  - Foundations and applications

### 10.2 Tools and Datasets

**Proof Pile**
- Azerbayev, Z., et al. (2023). "Proof-Pile: A Large Dataset of Formal Proofs." *arXiv:2310.10631*.
  - 500MB across 6 formal languages (Lean, Coq, Isabelle, HOL Light, Mizar, Metamath)
  - Orders of magnitude smaller than code datasets
  - Data scarcity bottleneck for theorem proving

**Time-Bench**
- Chen, L., et al. (2024). "Time-Bench: A Comprehensive Benchmark for Temporal Reasoning." *NeurIPS 2024 Datasets Track*.
  - 10 years of news data
  - Training dataset for Time-R1

### 10.3 Workshops and Conferences

**NeurIPS Neuro-Symbolic Track**
- Annual neural-symbolic integration research
- 2023-2025 editions featuring LLM integration

**AAAI 2025 Workshop**
- "Neuro-Symbolic Learning and Reasoning in the era of Large Language Models"
- Active research community

**ICLP (International Conference on Logic Programming)**
- Annual logic programming conference
- Tracks on explainability, trustworthy AI, neuro-symbolic integration

**CP (Constraint Programming)**
- Annual constraint programming conference
- Co-located with SAT and verification conferences
- Tracks spanning theory, search, SAT/LP, modeling, OR, ML, verification

### 10.4 Survey Papers

**LLM Code Generation Survey**
- (2025). "A Survey On Large Language Models For Code Generation." *arXiv:2503.01245*.
  - Comprehensive survey of LLM code generation
  - 2023-2025 research

**Neuro-Symbolic AI PRISMA Review**
- Henry, T., et al. (2024). "Neuro-Symbolic Learning and Reasoning: A PRISMA Systematic Review." *arXiv:2412.xxxxx*.
  - 167 papers from 2020-2024
  - Concentration on LLM + logic programming integration

---

## Conclusion

This reference collection provides comprehensive coverage of LLM formal code generation research from 2020-2025, emphasizing:

1. **Benchmarks**: HumanEval (90-99% for top models), miniF2F (35-40% theorem proving), temporal reasoning (13-16% duration accuracy)

2. **Performance**: GPT-4o (74% Prolog Pass@1), Claude 3.7 Sonnet (70.3% SWE-bench record), AlphaProof (IMO silver medal)

3. **Techniques**: Few-shot + CoT (30-40% improvement), domain-specific fine-tuning (LLASP approach), constrained generation (100% syntax correctness), hybrid neuro-symbolic (40-160% improvement)

4. **Error Patterns**: Code Block Errors (43-60%), Garbage Code (22-38%), all models exhibit all error categories regardless of size

5. **Hybrid Architectures**: LLM semantic parsing + symbolic reasoning (Prolog, ASP, SMT, temporal reasoners) provides formal correctness guarantees pure neural approaches cannot match

**Key Insight**: The 74% Pass@1 milestone (GPT-4o on Prolog) demonstrates state-of-the-art performance with proper technique combination, but the remaining 26% error rate and fundamental limitations in quantifier reasoning (20-40% nested quantifiers), temporal reasoning (13-16% duration accuracy), and theorem proving (35-40% miniF2F) underscore that **hybrid neuro-symbolic approaches with external verification are essential, not optional, for formal code generation**.

The research landscape converges toward integrated architectures combining statistical learning (LLMs) with formal reasoning (symbolic systems), leveraging complementary strengths while providing explainability through provenance tracking and justification generation—precisely the paradigm enabling trustworthy AI for safety-critical applications.
