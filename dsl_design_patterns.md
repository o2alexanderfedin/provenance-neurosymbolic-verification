# DSL Design Patterns for LLM Integration

## Executive Summary

This document identifies 15 core design patterns for integrating domain-specific languages (DSLs) with large language models (LLMs), based on analysis of 35+ deployed neuro-symbolic systems (2020-2025), production DSL-LLM frameworks, and formal verification research. The patterns span architecture (Neural[Symbolic], Symbolic[Neural]), generation (grammar prompting, constrained generation), verification (proof-carrying code, provenance tracking), and explanation (justification trees, counterfactual reasoning). **The unifying principle**: LLMs should parse and generate; symbolic systems should compute and verify.

## Pattern Categories

1. **Architectural Patterns** (3): How to structure LLM-DSL integration
2. **Generation Patterns** (4): How LLMs produce valid DSL code
3. **Verification Patterns** (3): How to ensure correctness
4. **Explanation Patterns** (3): How to make reasoning transparent
5. **Optimization Patterns** (2): How to improve performance

---

## ARCHITECTURAL PATTERNS

### Pattern 1: Neural[Symbolic] - LLM Orchestrator

**Intent**: LLM controls workflow, invoking symbolic reasoners as tools.

**Motivation**: Complex tasks require multiple reasoning steps with different symbolic systems. LLM provides planning and coordination; symbolic systems provide verified computation.

**Structure**:
```
User Query (NL)
    ↓
LLM Parser/Planner
    ↓
LLM generates DSL code/query
    ↓
Symbolic Solver (Prolog/ASP/SMT/PDDL)
    ↓
Results returned to LLM
    ↓
LLM formats response (NL)
    ↓
User receives explanation
```

**Examples**:

1. **Proof of Thought (Math Reasoning)**:
   - LLM translates word problem → JSON DSL (logical constructs)
   - Z3 SMT solver verifies constraints
   - Result: 40% error reduction on mathematical reasoning

2. **CLMASP (Robotic Planning)**:
   - LLM generates skeleton plan (high-level actions)
   - ASP refines with constraint solving
   - Result: 90%+ execution rates

3. **Logic.py (ZebraLogicBench)**:
   - LLM formalizes puzzle in domain-specific language
   - Constraint solver finds solution
   - Result: 65% absolute improvement over baseline

**Implementation**:
```python
class NeuralSymbolic:
    def solve(self, query: str) -> str:
        # LLM parses natural language
        dsl_code = self.llm.generate_dsl(query)

        # Symbolic solver computes
        result = self.symbolic_solver.solve(dsl_code)

        # LLM formats explanation
        explanation = self.llm.explain(result, query)

        return explanation
```

**Tradeoffs**:
- ✓ LLM flexibility for complex workflows
- ✓ Symbolic correctness guarantees
- ✓ Natural language interface
- ✗ LLM errors propagate to solver
- ✗ Higher latency (multiple LLM calls)

**When to Use**:
- Multi-step reasoning required
- Domain requires planning + verification
- Natural language input/output critical
- User workflow exploratory

---

### Pattern 2: Symbolic[Neural] - Symbolic Orchestrator

**Intent**: Symbolic system controls workflow, invoking LLM for specific subtasks.

**Motivation**: Symbolic reasoning provides structure and guarantees; LLM fills gaps where symbolic methods struggle (NL understanding, auxiliary constructs).

**Structure**:
```
Formal Specification (DSL)
    ↓
Symbolic Reasoner (primary)
    ↓
Gaps identified (missing axioms, constructs)
    ↓
LLM generates auxiliary content
    ↓
Symbolic Reasoner verifies/integrates
    ↓
Proof/Solution (formal)
```

**Examples**:

1. **AlphaGeometry 2 (IMO Geometry)**:
   - Symbolic deduction engine (primary, 200× faster than v1)
   - Gemini generates auxiliary constructs when needed
   - Result: 83% on 25-year IMO geometry history (vs 53% v1)

2. **AlphaProof (IMO Algebra/Number Theory)**:
   - Lean 4 kernel (verification)
   - RL-trained LLM generates tactics
   - Result: IMO silver medal level (first AI)

3. **Sledgehammer + LLM (Isabelle)**:
   - Sledgehammer automatic proof search (primary)
   - LLM suggests proof strategies when stuck
   - Integration under research

**Implementation**:
```lean
-- Symbolic primary, LLM auxiliary
structure GeometrySolver where
  symbolic_engine : SymbolicDeduction
  llm_auxiliary : LLMConstructGenerator

  def solve (problem : GeometryProblem) : Proof :=
    loop
      match symbolic_engine.attempt_proof problem with
      | success proof => return proof
      | stuck state =>
          let construct := llm_auxiliary.generate state
          let extended_problem := problem.add construct
          continue with extended_problem
```

**Tradeoffs**:
- ✓ Symbolic correctness maintained (kernel verification)
- ✓ LLM augments rather than replaces reasoning
- ✓ Formal guarantees preserved
- ✗ Requires sophisticated symbolic system
- ✗ LLM integration points must be carefully designed

**When to Use**:
- Formal correctness non-negotiable
- Symbolic reasoning primary task
- LLM assists with creativity/heuristics
- Safety-critical applications (verified kernel)

---

### Pattern 3: Dual-Track - Parallel LLM + Symbolic

**Intent**: Run LLM and symbolic approaches in parallel, combine results.

