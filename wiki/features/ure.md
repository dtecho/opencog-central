
# URE (Unified Rule Engine)

## Overview
The Unified Rule Engine (URE) is OpenCog's automated reasoning system that provides backward and forward chaining inference capabilities. It serves as the core reasoning infrastructure for various OpenCog applications.

## Key Features

### Forward Chaining
- Automatic rule application from premises to conclusions
- Configurable inference control strategies
- Support for probabilistic inference

### Backward Chaining
- Goal-directed reasoning from conclusions to premises
- Query-driven inference
- Integration with pattern matching

### Rule Management
- Dynamic rule loading and configuration
- Rule priority and weight management
- Custom rule definition support

## Architecture

### Core Components
- **Rule Engine**: Main inference orchestrator
- **Control System**: Manages inference strategies
- **Rule Base**: Repository of inference rules
- **Inference History**: Tracks reasoning steps

### Integration Points
- AtomSpace for knowledge representation
- PLN for probabilistic logic
- Pattern matcher for rule application
- Attention system for resource allocation

## Usage Examples

### Basic Forward Chaining
```scheme
(use-modules (opencog ure))

; Define a simple rule
(define my-rule
  (BindLink
    (VariableList (Variable "$X") (Variable "$Y"))
    (AndLink
      (Inheritance (Variable "$X") (Concept "human"))
      (Inheritance (Concept "human") (Variable "$Y")))
    (Inheritance (Variable "$X") (Variable "$Y"))))

; Apply forward chaining
(cog-fc my-rule-base (Concept "Socrates"))
```

### Backward Chaining Query
```scheme
; Query for all mortals
(cog-bc my-rule-base 
  (Inheritance (Variable "$X") (Concept "mortal")))
```

## Configuration

### Rule Base Setup
- Rule selection criteria
- Inference termination conditions
- Maximum inference steps
- Complexity penalties

### Performance Tuning
- Memory usage limits
- Inference timeout settings
- Rule application priorities
- Attention allocation parameters

## Applications

### Knowledge Integration
- Automated fact derivation
- Consistency checking
- Knowledge base completion

### Question Answering
- Query resolution
- Explanation generation
- Hypothesis testing

### Learning Systems
- Rule discovery
- Pattern generalization
- Adaptive reasoning

## Technical Details

### Rule Format
- Standard AtomSpace representation
- Support for typed variables
- Probabilistic annotations
- Meta-rule capabilities

### Inference Strategies
- Breadth-first search
- Depth-first search
- Best-first search
- Hybrid approaches

### Integration APIs
- Scheme interface
- Python bindings
- C++ direct access
- REST API endpoints

## Status: Archived
Note: URE is currently archived but contains valuable reasoning algorithms and insights for cognitive architectures.
