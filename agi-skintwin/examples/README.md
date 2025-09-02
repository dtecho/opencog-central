
# SkinTwin Examples

This directory contains example scripts and tutorials demonstrating the capabilities of the SkinTwin multiscale skin modeling system.

## Basic Examples

### 1. Molecular System Creation
```python
from skin_twin.cython_integration import SkinModelInterface

# Initialize interface
skin_interface = SkinModelInterface()

# Create molecular system
molecules = [
    {'name': 'water', 'formula': 'H2O'},
    {'name': 'ceramide_ns', 'formula': 'C18H35NO3'},
    {'name': 'collagen_1', 'sequence': 'GLYPROALAHYP', 'type': 'protein'}
]

molecule_handles = skin_interface.create_molecular_system(molecules)
```

### 2. Cellular Population Modeling
```python
# Define cell specifications
cell_specs = [
    {
        'type': 'keratinocyte',
        'count': 100,
        'components': ['nucleus', 'keratin_filaments']
    },
    {
        'type': 'fibroblast',
        'count': 50, 
        'components': ['nucleus', 'endoplasmic_reticulum']
    }
]

cell_handles = skin_interface.create_cellular_population(cell_specs)
```

### 3. Tissue Architecture
```python
# Create tissue layers
tissue_specs = [
    {'name': 'stratum_corneum', 'cells': cell_handles[:20]},
    {'name': 'stratum_basale', 'cells': cell_handles[20:]}
]

tissue_handles = skin_interface.create_tissue_architecture(tissue_specs)
```

### 4. Permeation Analysis
```python
# Simulate molecular permeation
test_molecule = skin_interface.skin_atomspace.create_molecule("caffeine", "CN1C=NC2=C1C(=O)N(C(=O)N2C)C")
barrier = skin_interface.atomspace.add_node("ConceptNode", "stratum_corneum_barrier")

concentrations = skin_interface.simulate_permeation(test_molecule, barrier, 100)
```

## Advanced Examples

See individual example files for more detailed demonstrations:

- `basic_modeling.py` - Basic skin model creation
- `permeation_study.py` - Detailed permeation analysis
- `multiscale_simulation.py` - Full multiscale simulation
- `web_interface_demo.py` - Web interface demonstration
- `data_analysis.py` - Statistical analysis and visualization

## Running Examples

```bash
# Basic example
python examples/basic_modeling.py

# Web interface demo
python examples/web_interface_demo.py

# Full simulation
python examples/multiscale_simulation.py
```

## Requirements

- SkinTwin package installed
- OpenCog AtomSpace (or mock implementation)
- Required Python dependencies (see requirements.txt)

## Troubleshooting

If you encounter import errors, ensure that:
1. SkinTwin is properly installed (`pip install -e .`)
2. OpenCog dependencies are available
3. Cython extensions are compiled
