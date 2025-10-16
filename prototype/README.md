**Navigation**: [🏠 Home](../README.md) | [📄 Paper](../paper_main.md) | [🚀 Quick Start](../QUICK_START.md) | [📑 Index](../PROJECT_INDEX.md)

---

# Hybrid Neuro-Symbolic Temporal Reasoning Prototype

A proof-of-concept implementation demonstrating hybrid neuro-symbolic architecture for temporal reasoning, combining LLM-based extraction with symbolic Allen's Interval Algebra reasoning.

## Overview

This prototype demonstrates how combining neural (LLM) and symbolic (Allen's Interval Algebra) approaches can improve temporal reasoning accuracy, verifiability, and explainability compared to pure LLM approaches.

### Key Features

- **Three-Level Temporal Reasoning**:
  - Level 1: Event extraction from natural language
  - Level 2: Temporal ordering and relationship inference
  - Level 3: Duration calculations and temporal arithmetic

- **Allen's Interval Algebra**: Implementation of all 13 basic temporal relations with constraint propagation

- **Hybrid Architecture**: Seamless integration of LLM extraction and symbolic verification

- **Provenance Tracking**: Complete reasoning chain tracking for transparent explanations

- **Comprehensive Test Suite**: 20 test cases covering medical, financial, project management, and other domains

## Architecture

```
Natural Language Query
        ↓
   LLM Extraction
   (temporal_core.py)
        ↓
  Symbolic Conversion
  (Allen's Relations)
        ↓
  Constraint Solving
  (temporal_core.py)
        ↓
   Verification
        ↓
  Provenance-Tracked Answer
```

## Installation

### Requirements

- Python 3.8 or higher
- No external dependencies required (uses only Python standard library)

### Setup

```bash
# Clone or navigate to the prototype directory
cd ./prototype/

# Optional: Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# No package installation needed - all dependencies are in standard library
```

## Quick Start

### Running Individual Components

#### 1. Allen's Interval Algebra Demo

```bash
python temporal_core.py
```

This demonstrates:
- Determining relations between time intervals
- Temporal constraint solving
- Relation composition

#### 2. Mock LLM Interface Demo

```bash
python llm_interface.py
```

This shows:
- LLM extraction of temporal information
- Different accuracy levels
- Domain-specific handling (medical, financial, etc.)

#### 3. Provenance Tracking Demo

```bash
python provenance.py
```

This illustrates:
- Recording reasoning steps
- Generating explanations
- Confidence tracking

#### 4. Hybrid Reasoner Demo

```bash
python hybrid_reasoner.py
```

This demonstrates:
- Complete hybrid reasoning pipeline
- LLM + symbolic integration
- Conflict resolution
- Comparison with pure LLM approach

### Running Test Cases

```bash
# View test suite summary
python test_cases.py

# Run comprehensive evaluation
python run_experiments.py
```

## Usage Examples

### Example 1: Simple Temporal Reasoning

```python
from hybrid_reasoner import HybridTemporalReasoner

# Initialize reasoner
reasoner = HybridTemporalReasoner(llm_accuracy="medium")

# Ask a temporal question
question = "Patient was admitted Monday, had surgery Tuesday, discharged Friday. How long was the stay?"

# Get hybrid reasoning result
result = reasoner.reason(question)

print(f"Answer: {result.verified_answer}")
print(f"Confidence: {result.confidence:.2f}")
print(f"Used Symbolic Verification: {result.used_symbolic}")
```

### Example 2: Comparing Hybrid vs Pure LLM

```python
from hybrid_reasoner import HybridTemporalReasoner

reasoner = HybridTemporalReasoner()

question = "Meeting lasted 2 hours, 30 min break, 1 hour workshop. Total time?"

# Get comparison
comparison = reasoner.compare_with_pure_llm(question)

print(f"Pure LLM: {comparison['pure_llm_answer']}")
print(f"Hybrid: {comparison['hybrid_answer']}")
print(f"Improvement: {comparison['improvement']}")
```

### Example 3: Accessing Provenance

```python
from hybrid_reasoner import HybridTemporalReasoner

reasoner = HybridTemporalReasoner()
result = reasoner.reason("What events occurred?")

# Get detailed explanation
explanation = reasoner.provenance.generate_explanation(result.provenance_id)
print(explanation)

# Get confidence breakdown
confidence = reasoner.provenance.get_confidence_score(result.provenance_id)
print(f"Overall confidence: {confidence:.2f}")
```

## File Structure

```
prototype/
├── temporal_core.py        # Allen's Interval Algebra implementation
├── llm_interface.py        # Mock LLM with temporal extraction
├── provenance.py           # Provenance tracking system
├── hybrid_reasoner.py      # Main hybrid reasoning system
├── test_cases.py           # 20 comprehensive test cases
├── run_experiments.py      # Experimental evaluation script
├── requirements.txt        # Python dependencies (none required)
├── README.md              # This file
└── test_cases.json        # Exported test cases (generated)
```

## Test Suite

The prototype includes 20 carefully designed test cases:

### By Level
- **Level 1 (Extraction)**: 4 test cases
- **Level 2 (Ordering)**: 9 test cases
- **Level 3 (Calculation)**: 7 test cases

### By Domain
- Medical: 7 tests
- Financial: 3 tests
- Project Management: 6 tests
- Travel: 2 tests
- Academic: 1 test
- General: 1 test

### By Difficulty
- Easy: 7 tests
- Medium: 9 tests
- Hard: 4 tests

Run `python test_cases.py` to see the complete suite.

## Architecture Components

### 1. Temporal Core (`temporal_core.py`)

Implements Allen's Interval Algebra:
- 13 basic temporal relations
- Composition table for constraint propagation
- Temporal constraint solver
- Interval arithmetic

Key classes:
- `AllenRelation`: Enum of 13 relations
- `TimeInterval`: Temporal interval representation
- `AllenAlgebra`: Reasoning operations
- `TemporalConstraintSolver`: CSP solver

### 2. LLM Interface (`llm_interface.py`)

Mock LLM for temporal extraction:
- Simulates realistic LLM behavior
- Configurable accuracy levels
- Domain-specific patterns
- Error injection for testing

Key classes:
- `MockLLM`: Main LLM interface
- `LLMResponse`: Structured extraction results
- `ExtractionLevel`: Reasoning levels enum

### 3. Provenance System (`provenance.py`)

Tracks reasoning provenance:
- Step-by-step reasoning chain
- Confidence tracking
- Explanation generation
- Debugging support

Key classes:
- `ProvenanceTracker`: Main tracking system
- `ProvenanceChain`: Complete reasoning trace
- `ProvenanceNode`: Individual reasoning step

### 4. Hybrid Reasoner (`hybrid_reasoner.py`)

Main integration component:
- Combines LLM and symbolic reasoning
- Verifies LLM outputs
- Resolves conflicts
- Generates provenance-tracked answers

Key class:
- `HybridTemporalReasoner`: Main reasoning pipeline

## Evaluation

To run comprehensive evaluation:

```bash
python run_experiments.py
```

This will:
1. Run all 20 test cases
2. Compare hybrid vs pure LLM approaches
3. Generate accuracy metrics
4. Produce detailed results report
5. Show example provenance traces

Expected outputs:
- Success rates by level and domain
- Confidence score distributions
- Symbolic verification usage statistics
- Example explanations

## Key Results Demonstrated

The prototype demonstrates:

1. **Improved Accuracy**: Symbolic verification catches LLM errors in arithmetic and ordering

2. **Verifiability**: All answers include complete reasoning provenance

3. **Explainability**: Human-readable explanations of reasoning steps

4. **Error Detection**: Identifies inconsistencies in LLM extractions

5. **Confidence Calibration**: Provides well-calibrated confidence scores

## Limitations

This is a proof-of-concept prototype with intentional limitations:

- Mock LLM (not integrated with real LLM APIs)
- Simplified Allen's Algebra composition table
- Basic constraint solver (not full CSP)
- Limited time parsing capabilities
- No learning/adaptation mechanisms

For production use, you would need:
- Real LLM integration (GPT-4, Claude, etc.)
- Full Allen's Algebra implementation
- Advanced CSP solver (Z3, python-constraint)
- Robust NLP for time extraction
- Training data for error patterns

## Extension Ideas

1. **Real LLM Integration**: Connect to GPT-4, Claude, or other LLMs

2. **Advanced Solvers**: Integrate Z3 or other SMT solvers

3. **Learning Component**: Learn from corrections to improve extraction

4. **Broader Coverage**: Extend to other reasoning domains (spatial, causal)

5. **Interactive Mode**: Allow users to correct and refine extractions

6. **Visualization**: Add graphical timeline visualization

7. **Benchmarking**: Evaluate on established temporal reasoning benchmarks

## Research Context

This prototype supports research on:

- Hybrid neuro-symbolic architectures
- Temporal reasoning with LLMs
- Provenance and explainability in AI systems
- Verification of neural system outputs
- Domain-specific language understanding

## Citation

If you use this prototype in research, please cite:

```
Hybrid Neuro-Symbolic Temporal Reasoning Prototype
[Your Name/Institution]
2024
```

## License

This is research/educational code provided as-is for demonstration purposes.

## Contact

For questions or suggestions about this prototype, please contact [your contact information].

## Acknowledgments

- Allen's Interval Algebra: Based on James F. Allen's seminal work (1983)
- Inspired by recent work on neuro-symbolic AI and LLM reasoning
- Built for temporal reasoning research in hybrid AI systems
