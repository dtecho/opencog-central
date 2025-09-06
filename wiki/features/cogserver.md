
# CogServer - Multi-User Network Server

## Overview

The **CogServer** is OpenCog's multi-user network server that provides remote access to AtomSpace instances and cognitive operations. It enables distributed cognitive architectures and collaborative AI development through a sophisticated client-server framework.

## Key Features

### Network Architecture
- **Multi-User Access**: Simultaneous connections from multiple clients
- **Protocol Support**: Telnet, WebSocket, REST API, and custom protocols
- **Authentication**: User authentication and session management
- **Load Balancing**: Distributed processing across multiple servers

### Client Interfaces
- **Shell Access**: Interactive Scheme and Python shells
- **Web Interface**: Browser-based AtomSpace exploration
- **API Endpoints**: RESTful web services
- **Custom Protocols**: Extensible protocol framework

### Module System
- **Dynamic Loading**: Runtime module loading and unloading
- **Agent Framework**: Cognitive agents with lifecycle management
- **Request Handlers**: Custom command processors
- **Event System**: Publish-subscribe event notifications

## Architecture Components

### Core Server
- **Request Router**: Distributes requests to appropriate handlers
- **Session Manager**: Manages client sessions and state
- **Module Registry**: Tracks loaded modules and agents
- **Configuration System**: Flexible server configuration

### Communication Layers
- **Socket Manager**: Low-level network communication
- **Protocol Handlers**: Protocol-specific message processing
- **Message Queue**: Asynchronous message handling
- **Event Dispatcher**: Real-time event distribution

### Security Framework
- **Access Control**: Fine-grained permission system
- **SSL/TLS Support**: Encrypted communications
- **Rate Limiting**: Protection against abuse
- **Audit Logging**: Security event tracking

## Network Protocols

### Telnet Interface
```bash
# Connect via telnet
telnet localhost 17001

# Execute Scheme commands
guile> (cog-atomspace)
guile> (Concept "hello")
```

### WebSocket API
```javascript
// WebSocket connection
const ws = new WebSocket('ws://localhost:17002');

// Send AtomSpace queries
ws.send(JSON.stringify({
  cmd: 'query',
  pattern: '(Concept "test")'
}));
```

### REST API
```bash
# HTTP GET requests
curl http://localhost:17003/api/v1/atoms

# POST new atoms
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"type": "Concept", "name": "example"}' \
  http://localhost:17003/api/v1/atoms
```

## Module Development

### Agent Framework
```cpp
class MyAgent : public Agent {
public:
    virtual void run() {
        // Agent logic here
        std::cout << "Agent running..." << std::endl;
    }
};

// Register agent
server().registerAgent(INVOKE, new MyAgent());
```

### Request Handlers
```cpp
class CustomHandler : public GenericShell {
public:
    virtual std::string eval(const std::string& command) {
        // Process custom commands
        return "Result: " + process(command);
    }
};
```

### Module Registration
```cpp
extern "C" {
    void opencog_module_init(CogServer& server) {
        server.registerHandler("custom", new CustomHandler());
    }
}
```

## Configuration

### Server Configuration
```scheme
; cogserver.conf
(define MODULES
  "opencog/modules/libPythonModule.so"
  "opencog/modules/libSchemeShell.so"
  "opencog/modules/libRestAPIModule.so")

(define SERVER_PORT 17001)
(define LOG_LEVEL "info")
```

### Network Settings
```ini
# Network configuration
[network]
port = 17001
interface = 0.0.0.0
max_connections = 100
timeout = 300
```

## Distributed Architecture

### Multi-Server Setup
- **Primary Server**: Main AtomSpace instance
- **Secondary Servers**: Read replicas and specialized processors
- **Load Balancer**: Request distribution
- **Synchronization**: Cross-server state management

### Clustering Features
- **Node Discovery**: Automatic cluster member detection
- **Health Monitoring**: Server health checks and failover
- **Data Replication**: AtomSpace synchronization
- **Distributed Queries**: Cross-cluster query execution

## Monitoring and Management

### Health Monitoring
```bash
# Server status
echo "stats" | nc localhost 17001

# Performance metrics
curl http://localhost:17003/api/v1/stats
```

### Log Management
- **Structured Logging**: JSON-formatted log entries
- **Log Levels**: Configurable verbosity
- **Rotation**: Automatic log file rotation
- **Remote Logging**: Centralized log aggregation

### Performance Metrics
- **Connection Statistics**: Active connections and throughput
- **Request Metrics**: Response times and error rates
- **Resource Usage**: CPU, memory, and network utilization
- **AtomSpace Metrics**: Knowledge base statistics

## Security Features

### Authentication
```cpp
// User authentication
bool authenticateUser(const std::string& username, 
                     const std::string& password) {
    return authManager.verify(username, password);
}
```

### Access Control
```scheme
; Permission configuration
(define-permission "read-atoms" 
  (lambda (user atom) 
    (has-role? user "reader")))

(define-permission "write-atoms"
  (lambda (user atom)
    (has-role? user "writer")))
```

## Integration Examples

### Python Client
```python
import socket
import json

# Connect to CogServer
client = socket.socket()
client.connect(('localhost', 17001))

# Send Scheme command
client.send(b'(Concept "test")\n')
response = client.recv(1024)
```

### JavaScript Web Client
```javascript
class CogServerClient {
    constructor(url) {
        this.ws = new WebSocket(url);
        this.setupHandlers();
    }
    
    query(pattern) {
        return new Promise((resolve) => {
            this.ws.send(JSON.stringify({
                cmd: 'query',
                pattern: pattern
            }));
        });
    }
}
```

## Use Cases

### Development Environment
- Interactive AtomSpace exploration
- Collaborative AI development
- Real-time debugging and monitoring
- Rapid prototyping and testing

### Production Deployment
- Scalable AI service hosting
- Multi-tenant cognitive architectures
- High-availability configurations
- Enterprise integration

### Research Applications
- Distributed cognitive experiments
- Multi-agent simulations
- Large-scale knowledge processing
- Collaborative research platforms

## Related Components

- **AtomSpace**: Core knowledge representation
- **REST API**: HTTP-based web services
- **WebSocket Handler**: Real-time web communication
- **Python Shell**: Interactive Python interface
- **Scheme Shell**: Interactive Scheme interface

## Performance Characteristics

### Scalability
- **Concurrent Connections**: Thousands of simultaneous clients
- **Request Throughput**: High-performance request processing
- **Memory Efficiency**: Optimized memory usage
- **Network Optimization**: Efficient protocol implementations

### Reliability
- **Fault Tolerance**: Graceful error handling
- **Connection Recovery**: Automatic reconnection
- **State Persistence**: Session state management
- **Graceful Shutdown**: Clean server termination

The CogServer enables the creation of sophisticated distributed cognitive architectures, providing the network infrastructure needed for scalable AI applications and collaborative cognitive computing.
