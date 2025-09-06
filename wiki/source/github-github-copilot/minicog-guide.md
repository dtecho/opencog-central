# MiniCog Testing and Usage Guide

## Overview

MiniCog is a minimal installation of the OpenCog cognitive architecture, including core components:

- **CogUtil**: Basic utility library
- **AtomSpace**: The core knowledge representation framework
- **URE (Unified Rule Engine)**: The reasoning engine
- **Unify**: Pattern matching and unification capabilities

This guide provides instructions for using MiniCog and explains the test suite created to demonstrate its functionality.

## Core Components

### AtomSpace

The AtomSpace is OpenCog's primary knowledge representation system. It's a hypergraph database designed to store relationships between entities, with support for:

- **Nodes**: Represent entities or concepts
- **Links**: Represent relationships between entities
- **Values**: Attach data to nodes and links
- **Atomese**: The programming language for AtomSpace

### URE (Unified Rule Engine)

The reasoning system that allows for:
- Forward and backward chaining inference
- Rule-based deduction
- Probabilistic reasoning

### Unify

The pattern matching and unification system that provides:
- Variable binding
- Pattern matching across complex structures
- Support for type constraints

## How to Use These Tests

1. First, ensure MiniCog is properly installed by running:
   ```bash
   cd /workspaces/opencog-central/ocpkg
   ./ocpkg minicog
   ```

2. Then you can run any of the test scripts using Guile:
   ```bash
   guile -l /workspaces/opencog-central/minicog-tests/basic_atomspace.scm
   ```

3. To modify or extend these examples, open the script files in your favorite editor and experiment with different patterns, rules, or knowledge structures.

## What You'll Learn

By exploring the provided examples, you'll learn:

- **Knowledge Representation**: How to create and manipulate the AtomSpace knowledge representation
- **Pattern Matching**: How to perform complex pattern matching queries on knowledge
- **Inference**: How to set up and execute inference rules using URE
- **Unification**: How to use the unification system for advanced pattern matching

Each script is thoroughly commented to explain what's happening at each step, making them useful not just as tests but also as learning materials.

## Test Suite Contents

1. **basic_atomspace.scm**: 
   - Creating nodes and links
   - Adding values to atoms
   - Performing basic queries
   - Accessing and modifying the AtomSpace

2. **pattern_matching.scm**:
   - Creating a knowledge base about animals and their properties
   - Performing simple and complex pattern matches
   - Using multiple variables in patterns
   - Finding specific relationships in the knowledge base

3. **simple_inference.scm**:
   - Setting up a rule-based inference system
   - Implementing the classic "Socrates is mortal" reasoning example
   - Configuring and running the URE
   - Verifying inference results

4. **unification_test.scm**:
   - Creating patterns with variables
   - Matching patterns against expressions
   - Using type constraints in unification
   - Working with complex nested structures

## Next Steps

If you want to extend these examples or create your own tests:

1. **Study the patterns**: Look at the existing examples to understand the core design patterns
2. **Experiment with variations**: Modify the knowledge base or queries to see different results
3. **Combine capabilities**: Try integrating multiple features (e.g., inference with unification)
4. **Build practical applications**: Use these components to solve real-world problems

The MiniCog installation provides core functionality without some of the optional components of the full OpenCog system, but it offers all the essential tools for building cognitive systems and experimenting with knowledge representation and reasoning.

## Common Use Cases

- **Knowledge representation**: Store and query structured information
- **Natural language understanding**: Model the meaning of language
- **Decision making**: Create reasoning systems that can make decisions
- **Cognitive modeling**: Implement models of cognitive processes
- **Data integration**: Combine data from multiple sources in a unified framework

## Tips for Effective Use

1. **Start small**: Begin with simple knowledge structures and gradually build up complexity
2. **Visualize**: Use tools to visualize your AtomSpace to better understand its structure
3. **Test incrementally**: Test your patterns and rules in isolation before combining them
4. **Mind performance**: For large knowledge bases, be mindful of query complexity

---

*This guide was created by GitHub Copilot to help users understand and effectively utilize MiniCog, the minimal OpenCog cognitive architecture installation.*