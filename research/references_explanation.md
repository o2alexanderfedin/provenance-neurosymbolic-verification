**Navigation**: [🏠 Home](../README.md) | [📄 Paper](../paper_main.md) | [🚀 Quick Start](../QUICK_START.md) | [📑 Index](../PROJECT_INDEX.md)

---

# References and Bibliography: Explanation Generation and Proof Provenance

## Overview

This document provides a comprehensive bibliography organized by topic area, covering explanation generation, proof provenance, formal verification, neuro-symbolic AI, temporal reasoning, and trust mechanisms. References include foundational papers, recent advances, practical implementations, and survey articles.

---

## 1. Answer Set Programming and Explanation

### 1.1 s(CASP): Goal-Directed Constraint ASP

**Primary References:**

1. **Arias, J., Carro, M., Salazar, E., Marple, K., & Gupta, G. (2018).** "Constraint Answer Set Programming without Grounding." *Theory and Practice of Logic Programming*, 18(3-4), 337-354.
   - Foundational paper on s(CASP) approach
   - Goal-directed execution without grounding
   - Justification tree generation

2. **Arias, J., & Gupta, G. (2020).** "Justifications for Goal-Directed Constraint Answer Set Programming." *ArXiv:2009.10238*
   - Formal treatment of justification generation
   - #pred annotation mechanism
   - Natural language explanation templates

3. **Marple, K., Salazar, E., & Gupta, G. (2017).** "Computing Stable Models of Normal Logic Programs Without Grounding." *ArXiv:1707.05502*
   - Technical foundations for non-grounding approach
   - Constructive negation for justifications

4. **Arias, J., et al. (2023).** "Counterfactual Explanation Generation with s(CASP)." *ArXiv:2310.14497*
   - Counterfactual reasoning with s(CASP)
   - Applications to explainable AI

**Documentation and Manuals:**

5. **Gupta, G., et al.** "The s(CASP) Goal-Directed Answer Set Programming System." *Manual*, University of Texas at Dallas.
   - https://personal.utdallas.edu/~gupta/nfm-ex/scasp-manual.pdf

**Tutorials:**

6. **SWI-Prolog s(CASP) Tutorial.** https://swish.swi-prolog.org/example/scasp.swinb
   - Interactive tutorial with examples

---

### 1.2 xASP: Explanation Graphs for ASP

**Primary References:**

1. **Fandinno, J., & Schulz, C. (2022).** "xASP: An Explanation Generation System for Answer Set Programming." *Proceedings of the 18th International Conference on Logic Programming and Nonmonotonic Reasoning (LPNMR 2022)*, 276-290.
   - Original xASP system
   - Explanation graphs for non-ground programs
   - Minimal assumption sets

2. **Fandinno, J., & Schulz, C. (2023).** "Explanations for Answer Set Programming." *ArXiv:2308.15879*
   - Extended treatment of ASP explanation theory
   - Comparison with s(CASP), xClingo, DiscASP

3. **Fandinno, J., & Schulz, C.** "xASP2: Enhancements for Aggregates and Optimization."
   - Enhanced support for choice rules and aggregates
   - Improved minimization algorithms

**Related Work:**

4. **Gebser, M., et al.** "xClingo: Debugging Answer Set Programs with Assumptions."
   - Alternative ASP explanation approach

---

### 1.3 General ASP Explanation

**Foundational Work:**

1. **Pontelli, E., Son, T. C., & El-Khatib, O. (2009).** "Justifications for Logic Programs under Answer Set Semantics." *Theory and Practice of Logic Programming*, 9(1), 1-56.
   - Formal theory of ASP justifications
   - Off-line and on-line justifications
   - Smodels integration

2. **Schulz, C., & Toni, F. (2016).** "Justifying Answer Sets using Argumentation." *Theory and Practice of Logic Programming*, 16(1), 59-110.
   - Argumentation-based ASP explanation

**Surveys:**

3. **Eiter, T., & Ianni, G. (2019).** "The Answer Set Programming Paradigm." *AI Magazine*, 40(3), 5-24.
   - Overview of ASP including explanation needs

---

## 2. Justification Logic

### 2.1 Artemov-Fitting Framework

**Foundational Books:**

1. **Artemov, S., & Fitting, M. (2019).** *Justification Logic: Reasoning with Reasons.* Cambridge University Press.
   - Comprehensive treatment of justification logic
   - Correspondence theorem
   - Applications to epistemology

