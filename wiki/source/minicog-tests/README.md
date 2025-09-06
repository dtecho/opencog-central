# MiniCog Testing Guide

## What is MiniCog?

MiniCog is a minimal installation of the OpenCog cognitive architecture, including core components:

- **CogUtil**: Basic utility library
- **AtomSpace**: The core knowledge representation framework
- **URE (Unified Rule Engine)**: The reasoning engine
- **Unify**: Pattern matching and unification capabilities

## Getting Started

MiniCog provides the basics needed to work with the AtomSpace and perform reasoning operations. This guide will walk you through using MiniCog's core components.

### Prerequisites

Make sure MiniCog is installed by running:

```bash
cd /workspaces/opencog-central/ocpkg
./ocpkg minicog
```

### Components Overview

1. **AtomSpace**: The foundational data structure for storing and querying knowledge
2. **URE**: Engine for applying logical rules for inference
3. **Unify**: Performs pattern matching and unification

## Running Tests

In this directory, you'll find several examples that test and demonstrate MiniCog's functionality:

- `basic_atomspace.scm`: Tests basic AtomSpace operations
- `pattern_matching.scm`: Demonstrates pattern matching capabilities
- `simple_inference.scm`: Shows a simple inference using URE
- `unification_test.scm`: Tests the unification capabilities

To run these tests, use the Guile interpreter:

```bash
guile -l basic_atomspace.scm
```

## Documentation Resources

For more detailed documentation:

- AtomSpace: https://wiki.opencog.org/w/AtomSpace
- Pattern Matching: https://wiki.opencog.org/w/Pattern_matching
- URE: https://wiki.opencog.org/w/URE