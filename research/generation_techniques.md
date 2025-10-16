**Navigation**: [🏠 Home](../README.md) | [📄 Paper](../paper_main.md) | [🚀 Quick Start](../QUICK_START.md) | [📑 Index](../PROJECT_INDEX.md)

---

# LLM Code Generation Techniques: Prompting and Fine-Tuning Methods

## Executive Summary

Modern LLM code generation employs sophisticated techniques spanning prompting strategies (few-shot, chain-of-thought, self-verification), constrained generation (grammar-based, JSON schema), fine-tuning approaches (domain-specific, LoRA, QLoRA), and hybrid neuro-symbolic integration. Research from 2023-2025 demonstrates that **technique selection matters as much as model selection**, with proper prompting providing 10-40% improvements and domain-specific fine-tuning enabling smaller models (7-32B) to outperform frontier models (175B+) on specialized tasks.

---

## 1. Prompting Techniques

### 1.1 Few-Shot Prompting

**Definition**: Providing 1-5 example input-output pairs before the target task.

**Performance Impact**:
- **0-shot → 3-shot**: 15-25% accuracy improvement (general code)
- **3-shot → 5-shot**: 5-10% additional improvement (diminishing returns)
- **Optimal range**: 3-5 examples for code generation

**Example Structure**:
```
# Example 1: [Problem description]
# Solution: [Code]

# Example 2: [Problem description]
# Solution: [Code]

# Example 3: [Problem description]
# Solution: [Code]

# Your task: [Target problem]
```

**Best Practices**:
- Select diverse, representative examples
- Match example complexity to target task
- Include edge cases in examples
- For formal languages: Leverage syntax permutation invariance (Prolog, ASP)

**Prolog-Specific Innovation** (Yang, Chen, Tam 2024):
- **Predicate permutation as data augmentation**
- Prolog's ordering-insensitivity enables creating multiple valid examples from one solution
- Improves robustness to different predicate ordering styles

### 1.2 Chain-of-Thought (CoT) Prompting

**Definition**: Explicitly prompting models to show intermediate reasoning steps before final code.

**Standard CoT Structure**:
```
Problem: [Description]

Let's solve this step by step:
1. [Reasoning step 1]
2. [Reasoning step 2]
3. [Reasoning step 3]

Therefore, the solution is:
[Code]
```

**Performance Impact**:
- **Mathematical reasoning**: 20-40% accuracy improvement
- **Complex algorithms**: 15-30% improvement
- **Simple code**: Minimal improvement (5-10%), sometimes negative

**Variants**:

**Self-Planning Code Generation** (2024):
- **Two-phase approach**: Planning phase + Implementation phase
- LLM plans concise solution steps from intent
- **Performance**: Up to 25.4% improvement in Pass@1 vs. direct generation
- **11.9% improvement** vs. standard CoT

**Zero-Shot CoT**:
- Single prompt: "Let's think step by step"
- 10-15% improvement without examples
- Cost-effective for simple tasks

**When to Use CoT**:
- ✅ Complex algorithms requiring multi-step reasoning
- ✅ Mathematical problem-solving
- ✅ Planning and decomposition tasks
- ❌ Simple, well-defined single-function problems
- ❌ When interpretability isn't required

### 1.3 Self-Verification Prompting

**Definition**: LLM generates solution, then verifies its own correctness through reasoning.

**Basic Self-Verification Process**:
1. Generate candidate solution
2. LLM analyzes solution for correctness
3. Identify potential errors
4. Refine solution based on self-critique

**Self-Verification Techniques**:

**Self-Refine Framework**:
- Generate output
- Provide self-feedback
- Refine output based on feedback
- Iterate until confidence threshold met

**Self-Consistency Sampling**:
- Generate multiple reasoning paths (5-10 samples)
- Select most consistent answer across samples
- **Improvement**: 15-25% accuracy boost
- **Cost**: 5-10× computational overhead

**Chain-of-Verification (CoVe)** (2024):
- Four-step process: Draft → Verify → Identify Issues → Refine
- Addresses hallucination in generation
- Particularly effective for factual accuracy
- **Improvement**: 20-30% reduction in hallucinations

**Performance Data**:
- **Self-verification**: 10-20% accuracy improvement over direct generation
- **Self-consistency (K=10)**: 15-25% improvement, but 10× cost
- **Optimal strategy**: Self-verification + limited self-consistency (K=3-5)