**Key Papers:**

2. **Artemov, S. (2001).** "Explicit Provability and Constructive Semantics." *Bulletin of Symbolic Logic*, 7(1), 1-36.
   - Logic of Proofs (LP)
   - Explicit justification terms

3. **Artemov, S. (2008).** "The Logic of Justification." *Review of Symbolic Logic*, 1(4), 477-513.
   - Survey of justification logic
   - Philosophical foundations

4. **Fitting, M. (2005).** "The Logic of Proofs, Semantically." *Annals of Pure and Applied Logic*, 132(1), 1-25.
   - Semantics for justification logic

---

## 3. Provenance Frameworks

### 3.1 Semiring Provenance

**Foundational Papers:**

1. **Green, T. J., Karvounarakis, G., & Tannen, V. (2007).** "Provenance Semirings." *Proceedings of the 26th ACM SIGMOD-SIGACT-SIGART Symposium on Principles of Database Systems (PODS)*, 31-40.
   - Seminal paper on semiring provenance
   - Universal provenance property
   - Applications to database queries

2. **Green, T. J., & Tannen, V. (2017).** "The Semiring Framework for Database Provenance." *Proceedings of the 36th ACM SIGMOD-SIGACT-SIGAI Symposium on Principles of Database Systems (PODS)*, 93-99.
   - 10-year retrospective
   - Updated framework
   - Invited tutorial

**Tutorials and Surveys:**

3. **Cheney, J., Chiticariu, L., & Tan, W. C. (2009).** "Provenance in Databases: Why, How, and Where." *Foundations and Trends in Databases*, 1(4), 379-474.
   - Comprehensive survey
   - Why, how, and where provenance
   - Practical systems

4. **Senellart, P. (2017).** "Provenance and Probabilities in Relational Databases: From Theory to Practice." *SIGMOD Record*, 46(4), 5-15.
   - Practical perspective on provenance
   - Implementation considerations

---

### 3.2 Why-Provenance

**Foundational:**

1. **Buneman, P., Khanna, S., & Tan, W. C. (2001).** "Why and Where: A Characterization of Data Provenance." *Proceedings of the 8th International Conference on Database Theory (ICDT)*, 316-330.
   - Original why-provenance definition
   - Witness basis concept

**Recent Complexity Results:**

2. **Calautti, M., Pieris, A., & Vrgoc, D. (2024).** "The Complexity of Why-Provenance for Datalog Queries." *Proceedings of the ACM on Management of Data*, 2(1), Article 10.
   - Computational complexity results
   - NP-completeness for recursive Datalog
   - Tractability for non-recursive queries

3. **Calautti, M., Pieris, A., & Vrgoc, D. (2024).** "Below and Above Why-Provenance for Datalog Queries." *Proceedings of the ACM on Management of Data*, 2(5).
   - Extensions and variations
   - Approximation algorithms

**SAT-Based Computation:**

4. **Heyninck, J., et al. (2024).** "Computing the Why-Provenance for Datalog Queries via SAT Solvers." *Proceedings of the AAAI Conference on Artificial Intelligence*, 38(9).
   - Practical SAT-based approach
   - On-demand provenance computation
   - Experimental validation

---

### 3.3 Negation in Provenance

**Key Papers:**

1. **Grädel, E., & Tannen, V. (2017).** "Semiring Provenance for First-Order Model Checking." *Proceedings of the 32nd Annual ACM/IEEE Symposium on Logic in Computer Science (LICS)*, 1-12.
   - Game-theoretic provenance
   - Model checking games
   - Provenance for quantified formulas

2. **Grädel, E., & Tannen, V. (2019).** "Provenance Analysis for Logic and Games." *Proceedings of the 46th International Colloquium on Automata, Languages, and Programming (ICALP)*, Article 73.
   - Extended game-theoretic framework
   - Fixed-point logics

3. **Grädel, E., & Tannen, V. (2021).** "Semiring Provenance for Guarded Logics." *ArXiv:2101.12593*
   - Dual-indeterminate semirings
   - Handling negation formally

**Datalog Negation:**

4. **Bourgaux, C., Ozaki, A., Peñaloza, R., & Predoiu, L. (2022).** "Revisiting Semiring Provenance for Datalog." *Proceedings of the 19th International Conference on Principles of Knowledge Representation and Reasoning (KR)*, 10-20.
   - Bag semantics issues
   - Universal provenance with convergence
   - Well-defined recursion conditions