**Motivation**: LLM and symbolic approaches have complementary strengths. Parallel execution provides redundancy and cross-validation.

**Structure**:
```
Input Problem
    ├→ LLM Track (statistical reasoning)
    └→ Symbolic Track (formal reasoning)
         ↓                  ↓
    LLM Solution      Symbolic Solution
         ↓                  ↓
         └──── Combiner ────┘
                  ↓
         Validated Result
```

**Examples**:

1. **TReMu Framework (Temporal Reasoning)**:
   - Track 1: LLM memorization via timeline summarization
   - Track 2: Neuro-symbolic Python code generation
   - Result: GPT-4o improves from 29.83 → 77.67 (160% improvement)

2. **ASP Competition + LLM**:
   - Track 1: Traditional ASP solver (CLASP)
   - Track 2: LLM-generated candidate solutions
   - Combine: Solver verification + LLM exploration

**Implementation**:
```python
class DualTrack:
    def solve(self, problem: Problem) -> Solution:
        # Parallel tracks
        llm_future = asyncio.create_task(
            self.llm.solve(problem)
        )
        symbolic_future = asyncio.create_task(
            self.symbolic.solve(problem)
        )

        # Await both
        llm_solution, symbolic_solution = await asyncio.gather(
            llm_future, symbolic_future
        )

        # Validate and combine
        if symbolic_solution.verified:
            return symbolic_solution
        elif llm_solution.plausible and can_verify(llm_solution):
            return verify_and_return(llm_solution)
        else:
            return merge_insights(llm_solution, symbolic_solution)
```

**Tradeoffs**:
- ✓ Redundancy improves robustness
- ✓ Complementary strengths leveraged
- ✓ Cross-validation detects errors
- ✗ Higher computational cost (parallel execution)
- ✗ Combining strategies complex

**When to Use**:
- Reliability critical (redundancy valuable)
- Computational budget allows parallelism
- LLM and symbolic have comparable performance
- Cross-validation provides confidence

---

## GENERATION PATTERNS

### Pattern 4: Grammar Prompting

**Intent**: Provide LLM with BNF grammar during in-context learning to constrain generation.

**Motivation**: LLMs struggle with structured languages without syntactic guidance. Grammars provide explicit constraints during generation.

**Structure**:
```
Task Description
    +
BNF Grammar (minimal subset for this task)
    +
Few-shot Examples (each with its grammar)
    ↓
LLM predicts target grammar
    ↓
LLM generates output conforming to grammar
```

**Examples**:

1. **Wang et al. (Semantic Parsing, PDDL, SMILES)**:
   - Augment each demo with specialized grammar (minimal sufficient subset)
   - LLM predicts BNF grammar for test input
   - LLM generates output using predicted grammar
   - Result: Competitive performance across SMCalFlow, Overnight, GeoQuery, PDDL

2. **PDDL Name Grounding**:
   - Grammar includes valid object/action names
   - LLM generates syntactically and semantically valid PDDL
   - Critical for GPT-4 planning success

**Implementation**:
```python
# Grammar prompting example
grammar_prompt = """
Generate PDDL action using this grammar:

<action> ::= "(:action" <name> <parameters> <precondition> <effect> ")"
<parameters> ::= ":parameters" "(" <typed-list> ")"
<precondition> ::= ":precondition" <formula>
<effect> ::= ":effect" <formula>

Example with grammar:
<typed-list> ::= "?obj - object" | "?from ?to - location"

(:action move
  :parameters (?obj - object ?from ?to - location)
  :precondition (and (at ?obj ?from) (clear ?to))
  :effect (and (at ?obj ?to) (not (at ?obj ?from))))

Now generate action for: {task_description}
Using grammar: {task_specific_grammar}
"""
```

**Tradeoffs**:
- ✓ Improved generation quality
- ✓ Syntax errors reduced
- ✓ No fine-tuning required
- ✗ Grammar must be specified
- ✗ Longer prompts (context window)
- ✗ LLM may ignore grammar constraints

**When to Use**:
- DSL has formal grammar
- Few-shot learning approach
- Syntax errors problematic
- Fine-tuning resources unavailable

---

### Pattern 5: Constrained Generation

**Intent**: Use logit masking or structured output to guarantee syntactic validity.

**Motivation**: Grammar prompting suggests constraints; constrained generation enforces them. Eliminates syntax errors entirely.

**Structure**:
```
DSL Grammar (CFG or JSON Schema)
    ↓
Parser (earley/LR)
    ↓
Valid next-token set computation
    ↓
LLM token generation with logit masking
    ↓
Guaranteed valid output
```

**Examples**:

1. **Outlines (Open-Source Framework)**:
   - Context-free grammar → regex → finite state machine
   - Logit masking ensures only valid tokens sampled
   - Supports JSON Schema, regex, custom grammars

2. **OpenAI Structured Outputs**:
   - JSON Schema specification
   - Internal constrained decoding
   - Guaranteed schema conformance

3. **GenCP (Constrained Text Generation)**:
   - LLM predicts domain
   - Constraint programming search enforces constraints
   - Result: Faster than Beam Search, 100% constraint satisfaction