**When to Use**:
- ✅ High-stakes applications requiring correctness
- ✅ Complex reasoning where errors are common
- ✅ When computational budget allows sampling
- ❌ Real-time applications (latency constraints)
- ❌ Simple tasks where accuracy already high (>90%)

### 1.4 Tree-of-Thoughts Prompting

**Definition**: Explore multiple reasoning paths simultaneously in tree structure, backtracking when paths fail.

**Structure**:
- Generate multiple candidate next steps (breadth)
- Evaluate each path's promise
- Expand most promising paths (depth)
- Backtrack on failures

**Performance**:
- **Complex reasoning**: 30-40% improvement over linear CoT
- **Planning tasks**: 25-35% improvement
- **Computational cost**: 10-50× baseline (depending on tree depth)

**Trade-offs**:
- Highest accuracy for extremely complex tasks
- Prohibitive cost for most applications
- Best suited for competition-level problems, not production code

### 1.5 Narrative-of-Thought (NoT) for Temporal Reasoning

**Definition**: Convert events to structured representations (Python classes), generate temporally grounded narratives, guide temporal graph generation.

**Process**:
1. Extract events from text
2. Convert to Python class representations
3. Generate narrative grounding temporal relationships
4. Construct temporal graph from narrative

**Performance** (Schema-11 benchmark):
- **Highest F1 score** among temporal reasoning methods
- Effective for complex temporal dependencies
- Combines natural language understanding with formal structure

**Application**: Temporal reasoning tasks requiring event ordering, duration calculation, timeline synthesis.

---

## 2. Constrained Generation Techniques

### 2.1 Grammar Prompting

**Definition**: Augment prompts with Backus-Naur Form (BNF) grammars defining valid output structure.

**Approach** (Wang et al. 2024):
1. For each example, provide minimal grammar subset sufficient for that output
2. LLM predicts BNF grammar for test input
3. Generate output conforming to predicted grammar

**Performance**:
- **Semantic parsing**: Competitive with fine-tuned models
- **PDDL planning**: 15-20% improvement over unconstrained generation
- **SMILES molecules**: Guaranteed syntactic validity

**Advantages**:
- Eliminates syntax errors by construction
- Generalizes from few examples
- Applicable to any formal language with BNF grammar

**Limitations**:
- Requires grammar specification
- Semantic correctness not guaranteed (only syntax)
- LLM must predict appropriate grammar subset

### 2.2 JSON Schema Constrained Generation

**Definition**: Transform domain-specific languages (DSLs) into JSON Schema, constrain LLM output to schema-valid JSON.

**Implementation**:
- **OpenAI Structured Outputs**: Built-in feature for GPT-4+
- **Outlines** (open-source): Context-free grammar constraints via logit masking
- **JSON mode**: Simpler approach, forces valid JSON structure

**Performance Impact**:
- **100% syntactic correctness** for schema-conformant outputs
- **Eliminates hallucination** of non-existent constructs
- **10-20% accuracy improvement** by preventing syntax errors

**Use Cases**:
- ✅ Formal language generation (ASP, Prolog, constraints)
- ✅ Structured data extraction
- ✅ API call generation
- ✅ Configuration file generation

**Advantages Over Fine-Tuning**:
- No training data required
- More reliable for rare syntactic constructs
- Immediate applicability to new DSLs
- Cost-effective (no training costs)

**Example**: Prolog/ASP generation as JSON objects representing predicates, rules, constraints → Parse JSON → Emit formal language syntax.

### 2.3 Logit Masking & LMQL

**Definition**: Constrain LLM output at token level by masking invalid logits during generation.

**LMQL (Language Model Query Language)**:
- Declarative language for constrained generation
- Supports regex, grammars, type constraints
- Real-time constraint enforcement during decoding

**Example Constraints**:
```python
"Generate a Python function [FUNCTION]"
where len(FUNCTION) < 500 and FUNCTION.startswith("def")
```

**Performance**:
- **Guaranteed constraint satisfaction**
- **5-15% accuracy improvement** by preventing invalid outputs
- **Latency impact**: 10-30% slower generation (depends on constraint complexity)

