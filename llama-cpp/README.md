
# OpenCog-LLaMA Integration

This directory contains a comprehensive implementation that integrates the LLaMA.cpp framework with OpenCog's cognitive architecture, providing a powerful platform for artificial general intelligence research and development.

## Overview

The OpenCog-LLaMA integration combines:
- **LLaMA.cpp**: High-performance LLM inference framework
- **OpenCog AtomSpace**: Symbolic knowledge representation
- **Cognitive Reasoning**: Hybrid symbolic-neural processing
- **Pattern Matching**: Advanced pattern recognition capabilities

## Architecture

```
llama-cpp/
├── include/           # Header files
│   ├── opencog_llama.h      # Main integration interface
│   └── atomspace_llama.h    # AtomSpace integration
├── src/               # Implementation files
│   ├── opencog_llama.cpp    # Core implementation
│   ├── atomspace_llama.cpp  # AtomSpace interface
│   ├── cognitive_inference.cpp
│   ├── pattern_matching.cpp
│   └── memory_management.cpp
├── examples/          # Usage examples
│   └── basic_reasoning.cpp
├── tools/             # Utility tools
│   └── cognitive_shell.cpp
└── CMakeLists.txt     # Build configuration
```

## Features

### 1. Hybrid Reasoning
- **Symbolic Reasoning**: Logic-based inference using AtomSpace
- **Neural Processing**: Deep learning capabilities via LLaMA
- **Integrated Cognition**: Seamless combination of both approaches

### 2. Knowledge Management
- **AtomSpace Integration**: Store and retrieve structured knowledge
- **Dynamic Learning**: Update knowledge base from interactions
- **Relationship Mapping**: Model complex conceptual relationships

### 3. Advanced Pattern Recognition
- **Semantic Matching**: Content-aware pattern matching
- **Concept Extraction**: Automatic identification of key concepts
- **Similarity Analysis**: Vector-based similarity computation

### 4. Cognitive Processing
- **Deductive Reasoning**: Logical conclusion derivation
- **Inductive Reasoning**: Pattern-based generalization
- **Abductive Reasoning**: Best explanation inference

## Building

### Prerequisites
- CMake 3.18+
- C++17 compatible compiler
- LLaMA.cpp library (built from 3p/llama.cpp)
- GGML library (built from ggml/)

### Build Steps

1. **Build dependencies:**
```bash
# Build GGML
cd ggml
mkdir build && cd build
cmake ..
make -j

# Build LLaMA.cpp
cd ../../3p/llama.cpp
mkdir build && cd build
cmake ..
make -j
```

2. **Build OpenCog-LLaMA:**
```bash
cd llama-cpp
mkdir build && cd build
cmake ..
make -j
```

## Usage

### Basic Example

```cpp
#include "opencog_llama.h"

int main() {
    using namespace opencog::llama;
    
    OpenCogLLaMA cognitive_system;
    
    // Initialize with model
    if (!cognitive_system.initialize("path/to/model.gguf")) {
        return 1;
    }
    
    // Generate text
    std::string response = cognitive_system.generate_text(
        "What is consciousness?", 200
    );
    
    // Reason about concepts
    std::vector<std::string> concepts = {"mind", "brain", "awareness"};
    std::string reasoning = cognitive_system.reason_about_concepts(concepts);
    
    // Pattern matching
    bool matches = cognitive_system.match_patterns(
        "artificial intelligence", 
        "machine learning and neural networks"
    );
    
    return 0;
}
```

### Interactive Shell

The cognitive shell provides an interactive interface:

```bash
./cognitive_shell path/to/model.gguf

cognitive> generate What is the nature of intelligence?
cognitive> reason intelligence consciousness learning
cognitive> match "cognitive science" "study of mind and intelligence"
cognitive> extract "Machine learning enables artificial intelligence systems"
```

### Available Commands

- `generate <text>` - Generate text continuation
- `reason <concepts>` - Reason about space-separated concepts  
- `match <pattern> <text>` - Check pattern matching
- `extract <text>` - Extract key concepts
- `query <question>` - Process AtomSpace queries
- `embeddings <text>` - Get text embeddings

## API Reference

