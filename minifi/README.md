
# Apache MiniNiFi for OpenCog Ecosystem

A lightweight data flow processing system designed for edge computing and resource-constrained environments, integrated with the OpenCog AtomSpace and cognitive architecture.

## Architecture

- **minifi-core/**: Core lightweight flow processing engine
- **minifi-agents/**: Lightweight data processing agents
- **minifi-c2/**: Command and Control protocol implementation
- **minifi-api/**: REST API for remote management
- **minifi-atomspace/**: AtomSpace integration for cognitive data flows
- **minifi-edge/**: Edge computing optimizations

## Features

- Lightweight agent-based architecture
- Remote configuration via C2 protocol
- AtomSpace integration for cognitive processing
- Edge-optimized data flows
- Real-time telemetry and monitoring
- OpenCog integration for intelligent data routing

## Usage

```bash
python minifi/main.py --config minifi/config/minifi.yaml
```

The MiniNiFi agent will connect to the configured C2 server for remote management.

## Configuration

Configure via YAML files in the `config/` directory or through the C2 protocol.
