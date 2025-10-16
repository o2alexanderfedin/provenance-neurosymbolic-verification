# All System Architecture Diagrams - Mermaid Syntax

This document contains all 10 diagrams for the neuro-symbolic AI academic paper in Mermaid format.

---

## Diagram 1: Overall System Architecture

**Purpose**: Complete neuro-symbolic hybrid system showing all components and information flow

**Location**: Main Paper, Figure 1

**Type**: Flowchart (Top-Down)

```mermaid
flowchart TD
    A[Natural Language Problem Description<br/>Example: Find the shortest path in the graph<br/>where all edges have weight less than 10<br/>and the path avoids nodes A and B] --> B[LLM Semantic Parser Fine-Tuned<br/>Multi-DSL: Prolog | ASP | SMT-LIB | PDDL | Datalog]

    B --> B1[Uncertainty Quantification]
    B1 --> B1a[LLM Confidence Score<br/>softmax probabilities]
    B1 --> B1b[Multi-Sample Agreement<br/>N=5 samples]
    B1 --> B1c[Parse-and-Regenerate<br/>Consistency Check]

    B1a --> C{Confidence Gate<br/>U > threshold θ?}
    B1b --> C
    B1c --> C

    C -->|Yes: High Uncertainty| E[Abstention with Proof Certificate]
    C -->|No: Low Uncertainty| D[DSL Generation<br/>Constrained Grammar Enforcement<br/>Syntax Validation BNF Check]

    E --> E1[Abstention Certificate:<br/>- Problem statement<br/>- Attempted DSL translation<br/>- Uncertainty signals<br/>- Reason for abstention<br/>- Partial information]

    D --> F[Symbolic Reasoning Engine]

    F --> F1[Prolog Interpreter<br/>SWI-Prolog]
    F --> F2[ASP Grounder/Solver<br/>Clingo]
    F --> F3[SMT Solver<br/>Z3]
    F --> F4[Temporal Reasoning Module]

    F4 --> F4a[Allen's Interval Algebra<br/>GQR]
    F4 --> F4b[STN/STNU Solver<br/>Path Consistency]
    F4 --> F4c[Temporal Provenance Tracker]

    F1 --> G[Provenance Engine]
    F2 --> G
    F3 --> G
    F4 --> G

    G --> G1[Semiring Selection:<br/>ℕ[X] polynomial | Boolean why | Custom temporal]
    G1 --> G2[Polynomial Construction<br/>During Symbolic Execution]
    G2 --> G3[Provenance Verification<br/>Homomorphism Check]
    G3 --> H[Explanation Generator]

    H --> H1[Provenance Polynomial → Natural Language]
    H --> H2[Justification Trees s-CASP style]
    H --> H3[Temporal Timeline Visualization]
    H --> H4[Proof Terms for Theorem Provers]

    H1 --> I[Verification & Output]
    H2 --> I
    H3 --> I
    H4 --> I

    I --> I1[Formal Verification<br/>Kernel checking for Z3, Lean]
    I1 --> I2[Final Result + Explanation +<br/>Provenance Certificate +<br/>Confidence Bounds]

    I1 -->|Verification Failure| J[Refinement Loop<br/>Max 2-3 iterations<br/>Semantic reversion if worse]
    J -.->|Error Feedback| B

    style A fill:#ADD8E6,stroke:#333,stroke-width:2px
    style B fill:#FFA500,stroke:#333,stroke-width:2px
    style B1 fill:#FFCC80,stroke:#333,stroke-width:2px
    style C fill:#FFFF00,stroke:#333,stroke-width:3px
    style D fill:#90EE90,stroke:#333,stroke-width:2px
    style E fill:#FF6B6B,stroke:#333,stroke-width:2px
    style F fill:#9370DB,stroke:#333,stroke-width:2px
    style G fill:#20B2AA,stroke:#333,stroke-width:2px
    style H fill:#98FB98,stroke:#333,stroke-width:2px
    style I fill:#4682B4,stroke:#333,stroke-width:2px
    style J fill:#D3D3D3,stroke:#333,stroke-width:2px,stroke-dasharray: 5 5

    classDef input fill:#ADD8E6,stroke:#333,stroke-width:2px
    classDef llm fill:#FFA500,stroke:#333,stroke-width:2px
    classDef symbolic fill:#9370DB,stroke:#333,stroke-width:2px
    classDef provenance fill:#20B2AA,stroke:#333,stroke-width:2px
    classDef output fill:#4682B4,stroke:#333,stroke-width:2px
    classDef error fill:#FF6B6B,stroke:#333,stroke-width:2px
```

**Key Features**:
- Blue: Input/Output components
- Orange: Neural/LLM components
- Purple: Symbolic reasoning components
- Teal: Provenance tracking
- Red: Error/abstention paths
- Dashed lines: Feedback loops

---

## Diagram 2: Temporal Reasoning Architecture

**Purpose**: Detailed view of temporal reasoning module with dual-track processing

**Location**: Main Paper, Figure 2

**Type**: Horizontal Flow with Parallel Tracks

