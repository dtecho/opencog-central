
# P-Lingua Examples

This directory contains example P-systems demonstrating various features of the P-Lingua framework.

## Basic Examples

- `basic/transition.pli` - Simple transition P-system with evolution rules
- `basic/communication.pli` - P-system with communication rules
- `basic/dissolution.pli` - P-system with membrane dissolution

## Advanced Examples

- `tissue/cell_network.pli` - Tissue P-system with cell communication
- `neural/spiking.pli` - Spiking neural P-system
- `probabilistic/random_walk.pli` - Probabilistic P-system

## Applications

- `biology/gene_regulation.pli` - Gene regulatory network model
- `math/arithmetic.pli` - Arithmetic operations in P-systems
- `algorithms/sorting.pli` - Sorting algorithm implementation

## Running Examples

```bash
# Simulate a basic transition P-system
python -m plingua.tools.simulate basic/transition.pli --trace --verbose

# Run with custom parameters
python -m plingua.tools.simulate basic/transition.pli --max-steps 50 --output results.json
```

## File Format

All examples use the standard P-Lingua syntax:

- `@model<type>` - Declares the P-system type
- `@mu = structure` - Defines membrane structure
- `@ms(label) = objects` - Sets initial multisets
- Rule definitions follow standard P-Lingua notation