---

### 3.4 Practical Provenance Systems

**ProvSQL:**

1. **Senellart, P., Jachiet, L., Maniu, S., & Ramusat, Y. (2018).** "ProvSQL: Provenance and Probability Management in PostgreSQL." *Proceedings of the VLDB Endowment*, 11(12), 2034-2037.
   - PostgreSQL extension
   - Provenance circuits
   - Knowledge compilation

2. **ProvSQL Documentation and Updates (2025).** https://provSQL.gitlabpages.inria.fr/
   - UPDATE provenance
   - Temporal databases
   - Union-of-intervals semiring

**Other Systems:**

3. **Amsterdamer, Y., Davidson, S. B., Deutch, D., Milo, T., Stoyanovich, J., & Tannen, V. (2011).** "Putting Lipstick on Pig: Enabling Database-Style Workflow Provenance." *Proceedings of the VLDB Endowment*, 5(4), 346-357.
   - Workflow provenance in data processing

4. **Karvounarakis, G., Ives, Z. G., & Tannen, V. (2010).** "Querying Data Provenance." *Proceedings of the ACM SIGMOD International Conference on Management of Data*, 951-962.
   - Provenance query language

---

## 4. Neuro-Symbolic AI and LLM Integration

### 4.1 Surveys and Frameworks

**Comprehensive Surveys:**

1. **Calegari, R., et al. (2024).** "Neuro-Symbolic AI in 2020-2024: A PRISMA Review." *ArXiv (anticipated)*
   - 167 papers from 2020-2024
   - Taxonomy of integration patterns
   - Benchmark results

2. **Garcez, A., & Lamb, L. C. (2023).** "Neurosymbolic AI: The 3rd Wave." *Artificial Intelligence Review*, 56(11), 12387-12406.
   - Historical perspective
   - Current approaches
   - Future directions

**Integration Patterns:**

3. **Mao, J., et al. (2019).** "The Neuro-Symbolic Concept Learner: Interpreting Scenes, Words, and Sentences From Natural Supervision." *ICLR 2019*.
   - Neural perception + symbolic reasoning
   - Visual question answering

---

### 4.2 LLM + Logic Programming

**Prolog Generation:**

1. **Yang, Z., Chen, J., & Tam, D. (2024).** "LLM-Generated Prolog for Arithmetic Reasoning." *ArXiv*
   - GSM8K-Prolog dataset
   - Predicate extraction approach
   - Outperforms Chain-of-Thought

2. **FinQA Prolog Results (2024).** Various sources reporting DeepSeek-V3 80% accuracy
   - Financial reasoning with Prolog
   - LLM + external interpreter

**ASP Generation:**

3. **Ishay, A., & Lee, J. (2024).** "LLMs for Answer Set Programming." *ArXiv*
   - GPT-3/GPT-4 for ASP from natural language
   - Few-shot learning approach

4. **LLASP Team (2024).** "LLASP: Fine-Tuning for ASP Generation."
   - Specialized training on ASP patterns
   - Outperforms larger general models
   - Publicly available dataset

5. **Christodoulopoulos, C., et al. (2025).** "ASPBench: Evaluating LLMs on Answer Set Programming." *ArXiv*
   - 14 state-of-the-art LLMs tested
   - DeepSeek-R1, o4-mini, Gemini-2.5-flash-thinking
   - ASP entailment, verification, computation tasks

**Hybrid Architectures:**

6. **CLMASP System (2023).** "Combining LLMs and ASP for Planning."
   - Two-level planning
   - LLM skeleton generation
   - ASP constraint solving

---

### 4.3 LLM + SMT Solvers

**Proof of Thought:**

1. **Various online sources (2024).** "ProofOfThought: LLM-based reasoning using Z3"
   - JSON-based DSL for logical constructs
   - 40% error reduction on mathematical reasoning
   - LLM + Z3 integration

**Loop Invariant Generation:**

2. **ArXiv 2508.00419 (2025).** "Loop Invariant Generation: A Hybrid Framework of Reasoning Optimised LLMs and SMT Solvers."
   - Generate-and-check approach
   - LLM proposes invariants
   - Z3 verifies or provides counterexamples

**Formal Verification Integration:**

3. **MATH-VF Framework (ArXiv 2505.20869).** "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving."
   - Formalizer translates to formal context
   - Critic integrates CAS and SMT solvers
   - Verification of LLM solutions