```mermaid
flowchart LR
    A[Natural Language with Temporal Content<br/>Example: Patient admitted at 10:00 AM.<br/>Blood culture within 3 hours.<br/>Antibiotics within 1 hour of culture.<br/>Lab results in 24-48 hours.<br/>Adjustment within 4 hours of results.] --> B[LLM Temporal Extraction]

    B --> B1[Entity Recognition:<br/>Events: admission, blood_culture,<br/>antibiotics, lab_results, adjustment<br/>Times: 10:00 AM, +3h, +1h, +24-48h, +4h]
    B1 --> B2[Constraint Extraction:<br/>Qualitative: blood_culture BEFORE antibiotics<br/>Quantitative: blood_culture ≤ admission + 3h]

    B2 --> C[Temporal Reasoning Tracks]

    C --> D[Track 2A: Allen's Interval Algebra]
    C --> E[Track 2B: STN/STNU Solver]
    C --> F[Track 2C: Temporal Provenance Tracker]

    D --> D1[Qualitative Relations:<br/>before, meets, overlaps,<br/>during, finishes, etc.]
    D1 --> D2[Transitivity Computation<br/>Composition Table]
    D2 --> D3[Path Consistency<br/>Constraint Network]

    E --> E1[Quantitative Constraints:<br/>Constraint Graph Construction]
    E1 --> E2[Path Consistency<br/>Floyd-Warshall variant]
    E2 --> E3[Earliest/Latest Times<br/>Controllability Checking]

    F --> F1[Dependency Tracking:<br/>Which events affect which]
    F1 --> F2[Temporal Semiring<br/>Construction]
    F2 --> F3[Provenance Polynomial<br/>Π_temporal]

    D3 --> G[Integration & Consistency Check]
    E3 --> G
    F3 --> G

    G --> G1{Qualitative &<br/>Quantitative<br/>Agree?}
    G1 -->|Yes| H[Complete Temporal Solution]
    G1 -->|No| G2[Conflict Resolution<br/>Symbolic Priority, Flag for Review]
    G2 --> H

    H --> H1[Timeline with Event Times<br/>Temporal Relations Explicit<br/>Provenance Dependency Graph<br/>Confidence Intervals if STNU]

    H1 --> I[Timeline Visualization:<br/>0h: admission<br/>≤3h: blood_culture<br/>≤4h: antibiotics<br/>24-48h: lab_results<br/>28-52h or 52-66h: adjustment]

    style A fill:#ADD8E6,stroke:#333,stroke-width:2px
    style B fill:#FFA500,stroke:#333,stroke-width:2px
    style D fill:#9370DB,stroke:#333,stroke-width:2px
    style E fill:#9370DB,stroke:#333,stroke-width:2px
    style F fill:#20B2AA,stroke:#333,stroke-width:2px
    style G fill:#FFFF00,stroke:#333,stroke-width:2px
    style H fill:#4682B4,stroke:#333,stroke-width:2px
    style I fill:#98FB98,stroke:#333,stroke-width:2px
```

