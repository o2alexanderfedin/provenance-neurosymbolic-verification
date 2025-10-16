**Navigation**: [🏠 Home](../README.md) | [📄 Paper](../paper_main.md) | [🚀 Quick Start](../QUICK_START.md) | [📑 Index](../PROJECT_INDEX.md)

---

# DSL Taxonomy for Formal Verification and LLM Integration

## Executive Summary

This taxonomy categorizes formal verification domain-specific languages (DSLs) across seven major categories, analyzing their expressiveness, learnability, and LLM-friendliness based on research from 2020-2025 and examination of production systems. The analysis reveals that **logic programming approaches (Prolog, ASP) offer fundamentally superior explainability** compared to SMT-based verification while achieving competitive or superior performance on many reasoning tasks, with neuro-symbolic systems combining LLMs with logic programming outperforming pure neural approaches by 40-160% on reasoning benchmarks.

## Category 1: Logic Programming DSLs

### 1.1 Prolog

**Expressiveness:**
- First-order logic with full quantification through variables
- Native recursion and backtracking search
- Natural compound terms and unification
- Meta-programming capabilities via predicates as data
- Definite Clause Grammars for parsing/NLP

**Learnability:**
- **High initial barrier**: Declarative paradigm shift from imperative thinking
- Requires understanding unification, backtracking, and cut operators
- Pattern matching relatively intuitive once paradigm understood
- SWI-Prolog documentation and community support strong

**LLM-Friendliness (74% Pass@1 for GPT-4o):**
- LLM-extracted predicates + external Prolog interpreters outperform Chain-of-Thought
- Predicate permutation as data augmentation (leverages ordering-insensitivity)
- DeepSeek-V3: 80% accuracy on financial reasoning (vs 63-76% pure CoT)
- Deterministic, explainable reasoning with explicit logical predicates
- **Pattern**: LLMs should extract predicates; interpreters handle execution

**Key Characteristics:**
```prolog
% Declarative rule definition
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).

% Recursive definition
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
```

**Production Systems:**
- ECLiPSe: Used at Cisco, Opel/Flexis (VDA Logistics Award 2015)
- SWI-Prolog: 500+ universities, extensive library ecosystem
- SICStus Prolog: Fastest finite domain constraint solver

**Tradeoffs:**
- ✓ Natural expression of rules and facts
- ✓ Execution traces show reasoning steps (SLD resolution trees)
- ✗ Arithmetic constraints inefficient without CLP extensions
- ✗ Depth-first search can be inefficient without optimization
- ✗ "Obvious" identities (x+y=y+x) difficult to deduce natively

### 1.2 Answer Set Programming (ASP)