**Implementation**:
```python
from outlines import models, generate

# Define JSON Schema for DSL
schema = {
    "type": "object",
    "properties": {
        "action": {"type": "string", "enum": ["move", "pickup", "putdown"]},
        "parameters": {
            "type": "array",
            "items": {"type": "string"}
        },
        "preconditions": {
            "type": "array",
            "items": {"$ref": "#/definitions/formula"}
        }
    },
    "required": ["action", "parameters"],
    "definitions": {
        "formula": {
            "type": "object",
            "properties": {
                "predicate": {"type": "string"},
                "args": {"type": "array"}
            }
        }
    }
}

model = models.transformers("gpt-4")
generator = generate.json(model, schema)
result = generator(prompt)  # Guaranteed to conform to schema
```

**Tradeoffs**:
- ✓ **Zero syntax errors** (guaranteed valid)
- ✓ No grammar in prompt (shorter context)
- ✓ More reliable than prompting alone
- ✗ Requires CFG or JSON Schema
- ✗ Framework-dependent (Outlines, OpenAI, etc.)
- ✗ May restrict semantic diversity

**When to Use**:
- Syntax errors unacceptable
- DSL has formal grammar/schema
- Framework support available (Outlines/OpenAI)
- Reliability > flexibility

---

### Pattern 6: Fine-Tuning on DSL Corpus

**Intent**: Specialize LLM for DSL generation through domain-specific training.

**Motivation**: General-purpose LLMs lack training on specialized DSLs. Fine-tuning provides DSL-specific patterns and conventions.

**Structure**:
```
Base LLM (GPT, Llama, CodeLlama)
    +
DSL Corpus (code examples, NL-DSL pairs)
    ↓
Fine-tuning (LoRA, QLoRA, full)
    ↓
Specialized DSL Generator
```

**Examples**:

1. **LLASP (ASP Generation)**:
   - Fine-tuned on fundamental ASP patterns
   - Lightweight model dramatically outperforms larger non-fine-tuned LLMs
   - **Key finding**: Specialized training >> general scale
   - Publicly available dataset + code

2. **ConstraintLLM (Industrial Constraint Programming)**:
   - Fine-tuned Qwen2.5-Coder-32B-Instruct
   - QLoRA on 3× NVIDIA RTX A6000 GPUs (cost-effective)
   - Result: Competitive with GPT-4o and Deepseek-V3-685B

3. **DSL-Xpert (Generic DSL Generation)**:
   - Multi-phase fine-tuning on DSL vocabulary
   - Handles unpublished/less-known DSLs
   - Result: Reliable domain-specific code generation

**Implementation**:
```python
from transformers import AutoModelForCausalLM, TrainingArguments
from peft import LoraConfig, get_peft_model

# Load base model
model = AutoModelForCausalLM.from_pretrained("codellama/CodeLlama-7b")

# LoRA config (efficient fine-tuning)
lora_config = LoraConfig(
    r=16,  # rank
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    task_type="CAUSAL_LM"
)

# Apply LoRA
model = get_peft_model(model, lora_config)

# Fine-tune on DSL corpus
training_args = TrainingArguments(
    output_dir="./asp-fine-tuned",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    learning_rate=2e-4
)

# Train with (natural_language, dsl_code) pairs
trainer.train()
```

**Tradeoffs**:
- ✓ **Dramatic quality improvements** (LLASP)
- ✓ Specialized patterns learned
- ✓ Cost-effective with LoRA/QLoRA
- ✗ Requires curated training data
- ✗ Training infrastructure needed
- ✗ Overfitting risk on small corpora

**When to Use**:
- Sufficient DSL corpus available (1000+ examples)
- DSL poorly represented in pre-training
- Quality requirements high
- Training resources available (3+ GPUs)
- Ongoing deployment justifies investment

---

### Pattern 7: Predicate Extraction + External Interpreter

**Intent**: LLM extracts logical predicates from natural language; external interpreter handles computation.

**Motivation**: LLMs excel at semantic parsing but struggle with precise logical reasoning. Separation of concerns leverages strengths.

**Structure**:
```
Natural Language Problem
    ↓
LLM extracts predicates/facts
    ↓
Generate DSL code (Prolog/Datalog)
    ↓
External Interpreter executes
    ↓
Deterministic Result
```

**Examples**:

1. **Yang et al. (Prolog Generation)**:
   - LLM extracts predicates from word problems
   - External Prolog interpreter executes
   - Result: Outperforms Chain-of-Thought across Llama2, CodeLlama, Mistral
   - GSM8K-Prolog dataset with predicate permutation augmentation

2. **DeepSeek-V3 (Financial Reasoning)**:
   - Generates Prolog code from financial questions
   - External interpreter evaluates
   - Result: 80% accuracy (vs 63-76% foundation models pure CoT)

3. **ProSynth (Datalog Synthesis)**:
   - Why/why-not provenance guides predicate extraction
   - 10× speedup over baseline on 40 synthesis tasks
   - Learned constraints from provenance information

**Implementation**:
```python
class PredicateExtraction:
    def solve(self, nl_problem: str) -> Result:
        # LLM extracts predicates
        predicates = self.llm.extract_predicates(nl_problem)

        # Generate Prolog code
        prolog_code = self.llm.generate_prolog(predicates, nl_problem)

        # External interpreter executes
        result = self.prolog_interpreter.query(prolog_code)

        return result

# Example: Financial reasoning
nl_problem = "If revenue increased 20% from $100M, what is new revenue?"

# LLM extraction:
predicates = [
    "revenue(old, 100000000)",
    "increase_percent(20)",
    "new_revenue(New) :- revenue(old, Old), increase_percent(P),
                         New is Old * (1 + P/100)"
]

# Prolog interpreter executes deterministically
result = query("new_revenue(X)")  # X = 120000000
```

