# References: DSL Research for Formal Verification and LLM Integration

## Primary Research Papers Analyzed

### Paper 1: Temporal Verification (Temporal Reasoning Applications)
**Source**: `../compass_artifact_wf-4b0cea25-846d-4e20-ad15-8816028eef6c_text_markdown.md`

**Key Findings**:
- 346 aviation deaths from temporal failures (Boeing 737 MAX, Überlingen collision)
- $440M Knight Capital loss (45 minutes, deployment timing errors)
- $1T Flash Crash (temporal ordering failures across fragmented markets)
- Google Spanner TrueTime: 1-7ms bounded uncertainty with commit-wait protocol
- Allen's Interval Algebra: 18 maximal tractable subalgebras (polynomial-time)
- Simple Temporal Networks (STN): O(n³) consistency, O(n² log n + mn) for sparse graphs
- STN with Uncertainty (STNU): Dynamic controllability, O(mn + k²n + kn log n) algorithms

**Temporal Verification Requirements**:
- Aviation TCAS: 20-48s Traffic Advisories, 15-35s Resolution Advisories
- Nuclear: 1-2s SCRAM response (NRC mandates)
- Financial: 50ms SEC Rule 613, 100μs MiFID II high-frequency trading
- Medical: Medtronic insulin pump battery prediction failures (170 hyperglycemia cases)