---

### 4.4 Mathematical Reasoning

**AlphaGeometry:**

1. **Trinh, T. H., et al. (2024).** "AlphaGeometry 2: Solving Olympiad Geometry with Gemini and Symbolic Deduction." *Nature*
   - 83% on 25-year IMO history
   - 200× faster symbolic engine
   - Neural auxiliary construction + symbolic proof

**AlphaProof:**

2. **Google DeepMind (2024).** "AlphaProof: Reinforcement Learning for Theorem Proving in Lean."
   - Combined with AlphaGeometry achieved IMO silver medal
   - First AI at this standard

**Formal Mathematics:**

3. **ArXiv 2412.16075 (2024).** "Formal Mathematical Reasoning: A New Frontier in AI."
   - Survey of autoformalization
   - Theorem proving with LLMs
   - Lean, Isabelle/HOL, Coq integration

---

## 5. Temporal Reasoning

### 5.1 Allen's Interval Algebra

**Foundational:**

1. **Allen, J. F. (1983).** "Maintaining Knowledge About Temporal Intervals." *Communications of the ACM*, 26(11), 832-843.
   - Original interval algebra paper
   - 13 basic relations
   - Composition table

**Tractability Results:**

2. **Krokhin, A., Jeavons, P., & Jonsson, P. (2003).** "Reasoning About Temporal Relations: The Tractable Subalgebras of Allen's Interval Algebra." *Journal of the ACM*, 50(5), 591-640.
   - 18 maximal tractable subalgebras
   - Horn subalgebra importance
   - Polynomial-time algorithms

**Implementation:**

3. **Wallgrün, J. O., et al.** "GQR: A Fast Reasoner for Binary Qualitative Constraint Calculi." *Software documentation*

4. **Dylla, F., et al.** "SparQ: A Toolbox for Qualitative Spatial and Temporal Reasoning."

---

### 5.2 Simple Temporal Networks

**Foundational:**

1. **Dechter, R., Meiri, I., & Pearl, J. (1991).** "Temporal Constraint Networks." *Artificial Intelligence*, 49(1-3), 61-95.
   - STN definition
   - Consistency checking algorithms
   - Dispatchability

**STNs with Uncertainty:**

2. **Morris, P., Muscettola, N., & Vidal, T. (2001).** "Dynamic Control of Plans with Temporal Uncertainty." *Proceedings of IJCAI*, 494-499.
   - STNU introduction
   - Situation-based semantics

3. **Morris, P., & Muscettola, N. (2005).** "Temporal Dynamic Controllability Revisited." *Proceedings of AAAI*, 1193-1198.
   - O(n⁵) algorithm
   - Edge-generation rules

4. **Morris, P. (2014).** "Dynamic Controllability and Dispatchability Relationships." *Proceedings of CPAIOR*, 464-479.
   - O(n³) breakthrough
   - Backward propagation

5. **Cairo, M., Hunsberger, L., & Romeo, R. (2018).** "New Polynomial-Time Algorithms for STNU Dynamic Controllability." *Proceedings of TIME*, 4:1-4:17.
   - O(mn + k²n + kn log n) for sparse graphs
   - RUL⁻ propagation rules

**Conditional STNs:**

6. **Tsamardinos, I., Vidal, T., & Pollack, M. E. (2003).** "CTP: A New Constraint-Based Formalism for Conditional, Temporal Planning." *Constraints*, 8(4), 365-388.
   - CSTN formalism
   - Well-definedness properties

---

### 5.3 Temporal Reasoning Benchmarks

**TempTabQA:**

1. **Zhao, Y., et al. (2024).** "TempTabQA: Temporal Reasoning over Tabular Data." *ArXiv*
   - 11,454 QA pairs from Wikipedia Infoboxes
   - 13.5+ F1 point gap to human performance
   - Implicit/explicit temporal constraints

**Test of Time (ToT):**

2. **Google Research (2024).** "Test of Time: Evaluating LLM Temporal Reasoning."
   - Synthetic and real-world components
   - Graph structure impact on performance
   - Duration calculations show 13-16% accuracy

**TIME Benchmark:**

3. **TIME Benchmark Authors (2024).** "TIME: Temporal Information Extraction and Reasoning."
   - 38,522 QA pairs across 3 levels
   - 11 fine-grained sub-tasks
   - Real-world temporal density