**Tradeoffs**:
- ✓ **Deterministic computation** (no LLM arithmetic errors)
- ✓ Explainable reasoning (Prolog trace)
- ✓ LLM focuses on semantic understanding
- ✗ Requires external interpreter integration
- ✗ LLM predicate extraction errors propagate
- ✗ Limited to domains expressible in logic

**When to Use**:
- Logical reasoning central
- Arithmetic/computation required
- Explainability important
- Deterministic results required
- External interpreter available (Prolog/Datalog)

---

## VERIFICATION PATTERNS

### Pattern 8: Generate-Validate-Iterate Loop

**Intent**: LLM generates candidates; symbolic verifier checks correctness; iterate with feedback.

**Motivation**: LLM generation unreliable; symbolic verification catches errors; feedback improves subsequent attempts.

**Structure**:
```
LLM generates DSL code (candidate)
    ↓
Symbolic Verifier checks correctness
    ↓
If valid: Return solution
    ↓
If invalid: Error feedback to LLM
    ↓
LLM generates revised candidate
    ↓
Repeat until valid or max iterations
```

**Examples**:

1. **Automated Debugging (PDDL Planning)**:
   - GPT-4 generates PDDL domain/problem
   - Validate against training tasks
   - Feedback loops improve quality
   - **Critical factor** for success (identified in ablation studies)

2. **ConstraintLLM (MiniZinc)**:
   - LLM generates constraint model
   - MiniZinc solver validates
   - Iterative refinement with error messages
   - Result: State-of-the-art on industrial benchmarks

3. **Automatic Constraint Model Generator**:
   - Semantic entity extraction
   - Constraint model generation with fine-tuned LLM
   - Iterative validation using solver feedback

**Implementation**:
```python
class GenerateValidateIterate:
    def solve(self, problem: str, max_iter: int = 5) -> DSLCode:
        for i in range(max_iter):
            # Generate candidate
            candidate = self.llm.generate(problem, history=self.feedback_history)

            # Validate
            validation_result = self.verifier.validate(candidate)

            if validation_result.valid:
                return candidate

            # Add feedback for next iteration
            self.feedback_history.append({
                'attempt': i,
                'code': candidate,
                'error': validation_result.error_message
            })

        raise ValidationError(f"Failed after {max_iter} attempts")

# Example: PDDL validation
verifier = PDDLValidator(training_tasks)
generator = GPT4Generator()

attempt_1 = generator.generate("Move block A onto B")
# Error: "Action 'move' has ungrounded parameter '?x'"

attempt_2 = generator.generate(
    "Move block A onto B",
    feedback="Previous error: Ungrounded parameter. Fix: Ensure all parameters typed."
)
# Success: Valid PDDL with typed parameters
```

**Tradeoffs**:
- ✓ **Iterative improvement** (errors → learning)
- ✓ Symbolic verification guarantees correctness
- ✓ Feedback improves LLM over iterations
- ✗ Multiple LLM calls (latency, cost)
- ✗ May not converge within iteration limit
- ✗ Verifier must provide actionable feedback

**When to Use**:
- Fast symbolic verifier available
- LLM first-attempt success rate moderate (30-70%)
- Latency budget allows iteration (3-5 attempts)
- Verifier provides clear error messages
- Correctness non-negotiable

---

### Pattern 9: Proof-Carrying Code

**Intent**: LLM generates DSL code + proof of correctness; kernel verifies proof independently.

**Motivation**: Trust LLM output by verification, not generation. Proof carries correctness guarantee.

**Structure**:
```
LLM generates:
  1. DSL Code (program)
  2. Proof (correctness certificate)
    ↓
Small Trusted Kernel verifies proof
    ↓
If proof valid: Accept code (guaranteed correct)
    ↓
If proof invalid: Reject (regardless of code quality)
```

**Examples**:

1. **AlphaProof (Lean 4 Theorem Proving)**:
   - RL-trained LLM generates Lean tactics (proofs)
   - Lean kernel verifies independently
   - Result: IMO silver medal (first AI)
   - **Critical**: Kernel verification ensures soundness

2. **Lean 4 Compiler**:
   - Tactics generate proofs (LLM or human)
   - Kernel checks proof terms
   - Soundness guaranteed by small verified kernel

3. **CompCert (Coq-verified C Compiler)**:
   - Compilation phases proved correct in Coq
   - Extracted code carries correctness guarantees
   - Bugs only possible in kernel (auditable)

**Implementation**:
```lean
-- LLM generates proof tactics
def llm_generated_proof (n : Nat) : n + 0 = n := by
  induction n with
  | zero => rfl
  | succ n ih =>
      simp [Nat.add_succ]
      exact congrArg Nat.succ ih

-- Lean kernel verifies proof independently
-- If verified: Proof accepted, theorem established
-- If rejected: Error, theorem unproven

-- Kernel is small (~10K LOC) and auditable
-- All soundness rests on kernel correctness
```

**Tradeoffs**:
- ✓ **Absolute correctness** (kernel verification)
- ✓ LLM errors caught (invalid proofs rejected)
- ✓ Small trusted computing base (TCB)
- ✗ Requires proof-capable language (Lean/Coq)
- ✗ LLM must generate valid proofs (hard)
- ✗ Not applicable to non-theorem-proving DSLs