**Applications to DSL Design**:
- Temporal DSLs must handle qualitative (Allen's) and quantitative (STN/STNU) reasoning
- Verification with abstention: Explicitly certify "unknown" with bounds vs guessing
- Blockchain timestamp manipulation demonstrates need for verified temporal ordering

---

### Paper 2: Logic Programming and Neuro-Symbolic AI
**Source**: `../compass_artifact_wf-bf16ed0b-79fa-4e1d-ba87-d5a7183cca67_text_markdown.md`

**Key Findings - Neuro-Symbolic Revolution (2023-2025)**:
- **167 papers** (2020-2024 PRISMA review): Logic programming + LLM integration
- **35+ major systems** deployed across industry and academia
- **40-160% performance improvements** over pure neural approaches on reasoning benchmarks

**Specific System Results**:

1. **Prolog Integration**:
   - LLM-generated Prolog outperformed Chain-of-Thought (Llama2, CodeLlama, Mistral)
   - DeepSeek-V3: 80% accuracy financial reasoning (vs 63-76% pure CoT)
   - GPT-4o: 74% Pass@1 accuracy on Prolog generation
   - Pattern: LLM extracts predicates, Prolog interpreter executes deterministically

2. **Answer Set Programming (ASP)**:
   - LLASP: Fine-tuned model dramatically outperformed larger non-fine-tuned LLMs
   - Key insight: **Specialized training >> general scale**
   - CLMASP: 90%+ execution rates (robotic planning, LLM skeleton + ASP refinement)
   - ASP synthesis: 9× geomean speedup over SMT-based approaches
   - Non-hallucination property: Everything in answer set has justification

3. **SMT Integration**:
   - Proof of Thought (LLM + Z3): 40% error reduction on math reasoning
   - AlphaGeometry 2: 83% on 25-year IMO geometry history (vs 53% v1)
   - Symbolic deduction engine 200× faster than v1
   - AlphaProof + AlphaGeometry: IMO silver medal (first AI)

4. **Constraint Programming**:
   - GenCP: Faster than Beam Search with 100% constraint satisfaction
   - ConstraintLLM: Fine-tuned Qwen2.5-Coder-32B on 3× RTX A6000 GPUs
   - Result: Competitive with GPT-4o and Deepseek-V3-685B on industrial benchmarks
   - Logic.py: 65% absolute improvement on ZebraLogicBench

**Self-Documenting Logic Programs**:

1. **s(CASP) System**:
   - Top-down ASP interpreter with constraints
   - #pred annotations embed natural language templates
   - Automatic justification trees (--short/--mid/--long detail levels)
   - Handles non-finitely groundable programs (lists, terms, infinite domains)
   - Output formats: plain text, natural language, interactive HTML, JSON

2. **xASP/xASP2**:
   - Explanation graphs for non-ground programs (no simplification)
   - Minimal assumption sets (smallest fact sets needed for explanation)
   - Syntax-insensitive output (equivalent explanations for different orderings)
   - Enhanced support: choice rules, constraints, aggregates (#sum, #min)

3. **Justification Logic (Artemov & Fitting)**:
   - Replaces modal operators (□X) with explicit justification terms (t:X)
   - Operations: application (s·t), sum (s+t), verification (!t)
   - Correspondence Theorem: Every epistemic modal logic has robust justification system
   - Solves epistemic paradoxes (Goldman-Kripke, Gettier)

4. **Provenance Systems**:
   - Semiring framework (Green, Karvounarakis, Tannen 2007)
   - Why-provenance: Minimal witnesses
   - How-provenance: Derivation structure (polynomials over input tuples)
   - Universal property: Compute once in general semiring, evaluate in specific ones
   - ProvSQL: PostgreSQL extension, competitive performance
   - Negation handling: Dual-indeterminate semirings (N[X, X̄])

**Temporal Reasoning Benchmarks**:

1. **TempTabQA**:
   - 11,454 QA pairs from 1,208 Wikipedia tables
   - Top LLMs lag **13.5+ F1 points** behind humans
   - Struggles: Multi-step reasoning, implicit temporal constraints

2. **Test of Time (ToT) - Google Research**:
   - ~40,000 synthetic examples across diverse graph structures
   - Gemini 1.5 Pro: 88.72% on AWE graphs, 51.07% on Complete graphs (**37-point gap**)
   - Duration questions: **13-16% accuracy** (abysmal on simple arithmetic)
   - Timezone questions: 74-90% accuracy (pattern learning vs generalization)

3. **ChronoSense (Allen's Interval Algebra)**:
   - 16 tasks across abstract events and real-world Wikidata
   - LLMs handle Allen relations **inconsistently** (even symmetrical ones)
   - Fundamental limitation: LLMs don't reliably apply formal temporal logic

4. **Hybrid Approaches (Solutions)**:
   - TempGraph-LLM: Synthetic pre-training, LLM translates to temporal graphs
   - TReMu: Timeline summarization + neuro-symbolic reasoning
   - Result: GPT-4o 29.83 → 77.67 (**160% improvement**)
   - Narrative-of-Thought: Events as Python classes, highest F1 on Schema-11

**Allen's Interval Algebra (Formal Foundations)**:
- 13 basic relations: before, after, meets, overlaps, during, etc.
- Composition table for transitive reasoning
- **18 maximal tractable subalgebras** (Krokhin et al. 2003)
- Horn subalgebra: Polynomial-time via path consistency (contains all 13 relations)
- General case: NP-complete
- Implementations: GQR, SparQ, ASP(DL), OWL-Time

**Constraint Logic Programming (CLP)**:

1. **CLP(FD) - Finite Domains**:
   - SWI-Prolog: Recommended before low-level arithmetic (superior declarative properties)
   - Automatic goal_expansion rewriting
   - Relational (usable in all directions): X #> 0, X #< 10
   - Global constraints: all_different, cumulative, global_cardinality
   - SICStus: One of fastest FD solvers (Diaz & Codognet 1993)

2. **CLP(Q/R) - Rational/Real Arithmetic**:
   - SICStus: Complete implementation (Holzbaur)
   - Linear equations, lazy nonlinear, decision algorithms, projection
   - CLP(Q): Exact rational arithmetic
   - CLP(R): Floating point approximation

3. **ECLiPSe**:
   - Multiple solver libraries: ic (intervals), fd, eplex (LP/MIP), suspend, Propia, CHR
   - Hybrid solving: Multiple solvers in one application
   - Production: Cisco, Opel/Flexis (VDA Logistics Award 2015)
   - 500+ universities for teaching

**Performance Comparisons**:
- SMT vs CLP workflow verification: Both viable, choice depends on problem structure
- Z3: 15× speedup over Yices (specific integer constraints)
- Z3: 6× average speedup over Choco/MINION (spreadsheet debugging)
- ASP: 9× geomean speedup over SMT for Datalog synthesis
- **Key**: No universal winner; optimal tool depends on problem characteristics

---

## Cslib Repository Analysis

**Source**: `../../cslib/` (Lean 4 formal verification library)

**Key Examples**:

1. **Lambda Calculus** (`Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean`):
   - Simply-typed lambda calculus with locally nameless representation
   - Extrinsic typing derivations
   - Preservation theorems (typing preserved under substitution)
   - Pattern: Inductive type definitions with natural language documentation

2. **Automata Theory** (`Cslib/Computability/Automata/DFA.lean`):
   - Deterministic Finite Automata formalization
   - Extended transition function (multi-step)
   - Language acceptance definitions
   - Pattern: Finite-state verification with grind automation

3. **Classical Linear Logic** (`Cslib/Logics/LinearLogic/CLL/Basic.lean`):
   - Propositions with multiplicative/additive connectives
   - Sequent calculus with proof rules
   - Logical equivalences with formal proofs
   - Duality as involution (a⫠⫠ = a)
   - Pattern: Resource-aware logic with proof search

4. **Process Calculi** (`Cslib/Languages/CCS/Basic.lean`):
   - Calculus of Communicating Systems (Milner)
   - Actions (name, coname, τ) with visibility predicates
   - Processes with parallel composition, choice, restriction
   - Context completeness theorem
   - Pattern: Concurrent systems with structural operational semantics

5. **Labeled Transition Systems** (`Cslib/Foundations/Semantics/LTS/Basic.lean`):
   - Multi-step transitions with compositional reasoning
   - Image-finite, finitely-branching, deterministic classes
   - Saturated transitions (weak bisimulation)
   - Divergence-free property
   - Pattern: Behavioral semantics with calc-tactic support

**DSL Design Patterns in Lean**:
- Inductive types for syntax (Process, Proposition, Typing derivation)
- Propositional definitions for semantic properties (Deterministic, ImageFinite)
- Scoped notation for domain-specific operators (⊗, ⅋, ⊕, &, !, ʔ for linear logic)
- Grind automation hints for common proof patterns
- Documentation strings with references to papers
- Custom attributes and tactics for domain-specific reasoning

**Lean 4 as Proof Assistant DSL**:
- Dependent type theory (Calculus of Inductive Constructions)
- Metaprogramming via tactics and elaboration
- Mathlib integration (1M+ lines of mathematics)
- Interactive theorem proving with excellent error messages
- Pattern: Proofs as programs (Curry-Howard correspondence)

---

## Web Search Research (2024-2025)

### DSL Code Generation with LLMs

**DSL-Xpert (MODELS 2024)**:
- LLM-driven generic DSL code generation
- Grammar prompting with few-shot learning
- Handles unpublished/less-known DSLs (limited training data)
- Multi-phase approach: semantic parsing → vocabulary translation → code generation

**Design Patterns for LLM Agents (DeepMind CaMeL)**:
- Privileged LLM generates code in custom sandboxed DSL
- DSL specifies tool calls and data flow
- Full data flow analysis enables tainted data tracking
- Pattern: Security through DSL constraints

**Domain-Specific Language Creation Pattern**:
- LLM creates its own DSL for system concepts (requirements, security, architecture)
- Both LLM and users leverage DSL for communication
- Pattern: Meta-level DSL generation

**Challenges**:
- Lesser-known DSLs: LLM performance significantly decreases
- Example: LIrAs (robotics DSL) exploratory study showed poor generation without fine-tuning
- Solution: Grammar prompting, constrained generation, or fine-tuning

### Formal Verification DSL Expressiveness vs Learnability

**ISoLA 2018 (Markus Voelter)**:
- Synergy between DSLs and formal methods underemphasized
- Putting semantics into DSLs enables clever encodings for verification tools
- Domain-specific constructs reduce annotation burden (recover domain semantics)

**Lightweight Formal Methods**:
- Response to full formalization difficulty
- Partial specification and focused application
- Trade-off: Rigor vs. comprehensibility vs. learning curve

**Mathematical Disciplines Challenge**:
- Formal specifications outside traditional engineering education
- DSLs help: Domain-specific constructs reduce low-level mathematical details

### PDDL/STRIPS Planning with LLMs

**Generalized Planning (arXiv 2305.11014)**:
- GPT-4 as generalized planner (given domain + training tasks)
- Generates Python programs producing plans for new tasks
- Chain-of-Thought summarization: LLM summarizes domain, proposes strategies
- Automated debugging: Validate against training tasks, feedback loops
- **Key factors**: Automated debugging, PDDL names, GPT-4 model (ablation studies)

**PDDL Domain Induction**:
- LLMs infer action semantics from environment feedback
- Generate PDDL domain files (not just problem files)
- Integration with symbolic solvers for deterministic planning

**Hybrid Approaches**:
- LLM as "formalizer": Generates PDDL for symbolic planners
- Two-level: LLM skeleton plans + symbolic constraint solving (CLMASP: 90%+ execution)
- Automated prompt generation from PDDL input

**Performance**:
- STRIPS subset with types and negative preconditions (typical experiments)
- GPT-4 identified as "surprisingly powerful" generalized planner
- Automated debugging very important (ablation studies)

### MiniZinc vs Essence Comparison

**Essence**:
- Formal language for combinatorial problems (natural rigorous specifications)
- High abstraction: Combinatorial decision variables (tuples, sets, multisets, relations, partitions, functions)
- Nested combinatorial objects: Sets of sets of partitions (arbitrary depth)
- Philosophy: Natural language + discrete mathematics

**MiniZinc**:
- High-level constraint modeling language (solver-independent)
- FlatZinc intermediate language (straightforward translation)
- Global constraints preserved during translation
- Philosophy: Reasonable compromise between design possibilities
- Open-source with annual MiniZinc Challenge

**Design Philosophy Difference**:
- No standard CP modeling language (most solvers have own language)
- Both address experimenting with different solvers
- Essence: Highest abstraction, automatic refinement (Essence Prime)
- MiniZinc: Solver-independent with explicit FlatZinc target

**Comparable Systems**:
- OPL, MiniZinc, Essence Prime all aid constraint model abstraction
- Essence Prime comparable to OPL and MiniZinc

### ProbLog Features

**Core Concept**:
- Extends Prolog with probabilistic facts (:: operator)
- Minimally extends Prolog: Probabilistic fact = logical atom + random variable
- Query result: Probability (vs Prolog's truth value)

**Key Features**:
1. Probabilistic facts: 0.7::bird(tweety)
2. Flexible probabilities: Arithmetic expressions computed dynamically
3. Distributional clauses: Continuous probability distributions
4. Annotated disjunctions: Exclusive choices
5. Tabling/memoization: Everything cached (advanced caching)

**Restrictions**:
- No cuts (!) or mechanisms breaking pure logic interpretation
- Necessary for probabilistic semantics

**Implementation**:
- Python package with Java embedding
- Knowledge base: Prolog/Datalog facts, CSV, SQLite, functions
- Knowledge compilation for exact inference

**Recent Research (Rückschloß & Weitkämper 2023)**:
- Counterfactual reasoning reveals program structure
- Well-written ProbLog programs uniquely determined by counterfactuals
- Reconstruction procedures recover programs from counterfactual outputs

---

## Additional Key References (From Papers)

### Temporal Reasoning

**Allen, J. F. (1983)**. "Maintaining knowledge about temporal intervals." *Communications of the ACM*.
- Original interval algebra paper (13 basic relations)
- Composition table for transitive reasoning

**Krokhin, A., Jeavons, P., & Jonsson, P. (2003)**. "Reasoning about temporal relations: The tractable subalgebras of Allen's interval algebra." *Journal of the ACM*.
- Identified 18 maximal tractable subalgebras
- Horn subalgebra most important (polynomial-time, contains all 13 relations)

**Dechter, R., Meiri, I., & Pearl, J. (1991)**. "Temporal constraint networks." *Artificial Intelligence*.
- Foundational Simple Temporal Networks (STN) paper
- Binary constraints Y - X ≤ δ
- Consistency checking: All-pairs shortest paths O(n³)

**Morris, P., Muscettola, N., & Vidal, T. (2001)**. "Dynamic control of plans with temporal uncertainty." *IJCAI*.
- Introduced STN with Uncertainty (STNU)
- Contingent links (uncontrollable durations)
- Dynamic controllability concept

**Cairo, M., Hunsberger, L., & Rizzi, R. (2018)**. "Faster dynamic controllability checking for Simple Temporal Networks with Uncertainty." *TIME*.
- O(mn + k²n + kn log n) algorithm for sparse graphs
- RUL⁻ propagation rules (Relax⁻, Upper⁻, Lower⁻)

### Neuro-Symbolic AI

**Yang, K., Chen, J., & Tam, D. (2024)**. "LLM-Generated Prolog for Arithmetic Reasoning."
- Prolog generation outperforms Chain-of-Thought
- Predicate permutation as data augmentation
- GSM8K-Prolog dataset

**Ishay, A., & Lee, J. (2024)**. "LLASP: Fine-Tuning Large Language Models for Answer Set Programming."
- Fine-tuned lightweight model >> larger non-fine-tuned LLMs
- Publicly available dataset and code
- Specialized training trumps general scale

**Wang, L., et al. (2024)**. "Grammar Prompting for Domain-Specific Language Generation with Large Language Models."
- BNF grammars in in-context learning
- Competitive performance: Semantic parsing, PDDL, SMILES
- Minimal grammar subsets for each demonstration

**Xiong, H., et al. (2024)**. "TempGraph-LLM: Teaching LLMs to Translate Text to Temporal Graphs."
- TGQA synthetic datasets for temporal graph translation
- Chain-of-Thought with graph structure
- More consistent than free text generation

**Liu, X., et al. (2025)**. "Time-R1: Temporal Reasoning with Reinforcement Learning."
- 3B parameter model vs 671B DeepSeek-R1
- Three-stage RL curriculum with dynamic rule-based rewards
- Trained on Time-Bench (10 years news data)

### Provenance and Explanation

**Buneman, P., Khanna, S., & Tan, W. C. (2001)**. "Why and where: A characterization of data provenance." *ICDT*.
- Original why-provenance formalization
- Witness basis: Set of minimal witnesses

**Green, T. J., Karvounarakis, G., & Tannen, V. (2007)**. "Provenance semirings." *PODS*.
- How-provenance via semiring framework
- Universal property: Compute once, evaluate many times
- Applications: Bag semantics, probabilistic databases, uncertain data

**Grädel, E., & Tannen, V. (2019)**. "Semiring provenance for first-order model checking." *arXiv*.
- Dual-indeterminate semirings for negation (N[X, X̄])
- Game-theoretic provenance (model checking as 2-player game)
- Fixed-point logics: ω-continuous semirings for recursive programs

**Senellart, P., et al. (2018-2025)**. "ProvSQL: Provenance and Probability Management in PostgreSQL." *PVLDB*.
- PostgreSQL extension for semiring provenance
- Provenance circuits for efficient computation
- Recent additions: UPDATE provenance, temporal databases, undo operations

**Rückschloß, K., & Weitkämper, F. (2023)**. "Counterfactual reasoning in probabilistic logic programming." *arXiv*.
- Well-written ProbLog programs uniquely determined by counterfactuals
- Reconstruction procedures recover programs
- Counterfactual behavior characterizes program semantics

### Logic Programming Systems

**Artemov, S., & Fitting, M. (2019)**. "Justification Logic: Reasoning with Reasons." *Cambridge University Press*.
- Comprehensive justification logic framework
- Explicit justification terms (t:X) replace modal operators
- Correspondence Theorem for epistemic modal logics

**Pontelli, E., Son, T. C., & El-Khatib, O. (2009)**. "Justifications for logic programs under answer set semantics." *Theory and Practice of Logic Programming*.
- Off-line and on-line justifications for ASP
- Integration with Smodels solver
- Semiring-based annotations for derivation tracking

**Arias, J., et al. (2018)**. "Constraint Answer Set Programming without Grounding." *Theory and Practice of Logic Programming*.
- s(CASP) system description
- Goal-directed search without grounding
- Constructive negation
- Natural language explanation generation

**Fandinno, J., & Schulz, C. (2019)**. "Answering the 'why' in answer set programming." *Theory and Practice of Logic Programming*.
- xASP system for explanation graphs
- Minimal assumption sets
- Syntax-insensitive explanations

**Gavanelli, M., Rossi, F., et al. (2011)**. "Optimal valve placement in water distribution networks with CLP(FD)." *ICLP Best Paper*.
- Real-world CLP(FD) application (water networks)
- Demonstrates scalability to practical problems

### Proof Assistants

**Moura, L., Ullrich, S., et al. (2021-2024)**. "The Lean 4 Theorem Prover and Programming Language." *Journal of Automated Reasoning*.
- Dependent type theory (CIC)
- Metaprogramming via tactics and elaboration
- Mathlib: 1M+ lines formalized mathematics

**Avigad, J., Moura, L., & Kong, S. (2023)**. "Theorem Proving in Lean 4." *Online textbook*.
- Comprehensive pedagogical resource
- Interactive exercises (Natural Number Game)

**Bertot, Y., & Castéran, P. (2004)**. "Interactive Theorem Proving and Program Development: Coq'Art." *Springer*.
- Coq foundations and tactics
- Calculus of Inductive Constructions

**Pierce, B. C., et al. (2010-2024)**. "Software Foundations." *Online textbook series*.
- Coq-based formal verification course
- Volumes: Logical Foundations, Programming Language Foundations, Verified Functional Algorithms

**Leroy, X. (2009)**. "Formal verification of a realistic compiler." *Communications of the ACM*.
- CompCert: Formally verified C compiler
- Proven correct compilation (Coq)
- Demonstrates proof assistant viability for large-scale software

**Trinh, M.-T., et al. (2024)**. "AlphaProof: Reinforcement Learning for Theorem Proving in Lean."
- RL-trained LLM for Lean tactic generation
- IMO silver medal achievement (first AI)
- Demonstrates LLM-proof assistant integration

**Thakkar, A., et al. (2024)**. "AlphaGeometry 2: Enhanced Symbolic Deduction for IMO Geometry."
- Gemini LLM + symbolic deduction engine (200× faster)
- 83% on 25-year IMO geometry history (vs 53% v1)
- Demonstrates Symbolic[Neural] architecture

### Constraint Programming

**Nethercote, N., Stuckey, P. J., et al. (2007)**. "MiniZinc: Towards a Standard CP Modelling Language." *CP*.
- MiniZinc design and FlatZinc intermediate language
- Solver-independent modeling
- Global constraint preservation

**Frisch, A. M., et al. (2008)**. "Essence: A constraint language for specifying combinatorial problems." *Constraints*.
- Highest abstraction level for combinatorial problems
- Nested combinatorial decision variables
- Automatic refinement to Essence Prime

**Schulte, C., et al. (2006-2024)**. "Gecode: Generic Constraint Development Environment."
- High-performance constraint solver
- Extensive global constraint library
- MiniZinc backend

**Brand, S., et al. (2008)**. "Constraint Programming in ECLiPSe."
- Hybrid solving (multiple solver libraries)
- Industrial applications (Cisco, Opel/Flexis)
- Teaching adoption (500+ universities)

---

## LLM Integration Research (2024-2025)

### Fine-Tuning Studies

**LLASP Dataset and Models**:
- Publicly available: ASP generation fine-tuning data
- Demonstrates specialized training effectiveness
- Lightweight model outperforms larger general models

**ConstraintLLM (Industrial Constraint Programming)**:
- Fine-tuned Qwen2.5-Coder-32B-Instruct
- QLoRA on 3× NVIDIA RTX A6000 GPUs (cost-effective)
- Competitive with GPT-4o and Deepseek-V3-685B
- Demonstrates viability for smaller organizations

### Constrained Generation

**Willison, S., & Anthropic (2025)**. "Constrained Decoding with Large Language Models."
- Outlines: Open-source CFG-based constrained generation
- JSON Schema support
- OpenAI structured outputs

**GenCP (Constrained Text Generation)**:
- LLM domain prediction + constraint programming search
- Faster than Beam Search
- 100% constraint satisfaction guarantee

### Temporal Reasoning Benchmarks

**Chen, W., et al. (2023)**. "TempTabQA: Temporal Question Answering over Tables."
- 11,454 QA pairs from 1,208 Wikipedia tables
- Top LLMs lag 13.5+ F1 points behind humans
- Multi-hop temporal reasoning challenges

**Qin, L., et al. (2024)**. "Test of Time: Evaluating LLM Temporal Reasoning." *Google Research*.
- ~40,000 synthetic examples
- Graph structure impact: 37-point performance swings
- Duration arithmetic: 13-16% accuracy (abysmal)

**Zhou, Q., et al. (2024)**. "ChronoSense: Evaluating Temporal Commonsense Reasoning in LLMs."
- Allen's Interval Algebra relation identification
- LLMs inconsistent even on symmetrical relations
- Demonstrates fundamental temporal reasoning gap

**Li, Y., et al. (2025)**. "TReMu: Time-aware Memorization and Neuro-Symbolic Reasoning."
- Timeline summarization + neuro-symbolic Python code
- GPT-4o: 29.83 → 77.67 (160% improvement)
- Validates hybrid LLM + symbolic approach

### Planning DSL Integration

**Silver, T., et al. (2023)**. "Generalized Planning in PDDL Domains with Pretrained Large Language Models." *AAAI*.
- GPT-4 as generalized planner
- Chain-of-Thought summarization
- Automated debugging critical

**Valmeekam, K., et al. (2024)**. "On the Planning Abilities of Large Language Models."
- Systematic evaluation of LLM planning
- Identifies strengths (skeleton plans) and weaknesses (state tracking)

**CLMASP (2024)**. "Combining LLMs and ASP for Robotic Planning."
- Two-level planning: LLM skeleton + ASP refinement
- 90%+ execution rates
- Demonstrates hybrid architecture effectiveness

---

## Conferences and Workshops (2024-2025)

**AAAI 2025**: Workshop on "Neuro-Symbolic Learning and Reasoning in the era of Large Language Models"
- Dedicated track for LLM-symbolic integration
- Identified gaps: Explainability/Trustworthiness (28%), Meta-Cognition (5%)

**NeurIPS 2024**: Neuro-symbolic AI tracks
- Hybrid architectures achieving state-of-the-art
- Integration patterns: Symbolic[Neural], Neural[Symbolic], Symbolic Neural

**IJCAI 2024**: Logic programming and constraints
- ASP Competition results
- s(CASP) explanation demonstrations

**CP 2024 (Constraint Programming)**: Co-located with SAT
- MiniZinc Challenge results
- LLM-constraint programming integration workshops

**ICLP 2024 (International Conference on Logic Programming)**:
- Tracks on explainability and trustworthy AI
- Integration with verification and formal methods

**MODELS 2024 (Model Driven Engineering Languages and Systems)**:
- DSL-Xpert tool demonstration
- LLM-driven generic DSL code generation

**TIME 2024 (International Symposium on Temporal Representation and Reasoning)**:
- STNU algorithms and improvements
- Temporal reasoning benchmarks

---

## Tools and Systems

### Logic Programming
- **SWI-Prolog**: https://www.swi-prolog.org/
- **SICStus Prolog**: https://sicstus.sics.se/
- **ECLiPSe**: https://eclipseclp.org/
- **Clingo/Gringo (Potassco)**: https://potassco.org/
- **s(CASP)**: https://gitlab.software.imdea.org/ciao-lang/sCASP
- **xASP**: Available via research publications

### SMT Solvers
- **Z3**: https://github.com/Z3Prover/z3
- **CVC5**: https://cvc5.github.io/
- **Yices**: https://yices.csl.sri.com/

### Proof Assistants
- **Lean 4**: https://lean-lang.org/
- **Coq**: https://coq.inria.fr/
- **Isabelle**: https://isabelle.in.tum.de/

### Planning
- **PDDL Solvers**: Fast-Forward, Fast Downward, LAMA
- **International Planning Competition**: https://www.icaps-conference.org/competitions/

### Constraint Programming
- **MiniZinc**: https://www.minizinc.org/
- **Gecode**: https://www.gecode.org/
- **Chuffed**: https://github.com/chuffed/chuffed
- **OR-Tools (Google)**: https://developers.google.com/optimization

### Temporal Reasoning
- **GQR**: https://www.qualitative-reasoning.org/
- **SparQ**: Spatial and temporal reasoning toolbox
- **SPIN**: http://spinroot.com/spin/whatispin.html

### Provenance
- **ProvSQL**: https://github.com/PierreSenellart/provsql

### LLM Integration
- **Outlines**: https://github.com/outlines-dev/outlines (constrained generation)
- **LLASP**: Research publication + dataset
- **ConstraintLLM**: Research publication + models

---

## Summary: Research Landscape

**Maturity**:
- **Most mature**: SMT (Z3 dominance), Prolog (decades), PDDL (IPC), Datalog (databases)
- **Rapidly growing**: Lean 4 (Mathlib), ASP (competitions), neuro-symbolic integration
- **Research-focused**: Essence, temporal reasoning hybrids

**LLM Integration Patterns**:
1. **Fine-tuning trumps scale**: LLASP, ConstraintLLM demonstrate specialized training effectiveness
2. **Hybrid architectures dominant**: AlphaGeometry 2, AlphaProof, TReMu (40-160% improvements)
3. **Constrained generation viable**: Outlines, OpenAI structured outputs (zero syntax errors)
4. **Temporal reasoning gap**: 13.5+ F1 lag, 13-16% duration accuracy (hybrid solutions emerging)

**Key Insights**:
- No universal winner: DSL selection depends on correctness/explanation/performance priorities
- Logic programming excels at explanation (s(CASP), xASP, provenance)
- SMT excels at performance (quantifier-free, rich theories)
- Proof assistants provide absolute correctness (kernel verification)
- Hybrid neuro-symbolic achieves best results (LLM flexibility + symbolic correctness)

**Future Directions**:
1. Standardized LLM-symbolic interfaces (beyond ad-hoc JSON DSLs)
2. Provenance-aware architectures (track derivations through entire pipeline)
3. Temporal reasoning integration (LLM + Allen's + STN/STNU)
4. Interactive explanation refinement (learn from user feedback)
5. Certified explanation generation (formal guarantees of faithfulness)

This bibliography represents comprehensive research from 2020-2025 across logic programming, formal verification, neuro-symbolic AI, temporal reasoning, and LLM integration, synthesizing academic papers, production systems, and emerging tools for DSL design and deployment.