**Limitations**:
- Currently limited model support (primarily OpenAI)
- Complex constraints may significantly slow generation
- Doesn't guarantee semantic correctness

---

## 3. Fine-Tuning Approaches

### 3.1 Full Fine-Tuning

**Definition**: Update all model parameters on domain-specific dataset.

**Data Requirements**:
- Minimum: 500-1,000 high-quality examples
- Optimal: 5,000-50,000 examples
- Quality > Quantity (small curated dataset better than large noisy dataset)

**Performance Impact**:
- **Domain-specific tasks**: 30-50% improvement over base model
- **Rare syntactic patterns**: 40-60% improvement
- **General capabilities**: Can degrade if training data too narrow

**Costs**:
- **Computational**: 1,000-10,000 GPU-hours (depending on model size)
- **Data curation**: Most expensive component (human annotation)
- **Inference**: Same as base model (no overhead)

**When to Use**:
- ✅ Large budget and large dataset available
- ✅ Domain-specific language with unique patterns
- ✅ Production deployment with high volume
- ❌ Limited data (<500 examples)
- ❌ Rapidly evolving domain
- ❌ Budget constraints

### 3.2 Low-Rank Adaptation (LoRA)

**Definition**: Fine-tune low-rank decomposition matrices added to attention layers, freezing base model.

**Technical Details**:
- Add trainable rank decomposition matrices: W' = W + BA (B ∈ R^(d×r), A ∈ R^(r×d), r << d)
- Typical rank: r = 4-64
- **Parameters trained**: 0.1-1% of full model
- **Memory footprint**: 3-5× lower than full fine-tuning

**Performance Impact**:
- **Domain-specific tasks**: 25-40% improvement (slightly less than full fine-tuning)
- **General capabilities**: Better preservation than full fine-tuning
- **Convergence**: Faster training (fewer parameters to update)

**Costs**:
- **Computational**: 10-50× cheaper than full fine-tuning
- **Data requirements**: 500-5,000 examples (less than full fine-tuning)
- **Inference**: Minimal overhead (merge LoRA weights or small adapter)

**Advantages**:
- Multiple LoRA adapters for different tasks from single base model
- Easy to share, version, and deploy
- Reversible (switch back to base model)

**Example**: DeepSeek-Prover-v2 uses LoRA for theorem proving specialization.

### 3.3 Quantized Low-Rank Adaptation (QLoRA)

**Definition**: Combine LoRA with 4-bit quantization of base model for extreme memory efficiency.

**Technical Innovation**:
- Quantize base model to 4-bit (INT4/NF4)
- Train LoRA adapters in full precision (FP16/BF16)
- **Memory reduction**: 4-8× vs. standard LoRA, 16-32× vs. full fine-tuning

**ConstraintLLM Case Study** (2024):
- Base: Qwen2.5-Coder-32B-Instruct
- Training: 3× NVIDIA RTX A6000 GPUs (48GB each)
- Performance: Competitive with GPT-4o and DeepSeek-V3-685B
- **Key Result**: 32B QLoRA-tuned ≈ 685B general model on domain tasks

**Performance Impact**:
- **Domain-specific tasks**: 20-35% improvement
- **Comparable to full LoRA** with 4-8× less memory
- **Slight quality degradation** from quantization (<5%)

**Costs**:
- **Computational**: Accessible on consumer GPUs (3× RTX A6000)
- **Data requirements**: 500-3,000 examples
- **Inference**: Can use quantized or full-precision serving