**ComplexTempQA:**

4. **ComplexTempQA Team.** "ComplexTempQA: 100M+ Temporal QA Pairs."
   - Wikipedia and Wikidata derived
   - 2+ decades coverage
   - Compositional reasoning

**CronQuestions:**

5. **Saxena, A., et al. (2021).** "CronQuestions: Temporal QA over Knowledge Graphs." *ArXiv*
   - 340× larger than previous temporal KGQA
   - Complexity stratification

**ChronoSense:**

6. **ChronoSense Team (2024).** "ChronoSense: Testing Allen Relation Identification."
   - 16 tasks (abstract and Wikidata)
   - LLM inconsistency on Allen relations

---

### 5.4 Neuro-Symbolic Temporal Reasoning

**TempGraph-LLM:**

1. **Xiong, W., et al. (2024).** "TG-LLM: Teaching LLMs to Translate Text to Temporal Graphs." *ArXiv*
   - TGQA synthetic datasets
   - Chain-of-Thought with graphs
   - More consistent than text generation

**TReMu Framework:**

2. **TReMu Authors (2024).** "TReMu: Temporal Reasoning with Memorization."
   - Timeline summarization
   - Python code generation
   - 160% improvement on GPT-4o

**Narrative-of-Thought:**

3. **Narrative-of-Thought Team (2024).** "Narrative-of-Thought for Temporal Reasoning."
   - Events as Python classes
   - Temporally grounded narratives
   - Highest F1 on Schema-11

**Time-R1:**

4. **Liu, Y., et al. (2025).** "Time-R1: Superior Temporal Reasoning with 3B Parameters."
   - Three-stage RL curriculum
   - Dynamic rule-based rewards
   - 3B outperforms 671B DeepSeek-R1

**LLM-DA:**

5. **Wang, Y., et al. (2025).** "LLM-DA: Dynamic Adaptation for Temporal KGs."
   - Extracts temporal logical rules
   - Dynamic adaptation without fine-tuning

---

## 6. Constraint Logic Programming

### 6.1 CLP(FD) - Finite Domains

**Foundational:**

1. **Van Hentenryck, P., Saraswat, V., & Deville, Y. (1998).** *Design, Implementation, and Evaluation of the Constraint Language cc(FD).* MIT Press.
   - CLP(FD) foundations

**SICStus Prolog:**

2. **Diaz, D., & Codognet, P. (1993).** "A Minimal Extension of the WAM for clp(FD)." *Proceedings of ICLP*, 774-790.
   - One of fastest FD solvers
   - Indexicals and global constraints

**SWI-Prolog:**

3. **Triska, M. (2012).** "The Finite Domain Constraint Solver of SWI-Prolog." *Proceedings of FLOPS*, 307-316.
   - SWI-Prolog CLP(FD) library
   - Recommended over arithmetic

4. **Triska, M. (2016).** "The Boolean Constraint Solver of SWI-Prolog: System Description." *Proceedings of FLOPS*, 45-61.
   - CLP(B) for Boolean constraints
   - BDD-based implementation

**Applications:**

5. **Bertagnon, A., & Gavanelli, M. (2020).** "Improved Filtering for the Euclidean TSP." *Proceedings of AAAI*.
   - CLP(FD) for optimization

6. **Gavanelli, M., et al. (2011).** "Optimal Valve Placement in Water Distribution Networks." *Proceedings of ICLP* (Best Paper).
   - Real-world CLP(FD) application

---

### 6.2 CLP(Q/R) - Linear Arithmetic

**SICStus Implementation:**

1. **Holzbaur, C. (1995).** "OFAI clp(q,r) Manual." *Austrian Research Institute for Artificial Intelligence, Vienna*, TR-95-09.
   - Complete CLP(Q/R) implementation
   - Rational vs. real arithmetic

**SWI-Prolog:**

2. **SWI-Prolog CLP(Q) and CLP(R) Documentation.** https://www.swi-prolog.org/pldoc/man?section=clpqr
   - Compatibility libraries
   - Currently orphaned (lacking maintainers)

---

### 6.3 ECLiPSe Constraint Programming

**System:**

1. **Apt, K., & Wallace, M. (2006).** *Constraint Logic Programming using ECLiPSe.* Cambridge University Press.
   - Comprehensive CLP book using ECLiPSe

2. **Niederliński, A. (2014).** *A Gentle Guide to Constraint Logic Programming via ECLiPSe.* Free PDF available.
   - Tutorial approach

