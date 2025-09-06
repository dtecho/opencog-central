
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
# P-Lingua Model Examples

This directory contains various P-system models implemented in P-Lingua for different domains:

## Basic Models

### transition.pli
Basic transition P-system demonstrating fundamental membrane operations.

### evolution.pli
Evolution P-system with membrane division and object evolution rules.

### division.pli
Division P-system showing membrane division and object migration.

## Cognitive Models

### attention.pli
Models cognitive attention mechanisms with working memory and long-term memory membranes.

### reasoning.pli
Implements logical reasoning with knowledge base, working memory, and inference engine membranes.

## Biological Models

### cell_division.pli
Biological cell division model with nucleus, cytoplasm, and cellular processes.

## Neural Models

### echo_state.pli
Echo State Network implementation using membrane computing principles with input layer, reservoir, and output layer membranes.

## Usage

To simulate any model:
```bash
python -m plingua.tools.simulate examples/basic/transition.pli
```

Each model demonstrates different aspects of membrane computing:
- Membrane structure and hierarchy
- Object evolution rules
- Membrane division and dissolution
- Communication between membranes
- Priorities and maximal parallelism