**When to Use**:
- ✅ Limited GPU memory (can't fit model + gradients)
- ✅ Cost-sensitive applications
- ✅ Moderate dataset size (500-5,000 examples)
- ✅ Domain-specific formal languages
- ❌ When maximum quality required (use full LoRA)

### 3.4 Instruction Fine-Tuning

**Definition**: Fine-tune on instruction-following format (instruction + response pairs) for better prompt adherence.

**Format**:
```
### Instruction:
[Task description]

### Input:
[Optional context/input]

### Response:
[Expected output]
```

**Performance Impact**:
- **Instruction following**: 30-50% improvement
- **Code generation from specs**: 20-35% improvement
- **Multi-turn interactions**: 25-40% improvement

**Data Requirements**:
- Instruction-response pairs: 1,000-50,000
- Diversity crucial (many task types)
- Human annotation often necessary

**Examples**:
- **LLaMA-2-Chat**: Instruction-tuned LLaMA-2
- **CodeLlama-Instruct**: Instruction-tuned CodeLlama
- **GPT-4**: Extensively instruction-tuned (proprietary data)

### 3.5 Domain-Specific Fine-Tuning for Formal Languages

**LLASP Case Study** (Answer Set Programming):
- **Approach**: Fine-tune lightweight model on fundamental ASP patterns
- **Result**: Dramatically outperformed non-fine-tuned larger models
- **Key Insight**: Domain-specific patterns > general-purpose scale

**Prolog Generation** (GSM8K-Prolog):
- **Dataset**: Augmented with predicate permutations
- **GPT-4o**: 74% Pass@1 (with external interpreter)
- **Technique**: Few-shot prompting + external Prolog interpreter validation

**General Pattern**:
1. Curate high-quality domain-specific dataset (500-5,000 examples)
2. Fine-tune 7-32B model with LoRA/QLoRA
3. Use external verifier/interpreter for correctness
4. **Result**: Outperform 100B+ general models on domain tasks

**Data Augmentation Strategies**:
- **Syntax permutation**: For order-insensitive languages (Prolog, ASP)
- **Semantic variation**: Generate equivalent programs with different structures
- **Error injection**: Train on common errors + corrections
- **Explanation augmentation**: Include reasoning traces (CoT-style)

---

## 4. Hybrid Neuro-Symbolic Techniques

### 4.1 LLM + Symbolic Reasoner Architectures

**Three Integration Patterns**:

1. **Symbolic[Neural]**: Symbolic system invokes neural components
   - Example: Symbolic planner uses LLM for heuristic guidance
   - Control flow: Symbolic system orchestrates

2. **Neural[Symbolic]**: Neural model calls symbolic reasoners
   - Example: LLM generates Prolog, invokes interpreter, uses result
   - Control flow: LLM orchestrates

3. **Symbolic Neural**: Words/tokens as input/output interface
   - Example: LLM translates natural language ↔ formal specification
   - Control flow: Pipeline (LLM → Symbolic → LLM)

**Performance Data**:
- **Hybrid approaches**: 40-160% improvement over pure neural
- **Prolog + LLM**: 80% accuracy (DeepSeek-V3) vs. 63-76% pure CoT
- **ASP + LLM**: 90%+ execution rate on robotic planning (CLMASP)
- **TReMu (temporal)**: 29.83 → 77.67 (160% improvement)

### 4.2 LLM + Prolog Integration

**Architecture**:
1. LLM extracts predicates from natural language
2. Generate Prolog program
3. External Prolog interpreter executes
4. Return results to LLM or user

**Advantages**:
- **Deterministic computation**: Prolog guarantees correctness for valid programs
- **Explainable**: Prolog execution traces human-readable
- **Efficient**: Prolog faster than LLM for logical inference

**Performance** (Yang, Chen, Tam 2024):
- **GSM8K-Prolog**: Outperformed CoT across Llama2, CodeLlama, Mistral
- **FinQA**: DeepSeek-V3 80% accuracy vs. 63-76% pure reasoning
- **GPT-4o**: 74% Pass@1 on financial reasoning tasks

**Best Practices**:
- Focus LLM on semantic parsing, not computation
- Use external Prolog interpreter (SWI-Prolog, SICStus)
- Validate generated Prolog syntax before execution
- Provide execution traces as feedback for refinement

### 4.3 LLM + Answer Set Programming (ASP)

**Architecture**:
1. LLM translates problem to ASP rules
2. ASP solver (CLASP, CLINGO) computes answer sets
3. LLM interprets results or generates explanations

**Advantages**:
- **Non-monotonic reasoning**: ASP handles defaults, exceptions
- **Optimization**: Native support for optimization problems
- **Non-hallucination**: Stable model semantics guarantees justifications

**LLASP System**:
- **Approach**: Fine-tuned lightweight model specifically for ASP generation
- **Result**: Substantially outperformed larger general-purpose LLMs
- **Semantic correctness**: Far superior to non-fine-tuned models

**CLMASP System** (Robotic Planning):
- **Architecture**: Two-level planning (LLM skeleton + ASP refinement)
- **Performance**: 90%+ execution rate on bAbI, StepGame, CLUTRR
- **Key Insight**: LLM high-level planning + ASP constraint solving

**ASPBench 2025 Findings**:
- LLMs struggle with ASP solving (core computation)
- Hybrid approach essential: LLM generation + ASP solver execution
- Fine-tuning critical for syntactic correctness

### 4.4 LLM + SMT Solver Integration

**Proof of Thought** (PoT):
- **Architecture**: LLM generates JSON-based DSL for logical constructs → Z3 SMT solver
- **Performance**: 40% error reduction on mathematical reasoning
- **Advantage**: Formal verification of reasoning steps

**Process**:
1. LLM understands problem in natural language
2. Generates JSON encoding of logical constraints
3. Z3 checks satisfiability and finds models
4. LLM interprets results back to natural language

**Use Cases**:
- Mathematical reasoning with formal verification
- Program synthesis with correctness guarantees
- Constraint satisfaction problems
- Verification of program properties

**Performance**:
- **40% error reduction** vs. pure LLM reasoning
- **100% correctness** for valid encodings (SMT proof-based)
- **Limitation**: LLM encoding errors remain (~20-30% of cases)

### 4.5 LLM + Constraint Programming (CP)

**GenCP** (Constrained Text Generation):
- **Architecture**: LLM predicts domain → CP search for valid outputs
- **Performance**: Faster than Beam Search + 100% constraint satisfaction
- **Application**: Text generation under hard constraints

**ConstraintLLM**:
- **Approach**: Fine-tune on industrial CP problems (MiniZinc)
- **Training**: Qwen2.5-Coder-32B with QLoRA (3× A6000 GPUs)
- **Performance**: Competitive with GPT-4o and DeepSeek-V3-685B

**Logic.py** (ZebraLogicBench):
- **Architecture**: Agentic solver engine formalizing problems in DSL → constraint solver
- **Performance**: 65% absolute improvement over baseline LLMs
- **Key**: Domain-specific language + constraint solving separation

**Automatic Constraint Model Generator**:
- **Process**: Semantic entity extraction → constraint model generation → MiniZinc validation
- **Result**: State-of-the-art on industrial CP benchmarks
- **Advantage**: Iterative refinement with solver feedback

### 4.6 LLM + Temporal Reasoning Integration

**TempGraph-LLM (TG-LLM)**:
- **Architecture**: LLM translates text → temporal graphs → CoT reasoning with graph structure
- **Training**: TGQA synthetic datasets for graph translation
- **Performance**: More consistent than free text generation

**TReMu Framework**:
- **Architecture**: Time-aware memorization (timeline summarization) + neuro-symbolic reasoning (Python code generation)
- **Performance**: GPT-4o 29.83 → 77.67 (160% improvement)
- **Key Innovation**: Combine temporal memory with symbolic computation

**Time-R1 Framework** (2025):
- **Architecture**: Three-stage RL curriculum with dynamic rule-based rewards
- **Training**: Time-Bench (10 years news data)
- **Performance**: 3B parameters superior to 671B DeepSeek-R1
- **Advantage**: Temporal-specific training curriculum

**LLM-DA Method**:
- **Architecture**: Extract temporal logical rules from historical temporal KGs → dynamic rule adaptation
- **Advantage**: No fine-tuning required, adapts to new events
- **Application**: Temporal knowledge graph reasoning

**Hybrid Temporal Architecture (Recommended)**:
1. **LLM**: Temporal expression extraction from natural language
2. **Allen's Algebra**: Qualitative temporal reasoning (before, during, overlaps)
3. **STN/STNU Solvers**: Quantitative temporal constraints (numeric bounds)
4. **Timeline Synthesis**: Event ordering and timeline generation

**Performance**: 40-160% improvement over pure LLM temporal reasoning.

---

## 5. Advanced Techniques

### 5.1 Retrieval-Augmented Generation (RAG)

**Definition**: Retrieve relevant examples/documentation before generation.

**Architecture**:
1. Embed query and knowledge base
2. Retrieve top-K relevant documents (K=3-10)
3. Augment prompt with retrieved context
4. Generate code with augmented context

**Performance Impact**:
- **LeanDojo/ReProver**: 10-15% improvement in theorem proving
- **General code**: 15-25% improvement with API documentation
- **Domain-specific**: 20-35% improvement with internal codebase context

**RAG for Theorem Proving**:
- **LeanDojo**: Retrieval of relevant lemmas/theorems from mathlib
- **Result**: Significant improvement in proof search success rate
- **Key**: Domain-specific embedding fine-tuned on mathematical text

**Implementation**:
- **Embedding models**: text-embedding-3-large (OpenAI), sentence-transformers
- **Vector stores**: FAISS, Pinecone, Weaviate
- **Retrieval**: Dense retrieval (embeddings) or hybrid (BM25 + dense)

### 5.2 Self-Correction with External Verification

**Process**:
1. LLM generates code
2. External verifier checks correctness (compiler, interpreter, test suite)
3. If errors: LLM receives error messages as feedback
4. LLM corrects code based on feedback
5. Iterate until correct or max iterations reached

**Performance** (2024 empirical study):
- **Compiler errors**: 60-80% self-correction success rate
- **Test failures**: 40-60% self-correction success rate
- **Semantic bugs**: 20-40% self-correction success rate

**Key Findings**:
- Self-correction most effective for syntax and runtime errors
- Semantic correctness harder to self-correct
- Diminishing returns after 2-3 correction iterations

**Best Practices**:
- Provide detailed error messages (not just "error")
- Include test failures with expected vs. actual outputs
- Limit to 2-3 correction iterations (cost-performance tradeoff)
- Use external verification, not LLM self-verification alone

### 5.3 Curriculum Learning

**Definition**: Train on progressively more difficult examples, starting with simple problems.

**Time-R1 Framework** (Temporal Reasoning):
- **Stage 1**: Basic temporal extraction
- **Stage 2**: Temporal ordering and relationships
- **Stage 3**: Complex temporal reasoning and counterfactuals
- **Result**: 3B model outperforms 671B general model

**Performance Impact**:
- **Complex reasoning**: 20-40% improvement over random training order
- **Sample efficiency**: 30-50% fewer examples needed to reach target performance
- **Generalization**: Better performance on out-of-distribution problems

**Implementation**:
- Define difficulty metric (problem complexity, solution length, dependencies)
- Sort training data by difficulty
- Train in phases with increasing difficulty
- Optionally: Revisit easier examples in later stages

**When to Use**:
- ✅ Complex domain with clear difficulty progression
- ✅ Limited training data (improves sample efficiency)
- ✅ High-quality labeled data (difficulty scoring requires understanding)
- ❌ Simple, uniform difficulty tasks
- ❌ When random sampling already achieves good performance

### 5.4 Multi-Agent Code Generation

**Definition**: Multiple LLM agents with different roles collaborate on code generation.

**Typical Roles**:
- **Planner**: Breaks down problem into sub-tasks
- **Coder**: Implements individual functions/modules
- **Reviewer**: Checks code quality and correctness
- **Tester**: Generates test cases and validates

**Architecture**:
- Sequential: Planner → Coder → Reviewer → Tester
- Parallel: Multiple coders work on different modules simultaneously
- Iterative: Feedback loops between roles

**Performance Impact**:
- **Complex systems**: 25-40% improvement over single-agent
- **Code quality**: 30-50% fewer bugs in multi-agent generation
- **Cost**: 3-5× computational overhead (multiple LLM calls)

**When to Use**:
- ✅ Large, complex code generation tasks
- ✅ When code quality critical (production systems)
- ✅ Budget allows multiple LLM calls
- ❌ Simple, single-function generation
- ❌ Real-time applications (high latency)

### 5.5 Prompt Chaining and Decomposition

**Definition**: Break complex tasks into sequential prompts, each handling one sub-task.

**Example Workflow**:
1. **Prompt 1**: "Analyze this problem and create a high-level plan."
2. **Prompt 2**: "Implement function X based on this plan: [Plan from Prompt 1]"
3. **Prompt 3**: "Implement function Y based on this plan: [Plan from Prompt 1]"
4. **Prompt 4**: "Integrate functions X and Y: [X code] [Y code]"

**Performance Impact**:
- **Complex tasks**: 20-35% improvement over single prompt
- **Maintainability**: Easier debugging (isolate failures to specific prompts)
- **Cost**: 2-4× more LLM calls, but smaller contexts per call

**Best Practices**:
- Explicitly pass context between prompts
- Each prompt should have clear, focused objective
- Validate intermediate outputs before proceeding
- Use structured formats for inter-prompt communication

---

## 6. Technique Selection Guide

### 6.1 Decision Matrix

| Goal | Recommended Technique | Expected Improvement | Cost | Complexity |
|------|----------------------|---------------------|------|-----------|
| **General code accuracy** | Few-shot (3-5 examples) | 15-25% | Low | Low |
| **Complex reasoning** | Chain-of-Thought | 20-40% | Low | Low |
| **Maximum accuracy** | Self-consistency (K=10) | 15-25% | High (10×) | Medium |
| **Formal language syntax** | JSON Schema constraints | 10-20% | Low | Medium |
| **Domain specialization** | QLoRA fine-tuning | 25-40% | Medium | High |
| **Theorem proving** | RAG + LoRA fine-tuning | 30-50% | High | High |
| **Temporal reasoning** | Hybrid (LLM + symbolic) | 40-160% | Medium | High |
| **Production deployment** | Fine-tuning + verification | 30-50% | High | High |

### 6.2 Technique Combinations

**High-Performance Stack** (Maximum accuracy, high cost):
- Domain-specific fine-tuning (LoRA/QLoRA)
- Few-shot prompting (3-5 examples)
- Chain-of-Thought reasoning
- Self-consistency sampling (K=5-10)
- External verification + self-correction
- **Expected improvement**: 60-100%+ over baseline
- **Cost**: 20-50× baseline computational cost

**Efficient Stack** (Good accuracy, low cost):
- Few-shot prompting (3 examples)
- Zero-shot CoT ("Let's think step by step")
- External verification (single attempt)
- **Expected improvement**: 25-40% over baseline
- **Cost**: 1.5-2× baseline computational cost

**Formal Verification Stack** (Correctness guarantees):
- Hybrid neuro-symbolic architecture
- Constrained generation (grammar/schema)
- External symbolic verifier (SMT/ASP/Prolog)
- Formal proof generation
- **Expected improvement**: 40-80% over pure neural
- **Cost**: 3-10× baseline, but includes correctness proof

**Production Stack** (Deployed systems):
- Domain-specific fine-tuning (QLoRA, 32B model)
- Constrained generation (schema-based)
- External verification + limited self-correction (2 iterations)
- Caching and prompt optimization
- **Expected improvement**: 40-60% over baseline
- **Cost**: Initial high (fine-tuning), amortized low (inference)

---

## 7. Emerging Techniques (2025)

### 7.1 Test-Time Compute Scaling

**Concept**: Allocate more compute at inference time (not just training) for better results.

**OpenAI o1 Model**:
- "Thinks" longer at inference time using extended chain-of-thought
- Performance improves with more test-time compute
- Trade-off: Latency vs. accuracy

**Application to Code Generation**:
- Generate multiple solution candidates
- Extended reasoning for complex problems
- Verify candidates before selecting best

**Performance**: 15-30% improvement on complex problems with 5-10× compute.

### 7.2 Reinforcement Learning from Human Feedback (RLHF) for Code

**DeepSeek-R1 Approach**:
- Generate high-quality CoT datasets for code generation
- Use RLHF to align reasoning process
- Result: Improved reasoning quality and consistency

**Process**:
1. Generate code with reasoning traces
2. Human annotators rate quality
3. Train reward model from ratings
4. Fine-tune policy with PPO/RLHF

**Performance**: 20-40% improvement in reasoning quality and explanation coherence.

### 7.3 Compact Models with Extended CoT (<70B Parameters)

**Trend**: Focus on smaller models (7-70B) capable of sustained chain-of-thought reasoning.

**Examples**:
- **Time-R1**: 3B model for temporal reasoning (outperforms 671B on specific tasks)
- **Phi-3**: 14B model competitive with much larger models on reasoning

**Motivation**:
- Cost efficiency (inference 10-100× cheaper)
- Latency reduction (faster generation)
- Deployment accessibility (consumer GPUs)

**Technique**: Intensive training on high-quality reasoning traces, curriculum learning.

### 7.4 Provenance-Aware Generation

**Concept**: Track derivation provenance through reasoning pipeline (LLM → symbolic system → output).

**Benefits**:
- Explainability: Trace final output back to input and reasoning steps
- Debugging: Identify where errors occur in pipeline
- Confidence calibration: Distinguish certain vs. uncertain reasoning

**Implementation**: Integrate provenance semirings (algebraic framework) with neuro-symbolic systems.

**Status**: Active research area, limited production deployments.

---

## 8. Practical Implementation Guidelines

### 8.1 Starting Point Recommendations

**For Newcomers** (minimal complexity):
1. Use frontier model (GPT-4o, Claude 3.5 Sonnet)
2. Apply few-shot prompting (3 diverse examples)
3. Add zero-shot CoT ("Let's think step by step")
4. **Expected**: 30-40% improvement over zero-shot baseline
5. **Cost**: Minimal (slightly longer prompts)

**For Intermediate Users** (balanced approach):
1. Choose appropriate model size (32-70B for cost, 175B+ for accuracy)
2. Few-shot prompting + explicit CoT
3. External verification (compiler/interpreter/tests)
4. Self-correction (1-2 iterations)
5. **Expected**: 50-70% improvement over baseline
6. **Cost**: 3-5× baseline

**For Advanced Users** (maximum performance):
1. Domain-specific fine-tuning (QLoRA on 32B model)
2. Hybrid neuro-symbolic architecture
3. Constrained generation (grammar/schema)
4. RAG with domain-specific retrieval
5. External verification + formal proofs
6. **Expected**: 70-150% improvement over baseline
7. **Cost**: High initial, amortized over volume

### 8.2 Common Pitfalls to Avoid

❌ **Over-reliance on model scale**: Technique often matters more than size
❌ **Ignoring external verification**: LLMs can't verify own correctness reliably
❌ **Too many few-shot examples**: Diminishing returns after 5, context overflow
❌ **Complex prompts without testing**: Start simple, iterate based on results
❌ **Fine-tuning on small datasets**: <500 examples often leads to overfitting
❌ **No fallback mechanisms**: Always have error handling for generated code
❌ **Assuming correctness**: Even 90% accuracy means 1 in 10 failures
❌ **Ignoring cost**: Self-consistency (K=100) rarely worth 100× cost

### 8.3 Evaluation Best Practices

**Metrics to Track**:
- **Pass@1**: First-attempt success rate (most important)
- **Pass@K**: Success within K attempts (K=10 typical)
- **Syntax correctness**: Percentage parsing/compiling successfully
- **Semantic correctness**: Percentage passing test suites
- **Execution time**: Runtime performance of generated code
- **Code quality**: Maintainability, readability (human eval)

**Evaluation Process**:
1. Create diverse, representative test set (100+ problems)
2. Evaluate on novel problems (avoid training data leakage)
3. Include edge cases and error conditions
4. Track errors by category (syntax, logic, edge cases)
5. Manually review failures to identify patterns

**Continuous Improvement**:
- Regularly update test sets with new problem types
- Analyze failure modes systematically
- Iterate on prompts/techniques based on error analysis
- A/B test technique changes with statistical rigor

---

## Conclusion

LLM code generation technique selection should match task requirements, not follow universal prescriptions. Key principles:

1. **Prompting before fine-tuning**: Proper prompting (few-shot + CoT) achieves 30-40% improvement with minimal cost
2. **Domain-specific beats general-purpose**: Fine-tuned 32B model often outperforms 175B+ general model on specialized tasks
3. **Hybrid architectures for formal verification**: Neuro-symbolic approaches provide 40-160% improvement over pure neural
4. **External verification essential**: LLMs cannot reliably verify own correctness
5. **Cost-performance tradeoffs**: Self-consistency (K=10) provides 15-25% improvement at 10× cost—carefully evaluate ROI

**State-of-the-Art (2025)**:
- **General code**: Few-shot + CoT + frontier models → 90-99% HumanEval
- **Formal languages**: QLoRA fine-tuning + external verifiers → 70-80% correctness
- **Theorem proving**: RAG + LoRA + symbolic reasoning → 35-40% competition-level success
- **Temporal reasoning**: Hybrid LLM + symbolic temporal reasoners → 40-160% improvement

The future of code generation lies in hybrid approaches combining statistical learning (LLMs) with formal reasoning (symbolic systems), leveraging strengths of both paradigms while mitigating weaknesses.