**Industrial Applications:**

3. **ECLiPSe at Cisco, Opel/Flexis.** Case studies in supply chain optimization
   - VDA Logistics Award 2015
   - Production deployments

**Documentation:**

4. **ECLiPSe Website.** http://eclipseclp.org/
   - Active development through 2025
   - MiniZinc/FlatZinc interface

---

### 6.4 CLP Applications to Verification

**Design Space Exploration:**

1. **Jackson, E. K., & Schulte, W. (2012).** "Formula: A Tool for Specifying and Finding Facts." *Microsoft Research Technical Report*.
   - Model-finding with CLP
   - UML+OCL verification

**Clinical Guidelines:**

2. **Ten Teije, A., et al. (2006).** "Improving Medical Protocols by Formal Methods." *Artificial Intelligence in Medicine*, 36(3), 193-209.
   - Verification using Formula

**Program Verification:**

3. **De Angelis, E., et al. (2014).** "Verification of Imperative Programs by Constraint Logic Programming." *Proceedings of LOPSTR*.
   - Partial correctness via CLP
   - Constraint Handling Rules

**Workflow Verification:**

4. **Comparison studies of SMT (Z3) vs. CLP (SICStus).** Various sources
   - Both viable, problem-structure dependent
   - SMT better for Boolean, CLP better for logical structure

---

## 7. Proof Checking and Trust

### 7.1 Curry-Howard and Proof Terms

**Foundational:**

1. **Howard, W. A. (1980).** "The Formulae-as-Types Notion of Construction." In *To H. B. Curry: Essays on Combinatory Logic, Lambda Calculus and Formalism*, 479-490. (Originally circulated 1969)
   - Original Curry-Howard paper

2. **Sørensen, M. H., & Urzyczyn, P. (2006).** *Lectures on the Curry-Howard Isomorphism.* Elsevier.
   - Comprehensive treatment
   - Historical development

**Recent Applications:**

3. **ArXiv 2510.01069 (2024).** "Typed Chain-of-Thought: A Curry-Howard Framework for Verifying LLM Reasoning."
   - Applying Curry-Howard to LLM verification
   - Typed reasoning traces

---

### 7.2 Proof Assistants

**Coq:**

1. **The Coq Development Team.** *The Coq Proof Assistant Reference Manual.* https://coq.inria.fr/
   - Official documentation

2. **Bertot, Y., & Castéran, P. (2004).** *Interactive Theorem Proving and Program Development: Coq'Art.* Springer.
   - Comprehensive Coq textbook

**Lean:**

3. **de Moura, L., & Ullrich, S. (2021).** "The Lean 4 Theorem Prover and Programming Language." *Proceedings of CADE*, 625-635.
   - Lean 4 foundations

4. **The mathlib Community.** "The Lean Mathematical Library." *ArXiv:1910.09336*
   - Extensive formalization in Lean

**Isabelle/HOL:**

5. **Nipkow, T., Paulson, L. C., & Wenzel, M. (2002).** *Isabelle/HOL: A Proof Assistant for Higher-Order Logic.* Springer.
   - Isabelle/HOL textbook

---

### 7.3 Verified Compilation

**CompCert:**

1. **Leroy, X. (2009).** "Formal Verification of a Realistic Compiler." *Communications of the ACM*, 52(7), 107-115.
   - CompCert overview
   - Verification approach

2. **Leroy, X., et al.** *CompCert Documentation.* https://compcert.org/
   - Technical specifications
   - Proof structure

**CakeML:**

3. **Kumar, R., et al. (2014).** "CakeML: A Verified Implementation of ML." *Proceedings of POPL*, 179-191.
   - Verified ML compiler
   - End-to-end verification

**seL4:**

4. **Klein, G., et al. (2009).** "seL4: Formal Verification of an OS Kernel." *Proceedings of SOSP*, 207-220.
   - Verified microkernel
   - Functional correctness proof

5. **Klein, G., et al. (2010).** "seL4: Formal Verification of an Operating-System Kernel." *Communications of the ACM*, 53(6), 107-115.
   - Accessible overview

---

### 7.4 SMT Solver Soundness

**Z3:**

1. **de Moura, L., & Bjørner, N. (2008).** "Z3: An Efficient SMT Solver." *Proceedings of TACAS*, 337-340.
   - Z3 system description

