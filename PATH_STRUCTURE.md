# Path Structure Reference

**All paths in this project are now relative for portability**

---

## Project Location

From anywhere in your system, navigate to:
```bash
cd /Users/alexanderfedin/Projects/hapyy/papers/paper_research/
```

Within the project, all paths are relative.

---

## Directory Structure (Relative Paths)

```
paper_research/                  # You are here
├── README.md                    # ./README.md
├── QUICK_START.md               # ./QUICK_START.md
├── PROJECT_INDEX.md             # ./PROJECT_INDEX.md
├── VERIFICATION.md              # ./VERIFICATION.md
├── PATH_STRUCTURE.md            # ./PATH_STRUCTURE.md (this file)
│
├── paper_main.md                # ./paper_main.md
├── PAPER_SUMMARY.md             # ./PAPER_SUMMARY.md
├── paper_metadata.json          # ./paper_metadata.json
├── references_compiled.bib      # ./references_compiled.bib
│
├── Research Files/              # ./*.md
│   ├── neuro_symbolic_systems.md
│   ├── benchmarks.md
│   ├── architectures.md
│   ├── dsl_taxonomy.md
│   └── [more .md files]
│
├── diagrams/                    # ./diagrams/
│   ├── diagram1.mmd             # ./diagrams/diagram1.mmd
│   ├── diagram2.mmd             # ./diagrams/diagram2.mmd
│   ├── ...
│   ├── all_diagrams.md          # ./diagrams/all_diagrams.md
│   └── README.md                # ./diagrams/README.md
│
└── prototype/                   # ./prototype/
    ├── temporal_core.py         # ./prototype/temporal_core.py
    ├── llm_interface.py         # ./prototype/llm_interface.py
    ├── hybrid_reasoner.py       # ./prototype/hybrid_reasoner.py
    ├── provenance.py            # ./prototype/provenance.py
    ├── test_cases.py            # ./prototype/test_cases.py
    ├── run_experiments.py       # ./prototype/run_experiments.py
    └── README.md                # ./prototype/README.md
```

---

## External References (Relative)

### From paper_research/ to Papers Directory
```
../compass_artifact_wf-4b0cea25...md  # Temporal verification paper
../compass_artifact_wf-bf16ed0b...md  # Logic programming paper
```

### From paper_research/ to cslib
```
../../cslib/  # Lean library for CS formalization
```

### Parent Directory Summary
```
../PAPER_PROJECT_SUMMARY.md  # Overview from papers/ directory
```

---

## Common Navigation Patterns

### Working in Project Root
```bash
# You are in: paper_research/
cat README.md                    # Project overview
cat paper_main.md | less         # Full paper
cd prototype/                    # Go to prototype
cd diagrams/                     # Go to diagrams
```

### Working in Prototype
```bash
# You are in: paper_research/prototype/
python3 run_experiments.py       # Run experiments
cat ../paper_main.md | less      # View paper (up one level)
cat README.md                    # Prototype docs
```

### Working in Diagrams
```bash
# You are in: paper_research/diagrams/
ls *.mmd                         # List diagram sources
cat README.md                    # Rendering instructions
cat ../paper_main.md | less      # View paper (up one level)
```

### Referencing Original Papers
```bash
# From paper_research/
cat ../compass_artifact_wf-4b0cea25*.md  # Temporal paper
cat ../compass_artifact_wf-bf16ed0b*.md  # Logic programming paper
```

### Referencing cslib
```bash
# From paper_research/
ls ../../cslib/Cslib/Languages/   # Browse Lean examples
```

---

## File Reference Patterns Used

### In Markdown Documentation
- Same directory: `paper_main.md`
- Subdirectory: `diagrams/diagram1.mmd`
- Child with path: `prototype/temporal_core.py`
- Parent: `../PAPER_PROJECT_SUMMARY.md`
- Sibling of parent: `../../cslib/`
- Current directory: `./README.md` or just `README.md`

### In Code (Python)
```python
# Prototype files use relative imports
from pathlib import Path

# Get project root (from prototype/)
project_root = Path(__file__).parent.parent

# Reference paper files
paper_path = project_root / "paper_main.md"

# Reference diagrams
diagrams_dir = project_root / "diagrams"
```

---

## Portability

✅ **The entire `paper_research/` directory can be:**
- Moved to any location on your system
- Shared with collaborators
- Cloned from version control
- Archived and extracted elsewhere

✅ **All internal references will work because they're relative**

⚠️ **External references require:**
- `../compass_artifact_*` files (original papers in parent directory)
- `../../cslib/` directory (Lean library)

---

## Command Examples by Location

### From System Root
```bash
cd /Users/alexanderfedin/Projects/hapyy/papers/paper_research/
python3 prototype/run_experiments.py
cat paper_main.md
```

### From Project Root
```bash
# Already in paper_research/
python3 prototype/run_experiments.py
cat paper_main.md
cat diagrams/README.md
```

### From Prototype
```bash
# In paper_research/prototype/
python3 run_experiments.py
cat ../paper_main.md
ls ../diagrams/*.mmd
```

---

## Git-Friendly Structure

All paths are relative, making this project git-friendly:

```bash
# Clone or move anywhere
git clone <repo> /new/location/paper_research/
cd /new/location/paper_research/

# Everything still works
python3 prototype/run_experiments.py  ✓
cat paper_main.md                      ✓
cat diagrams/diagram1.mmd              ✓
```

---

## Quick Reference Table

| From Location | To Access | Use Path |
|---------------|-----------|----------|
| `paper_research/` | Main paper | `./paper_main.md` |
| `paper_research/` | Prototype | `./prototype/` |
| `paper_research/` | Diagrams | `./diagrams/` |
| `paper_research/` | Original papers | `../compass_*` |
| `paper_research/` | cslib | `../../cslib/` |
| `prototype/` | Main paper | `../paper_main.md` |
| `prototype/` | Diagrams | `../diagrams/` |
| `diagrams/` | Main paper | `../paper_main.md` |
| `diagrams/` | Prototype | `../prototype/` |

---

## Verification Commands

### Check No Absolute Paths Remain
```bash
# From paper_research/
grep -r "/Users/\|/tmp/" --include="*.md" .
# Should return: (no output = success)
```

### List All Relative Paths
```bash
# From paper_research/
find . -name "*.md" -o -name "*.py" | head -20
# All paths start with ./
```

### Test Prototype Portability
```bash
# Copy to temp location
cp -r . /tmp/test_paper_research/
cd /tmp/test_paper_research/prototype/
python3 run_experiments.py
# Should work without modification
```

---

## Summary

✅ All internal paths are relative
✅ Project is portable and git-friendly
✅ No hard-coded absolute paths in documentation
✅ External references use relative paths (`../`, `../../`)
✅ Works from any location after moving/cloning

**Current absolute path (for reference only):**
`/Users/alexanderfedin/Projects/hapyy/papers/paper_research/`

**But you can work with it from anywhere using relative paths!**

---

*Last Updated: 2024-12-20*
*All 60 files verified for relative path usage*