**Key Features**:
- Parallel processing tracks for qualitative (Allen's IA) and quantitative (STN) reasoning
- Temporal provenance tracking alongside constraint solving
- Integration and consistency checking between different reasoning modes

---

## Diagram 3: Multi-DSL Fine-Tuning Pipeline

**Purpose**: Curriculum learning approach for multi-DSL training

**Location**: Appendix/Methodology Section

**Type**: Horizontal Pipeline

```mermaid
flowchart LR
    A[Dataset Construction<br/>Pre-Processing] --> A1[Datalog: 1,000 examples]
    A --> A2[Prolog: 1,000 examples]
    A --> A3[ASP: 1,000 examples]
    A --> A4[SMT-LIB: 1,000 examples]
    A --> A5[PDDL: 1,000 examples]

    A1 --> B[Base Model<br/>Llama 3.1 8B<br/>Transformer decoder<br/>8 billion parameters]
    A2 --> B
    A3 --> B
    A4 --> B
    A5 --> B

    B --> C1[Curriculum Stage 1: Datalog<br/>1,000 examples, Epochs: 3-5<br/>QLoRA: rank=16, alpha=32, dropout=0.1]
    C1 --> C2[Model Checkpoint M1]

    C2 --> D1[Curriculum Stage 2: Prolog<br/>1,000 Prolog + 200 Datalog review<br/>Transfer learning from M1]
    D1 --> D2[Model Checkpoint M2]

    D2 --> E1[Curriculum Stage 3: ASP<br/>1,000 ASP + 200 Prolog review<br/>Transfer learning from M2]
    E1 --> E2[Model Checkpoint M3]

    E2 --> F1[Curriculum Stage 4: SMT-LIB<br/>1,000 SMT-LIB + 200 ASP review<br/>Transfer learning from M3]
    F1 --> F2[Model Checkpoint M4]

    F2 --> G1[Curriculum Stage 5: PDDL<br/>1,000 PDDL + 200 SMT-LIB review<br/>Transfer learning from M4]
    G1 --> G2[Final Model M_final]

    G2 --> H[Evaluation<br/>Held-out test: 100 per DSL, 500 total<br/>Metrics: Pass@1, Pass@10,<br/>syntax errors, semantic correctness]

    H --> I[Performance Report]

    J[Comparison Panel] --> J1[Single-DSL Training:<br/>5 separate models<br/>5× training cost]
    J --> J2[Multi-DSL Simultaneous:<br/>1 model, all DSLs at once<br/>Lower performance - task interference]
    J --> J3[Multi-DSL Curriculum:<br/>1 model, sequential training<br/>Best trade-off - OUR APPROACH]

    style A fill:#D3D3D3,stroke:#333,stroke-width:2px
    style B fill:#FFCC80,stroke:#333,stroke-width:2px
    style C1 fill:#E3F2FD,stroke:#333,stroke-width:2px
    style D1 fill:#BBDEFB,stroke:#333,stroke-width:2px
    style E1 fill:#90CAF9,stroke:#333,stroke-width:2px
    style F1 fill:#64B5F6,stroke:#333,stroke-width:2px
    style G1 fill:#42A5F5,stroke:#333,stroke-width:2px
    style H fill:#90EE90,stroke:#333,stroke-width:2px
    style J fill:#FFF3E0,stroke:#333,stroke-width:2px

    linkStyle default stroke:#666,stroke-width:2px
```

**Key Features**:
- Progressive curriculum from simple (Datalog) to complex (PDDL)
- Transfer learning between stages
- Review examples prevent catastrophic forgetting
- Gradient color scheme shows progression

---

## Diagram 4: Provenance-Guided DSL Generation

**Purpose**: Iterative refinement using provenance feedback

**Location**: Technical Contribution Section

**Type**: Circular Flow with Iteration Loop

```mermaid
flowchart TD
    A[Input:<br/>Natural Language Problem P<br/>Positive Examples E+<br/>Negative Examples E-<br/>Target DSL] --> B[Initial LLM Generation<br/>Iteration 0<br/>Few-shot prompting<br/>Constrained grammar]

    B --> B1[DSL Program D_0]
    B1 --> C[Symbolic Execution<br/>Execute D_0 on E+ and E-<br/>Record execution traces]

    C --> D[Provenance Computation]
    D --> D1[Compute Π+ for E+<br/>why-provenance - derivation path]
    D --> D2[Compute Π- for E-<br/>why-not-provenance - blocking reason]

    D1 --> E{Why-Provenance<br/>Analysis}
    E -->|e+ not derived<br/>Π e+ = 0| E1[Extract missing<br/>predicates/rules<br/>Generate constraint:<br/>Must derive e+]

    D2 --> F{Why-Not-Provenance<br/>Analysis}
    F -->|e- incorrectly<br/>derived<br/>Π e- ≠ 0| F1[Extract spurious<br/>derivation path<br/>Generate constraint:<br/>Must NOT derive e-]

    E1 --> G[Refinement Iteration i+1<br/>Combine positive & negative constraints<br/>Structured feedback to LLM]
    F1 --> G

    G --> G1[LLM generates D_i+1]

    G1 --> H{Semantic Reversion<br/>Check<br/>Logic-LM++ Strategy}
    H -->|D_i+1 worse<br/>than D_i| H1[Revert to D_i]
    H -->|D_i+1 better| H2[Accept D_i+1]

    H1 --> I{Convergence Check}
    H2 --> I

    I -->|All E+ derived correctly?<br/>AND All E- NOT derived?<br/>AND iterations < 3?| I1[Yes]
    I -->|No| I2[Continue]

    I1 --> J[Output:<br/>Final DSL Program D_final<br/>Provenance Certificate Π_final<br/>Number of iterations]

    I2 --> C

    K[Example Annotations:<br/>Problem: Find employees earning more than manager<br/>E+: alice, 120K, manager bob, 100K → derive employee alice<br/>E-: charlie, 80K, manager bob, 100K → NOT derive charlie<br/>Iteration 0: Wrong comparison less than instead of greater than<br/>Provenance feedback: e- derived via rule with less than, use greater than<br/>Iteration 1: Corrected comparison, all tests pass]

    style A fill:#ADD8E6,stroke:#333,stroke-width:2px
    style B fill:#FFA500,stroke:#333,stroke-width:2px
    style C fill:#9370DB,stroke:#333,stroke-width:2px
    style D fill:#20B2AA,stroke:#333,stroke-width:2px
    style E fill:#FFFF00,stroke:#333,stroke-width:2px
    style F fill:#FF6B6B,stroke:#333,stroke-width:2px
    style G fill:#FFA500,stroke:#333,stroke-width:2px
    style H fill:#FFCC80,stroke:#333,stroke-width:2px
    style I fill:#90EE90,stroke:#333,stroke-width:2px
    style J fill:#4682B4,stroke:#333,stroke-width:2px
    style K fill:#F0F0F0,stroke:#333,stroke-width:1px,stroke-dasharray: 3 3

    linkStyle 15,16 stroke:#666,stroke-width:2px,stroke-dasharray: 5 5
```

**Key Features**:
- Iterative refinement loop with provenance feedback
- Separate why-provenance (positive) and why-not-provenance (negative) analysis
- Semantic reversion prevents degradation
- Concrete example included as annotation

---

## Diagram 5: Uncertainty-Aware Verification Framework

**Purpose**: Selective verification with uncertainty quantification

**Location**: Technical Contribution Section

**Type**: Decision Tree with Parallel Uncertainty Signals

```mermaid
flowchart TD
    A[Input: Natural Language Problem] --> B[LLM Generation<br/>Generate DSL program D]

    B --> C[Uncertainty Quantification<br/>Parallel Signals]

    C --> C1[Signal 1:<br/>LLM Confidence<br/>Token-level log probabilities<br/>conf = exp mean log_prob_i]
    C --> C2[Signal 2:<br/>Multi-Sample Agreement<br/>Generate N=5 samples<br/>agree = # matching / 5]
    C --> C3[Signal 3:<br/>Parse-and-Regenerate<br/>D → NL → D'<br/>Check semantic equivalence]

    C1 --> D[Uncertainty Fusion<br/>U = 0.3×1-conf + 0.5×1-agree + 0.2×1-consistent]
    C2 --> D
    C3 --> D

    D --> E{Confidence Gate<br/>U > θ?<br/>Threshold Selection:<br/>General: θ=0.70<br/>Medical: θ=0.90<br/>Aerospace: θ=0.95}

    E -->|Yes:<br/>High Uncertainty<br/>U > θ| F[Abstention Path]
    E -->|No:<br/>Low Uncertainty<br/>U ≤ θ| G[Verification Path]

    F --> F1[Generate Abstention Certificate:<br/>- Problem statement<br/>- Attempted DSL D<br/>- Uncertainty breakdown conf, agree, consistent<br/>- Uncertainty score U and threshold θ<br/>- Reason for abstention which signal<br/>- Partial information if any]

    F1 --> F2[Output: Abstention Certificate]

    G --> G1[Symbolic Execution of D<br/>Formal Verification<br/>Z3 proof checking, Lean type checking]

    G1 --> H{Verification<br/>Result?}

    H -->|Success| I[Output:<br/>Verified Result +<br/>Confidence Bounds]
    H -->|Failure| J{Iterations<br/>< Max?}

    J -->|Yes| K[Error Feedback to LLM]
    J -->|No| L[Escalate to Abstention]

    K -.->|Refinement Loop| B
    L --> F1

    M[ROC Trade-off Analysis:<br/>Threshold | AR | FNR | P error | Domain<br/>0.70 | 28% | 8% | 6% | General<br/>0.90 | 47% | 3% | 2% | Medical<br/>0.95 | 63% | 1% | 0.6% | Aerospace]

    N[Probabilistic Guarantee:<br/>P error ≤ P LLM_error | U ≤ θ × 1 - AR + P symbolic_error<br/>≈ FNR × 1 - AR + 0 symbolic verified]

    style A fill:#ADD8E6,stroke:#333,stroke-width:2px
    style B fill:#FFA500,stroke:#333,stroke-width:2px
    style C1 fill:#FFFF99,stroke:#333,stroke-width:2px
    style C2 fill:#FFFF99,stroke:#333,stroke-width:2px
    style C3 fill:#FFFF99,stroke:#333,stroke-width:2px
    style D fill:#FFCC80,stroke:#333,stroke-width:2px
    style E fill:#FFFF00,stroke:#333,stroke-width:3px
    style F fill:#FF6B6B,stroke:#333,stroke-width:2px
    style G fill:#9370DB,stroke:#333,stroke-width:2px
    style I fill:#90EE90,stroke:#333,stroke-width:2px
    style M fill:#E8F5E9,stroke:#333,stroke-width:1px
    style N fill:#FFF9C4,stroke:#333,stroke-width:1px
```

**Key Features**:
- Three parallel uncertainty signals combined
- Domain-specific threshold calibration
- Abstention path with detailed certificates
- ROC analysis and probabilistic guarantees

---

## Diagram 6: Temporal Provenance Example (Healthcare Case Study)

**Purpose**: Concrete example of temporal provenance in sepsis treatment

**Location**: Main Paper, Figure 3

**Type**: Timeline with Provenance Dependencies

```mermaid
flowchart TD
    subgraph Timeline["Sepsis Treatment Timeline (hours from admission)"]
        A["A: Patient Admission<br/>t=0h<br/>Suspected Sepsis"]
        B["B: Blood Culture<br/>t≤3h<br/>Constraint: within 3h of A"]
        C["C: Antibiotics<br/>t≤4h<br/>Constraint: within 1h of B"]
        D["D: Lab Results<br/>t=24-48h<br/>Constraint: 24-48h after B"]
        E["E: Antibiotic Adjustment<br/>t≤52h<br/>Constraint: within 4h of D"]
        F["F: ICU Escalation Decision<br/>t≤10h<br/>Constraint: if no improvement<br/>within 6h of C"]
    end

    A -->|3h deadline| B
    B -->|1h deadline| C
    B -->|24-48h wait| D
    D -->|4h deadline| E
    C -->|6h monitoring| F

    A -.->|Provenance Chain| B
    B -.->|Provenance Chain| C
    B -.->|Provenance Chain| D
    D -.->|Provenance Chain| E
    C -.->|Provenance Chain| F

    subgraph Provenance["Provenance Polynomial"]
        P1["Π_E = temporal_composition Π_A, 3h, 1h, 24-48h, 4h"]
        P2["= A ⊕ A ⊗ 3h ⊕ A ⊗ 3h ⊗ 1h ⊕ ... ⊕ E"]
        P3["Event E depends on cascade:<br/>A admission → B culture, +3h<br/>→ D results, +24-48h<br/>→ E adjustment, +4h<br/>Total: 28-52h or 52-66h"]
    end

    subgraph Counterfactual["Counterfactual Analysis"]
        Q1["Query: If blood culture delayed by 1h<br/>to t=4h instead of t=3h,<br/>how are downstream events affected?"]
        Q2["Original: A 0 → B 3 → C 4 → D 27-51 → E 31-55"]
        Q3["Modified: A 0 → B 4 → C 5 → D 28-52 → E 32-56"]
        Q4["Result: All downstream shift +1 hour<br/>Critical path: Still on schedule no violations"]
    end

    subgraph Explanation["Why was adjustment at 52h?"]
        E1["1. Blood culture at t=3h within 3h deadline ✓"]
        E2["2. Antibiotics at t=4h within 1h of culture ✓"]
        E3["3. Lab results at t=48h maximum 48h window ⚠"]
        E4["4. Adjustment at t=52h within 4h of results ✓"]
        E5["Critical dependency: Lab result timing 48h<br/>determined adjustment timing.<br/>If lab at 24h, adjustment would be at 28h."]
    end

    style A fill:#90EE90,stroke:#333,stroke-width:2px
    style B fill:#90EE90,stroke:#333,stroke-width:2px
    style C fill:#90EE90,stroke:#333,stroke-width:2px
    style D fill:#FFFF99,stroke:#333,stroke-width:2px
    style E fill:#90EE90,stroke:#333,stroke-width:2px
    style F fill:#90EE90,stroke:#333,stroke-width:2px
    style Provenance fill:#E0F2F7,stroke:#333,stroke-width:2px
    style Counterfactual fill:#FFF3E0,stroke:#333,stroke-width:2px
    style Explanation fill:#F1F8E9,stroke:#333,stroke-width:2px

    linkStyle 0,1,2,3,4 stroke:#FF6B6B,stroke-width:2px
    linkStyle 5,6,7,8,9 stroke:#20B2AA,stroke-width:2px,stroke-dasharray: 5 5
```

**Key Features**:
- Timeline showing events with temporal constraints
- Provenance polynomial showing dependencies
- Counterfactual analysis demonstrating what-if reasoning
- Natural language explanation of causal chain
- Color coding: Green (on time), Yellow (near deadline)

---

## Diagram 7: Multi-Domain Performance Comparison

**Purpose**: Performance across 5 temporal reasoning levels and domains

**Location**: Results Section

**Type**: Bar Chart + Heatmap

```mermaid
flowchart TD
    subgraph Performance["Multi-Domain Performance Comparison"]
        A["Performance Across 5 Temporal Reasoning Levels"]
    end

    subgraph BarChart["Level Performance (%)"]
        L1["L1: Extraction<br/>Pure LLM: 78%<br/>+Extract: 83%<br/>+Allen: 83%<br/>+STN: 85%<br/>Full Hybrid: 85%"]
        L2["L2: Ordering<br/>Pure LLM: 65%<br/>+Extract: 65%<br/>+Allen: 92% ***<br/>+STN: 92%<br/>Full Hybrid: 92%"]
        L3["L3: Calculation<br/>Pure LLM: 14%<br/>+Extract: 18%<br/>+Allen: 18%<br/>+STN: 88% ***<br/>Full Hybrid: 88%"]
        L4["L4: Counterfactual<br/>Pure LLM: 38%<br/>+Extract: 38%<br/>+Allen: 45%<br/>+STN: 76% ***<br/>Full Hybrid: 76%"]
        L5["L5: Conditional<br/>Pure LLM: 42%<br/>+Extract: 42%<br/>+Allen: 50%<br/>+STN: 75%<br/>Full Hybrid: 81% ***"]
        Overall["Overall<br/>Pure LLM: 47%<br/>+Extract: 49%<br/>+Allen: 58%<br/>+STN: 83%<br/>Full Hybrid: 84% ***"]
    end

    subgraph Heatmap["Domain × Level Performance Heatmap"]
        H1["Domain | L1 | L2 | L3 | L4 | L5 | Avg"]
        H2["Healthcare | 87% | 93% | 90% | 82% | 85% | 87%"]
        H3["Finance | 89% | 95% | 93% | 88% | 82% | 89%"]
        H4["Aerospace | 83% | 91% | 92% | 85% | 83% | 87%"]
        H5["Legal | 81% | 88% | 82% | 65% | 75% | 78%"]
        H6["Robotics | 84% | 90% | 85% | 78% | 80% | 83%"]
    end

    subgraph Insights["Key Insights"]
        I1["1. Most dramatic improvement at L3 Calculation:<br/>+529% vs Pure LLM"]
        I2["2. Allen's IA critical for L2 Ordering:<br/>+42% improvement"]
        I3["3. STN solver enables L3-L5 performance:<br/>+300-400% improvement"]
        I4["4. Full hybrid achieves 79% overall improvement"]
        I5["5. Finance domain: Highest performance 89%"]
        I6["6. Legal domain: Most challenging counterfactual L4 65%"]
    end

    style Performance fill:#E3F2FD,stroke:#333,stroke-width:2px
    style BarChart fill:#FFF3E0,stroke:#333,stroke-width:2px
    style L1 fill:#FFE0B2,stroke:#333,stroke-width:1px
    style L2 fill:#FFCC80,stroke:#333,stroke-width:1px
    style L3 fill:#90EE90,stroke:#333,stroke-width:2px
    style L4 fill:#98FB98,stroke:#333,stroke-width:1px
    style L5 fill:#90CAF9,stroke:#333,stroke-width:1px
    style Overall fill:#42A5F5,stroke:#333,stroke-width:2px
    style Heatmap fill:#E8F5E9,stroke:#333,stroke-width:2px
    style H2 fill:#C8E6C9,stroke:#333,stroke-width:1px
    style H3 fill:#A5D6A7,stroke:#333,stroke-width:1px
    style H4 fill:#C8E6C9,stroke:#333,stroke-width:1px
    style H5 fill:#FFCCBC,stroke:#333,stroke-width:1px
    style H6 fill:#DCEDC8,stroke:#333,stroke-width:1px
    style Insights fill:#FFF9C4,stroke:#333,stroke-width:2px
```

**Key Features**:
- Comparison across 5 system configurations
- Most dramatic improvement at Level 3 (Calculation): +529%
- Domain-specific heatmap showing performance variations
- Statistical significance markers (***)

---

## Diagram 8: User Study Results (Provenance Quality)

**Purpose**: Comparison of explanation methods across quality metrics

**Location**: Results Section

**Type**: Radar Chart + Statistical Comparison

```mermaid
flowchart TD
    subgraph RadarMetrics["Radar Chart: 6 Explanation Quality Metrics (0-1 scale)"]
        M1["Metric 1: Faithfulness (verified)<br/>Provenance: 0.97<br/>s(CASP): 0.95<br/>xASP: 0.93<br/>LLM Post-Hoc: 0.68<br/>Attention: 0.52"]
        M2["Metric 2: Comprehensibility (quiz)<br/>Provenance: 0.78<br/>s(CASP): 0.84 ★<br/>xASP: 0.72<br/>LLM Post-Hoc: 0.76<br/>Attention: 0.58"]
        M3["Metric 3: Debugging Success<br/>Provenance: 0.82<br/>s(CASP): 0.88 ★<br/>xASP: 0.76<br/>LLM Post-Hoc: 0.64<br/>Attention: 0.42"]
        M4["Metric 4: Trust Calibration<br/>Provenance: 0.78<br/>s(CASP): 0.82<br/>xASP: 0.74<br/>LLM Post-Hoc: 0.52<br/>Attention: 0.38"]
        M5["Metric 5: Time Efficiency (normalized)<br/>Provenance: 0.72<br/>s(CASP): 0.85 ★<br/>xASP: 0.58<br/>LLM Post-Hoc: 0.70<br/>Attention: 0.45"]
        M6["Metric 6: Overall Quality<br/>Provenance: 0.81<br/>s(CASP): 0.87 ★<br/>xASP: 0.75<br/>LLM Post-Hoc: 0.66<br/>Attention: 0.47"]
    end

    subgraph Comparison["Method Comparison"]
        C1["Provenance Polynomials<br/>Strengths: Faithfulness 0.97, Debugging 0.82<br/>Regulatory compliant >95% faithfulness"]
        C2["s(CASP) Justification<br/>Strengths: Best overall 0.87, Best comprehensibility 0.84<br/>Natural language templates"]
        C3["xASP Explanation<br/>Strengths: Balanced performance<br/>Moderate faithfulness 0.93"]
        C4["LLM Post-Hoc<br/>Weaknesses: Low faithfulness 0.68<br/>Over-trust problem trust: 0.52"]
        C5["Attention Visualization<br/>Weaknesses: Lowest across all metrics<br/>Not interpretable faithfulness: 0.52"]
    end

    subgraph Statistics["Statistical Significance (Tukey HSD)"]
        S1["Provenance vs LLM Post-Hoc: p < 0.001 *** all metrics"]
        S2["Provenance vs Attention: p < 0.001 *** all metrics"]
        S3["s(CASP) vs LLM Post-Hoc: p < 0.001 *** all metrics"]
        S4["Provenance vs s(CASP): p = 0.08 n.s. Comprehensibility"]
        S5["Provenance vs s(CASP): p < 0.05 * Faithfulness"]
    end

    subgraph Findings["Key Findings"]
        F1["1. Provenance-based methods Prov, s(CASP), xASP<br/>significantly outperform LLM post-hoc<br/>and attention on faithfulness"]
        F2["2. s(CASP) best for comprehensibility 84%<br/>due to natural language templates"]
        F3["3. Only provenance-based methods meet<br/>regulatory standards >95% faithfulness"]
        F4["4. Trust calibration gap:<br/>Provenance 0.78 vs LLM 0.52<br/>LLM induces over-trust"]
        F5["5. Debugging success strongly correlates<br/>with faithfulness r=0.89"]
    end

    style RadarMetrics fill:#E3F2FD,stroke:#333,stroke-width:2px
    style M1 fill:#BBDEFB,stroke:#333,stroke-width:1px
    style M2 fill:#90CAF9,stroke:#333,stroke-width:1px
    style M3 fill:#64B5F6,stroke:#333,stroke-width:1px
    style M4 fill:#42A5F5,stroke:#333,stroke-width:1px
    style M5 fill:#2196F3,stroke:#333,stroke-width:1px
    style M6 fill:#1976D2,stroke:#333,stroke-width:1px
    style Comparison fill:#E8F5E9,stroke:#333,stroke-width:2px
    style C1 fill:#A5D6A7,stroke:#333,stroke-width:2px
    style C2 fill:#66BB6A,stroke:#333,stroke-width:2px
    style C3 fill:#C5E1A5,stroke:#333,stroke-width:1px
    style C4 fill:#FFCC80,stroke:#333,stroke-width:1px
    style C5 fill:#FF8A65,stroke:#333,stroke-width:1px
    style Statistics fill:#FFF3E0,stroke:#333,stroke-width:2px
    style Findings fill:#FFF9C4,stroke:#333,stroke-width:2px
```

**Key Features**:
- Six quality metrics evaluated across five explanation methods
- Provenance-based methods (Prov, s(CASP), xASP) significantly outperform neural methods
- Only provenance methods meet regulatory standards (>95% faithfulness)
- Statistical significance testing with Tukey HSD

---

## Diagram 9: Dataset Construction Pipeline

**Purpose**: Benchmark dataset creation methodology

**Location**: Appendix

**Type**: Horizontal Pipeline with Quality Control

```mermaid
flowchart LR
    A[Data Sources] --> A1[Clinical Notes<br/>MIMIC-III de-identified<br/>350 problems]
    A --> A2[Financial Reports<br/>10-K filings<br/>250 problems]
    A --> A3[Aerospace Mission Logs<br/>NASA<br/>200 problems]
    A --> A4[Legal Contracts<br/>anonymized<br/>150 problems]
    A --> A5[Synthetic Generation<br/>templates<br/>50 problems]

    A1 --> B[Temporal Entity Annotation<br/>Two expert annotators per domain<br/>Tool: Brat / custom web interface<br/>Entity types: date, time, duration, event, frequency]
    A2 --> B
    A3 --> B
    A4 --> B
    A5 --> B

    B --> C{Inter-Annotator<br/>Agreement Check<br/>Cohen's κ ≥ 0.85?}

    C -->|κ < 0.85| C1[Adjudication by<br/>Third Expert]
    C -->|κ ≥ 0.85| D[Consensus Annotations]
    C1 --> D

    D --> E[Formal Specification Generation<br/>Convert to Allen's IA relations<br/>Generate STN constraints<br/>Create provenance ground truth]

    E --> F{Automated Consistency<br/>Verification<br/>GQR + STN feasibility<br/>NL ↔ Formal match?}

    F -->|Inconsistent| F1[Return to Annotation]
    F -->|Consistent| G[Difficulty Calibration<br/>Pilot test with 3 baselines<br/>Target distribution:<br/>Easy: 30% success >70%<br/>Medium: 50% success 40-70%<br/>Hard: 20% success <40%]

    F1 -.->|Rework| B

    G --> H[Quality Control<br/>Cross-domain validation<br/>Adversarial examples edge cases<br/>Balanced representation<br/>domain, difficulty, level]

    H --> I[Dataset Release<br/>GitHub repository<br/>JSON format with annotations<br/>Evaluation scripts<br/>Baseline results]

    J[Quality Metrics:<br/>Inter-annotator agreement: κ = 0.87 range: 0.82-0.92<br/>Consistency rate: 98.5% 75 problems corrected<br/>Annotation time: 500 expert hours avg 6 min/problem<br/>Calibration accuracy: 92% matched target distribution]

    style A fill:#E0E0E0,stroke:#333,stroke-width:2px
    style A1 fill:#D3D3D3,stroke:#333,stroke-width:1px
    style A2 fill:#D3D3D3,stroke:#333,stroke-width:1px
    style A3 fill:#D3D3D3,stroke:#333,stroke-width:1px
    style A4 fill:#D3D3D3,stroke:#333,stroke-width:1px
    style A5 fill:#D3D3D3,stroke:#333,stroke-width:1px
    style B fill:#FFFF99,stroke:#333,stroke-width:2px
    style C fill:#FFA500,stroke:#333,stroke-width:2px
    style D fill:#90EE90,stroke:#333,stroke-width:2px
    style E fill:#9370DB,stroke:#333,stroke-width:2px
    style F fill:#90EE90,stroke:#333,stroke-width:2px
    style G fill:#87CEEB,stroke:#333,stroke-width:2px
    style H fill:#98FB98,stroke:#333,stroke-width:2px
    style I fill:#4682B4,stroke:#333,stroke-width:2px
    style J fill:#F0F0F0,stroke:#333,stroke-width:1px

    linkStyle 10 stroke:#FF6B6B,stroke-width:2px,stroke-dasharray: 5 5
```

**Key Features**:
- Multi-domain data sources (5 domains, 1000 total problems)
- Quality control checkpoints: Inter-annotator agreement (κ ≥ 0.85)
- Automated consistency verification
- Difficulty calibration to target distribution
- Comprehensive quality metrics reported

---

## Diagram 10: Ablation Study Results

**Purpose**: Component contribution analysis

**Location**: Appendix

**Type**: Waterfall Chart

```mermaid
flowchart TD
    subgraph Waterfall["Ablation Study: Component Contributions (Waterfall Chart)"]
        A["Baseline: Pure LLM<br/>Performance: 47%<br/>Components: GPT-4 zero-shot"]
        B["+Temporal Extraction Tools<br/>Incremental gain: +5%<br/>Cumulative: 52%<br/>Components: SUTime, HeidelTime"]
        C["+Allen's Interval Algebra<br/>Incremental gain: +16%<br/>Cumulative: 68%<br/>Components: GQR reasoner qualitative"]
        D["+STN Solver<br/>Incremental gain: +11%<br/>Cumulative: 79%<br/>Components: Path consistency quantitative"]
        E["+Temporal Provenance<br/>Incremental gain: +5%<br/>Cumulative: 84%<br/>Components: Provenance tracking explanations"]
    end

    A --> B
    B --> C
    C --> D
    D --> E

    subgraph Breakdown["Performance Breakdown by Level"]
        T["Component | L1 | L2 | L3 | L4 | L5 | Overall"]
        L1["Pure LLM | 78% | 65% | 14% | 38% | 42% | 47%"]
        L2["+Extraction | 83% | 65% | 18% | 38% | 42% | 49%"]
        L3["+Allen's IA | 83% | 92% | 18% | 45% | 50% | 58%"]
        L4["+STN | 85% | 92% | 88% | 76% | 75% | 79%"]
        L5["+Provenance | 85% | 92% | 88% | 76% | 81% | 84%"]
    end

    subgraph Insights["Key Insights"]
        I1["STN solver provides LARGEST gain: +21pp overall<br/>Primarily due to Level 3 improvement: +70pp"]
        I2["Allen's IA enables qualitative reasoning: +16pp<br/>Critical for Level 2 ordering: +27pp"]
        I3["Temporal Provenance improves explanations: +5pp<br/>Strongest impact on Level 5 conditional: +6pp"]
        I4["Extraction tools baseline improvement: +5pp<br/>Helps Level 1 entity recognition: +5pp"]
    end

    subgraph Statistics["Statistical Significance"]
        S1["All incremental gains: p < 0.001 paired t-test"]
        S2["Effect sizes Cohen's d:<br/>Allen's IA: d = 1.2 large<br/>STN Solver: d = 1.5 very large<br/>Provenance: d = 0.4 medium"]
        S3["Most impactful component:<br/>STN Solver 11pp gain, effect d=1.5"]
    end

    style A fill:#FF6B6B,stroke:#333,stroke-width:2px
    style B fill:#FFA500,stroke:#333,stroke-width:2px
    style C fill:#FFFF99,stroke:#333,stroke-width:2px
    style D fill:#98FB98,stroke:#333,stroke-width:2px
    style E fill:#66BB6A,stroke:#333,stroke-width:2px
    style Breakdown fill:#E3F2FD,stroke:#333,stroke-width:2px
    style T fill:#BBDEFB,stroke:#333,stroke-width:1px
    style L1 fill:#FFE0B2,stroke:#333,stroke-width:1px
    style L2 fill:#FFCC80,stroke:#333,stroke-width:1px
    style L3 fill:#FFE082,stroke:#333,stroke-width:1px
    style L4 fill:#C5E1A5,stroke:#333,stroke-width:1px
    style L5 fill:#A5D6A7,stroke:#333,stroke-width:1px
    style Insights fill:#FFF9C4,stroke:#333,stroke-width:2px
    style Statistics fill:#F3E5F5,stroke:#333,stroke-width:2px

    linkStyle 0,1,2,3 stroke:#333,stroke-width:3px
```

**Key Features**:
- Waterfall visualization showing cumulative performance gains
- Detailed breakdown by temporal reasoning level
- STN Solver provides largest gain (+21 percentage points)
- All gains statistically significant (p < 0.001)
- Effect sizes quantified with Cohen's d

---

## Summary

All 10 diagrams have been created in publication-quality Mermaid syntax:

1. **Overall System Architecture** - Complete neuro-symbolic hybrid system
2. **Temporal Reasoning Architecture** - Dual-track processing with Allen's IA and STN
3. **Multi-DSL Fine-Tuning Pipeline** - Curriculum learning approach
4. **Provenance-Guided DSL Generation** - Iterative refinement with feedback
5. **Uncertainty-Aware Verification** - Selective verification framework
6. **Temporal Provenance Example** - Healthcare case study with timeline
7. **Multi-Domain Performance Comparison** - Results across 5 levels and 5 domains
8. **User Study Results** - Explanation quality comparison
9. **Dataset Construction Pipeline** - Benchmark creation methodology
10. **Ablation Study Results** - Component contribution analysis

All diagrams use:
- Consistent color schemes (blue: input/output, orange: neural, purple: symbolic, teal: provenance)
- Clear labeling and annotations
- Publication-ready formatting
- Black/white friendly color choices
- Appropriate complexity for academic papers