2. **Moura, L. de, & Bjørner, N. (2011).** "Satisfiability Modulo Theories: Introduction and Applications." *Communications of the ACM*, 54(9), 69-77.
   - Accessible SMT overview

**Certified Proof Checkers:**

3. **ArXiv 2405.10611 (2024).** "A Certified Proof Checker for Deep Neural Network Verification."
   - Soundness proof in Imandra
   - Guarantees for UNSAT results

**Soundness Issues:**

4. **What Does It Mean for a Program Analysis to Be Sound?** *SIGPLAN Blog*, August 2019.
   - Clarifying soundness definitions

---

## 8. Abstention and Uncertainty

### 8.1 LLM Uncertainty and Abstention

**Surveys:**

1. **ArXiv 2407.18418 (2024).** "Know Your Limits: A Survey of Abstention in Large Language Models."
   - Comprehensive abstention survey
   - Spectrum of abstention behaviors

**Formal Methods with Uncertainty:**

2. **ArXiv 2505.20047 (2025).** "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks."
   - Uncertainty quantification for LLM formalization
   - 14-100% error reduction
   - Selective verification

**Medical Diagnosis:**

3. **ArXiv 2502.18050 (2025).** "Uncertainty-Aware Abstention in Medical Diagnosis Based on Medical Texts."
   - Domain-specific abstention
   - Safety improvements

**Autonomous Systems:**

4. **IEEE Conference Publication.** "Uncertainty-Aware LiDAR-Camera Autonomy via Conformal Prediction and Principled Abstention."
   - Safety-critical perception
   - Conformal prediction framework
   - ROC-optimized abstention thresholds

---

### 8.2 Formal Verification Under Uncertainty

**Survey:**

1. **TransferLab — appliedAI Institute.** "Formal Verification Under Uncertainty" series.
   - https://transferlab.ai/series/formal-verification-under-uncertainty/
   - Probabilistic model-checking
   - Neuro-symbolic verification

**Cyber-Physical Systems:**

2. **ArXiv 1705.00519 (2017).** "Towards Verification of Uncertain Cyber-Physical Systems."
   - Verification with uncertain parameters
   - Robustness analysis

---

### 8.3 Certification and Safety

**Aerospace (DO-178C):**

1. **RTCA/DO-178C (2011).** *Software Considerations in Airborne Systems and Equipment Certification.*
   - Aviation software certification standard

**Medical Devices (FDA):**

2. **FDA Guidance.** *General Principles of Software Validation; Final Guidance for Industry and FDA Staff.*
   - Medical device software requirements

**Common Criteria:**

3. **Common Criteria for Information Technology Security Evaluation, Version 3.1.** https://www.commoncriteriaportal.org/
   - Security certification standard
   - EAL levels

**Financial Regulations:**

4. **SEC Rule 613 (CAT).** Consolidated Audit Trail requirements.
   - Timestamp synchronization mandates

5. **MiFID II / RTS 25.** European trading timestamp requirements.
   - 100μs for HFT, 1ms for algorithmic

---

## 9. Natural Language Explanation

### 9.1 Formal to Natural Language

**LTL Translation:**

1. **ArXiv, Springer (2022).** "Towards Explainable Formal Methods: From LTL to Natural Language with Neural Machine Translation."
   - OpenNMT for LTL → NL
   - 93.53% BLEU score

**Autoformalization:**

2. **Jiang, A. Q., et al. (2023).** "Draft, Sketch, and Prove: Guiding Formal Theorem Provers with Informal Proofs." *ICLR 2023*.
   - Informal → formal translation

**Isabelle Integration:**

3. **ArXiv 2405.01379 (2024).** "Verification and Refinement of Natural Language Explanations through LLM-Symbolic Theorem Proving."
   - LLM preliminary proofs → Isabelle/HOL
   - Syntactic refinement
   - Verification of NL explanations

---

### 9.2 Structured Explanations

**Formal Proofs as Explanations:**

1. **ArXiv 2311.08637 (2023).** "Formal Proofs as Structured Explanations: Proposing Several Tasks on Explainable Natural Language Inference."
   - Semi-automatic explanation from formal proofs
   - Structured explanation tasks

**Quality Metrics:**

2. **ArXiv 2203.11131 (2022).** "Towards Explainable Evaluation Metrics for Natural Language Generation."
   - Explainability for metrics
   - Tradeoff between quality and interpretability

**Reading Comprehension:**

