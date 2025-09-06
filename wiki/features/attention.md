
# Attention System (ECAN)

## Overview
The Economic Attention Networks (ECAN) system manages computational resources in OpenCog by allocating attention to the most relevant atoms in the AtomSpace. It implements a market-based economy for cognitive resource distribution.

## Key Features

### Attention Values
- **Short-Term Importance (STI)**: Current relevance of atoms
- **Long-Term Importance (LTI)**: Historical significance
- **Very Long-Term Importance (VLTI)**: Persistent importance

### Attention Dynamics
- Importance diffusion between connected atoms
- Rent collection from unused atoms
- Forgetting mechanisms for irrelevant information

### Attentional Focus
- Dynamic selection of most important atoms
- Resource allocation based on attention values
- Context-sensitive attention management

## Architecture

### Core Components
- **AttentionBank**: Central attention value storage
- **Importance Diffusion Agent**: Spreads attention through networks
- **Rent Collection Agent**: Removes attention from unused atoms
- **Forgetting Agent**: Removes low-importance atoms

### Attention Mechanisms
- Hebbian learning for connection strengthening
- Economic rent for resource management
- Spreading activation through atom networks
- Competition for limited attention resources

## Usage Examples

### Setting Attention Values
```cpp
#include <opencog/attentionbank/bank/AttentionBank.h>

// Set attention values for an atom
AttentionValuePtr av = createAttentionValue(100, 50, 25);
atom->setAttentionValue(av);

// Get current attention values
AttentionValuePtr current_av = atom->getAttentionValue();
short sti = current_av->getSTI();
short lti = current_av->getLTI();
short vlti = current_av->getVLTI();
```

### Attention Allocation
```scheme
(use-modules (opencog attention))

; Set attention values
(cog-set-av! (Concept "important") (av 100 50 1))

; Get attentional focus
(cog-af)

; Stimulate an atom
(cog-stimulate (Concept "focus-atom") 50)
```

## Configuration

### Attention Parameters
- **Attention Focus Size**: Number of atoms in focus
- **Diffusion Rate**: Speed of importance spreading
- **Rent Amount**: Attention decay per cycle
- **Forgetting Threshold**: Minimum importance to retain

### Economic Settings
- **Starting Funds**: Initial attention budget
- **Wage**: Attention earned by active atoms
- **Rent**: Attention cost for memory occupation
- **Tax**: Attention redistribution mechanism

## Applications

### Cognitive Control
- Working memory management
- Goal prioritization
- Resource allocation

### Learning and Memory
- Relevance-based retention
- Adaptive forgetting
- Experience consolidation

### Perception and Action
- Sensory attention allocation
- Action selection
- Context switching

## Technical Details

### Attention Algebra
- Mathematical operations on attention values
- Attention value arithmetic
- Normalization procedures
- Threshold functions

### Performance Metrics
- Attention distribution statistics
- Focus stability measures
- Resource utilization efficiency
- Memory management effectiveness

### Integration Points
- AtomSpace atom management
- Cognitive agents coordination
- Learning system feedback
- Perception system input

## Implementation Status

### Current Features
- Basic attention value management
- Importance diffusion algorithms
- Rent collection mechanisms
- Attentional focus calculation

### Future Enhancements
- Advanced attention strategies
- Multi-modal attention
- Attention-based learning
- Distributed attention systems
