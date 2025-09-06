
# RWKV.cpp Implementation

A comprehensive C++ implementation and wrapper around the RWKV.cpp library, providing an easy-to-use interface for RWKV language model inference.

## Features

- **C++ Wrapper**: Clean, modern C++ interface around the C API
- **Text Generation**: Built-in text generation with temperature and top-p sampling
- **Multi-threading**: Configurable thread count for optimal performance
- **GPU Acceleration**: Optional GPU layer offloading support
- **Utilities**: Model information, benchmarking, and conversion tools
- **Examples**: Ready-to-use examples for chat and inference

## Project Structure

```
rwkv-cpp/
├── include/           # Header files
├── src/              # Implementation files
├── examples/         # Example applications
├── tools/            # Utility tools
├── tests/            # Unit tests (optional)
└── CMakeLists.txt    # Build configuration
```

## Building

### Prerequisites

- CMake 3.12 or higher
- C++17 compatible compiler
- RWKV.cpp library (included in ../3p/rwkv.cpp/)

### Build Instructions

```bash
cd rwkv-cpp
mkdir build && cd build
cmake ..
make -j$(nproc)
```

### Build Options

```bash
# Release build (optimized)
cmake .. -DCMAKE_BUILD_TYPE=Release

# Debug build
cmake .. -DCMAKE_BUILD_TYPE=Debug

# Enable tests
cmake .. -DBUILD_TESTING=ON
```

## Usage

### Basic Model Loading

```cpp
#include "rwkv_wrapper.h"

// Load model
auto model = std::make_shared<rwkv_cpp::RWKVModel>(
    "path/to/model.bin", 
    4,  // threads
    0   // GPU layers
);

// Check if loaded
if (model->is_loaded()) {
    std::cout << "Model loaded successfully!" << std::endl;
}
```

### Text Generation

```cpp
// Create text generator
rwkv_cpp::TextGenerator generator(model);

// Generate text
std::string response = generator.generate(
    "Hello, how are you?",  // prompt
    100,                    // max tokens
    0.8f,                  // temperature
    0.9f                   // top_p
);

std::cout << response << std::endl;
```

### Manual Token Evaluation

```cpp
// Prepare buffers
std::vector<float> state(model->get_state_size(), 0.0f);
std::vector<float> logits(model->get_logits_size());

// Evaluate tokens
std::vector<uint32_t> tokens = {72, 101, 108, 108, 111}; // "Hello"
bool success = model->eval(tokens, nullptr, state.data(), logits.data());
```

## Examples

### Simple Chat

```bash
./examples/simple_chat model.bin 4 0
```

Interactive chat interface with the RWKV model.

### Model Information

```bash
./examples/model_info model.bin
```

Display detailed information about a model file.

### Benchmark

```bash
./examples/benchmark model.bin 4 100
```

Benchmark model performance with specified threads and token count.

## Tools

### Model Conversion

```bash
./tools/rwkv_convert input.bin output.bin
```

Convert between different RWKV model formats (placeholder).

### Model Quantization

```bash
./tools/rwkv_quantize input.bin output.bin Q4_0
```

Quantize models to reduce size and memory usage.

## API Reference

### RWKVModel Class

- `RWKVModel(path, threads, gpu_layers)` - Constructor
- `eval(tokens, state_in, state_out, logits_out)` - Evaluate tokens
- `get_vocab_size()` - Get vocabulary size
- `get_embed_size()` - Get embedding dimensions
- `get_layer_count()` - Get number of layers
- `get_state_size()` - Get state buffer size
- `get_logits_size()` - Get logits buffer size
- `is_loaded()` - Check if model is loaded

### TextGenerator Class

- `TextGenerator(model)` - Constructor
- `generate(prompt, max_tokens, temperature, top_p)` - Generate text
- `set_tokenizer(path)` - Set tokenizer (placeholder)

## Performance Tips

1. **Thread Count**: Use 4-8 threads for optimal CPU performance
2. **GPU Layers**: Offload layers to GPU if available for better performance
3. **Quantization**: Use quantized models (Q4_0, Q4_1) to reduce memory usage
4. **State Reuse**: Reuse state buffers between evaluations for efficiency

## Model Support

Supports RWKV models in the following formats:
- RWKV v4, v5, v6, v7 architectures
- FP32, FP16 precision
- Quantized formats: Q4_0, Q4_1, Q5_0, Q5_1, Q8_0

## System Information

View supported CPU features:
```cpp
std::cout << rwkv_cpp::RWKVModel::get_system_info() << std::endl;
```

## License

This implementation follows the same license as the underlying RWKV.cpp library.

## Contributing

1. Follow C++17 standards
2. Use consistent naming conventions
3. Add appropriate error handling
4. Include examples for new features
5. Update documentation

## Troubleshooting

### Model Loading Issues
- Verify model file exists and is accessible
- Check model format compatibility
- Ensure sufficient system memory

### Performance Issues
- Adjust thread count based on CPU cores
- Consider GPU acceleration for supported models
- Use quantized models for memory-constrained systems

### Build Issues
- Ensure CMake 3.12+ is installed
- Verify C++17 compiler support
- Check RWKV.cpp library dependencies
