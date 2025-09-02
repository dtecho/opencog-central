
# Apache NiFi Integration for OpenCog Ecosystem

This module provides Apache NiFi-like data flow processing capabilities integrated with the OpenCog AtomSpace and cognitive architecture.

## Architecture

- **nifi-core/**: Core flow processing engine
- **nifi-processors/**: Data processing components
- **nifi-web/**: Web UI for flow design and monitoring
- **nifi-api/**: REST API for programmatic control
- **nifi-atomspace/**: AtomSpace integration processors
- **nifi-cognitive/**: Cognitive processing workflows

## Features

- Visual flow designer
- AtomSpace data connectors
- Cognitive processing pipelines
- Real-time monitoring
- OpenCog integration

## Usage

```bash
python nifi/main.py --port 8080
```

Access the web interface at http://localhost:8080/nifi