### Core Classes

#### OpenCogLLaMA
Main integration class providing:
- `initialize(model_path)` - Initialize with LLaMA model
- `generate_text(prompt, max_tokens)` - Text generation
- `get_embeddings(text)` - Vector embeddings
- `reason_about_concepts(concepts)` - Conceptual reasoning
- `match_patterns(pattern, text)` - Pattern matching
- `extract_concepts(text)` - Concept extraction

#### AtomSpaceInterface
Knowledge management interface:
- `create_atom_from_text()` - Create atoms from text
- `query_related_atoms()` - Find related concepts
- `perform_logical_inference()` - Logical reasoning
- `store_generated_knowledge()` - Save new knowledge

#### CognitiveModel
High-level cognitive functions:
- `reason_deductively()` - Deductive inference
- `reason_inductively()` - Inductive generalization
- `reason_abductively()` - Abductive explanation
- `identify_patterns()` - Pattern recognition

## Model Requirements

### Supported Formats
- GGUF format (recommended)
- Quantized models (Q4_0, Q5_0, Q8_0)
- Full precision models (F16, F32)

### Recommended Models
- LLaMA 7B/13B for general reasoning
- Code-specialized models for technical domains
- Instruction-tuned models for better responses

### Memory Requirements
- 7B model: ~4-8GB RAM (depending on quantization)
- 13B model: ~8-16GB RAM
- GPU acceleration supported via CUDA/OpenCL

## Configuration

### Model Parameters
```cpp
llama_model_params params = llama_model_default_params();
params.n_gpu_layers = 32;  // GPU acceleration
params.use_mmap = true;    // Memory mapping
params.use_mlock = true;   // Memory locking
```

### Context Parameters
```cpp
llama_context_params ctx_params = llama_context_default_params();
ctx_params.n_ctx = 4096;   // Context window
ctx_params.n_batch = 512;  // Batch size
ctx_params.seed = 42;      // Random seed
```

## Integration Points

### OpenCog Components
- **AtomSpace**: Knowledge representation and storage
- **Pattern Matcher**: Advanced pattern recognition
- **PLN**: Probabilistic logic networks
- **URE**: Unified rule engine

### External Systems
- **ROS**: Robot operating system integration
- **Web APIs**: REST/GraphQL interfaces
- **Databases**: Persistent knowledge storage
- **Sensors**: Real-time data processing

## Performance Optimization

### CPU Optimization
- Enable SIMD instructions (AVX2, AVX-512)
- Use optimized BLAS libraries
- Adjust thread count for your system

### GPU Acceleration
- CUDA support for NVIDIA GPUs
- OpenCL for AMD/Intel GPUs
- Vulkan for cross-platform acceleration

### Memory Management
- Model quantization for reduced memory usage
- Memory mapping for large models
- Batch processing for efficiency

## Research Applications

### Cognitive Science
- Theory of mind modeling
- Consciousness research
- Learning mechanisms study

### AI Safety
- Interpretable AI systems
- Alignment research
- Robustness testing

### AGI Research
- Multi-modal reasoning
- Transfer learning
- Meta-learning systems

## Contributing

1. Fork the repository
2. Create feature branch
3. Implement changes with tests
4. Submit pull request

### Development Guidelines
- Follow C++ best practices
- Include comprehensive tests
- Document all public APIs
- Maintain backwards compatibility

## License

This project inherits licenses from its dependencies:
- LLaMA.cpp: MIT License
- OpenCog: AGPL v3
- GGML: MIT License

## Support

For questions and support:
- GitHub Issues: Technical problems
- Discussions: General questions
- Documentation: Implementation details
- Examples: Usage patterns

## Roadmap

### Near Term
- [ ] Enhanced pattern matching algorithms
- [ ] Improved memory management
- [ ] Additional reasoning modes
- [ ] Performance optimizations

### Long Term
- [ ] Multi-modal integration (vision, audio)
- [ ] Distributed processing support
- [ ] Advanced learning algorithms
- [ ] Real-time inference optimization

---

This implementation represents a significant step towards artificial general intelligence by combining the power of large language models with sophisticated symbolic reasoning capabilities.