**Expressiveness:**
- Non-monotonic reasoning with stable model semantics
- No quantifiers (grounding + SAT solving approach)
- Choice rules, aggregates (#sum, #min, #count)
- Constraints and optimization
- Inability to easily express linear arithmetic or difference logic

**Learnability:**
- **Moderate barrier**: Declarative but more structured than Prolog
- Stable model semantics more intuitive than classical logic for many
- Grounding concept requires understanding
- Clingo/Gringo toolchain well-documented

**LLM-Friendliness:**
- LLASP fine-tuning: **Specialized training >> general-purpose scale**
- Lightweight fine-tuned model dramatically outperforms larger non-fine-tuned LLMs
- GPT-3/GPT-4: Transform logic puzzles to ASP with few-shot examples (but errors common)
- ASPBench (2025): LLMs struggle most with answer set computation (core solving)
- **Key insight**: LLMs excel at NL→ASP translation; symbolic solvers essential for reasoning

**Key Characteristics:**
```asp
% Choice rule: bird(tweety) or not bird(tweety)
{ bird(tweety) }.

% Constraint: cannot be both
:- bird(X), not flies(X), not penguin(X).

% Weak constraint (optimization)
:~ bird(X). [1@1, X]

% Aggregates
total_birds(N) :- N = #count{X : bird(X)}.
```

**Unique Properties:**
- **Non-hallucination guarantee**: Everything in answer set has justification
- Stable model semantics prevents circular justifications
- ~9× geomean speedup over SMT for Datalog synthesis problems

**Production Systems:**
- s(CASP): Justification trees with natural language annotations (#pred)
- xASP/xASP2: Explanation graphs for non-ground programs
- CLASP: Consistently strong ASP Competition performance

**Self-Documenting Features:**
```asp
#pred bird(X) :: '@(X) is a bird'.
#pred flies(X) :: '@(X) can fly'.

% Query execution produces explanations:
% --short: Brief summary
% --mid: Medium detail
% --long: Full justification tree
```

**Tradeoffs:**
- ✓ Explicit justification for every derived fact
- ✓ Natural expression of combinatorial problems
- ✓ Boolean problem optimization (reduces to SAT)
- ✗ Grounding explosion for large domains
- ✗ Linear arithmetic support limited

### 1.3 Datalog

**Expressiveness:**
- Subset of Prolog: no function symbols, stratified negation
- Bottom-up evaluation (forward chaining)
- Polynomial-time data complexity
- Extensions: Datalog± (existential rules), temporal Datalog

**Learnability:**
- **Low barrier**: Simplest logic programming language
- No complex features (cut, non-stratified negation)
- SQL-like semantics familiar to database programmers
- Limited expressiveness aids comprehension

**LLM-Friendliness:**
- ASP synthesis achieves 9× speedup using why/why-not provenance
- ProSynth: Provenance from Datalog solvers guides synthesis
- Simple syntax aids LLM generation
- **Pattern**: Provenance information improves synthesis quality

**Key Characteristics:**
```datalog
path(X, Y) :- edge(X, Y).
path(X, Y) :- edge(X, Z), path(Z, Y).

% Stratified negation allowed
not_connected(X, Y) :- node(X), node(Y), !path(X, Y).
```

**Tradeoffs:**
- ✓ Polynomial-time guarantees
- ✓ Bottom-up evaluation predictable
- ✓ Natural database query expression
- ✗ No function symbols limits expressiveness
- ✗ Restricted compared to full Prolog

## Category 2: SMT-Based DSLs

### 2.1 SMT-LIB

**Expressiveness:**
- Quantifier-free first-order logic (primarily)
- Rich theories: QF_LIA (linear integer), QF_BV (bit-vectors), QF_AUFLIA (arrays)
- Native linear/non-linear arithmetic, bit-vectors, arrays, strings, sequences
- Efficient theory combination via congruence closure
- Quantifier support limited and often incomplete (heuristic E-matching)

**Learnability:**
- **Moderate barrier**: S-expression syntax unfamiliar
- Theory selection requires domain knowledge
- Performance varies dramatically by theory choice (QF_LIA vs QF_BV: order-of-magnitude differences)
- Extensive SMT-COMP benchmarks aid learning

**LLM-Friendliness:**
- Proof of Thought: LLM + Z3 via JSON DSL reduced errors 40% on math reasoning
- Standardized SMT-LIB format enables tool interoperability
- **Pattern**: LLMs generate constraints; SMT solvers verify/solve
- Grammar prompting with BNF aids generation

**Key Characteristics:**
```smt2
(set-logic QF_LIA)
(declare-const x Int)
(declare-const y Int)
(assert (> (+ x y) 10))
(assert (< x 5))
(check-sat)
(get-model)
```

**Production Systems:**
- Z3: Dominates SMT-COMP (15+ divisions), 21 benchmarks solvable only by Z3 (2013)
- CVC5: Strong performance, integrated with Lean theorem prover
- Yices: Specialized for certain problem classes
- Why3, Boogie, SLAM, BLAST: Program verification backends

**Tradeoffs:**
- ✓ Large-scale quantifier-free verification (10,000+ constraints)
- ✓ Bit-blasting handles magic squares order 10 easily
- ✓ Native bit-vector support for hardware verification
- ✗ Proofs large/cryptic for complex theory combinations
- ✗ Model generation "black box" to many users
- ✗ Quantifiers: undecidable when combined with non-linear arithmetic

### 2.2 Z3py

**Expressiveness:**
- Python API for Z3 SMT solver
- Object-oriented constraint construction
- Simplification/manipulation APIs
- Solver control (push/pop contexts)

**Learnability:**
- **Lower barrier**: Python syntax familiar
- Object-oriented API more intuitive than SMT-LIB
- Interactive exploration via Jupyter notebooks
- Rich documentation and examples

**LLM-Friendliness:**
- Python-based generation leverages LLM code generation strength
- ConstraintLLM framework demonstrates industrial viability
- **Pattern**: LLMs generate Z3py; solver provides verification

**Key Characteristics:**
```python
from z3 import *

x = Int('x')
y = Int('y')
s = Solver()
s.add(x + y > 10)
s.add(x < 5)
if s.check() == sat:
    print(s.model())
```

**Tradeoffs:**
- ✓ Python integration enables complex workflows
- ✓ Programmatic solver control
- ✓ Familiar syntax reduces learning curve
- ✗ Performance overhead vs native SMT-LIB
- ✗ Still inherits SMT explanation limitations

## Category 3: Planning DSLs

### 3.1 PDDL (Planning Domain Definition Language)

**Expressiveness:**
- STRIPS subset: types, negative preconditions
- ADL extensions: conditional effects, quantified preconditions
- Temporal planning (durative actions)
- Numeric fluents for resource management
- Preferences and constraints

**Learnability:**
- **Moderate barrier**: Clear syntax but domain modeling requires expertise
- Separation of domain and problem files aids organization
- Grounded action semantics intuitive
- International Planning Competition benchmarks extensive

**LLM-Friendliness:**
- GPT-4 "surprisingly powerful" as generalized planner
- Automated PDDL generation from natural language prompts
- Chain-of-Thought summarization: LLM summarizes domain before synthesis
- Automated debugging: Validate against training tasks with feedback
- **Critical factors**: Automated debugging, PDDL names, GPT-4 model choice

**Key Characteristics:**
```pddl
(:action move
  :parameters (?obj - object ?from ?to - location)
  :precondition (and (at ?obj ?from)
                     (clear ?to))
  :effect (and (at ?obj ?to)
               (not (at ?obj ?from))
               (clear ?from)
               (not (clear ?to))))
```

**Hybrid Approaches:**
- LLMs as "formalizers": Generate PDDL for symbolic solvers
- LLMs infer action semantics from environment feedback
- PSALM-V: Automating symbolic planning in visual environments
- **Two-level planning**: LLM skeleton plans + ASP constraint solving (CLMASP: 90%+ execution)

**Tradeoffs:**
- ✓ Domain-independent planning representation
- ✓ Rich competition ecosystem (IPC)
- ✓ Natural temporal action modeling
- ✗ Domain modeling requires expertise
- ✗ Scalability challenges for large state spaces

### 3.2 STRIPS

**Expressiveness:**
- Simplified PDDL: preconditions, add-list, delete-list
- No types, no conditional effects
- Propositional representation
- Foundation for modern planners

**Learnability:**
- **Low barrier**: Simplest planning formalism
- Clear semantics: state transformations
- Historical importance (1971 Stanford)
- Limited expressiveness aids learning

**LLM-Friendliness:**
- GPT-4 experiments typically use STRIPS subset
- Simplified syntax aids generation
- **Pattern**: Start with STRIPS; extend to PDDL as needed

**Key Characteristics:**
```strips
Action: MOVE(obj, from, to)
Precond: at(obj, from), clear(to)
Add: at(obj, to), clear(from)
Delete: at(obj, from), clear(to)
```

**Tradeoffs:**
- ✓ Simple semantics
- ✓ Historical foundation
- ✓ Easy to implement/understand
- ✗ Limited expressiveness
- ✗ No types or conditional effects

## Category 4: Constraint Modeling DSLs

### 4.1 MiniZinc

**Expressiveness:**
- High-level constraint modeling language
- Solver-independent (FlatZinc intermediate language)
- Global constraints (alldifferent, cumulative)
- Optimization support (minimize/maximize)
- Integer, Boolean, float, set variables
- Comprehensions and generators

**Learnability:**
- **Moderate barrier**: Declarative modeling requires practice
- Syntax closer to mathematical notation
- Extensive documentation and tutorials
- MiniZinc Challenge annual competition

**LLM-Friendliness:**
- Automatic Constraint Model Generator: Multi-step LLM process
- Semantic entity extraction → constraint generation → iterative validation
- ConstraintLLM fine-tuning on industrial benchmarks competitive with GPT-4o
- **Pattern**: Fine-tuned specialized models match/exceed massive general models

**Key Characteristics:**
```minizinc
var 1..9: x;
var 1..9: y;
constraint x + y > 10;
constraint x < 5;
solve satisfy;
```

**Design Philosophy:**
- **Compromise between design possibilities**
- Straightforward translation to FlatZinc preserves global constraints
- Solver backends: Gecode, Chuffed, OR-Tools, Gurobi, CPLEX

**Tradeoffs:**
- ✓ Solver-independent modeling
- ✓ Rich global constraint library
- ✓ Mathematical notation familiar
- ✗ FlatZinc compilation can be complex
- ✗ Performance varies by backend solver

### 4.2 Essence

**Expressiveness:**
- **Highest abstraction level** among constraint languages
- Combinatorial decision variables: sets, multisets, relations, partitions, functions
- **Nested combinatorial objects**: Sets of partitions, sets of sets of partitions
- Natural rigorous specifications (mix natural language + discrete math)
- Automatic refinement to executable models (Essence Prime → Savile Row → solvers)

**Learnability:**
- **Higher barrier**: Abstract mathematical concepts
- Very expressive but requires mathematical sophistication
- Automated refinement reduces manual encoding burden
- Smaller community than MiniZinc

**LLM-Friendliness:**
- High abstraction could aid LLM generation (closer to natural language)
- Limited LLM research (smaller training corpus)
- Automatic refinement means LLM generates specification, toolchain handles optimization

**Key Characteristics:**
```essence
given n : int
find x : set of int(1..n)
such that |x| = 5
such that forAll i,j in x . i + j > 10
```

**Design Philosophy:**
- **Abstraction over specification details**
- Combinatorial objects as first-class citizens
- Automated refinement to lower-level representations

**Tradeoffs:**
- ✓ Highest abstraction level
- ✓ Natural problem specification
- ✓ Automated refinement
- ✗ Smaller ecosystem than MiniZinc
- ✗ Requires mathematical sophistication
- ✗ Refinement process less transparent

## Category 5: Proof Assistant DSLs

### 5.1 Lean 4

**Expressiveness:**
- Dependent type theory (Calculus of Inductive Constructions)
- Curry-Howard correspondence: proofs as programs
- Metaprogramming via tactics and elaboration
- Mathematical library (Mathlib): 1M+ lines
- Interactive theorem proving

**Learnability:**
- **Very high barrier**: Type theory, tactics, proof engineering
- Steep learning curve but excellent documentation (Theorem Proving in Lean 4)
- Active community (Zulip, Lean Together conferences)
- Natural Number Game teaches basics interactively

**LLM-Friendliness:**
- AlphaProof: RL system for Lean theorem proving (IMO silver medal)
- LeanDojo: Benchmark for theorem proving with LLMs
- **Challenge**: Proof search space enormous
- **Pattern**: RL + LLMs for tactic generation; Lean kernel verifies

**Key Characteristics (from cslib):**
```lean
-- Simply-typed lambda calculus typing derivation
inductive Typing : Context Var (Ty Base) → Term Var → Ty Base → Prop
  | var : Γ✓ → ⟨x,σ⟩ ∈ Γ → Typing Γ (fvar x) σ
  | abs (L : Finset Var) :
      (∀ x ∉ L, Typing (⟨x,σ⟩ :: Γ) (t ^ fvar x) τ) →
      Typing Γ t.abs (σ ⤳ τ)
  | app : Typing Γ t (σ ⤳ τ) → Typing Γ t' σ → Typing Γ (app t t') τ

-- Classical Linear Logic propositions
inductive Proposition (Atom : Type u) : Type u where
  | atom (x : Atom)
  | atomDual (x : Atom)
  | one | zero | top | bot
  | tensor (a b : Proposition Atom)  -- ⊗
  | parr (a b : Proposition Atom)     -- ⅋
  | oplus (a b : Proposition Atom)    -- ⊕
  | with (a b : Proposition Atom)     -- &
  | bang (a : Proposition Atom)       -- !
  | quest (a : Proposition Atom)      -- ʔ
```

**cslib Examples (from ../../cslib/):**
- **Lambda calculus**: Locally nameless representation, type safety proofs
- **Automata theory**: DFA, NFA, epsilon-NFA with conversion proofs
- **Linear logic**: Classical linear logic with cut elimination
- **Process calculi**: CCS (Calculus of Communicating Systems) with bisimulation
- **LTS**: Labeled transition systems with multi-step transitions

**Production Systems:**
- Lean 4 compiler itself formally verified
- Mathlib: Comprehensive mathematical library
- Integration with AWS Zelkova (access control verification)

**Tradeoffs:**
- ✓ Absolute correctness guarantees (kernel verification)
- ✓ Rich mathematical library
- ✓ Metaprogramming powerful
- ✗ Extremely steep learning curve
- ✗ Proof engineering labor-intensive
- ✗ Small fraction of programmers can use effectively

### 5.2 Coq

**Expressiveness:**
- Calculus of Inductive Constructions
- Tactics-based proof construction
- Extraction to OCaml/Haskell
- Extensive standard library
- Software Foundations textbook series

**Learnability:**
- **Very high barrier**: Similar to Lean
- Software Foundations excellent pedagogical resource
- Tactics provide incremental proof construction
- Large ecosystem but aging infrastructure

**LLM-Friendliness:**
- CoqGym: Benchmark for Coq theorem proving
- RL approaches show promise
- Tactic generation main LLM application

**Tradeoffs:**
- ✓ Mature ecosystem (CompCert verified C compiler)
- ✓ Extraction to executable code
- ✓ Extensive textbooks/tutorials
- ✗ Aging infrastructure vs Lean 4
- ✗ Smaller active community growth
- ✗ Tactic language less principled than Lean 4

### 5.3 Isabelle/HOL

**Expressiveness:**
- Higher-order logic
- Sledgehammer: Automated proof search
- Archive of Formal Proofs: 700+ entries
- Code generation to ML/Haskell/Scala

**Learnability:**
- **Very high barrier**: Similar to Coq/Lean
- Sledgehammer reduces proof burden (automatic tactics)
- Isar structured proof language more readable

**LLM-Friendliness:**
- Sledgehammer integration could aid LLM-generated proofs
- Smaller LLM research focus than Lean/Coq

**Tradeoffs:**
- ✓ Sledgehammer automation
- ✓ Archive of Formal Proofs extensive
- ✓ Isar readability
- ✗ Smaller community than Lean/Coq
- ✗ HOL less expressive than dependent types

## Category 6: Temporal/Modal Logic DSLs

### 6.1 Linear Temporal Logic (LTL)

**Expressiveness:**
- Temporal operators: □ (always), ◇ (eventually), ○ (next), U (until)
- Linear time semantics
- Model checking decidable (PSPACE-complete)
- Natural specification of safety/liveness properties

**Learnability:**
- **Moderate barrier**: Temporal operators intuitive but subtle
- "Always eventually" vs "eventually always" confusing initially
- Graphical timeline representations aid understanding
- SPIN model checker provides tooling

**LLM-Friendliness:**
- TempGraph-LLM: Teaches LLMs to translate to temporal graphs
- LLMs struggle with temporal reasoning (13.5+ F1 gap on TempTabQA)
- **Duration calculations**: 13-16% accuracy (abysmal)
- **Pattern**: LLMs extract constraints; symbolic reasoners verify

**Key Characteristics:**
```ltl
□(request → ◇grant)        -- Every request eventually granted
□◇critical → □◇¬critical   -- Infinitely often in/out critical section
```

**Tradeoffs:**
- ✓ Natural safety/liveness specification
- ✓ Model checking well-developed
- ✓ Decidable verification
- ✗ Exponential state explosion
- ✗ Linear time only (no branching)

### 6.2 Computation Tree Logic (CTL)

**Expressiveness:**
- Branching time semantics
- Path quantifiers: A (all paths), E (exists path)
- Combined with temporal operators: AG, EF, AF, EG
- Different expressiveness than LTL (incomparable)

**Learnability:**
- **Moderate-high barrier**: Branching vs linear time conceptually harder
- Path quantification adds complexity
- Model checking algorithms well-studied

**LLM-Friendliness:**
- Limited LLM research
- Branching semantics challenging for LLMs

**Tradeoffs:**
- ✓ Expresses branching properties
- ✓ Model checking polynomial in formula size
- ✗ Incomparable to LTL (neither subsumes)
- ✗ More complex than LTL

### 6.3 Allen's Interval Algebra

**Expressiveness:**
- 13 basic relations between intervals: before, after, meets, during, overlaps, etc.
- Composition table for transitive reasoning
- Qualitative temporal reasoning (no numeric timestamps)
- 18 maximal tractable subalgebras identified (Krokhin et al. 2003)
- Horn subalgebra: Polynomial-time via path consistency

**Learnability:**
- **Low-moderate barrier**: Intuitive interval relations
- Qualitative reasoning matches human cognition
- Composition table requires study
- Tractability results enable efficient reasoning

**LLM-Friendliness:**
- ChronoSense benchmark: LLMs handle Allen relations **inconsistently**
- Even symmetrical relations applied incorrectly
- **Fundamental limitation**: LLMs don't reliably apply formal temporal logic
- **Pattern**: Symbolic reasoners (GQR, SparQ) handle Allen algebra; LLMs extract relations

**Key Characteristics:**
```
A before B: AAAA    BBBB
A meets B:  AAAABBBB
A overlaps B: AAAA
                BBBB
A during B:    AA
              BBBBBB
```

**Tractability:**
- General satisfaction: NP-complete
- Horn subalgebra: Polynomial-time (contains all 13 relations)
- Path consistency algorithms enable efficient reasoning

**Production Systems:**
- GQR (General Qualitative Reasoner)
- SparQ
- ASP(DL) encoding: Extends ASP with difference constraints
- OWL-Time: Time Ontology in OWL-2 DL

**Tradeoffs:**
- ✓ Qualitative (no precise timestamps needed)
- ✓ Matches human temporal cognition
- ✓ Polynomial-time for tractable subsets
- ✗ NP-complete in general case
- ✗ LLMs struggle with consistent application

## Category 7: Probabilistic DSLs

### 7.1 ProbLog

**Expressiveness:**
- Extends Prolog with probabilistic facts (:: operator)
- Distributional clauses for flexible probabilities
- Annotated disjunctions (exclusive choices)
- Knowledge compilation for exact inference
- Integration with Python/Java

**Learnability:**
- **Moderate barrier**: Prolog + probability theory
- Probabilistic facts intuitive extension
- Inference algorithms transparent
- Good documentation and tutorials

**LLM-Friendliness:**
- P-ASP scaffolds provide constraints on LLM outputs
- Probabilistic reasoning complements neural uncertainty
- **Pattern**: LLMs generate probabilistic programs; ProbLog infers

**Key Characteristics:**
```problog
0.7::bird(tweety).
0.9::bird(X) => flies(X).

% Query: probability of flies(tweety)?
% Result: 0.63 (0.7 * 0.9)
```

**Unique Features:**
- **Tabling/memoization**: Everything cached for speedup
- **Flexible probabilities**: Arithmetic expressions computed dynamically
- **No cuts**: Pure logic interpretation required for probabilistic semantics
- **Counterfactual reasoning**: Well-written programs uniquely determined by counterfactuals

**Tradeoffs:**
- ✓ Probabilistic reasoning + logic programming
- ✓ Exact inference via knowledge compilation
- ✓ Python/Java integration
- ✗ No cut operator (breaks probabilistic semantics)
- ✗ Restricted compared to full Prolog

### 7.2 Distributional Clauses

**Expressiveness:**
- Continuous probability distributions
- Sampling-based inference
- Integration with statistical models
- Flexible probabilistic modeling

**Learnability:**
- **Higher barrier**: Requires probability theory + sampling methods
- Continuous distributions more complex than discrete

**LLM-Friendliness:**
- Neural-symbolic integration natural fit
- Continuous distributions complement neural outputs

**Tradeoffs:**
- ✓ Continuous probability modeling
- ✓ Flexible distributions
- ✗ Inference often approximate
- ✗ Higher computational cost

## Cross-Category Comparison Matrix

| Category | Expressiveness | Learnability | LLM Pass@1 | Explanation Quality | Production Maturity |
|----------|---------------|--------------|------------|---------------------|---------------------|
| Prolog | High (recursion, unification) | Medium-High | 74% (GPT-4o) | Excellent (SLD trees) | Very High (500+ unis) |
| ASP | High (non-monotonic) | Medium | Good (LLASP) | Excellent (s(CASP)) | High (competitions) |
| Datalog | Medium (restricted) | Low | Very Good | Good (provenance) | High (databases) |
| SMT-LIB | Very High (theories) | Medium | Good (PoT: 40% error↓) | Poor (UNSAT cores) | Very High (Z3 dominance) |
| PDDL | High (planning) | Medium | Very Good (GPT-4) | Medium | High (IPC) |
| MiniZinc | High (constraints) | Medium | Good (fine-tuned) | Medium | High (annual challenge) |
| Essence | Very High (abstract) | High | Unknown (limited data) | Medium | Medium (smaller community) |
| Lean 4 | Extreme (dependent types) | Very High | Medium (AlphaProof) | Excellent (proofs=programs) | Medium (growing fast) |
| LTL | Medium (temporal) | Medium | Poor (TempGraph-LLM) | Good (model checking) | High (SPIN) |
| Allen's IA | Medium (qualitative) | Low-Medium | Poor (ChronoSense) | Excellent (intuitive) | Medium (GQR, SparQ) |
| ProbLog | High (probabilistic logic) | Medium | Unknown (limited data) | Good (counterfactuals) | Medium |

## Key Findings for LLM Integration

### 1. Specialized Training >> General Scale
- LLASP (fine-tuned lightweight): Dramatically outperforms larger non-fine-tuned LLMs
- ConstraintLLM (QLoRA on 3× RTX A6000): Competitive with GPT-4o and Deepseek-V3-685B
- **Implication**: Domain-specific fine-tuning more cost-effective than massive general models

### 2. Hybrid Architectures Dominant
- AlphaGeometry 2: 83% IMO geometry (Gemini + symbolic deduction 200× faster)
- TReMu: 160% improvement (LLM memorization + neuro-symbolic reasoning)
- CRONKGQA: 120% improvement (transformers + temporal KG embeddings)
- **Pattern**: LLMs for NL understanding; symbolic for verified reasoning

### 3. Explanation Quality Drives Adoption
- Logic programming: Automatic justification trees (s(CASP), xASP)
- SMT: UNSAT cores minimal but cryptic
- Proof assistants: Proofs as documentation
- **Critical**: Domain experts need domain-term explanations

### 4. Temporal Reasoning Fundamental Gap
- LLMs: 13.5+ F1 lag on TempTabQA, 13-16% duration accuracy
- Graph structure impacts performance: 37-point swings (ToT-Semantic)
- **Solution**: LLM extraction + symbolic temporal reasoning (Allen's, STN/STNU)

### 5. Constrained Generation > Fine-Tuning (Often)
- JSON Schema + logit masking eliminates syntax errors
- OpenAI structured outputs + Outlines framework
- Grammar prompting with BNF enables few-shot DSL generation
- **Tradeoff**: More reliable and cheaper than fine-tuning for many DSLs

## Recommendations for DSL Design (LLM Integration)

### For New DSLs:

1. **Declarative > Procedural**: LLMs generate specifications better than imperative code
2. **Self-documenting**: Embed natural language annotations (like s(CASP) #pred)
3. **Compositional**: Small building blocks compose better than monolithic constructs
4. **Explainable**: Design for explanation generation (provenance, justification trees)
5. **Formally verifiable**: Separate LLM generation from symbolic verification

### For Choosing Existing DSLs:

**Use Logic Programming (Prolog/ASP) when:**
- Human explanations required
- Domain-native reasoning needed
- Recursive definitions central
- Auditability/transparency critical
- Pass@1: 74% (Prolog), Very Good (ASP with fine-tuning)

**Use SMT (SMT-LIB/Z3py) when:**
- Large-scale quantifier-free verification
- Rich theory reasoning (bit-vectors, arrays)
- Automated verification (no human interpretation)
- Performance critical (10,000+ constraints)
- Pass@1: Good (Proof of Thought: 40% error reduction)

**Use Constraint Programming (MiniZinc/Essence) when:**
- Combinatorial optimization central
- Solver-independent modeling desired
- Global constraints available (alldifferent, cumulative)
- Mathematical notation preferred
- Pass@1: Good with fine-tuning

**Use Planning DSLs (PDDL/STRIPS) when:**
- Sequential action planning
- Temporal reasoning over actions
- Domain-independent planning
- Robotics/autonomous systems
- Pass@1: Very Good (GPT-4 "surprisingly powerful")

**Use Proof Assistants (Lean/Coq) when:**
- Absolute correctness required
- Mathematical proofs needed
- Software verification critical
- Long-term investment feasible
- Pass@1: Medium (AlphaProof RL-based, not pure LLM)

## Future Research Directions

1. **Standardized LLM-Symbolic Interfaces**: Universal intermediate representation beyond ad-hoc JSON DSLs
2. **Provenance-Aware Architectures**: Track derivations through NL→DSL→solving→explanation pipeline
3. **Temporal Reasoning Integration**: Hybrid LLM extraction + Allen's algebra + STN/STNU solvers
4. **Interactive Explanation Refinement**: Learn optimal explanations from user feedback
5. **Certified Explanation Generation**: Formal verification that explanations are faithful

## References

See `./references_dsl.md` for comprehensive bibliography.