**When to Use**:
- Correctness absolutely critical (safety-critical systems)
- Theorem proving or formal verification domain
- Proof assistant infrastructure available (Lean/Coq/Isabelle)
- Long-term investment justified
- Experts available for proof engineering

---

### Pattern 10: Provenance Tracking

**Intent**: Track derivation of every result through computation pipeline; provide formal explanation guarantees.

**Motivation**: Explanations should be provably correct, not ad-hoc. Provenance semirings provide algebraic foundations.

**Structure**:
```
Input Data (annotated with provenance)
    ↓
Computation (semiring operations preserve provenance)
    ↓
Output (annotated with derivation polynomial)
    ↓
Provenance Polynomial → Multiple Analyses:
  - Why-provenance (minimal witnesses)
  - How-provenance (derivation structure)
  - Lineage (data flow)
  - Counterfactuals (what-if)
```

**Examples**:

1. **ProvSQL (PostgreSQL Extension)**:
   - Semiring provenance for SQL queries
   - Provenance circuits for efficiency
   - Result: Competitive performance with formal guarantees
   - Recent additions: UPDATE provenance, temporal databases, undo operations

2. **ProSynth (Datalog Synthesis)**:
   - Why/why-not provenance from solver
   - Guides program synthesis with learned constraints
   - Result: 10× speedup over baseline

3. **Rückschloß & Weitkämper (ProbLog Counterfactuals)**:
   - Counterfactual reasoning reveals program structure
   - Well-written programs uniquely determined by counterfactuals
   - Reconstruction procedures recover programs from counterfactual outputs

**Implementation**:
```sql
-- ProvSQL example
CREATE TABLE employee (
    id INT PRIMARY KEY,
    name TEXT,
    salary INT
);

-- Enable provenance tracking
SELECT create_provenance_mapping('employee', 'id');

-- Query with provenance
SELECT provenance(), name, salary
FROM employee
WHERE salary > 50000;

-- Result includes provenance polynomial showing:
-- - Which input tuples contributed
-- - How they were combined (semiring operations)
-- - Minimal witnesses (why-provenance)

-- Provenance polynomial example:
-- Result for "Alice" = e1 + e2 * e3
--   where e1 = base record
--         e2 * e3 = joined from related tables
```

**Semiring Framework**:
```haskell
-- Universal provenance semiring
data Prov a = Polynomial [Monomial a]
data Monomial a = Product [a]

-- Specializations:
type WhyProv a = Set (Set a)           -- Minimal witnesses
type HowProv a = Polynomial a          -- Full derivation
type Lineage a = Set a                 -- Contributing tuples
type Counting = Nat                    -- Derivation count

-- Key property: Compute once, evaluate many times
evaluate :: (a -> k) -> Prov a -> k
```

**Tradeoffs**:
- ✓ **Formal explanation guarantees** (algebraically sound)
- ✓ Multiple analyses from single computation
- ✓ Provenance compositional (semiring structure)
- ✗ Overhead for provenance tracking (10-30%)
- ✗ Requires semiring-compatible operations
- ✗ Negation handling complex (dual-indeterminate semirings)

**When to Use**:
- Explanation correctness critical (regulatory compliance)
- Multiple provenance analyses needed (why/how/lineage)
- Data pipeline complex (many transformations)
- Debugging/auditing important
- Database or Datalog foundation

---

## EXPLANATION PATTERNS

### Pattern 11: Justification Trees with Natural Language

**Intent**: Generate hierarchical proof structures automatically; embed natural language templates in DSL.

**Motivation**: Domain experts need explanations in domain terms, not solver internals. Automatic generation ensures explanations match computation.

**Structure**:
```
DSL Code (with #pred annotations)
    ↓
Query execution (s(CASP) interpreter)
    ↓
Justification Tree (hierarchical proof)
    +
Natural Language Templates (#pred)
    ↓
Explanation (text/HTML/JSON)
  - Controllable detail (--short/--mid/--long)
  - Interactive visualization
```

**Examples**:

1. **s(CASP) System**:
   - Top-down ASP interpreter with constraints
   - #pred annotations embed NL templates in code
   - Automatic justification tree generation
   - Result: Human-readable explanations for non-finitely groundable programs

```asp
#pred bird(X) :: '@(X) is a bird'.
#pred flies(X) :: '@(X) can fly'.
#pred penguin(X) :: '@(X) is a penguin'.

bird(tweety).
penguin(tweety).

% Rule with embedded explanation
flies(X) :- bird(X), not penguin(X).

% Query: ?- flies(tweety).
% Explanation (--mid):
% "Tweety is a bird. Tweety is a penguin.
%  Therefore, tweety cannot fly because penguins are an exception."
```

2. **xASP/xASP2 (Explanation Graphs)**:
   - Operates on non-ground programs (no simplification)
   - DAG-based explanation graphs
   - Minimal assumption sets (smallest fact sets needed)
   - Result: Syntax-insensitive explanations

3. **CrossJustice (Legal Reasoning)**:
   - Italian legal articles encoded in logic programs
   - Learns from court decisions
   - Generates explanations accessible to non-lawyers
   - Result: Production deployment in legal domain

