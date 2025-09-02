
# KoboldCpp OpenCog Integration

This directory contains the integration layer between KoboldCpp and the OpenCog framework.

## Overview

KoboldCpp is a powerful AI text generation framework that supports GGML/GGUF models with features like:
- CPU and GPU inference
- Web UI for easy interaction
- Multiple API endpoints
- Memory management
- Various sampling methods

## Quick Start

1. **Get a GGUF model**: Download a compatible model (e.g., from Hugging Face)

2. **Run KoboldCpp**:
```bash
cd kobold-cpp
python scripts/run_koboldcpp.py --model /path/to/model.gguf --port 5001
```

3. **Access the web interface**: Open http://0.0.0.0:5001 in your browser

## Configuration Options

- `--model`: Path to your GGUF model file (required)
- `--port`: Server port (default: 5001)
- `--context`: Context size (default: 2048)
- `--gpu-layers`: Number of layers to offload to GPU (default: 0)
- `--usecuda`: Enable CUDA acceleration
- `--usevulkan`: Enable Vulkan acceleration

## GPU Acceleration

For better performance with larger models:

### CUDA (NVIDIA)
```bash
python scripts/run_koboldcpp.py --model model.gguf --usecuda --gpu-layers 32
```

### Vulkan (Cross-platform)
```bash
python scripts/run_koboldcpp.py --model model.gguf --usevulkan --gpu-layers 32
```

## API Usage

Test the API:
```bash
python scripts/run_koboldcpp.py --test --port 5001
```

Generate text programmatically:
```python
import requests

payload = {
    "prompt": "Once upon a time",
    "max_length": 100,
    "temperature": 0.7
}

response = requests.post("http://localhost:5001/api/v1/generate", json=payload)
print(response.json())
```

## OpenCog Integration

The integration provides:
- AtomSpace query processing
- Cognitive reasoning capabilities
- Memory management
- Pattern learning

## Model Recommendations

For different use cases:

- **Small/Fast**: 7B parameter models (4-8GB RAM)
- **Balanced**: 13B parameter models (8-16GB RAM)  
- **Large/Quality**: 30B+ parameter models (16GB+ RAM)

Popular models:
- `L3-8B-Stheno-v3.2-Q4_K_S.gguf` (smaller, faster)
- `LLaMA2-13B-Tiefighter.Q4_K_S.gguf` (balanced)
- `gemma-3-27b-it-abliterated.q4_k_m.gguf` (larger, higher quality)

## Troubleshooting

1. **Out of memory**: Reduce `--gpu-layers` or use smaller model
2. **Slow inference**: Increase `--gpu-layers` or use GPU acceleration
3. **Connection refused**: Check if port is available and firewall settings

## Building from Source

To build the C++ integration:
```bash
cd kobold-cpp
mkdir build && cd build
cmake ..
make -j$(nproc)
```