3. **Evaluation Metrics for Machine Reading Comprehension: Prerequisite Skills and Readability.** Various publications.
   - Substantive validity
   - Shortcut-proof questions

---

## 10. Provenance Postulates and Theory

**Recent Theoretical Work:**

1. **Bogaerts, B., et al. (2024).** "Postulates for Provenance." *Proceedings of PODS*.
   - Seven basic postulates
   - Instance-based provenance for FOL
   - Connection to Halpern-Pearl causality

**Counterfactual Reasoning:**

2. **Rückschloß, K., & Weitkämper, F. (2023).** "Counterfactual Reasoning in Probabilistic Logic Programming." *Proceedings of ICLP*.
   - Unique determination from counterfactuals
   - Reconstruction procedures

**Causality:**

3. **Halpern, J. Y., & Pearl, J. (2005).** "Causes and Explanations: A Structural-Model Approach." *British Journal for the Philosophy of Science*, 56(4), 843-887.
   - Structural causal models
   - Actual causality

---

## 11. Additional Resources

### 11.1 Workshops and Conferences

**Major Conferences:**
- AAAI: Neuro-Symbolic Learning and Reasoning in the Era of LLMs (2025 workshop)
- NeurIPS: Neuro-symbolic tracks
- ICLP: Logic Programming and Nonmonotonic Reasoning
- CP: Constraint Programming
- PODS: Principles of Database Systems
- LICS: Logic in Computer Science

### 11.2 Online Resources

**s(CASP):**
- Manual: https://personal.utdallas.edu/~gupta/nfm-ex/scasp-manual.pdf
- SWI-Prolog tutorial: https://swish.swi-prolog.org/example/scasp.swinb

**ProvSQL:**
- https://provSQL.gitlabpages.inria.fr/

**ECLiPSe:**
- http://eclipseclp.org/

**Proof Assistants:**
- Coq: https://coq.inria.fr/
- Lean: https://leanprover.github.io/
- Isabelle: https://isabelle.in.tum.de/

**SMT Solvers:**
- Z3: https://github.com/Z3Prover/z3
- CVC5: https://cvc5.github.io/

### 11.3 Datasets and Benchmarks

**Temporal Reasoning:**
- TempTabQA
- Test of Time (ToT)
- TIME Benchmark
- ComplexTempQA
- CronQuestions
- ChronoSense

**Neuro-Symbolic:**
- GSM8K (arithmetic)
- FinQA (financial reasoning)
- bAbI, StepGame, CLUTRR, gSCAN (various reasoning)
- ASPBench (ASP evaluation)

**Logic Programming:**
- ASP Competition benchmarks
- SMT-LIB (SMT benchmarks)
- TPTP (theorem proving)

---

## 12. Cross-Cutting Themes

### Key Insights from Literature

1. **Neuro-symbolic convergence**: LLMs excel at semantic parsing, symbolic systems at verified reasoning
2. **Provenance foundations**: Semiring framework provides mathematical rigor for explanations
3. **Abstention with proof**: Explicit uncertainty with certificates prevents silent failures
4. **Small trusted kernels**: Trust through simplicity, not complexity
5. **Self-documenting programs**: Logic programs as executable specifications with embedded explanations

### Research Gaps Identified

1. **Standardized interfaces** between LLMs and symbolic reasoners
2. **Provenance-aware neuro-symbolic architectures** with end-to-end tracking
3. **Temporal reasoning integration** combining LLMs, Allen's algebra, and STN solvers
4. **Interactive explanation refinement** learning from user feedback
5. **Certified explanation generation** with formal faithfulness guarantees

---

## Conclusion

This bibliography represents the state of the art in explanation generation and proof provenance for formal verification as of early 2025. The convergence of logic programming, provenance theory, neuro-symbolic AI, and formal verification creates unprecedented opportunities for building trustworthy AI systems with mathematically certified explanations. The references span foundational theory (semiring provenance, justification logic, Curry-Howard), practical systems (s(CASP), xASP, ProvSQL), recent neuro-symbolic advances (AlphaGeometry, LLM+ASP), and trust mechanisms (proof checking, abstention with certificates).

Researchers should consult the original papers for detailed technical content, proofs, and implementation specifics. Many papers are available on ArXiv or institutional repositories. The field is rapidly evolving with major conferences (AAAI, NeurIPS, ICLP, CP, PODS) featuring relevant work annually.