**Implementation**:
```python
# s(CASP) integration
class JustificationTree:
    def __init__(self, program: ASPProgram):
        self.program = program
        self.pred_annotations = program.extract_pred_annotations()

    def query(self, goal: str, detail: str = '--mid') -> str:
        # Execute query
        result = scasp_interpreter.query(self.program, goal)

        # Generate justification tree
        tree = result.justification_tree()

        # Apply NL templates
        explanation = self.render_tree(tree, self.pred_annotations, detail)

        return explanation

    def render_tree(self, tree, annotations, detail):
        if detail == '--short':
            return tree.summary_with_templates(annotations)
        elif detail == '--mid':
            return tree.medium_detail_with_templates(annotations)
        else:  # --long
            return tree.full_trace_with_templates(annotations)
```

**Tradeoffs**:
- ✓ **Automatic explanation generation** (no manual specification)
- ✓ Domain-term explanations (#pred templates)
- ✓ Controllable detail levels
- ✓ Guaranteed correspondence to computation
- ✗ Requires embedded annotations (#pred)
- ✗ Template quality varies with annotation effort
- ✗ Limited to logic programming (ASP/Prolog)

**When to Use**:
- Logic programming foundation (ASP/Prolog)
- Domain experts need transparency
- Explanations required for all queries
- Regulatory compliance (explainability mandates)
- Non-technical stakeholders

---

### Pattern 12: Argumentation-Based Explanation

**Intent**: Generate explanations as dialectical arguments (claim, support, counterarguments, rebuttals).

**Motivation**: Many domains (legal, ethical, medical) reason through argumentation. Natural explanation structure matches domain practice.

**Structure**:
```
Logic Program (facts, rules)
    ↓
Argumentation Framework (abstract argumentation)
    ↓
Attack Relations (conflicts between arguments)
    ↓
Acceptability Semantics (grounded, preferred, stable)
    ↓
Argument Graph (visual explanation)
```

**Examples**:

1. **Arg2P (Logic Programming + Argumentation)**:
   - Seamless integration of LP and argumentation
   - Applications in CrossJustice Project
   - Italian legal reasoning with court decision learning
   - Result: Non-lawyer-accessible explanations

2. **tExplain (Information Extraction + Explanation)**:
   - ASP for extraction and justification
   - Automatic explanation generation
   - Human-readable rationales for extracted information

3. **DeLP (Defeasible Logic Programming)**:
   - Defeasible rules (can be overridden)
   - Dialectical trees show argument/counter-argument structure
   - Result: Natural modeling of legal reasoning

**Implementation**:
```prolog
% Defeasible Logic Programming (DeLP) example

% Strict rules (cannot be defeated)
bird(X) <- penguin(X).

% Defeasible rules (can be defeated, marked with -<)
flies(X) -< bird(X).
~flies(X) -< penguin(X).

% Facts
penguin(tweety).

% Query: flies(tweety)?
% Argument A1: tweety is a bird (strict), birds fly (defeasible)
% Argument A2: tweety is a penguin (strict), penguins don't fly (defeasible)
% A2 defeats A1 (more specific)
% Conclusion: ~flies(tweety) accepted

% Explanation as dialectical tree:
%   A1: flies(tweety)
%      <- bird(tweety), flies(X) -< bird(X)
%         |
%         | defeated by
%         ↓
%   A2: ~flies(tweety)
%      <- penguin(tweety), ~flies(X) -< penguin(X)
%         (more specific, no defeaters)
```

**Tradeoffs**:
- ✓ **Natural for argumentation domains** (legal, ethical)
- ✓ Handles conflicting information
- ✓ Visual argument graphs intuitive
- ✗ Argumentation semantics complex
- ✗ Limited to defeasible reasoning
- ✗ Smaller ecosystem than mainstream LP

**When to Use**:
- Legal or ethical reasoning
- Conflicting information common
- Defeasible rules natural (exceptions, defaults)
- Stakeholders familiar with argumentation
- Transparent conflict resolution needed

---

### Pattern 13: Temporal Graph Explanation

**Intent**: Represent temporal reasoning as explicit graph structure; enable visual and formal temporal analysis.

**Motivation**: Temporal relationships opaque in text/code. Graph representation enables validation, visualization, and formal reasoning.

**Structure**:
```
Natural Language (temporal expressions)
    ↓
LLM extracts temporal entities and relations
    ↓
Temporal Graph Construction
  Nodes: Events/time points
  Edges: Temporal relations (Allen's algebra, before/after)
    ↓
Symbolic Temporal Reasoning
  - Consistency checking
  - Constraint propagation
  - Timeline generation
    ↓
Visual/Textual Explanation
```

**Examples**:

1. **TempGraph-LLM Framework**:
   - TGQA synthetic datasets teach LLMs temporal graph translation
   - Chain-of-Thought reasoning augmented with graph structure
   - Result: More consistent than free text generation

2. **Narrative-of-Thought (Schema-11)**:
   - Converts events to Python classes
   - Generates temporally grounded narratives
   - Guides temporal graph generation
   - Result: Highest F1 on Schema-11 benchmark

3. **TReMu Timeline Summarization**:
   - Time-aware memorization via timeline summarization
   - Neuro-symbolic temporal reasoning via Python code
   - Result: GPT-4o 29.83 → 77.67 (160% improvement)

**Implementation**:
```python
class TemporalGraphExplanation:
    def explain(self, nl_text: str) -> TemporalGraph:
        # LLM extracts temporal events and relations
        events = self.llm.extract_events(nl_text)
        relations = self.llm.extract_temporal_relations(nl_text, events)

        # Build temporal graph
        graph = TemporalGraph()
        for event in events:
            graph.add_node(event)
        for rel in relations:
            graph.add_edge(rel.source, rel.target, rel.type)

        # Symbolic reasoning
        if not graph.is_consistent():
            conflicts = graph.find_conflicts()
            return self.resolve_conflicts(conflicts, nl_text)

        # Generate timeline
        timeline = graph.topological_sort()

        # Visual explanation
        return graph.visualize(timeline)

# Example: "Alice arrived before Bob. Bob left after Charlie arrived."
events = [
    Event("alice_arrive", type="arrival"),
    Event("bob_arrive", type="arrival"),
    Event("bob_leave", type="departure"),
    Event("charlie_arrive", type="arrival")
]

relations = [
    TemporalRelation("alice_arrive", "bob_arrive", "before"),
    TemporalRelation("charlie_arrive", "bob_leave", "before")
]

# Graph enables:
# 1. Consistency checking (Allen's algebra composition table)
# 2. Timeline generation (topological sort)
# 3. Visual explanation (DAG rendering)
# 4. Formal verification (STN/STNU solvers)
```

**Tradeoffs**:
- ✓ **Visual temporal understanding** (intuitive)
- ✓ Formal consistency checking
- ✓ Timeline generation automatic
- ✗ LLM temporal extraction errors (13.5+ F1 gap)
- ✗ Complex temporal expressions challenging
- ✗ Graph construction from NL imperfect

**When to Use**:
- Temporal reasoning central
- Visual explanations valuable
- Consistency verification important
- Timeline generation needed
- Complex temporal constraints (Allen's algebra, STN)

---

## OPTIMIZATION PATTERNS

### Pattern 14: Provenance-Guided Synthesis

**Intent**: Use why/why-not provenance from symbolic solver to guide LLM program synthesis.

**Motivation**: Blind generation inefficient. Provenance reveals which input facts contributed (or didn't); guides generation toward relevant patterns.

**Structure**:
```
Initial Program (LLM-generated or minimal)
    ↓
Execute on test cases
    ↓
Provenance Analysis (why/why-not)
  - Why: Which facts enabled this result?
  - Why-not: Which facts prevented this result?
    ↓
Learned Constraints (from provenance patterns)
    ↓
LLM generates improved program (guided by constraints)
    ↓
Iterate until correct
```

**Examples**:

1. **ProSynth (Datalog Synthesis)**:
   - Why/why-not provenance from Datalog solvers
   - Guides synthesis with learned constraints
   - Result: **10× speedup** over baseline on 40 synthesis tasks

2. **ASP Synthesis with Provenance**:
   - Minimal assumption sets identify critical facts
   - xASP explanation graphs show derivation structure
   - Guide LLM toward relevant rules

**Implementation**:
```python
class ProvenanceGuidedSynthesis:
    def synthesize(self, spec: Specification) -> Program:
        program = self.llm.generate_initial(spec)

        for iteration in range(max_iterations):
            # Execute on test cases
            results = self.execute_tests(program, spec.test_cases)

            # Compute provenance
            why_provenance = {}
            why_not_provenance = {}

            for test_case, result in results:
                if result.correct:
                    # Why did this succeed?
                    why_provenance[test_case] = self.solver.why_provenance(
                        program, test_case, result.output
                    )
                else:
                    # Why not did this fail?
                    why_not_provenance[test_case] = self.solver.why_not_provenance(
                        program, test_case, spec.expected_output(test_case)
                    )

            # Learn constraints from provenance
            constraints = self.analyze_provenance(
                why_provenance, why_not_provenance
            )

            # Generate improved program
            program = self.llm.refine(program, constraints, spec)

            if self.all_tests_pass(program, spec):
                return program

        raise SynthesisError("Failed to synthesize correct program")

    def analyze_provenance(self, why, why_not):
        constraints = []

        # Pattern: If fact F always in why-provenance, likely essential
        essential_facts = self.find_common_facts(why.values())
        constraints.append(f"Must include facts: {essential_facts}")

        # Pattern: If fact F in why-not, likely needs additional rule
        missing_derivations = self.find_missing_derivations(why_not)
        constraints.append(f"Add rules for: {missing_derivations}")

        return constraints
```

**Tradeoffs**:
- ✓ **10× speedup** (ProSynth results)
- ✓ Guided generation more efficient than blind
- ✓ Provenance provides actionable feedback
- ✗ Requires provenance-capable solver (Datalog/ASP)
- ✗ Provenance computation overhead
- ✗ Constraint learning heuristic (not always optimal)

**When to Use**:
- Program synthesis task (not just generation)
- Provenance-capable solver available (Datalog/ASP/SQL)
- Test cases available for iteration
- Synthesis efficiency critical
- Baseline generation success rate low (<50%)

---

### Pattern 15: Predicate Permutation Augmentation

**Intent**: Leverage DSL's ordering-insensitivity to generate training data augmentations automatically.

**Motivation**: Many logic languages insensitive to clause/predicate ordering. Permutations create diverse training examples from single source.

**Structure**:
```
Original Program (single example)
    ↓
Extract Clauses/Predicates
    ↓
Generate Permutations (semantically equivalent)
    ↓
Augmented Training Set (N! larger)
    ↓
Fine-tune LLM (more robust to ordering variations)
```

**Examples**:

1. **Yang et al. (Prolog Generation)**:
   - GSM8K-Prolog dataset with predicate permutation
   - Prolog ordering-insensitivity enables automatic augmentation
   - Result: Robust training, improved generation quality

2. **ASP Clause Reordering**:
   - ASP semantics independent of clause order
   - Permutations create diverse syntactic forms
   - Same stable models, different presentations

**Implementation**:
```python
import itertools

class PredicatePermutationAugmentation:
    def augment(self, program: PrologProgram, max_permutations: int = 10) -> List[PrologProgram]:
        # Extract clauses (order-independent)
        clauses = program.extract_clauses()

        # Generate permutations
        permutations = []
        for perm in itertools.permutations(clauses):
            if len(permutations) >= max_permutations:
                break
            permutations.append(PrologProgram(list(perm)))

        return permutations

# Example: Original Prolog program
original = """
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
father(john, mary).
mother(jane, mary).
"""

# Augmentation generates permutations:
# Permutation 1:
"""
father(john, mary).
mother(jane, mary).
parent(X, Y) :- father(X, Y).
parent(X, Y) :- mother(X, Y).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
"""

# Permutation 2:
"""
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
parent(X, Y) :- mother(X, Y).
parent(X, Y) :- father(X, Y).
father(john, mary).
mother(jane, mary).
"""

# All permutations semantically identical but syntactically diverse
# LLM trained on augmented set more robust to ordering
```

**Tradeoffs**:
- ✓ **Automatic augmentation** (no manual labeling)
- ✓ Semantic equivalence guaranteed (same logic)
- ✓ Syntactic diversity improves robustness
- ✓ N! data expansion (combinatorial growth)
- ✗ Only applicable to order-insensitive languages
- ✗ Exponential growth (need sampling for large programs)
- ✗ May overfit to specific structural patterns

**When to Use**:
- DSL order-insensitive (Prolog, ASP, Datalog)
- Training data limited (augmentation valuable)
- Fine-tuning approach (not prompting)
- Robustness to syntactic variation desired
- Computational budget allows multiple permutations

---

## Pattern Selection Guide

| Task | Recommended Patterns | Rationale |
|------|---------------------|-----------|
| Mathematical Reasoning | Neural[Symbolic] + Constrained Generation + Generate-Validate | LLM translates → SMT verifies |
| Planning/Robotics | Symbolic[Neural] + Grammar Prompting + Temporal Graph | Symbolic planner primary; LLM aids |
| Legal/Ethical Reasoning | Argumentation-Based + Justification Trees | Natural argumentation structure |
| Program Synthesis | Provenance-Guided + Fine-Tuning + Generate-Validate | Provenance guides iteration |
| Temporal Reasoning | Dual-Track + Temporal Graph + Predicate Extraction | LLM + symbolic temporal solver |
| Explainability-Critical | Proof-Carrying Code + Provenance Tracking + Justification Trees | Formal explanation guarantees |
| Resource-Constrained | Constrained Generation + Predicate Permutation | No fine-tuning; automatic augmentation |
| Safety-Critical | Proof-Carrying Code + Symbolic[Neural] | Kernel verification essential |

## Cross-Pattern Synergies

Patterns often combine for superior results:

1. **Fine-Tuning + Constrained Generation + Generate-Validate**:
   - Fine-tuning improves semantic correctness
   - Constrained generation eliminates syntax errors
   - Generate-validate catches edge cases
   - Example: ConstraintLLM achieves industrial-grade quality

2. **Provenance-Guided + Justification Trees + Argumentation**:
   - Provenance provides formal foundations
   - Justification trees show derivation structure
   - Argumentation presents in domain terms
   - Example: CrossJustice legal reasoning system

3. **Dual-Track + Temporal Graph + Predicate Extraction**:
   - LLM track extracts temporal relations
   - Symbolic track verifies consistency
   - Temporal graph unifies both
   - Example: TReMu 160% improvement

## Implementation Checklist

When implementing LLM-DSL integration:

- [ ] **Architecture**: Choose Neural[Symbolic], Symbolic[Neural], or Dual-Track based on primary reasoning locus
- [ ] **Generation**: Select Constrained > Grammar Prompting > Fine-Tuning based on resources
- [ ] **Verification**: Always include Generate-Validate minimum; add Proof-Carrying for critical systems
- [ ] **Explanation**: Match domain expectations (Justification Trees for logic, Argumentation for legal, Temporal Graphs for temporal)
- [ ] **Optimization**: Add Provenance-Guided if synthesis task; use Predicate Permutation if training data limited

## Conclusion

These 15 patterns represent distilled best practices from 35+ deployed systems and 167+ research papers (2020-2025). The unifying insight: **LLMs excel at natural language understanding and generation; symbolic systems excel at formal reasoning and verification**. Successful integration leverages complementary strengths through architectural patterns (Neural[Symbolic], Symbolic[Neural]), ensures correctness through verification patterns (Generate-Validate, Proof-Carrying, Provenance), and provides transparency through explanation patterns (Justification Trees, Argumentation, Temporal Graphs).

The field is converging toward hybrid neuro-symbolic architectures where LLMs handle semantic parsing while symbolic DSLs provide verified computation. This synthesis enables systems that are both powerful (leveraging LLM flexibility) and trustworthy (maintaining symbolic correctness guarantees)—precisely the combination required for real-world deployment in safety-critical, regulatory-compliance, and high-stakes domains.

## References

See `./references_dsl.md` for comprehensive bibliography.
