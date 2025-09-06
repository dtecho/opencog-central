
# User Guides

## Getting Started

### Quick Start Tutorial

Welcome to OpenCog! This guide will get you up and running in 15 minutes.

#### Prerequisites

- Linux/macOS/Windows system
- 8GB+ RAM recommended
- Python 3.8+
- Git installed

#### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/opencog/opencog.git
   cd opencog
   ```

2. **Install Dependencies**
   ```bash
   # Ubuntu/Debian
   sudo apt-get install build-essential cmake cxxtest libboost-all-dev guile-3.0-dev
   
   # macOS
   brew install cmake boost guile cxxtest
   ```

3. **Build Core Components**
   ```bash
   mkdir build && cd build
   cmake ..
   make -j$(nproc)
   sudo make install
   ```

#### First Steps

1. **Start the CogServer**
   ```bash
   cogserver
   ```

2. **Connect via Python**
   ```python
   from opencog.atomspace import AtomSpace
   from opencog.type_constructors import *
   
   # Create atoms
   atomspace = AtomSpace()
   concept = ConceptNode("Hello OpenCog")
   print(f"Created: {concept}")
   ```

3. **Try Pattern Matching**
   ```scheme
   ; Connect via Scheme
   (use-modules (opencog))
   
   ; Create knowledge
   (ConceptNode "Socrates")
   (ConceptNode "man")
   (ConceptNode "mortal")
   
   (InheritanceLink
     (ConceptNode "Socrates")
     (ConceptNode "man"))
     
   (InheritanceLink
     (ConceptNode "man")
     (ConceptNode "mortal"))
   
   ; Query knowledge
   (cog-bind
     (BindLink
       (VariableNode "$who")
       (InheritanceLink
         (VariableNode "$who")
         (ConceptNode "mortal"))
       (VariableNode "$who")))
   ```

## Installation Guides

### Automated Installation (Recommended)

Using the OCPkg installer:

```bash
wget -O - https://raw.githubusercontent.com/opencog/ocpkg/master/ocpkg | bash
```

This will:
- Install all dependencies
- Build core components
- Set up environment
- Run basic tests

### Manual Installation

#### Ubuntu 20.04/22.04

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install -y \
    build-essential cmake cxxtest \
    libboost-all-dev libguile-3.0-dev \
    python3-dev python3-pip cython3 \
    postgresql-client-common libpq-dev \
    librocksdb-dev

# Install Python dependencies
pip3 install --user \
    opencog-atomspace \
    opencog-cogutil \
    opencog-cogserver

# Clone and build
git clone --recursive https://github.com/opencog/atomspace
cd atomspace
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install
```

#### macOS with Homebrew

```bash
# Install Homebrew if needed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install dependencies
brew install cmake boost guile cxxtest postgresql rocksdb

# Build from source
git clone --recursive https://github.com/opencog/atomspace
cd atomspace
mkdir build && cd build
cmake ..
make -j$(sysctl -n hw.ncpu)
make install
```

#### Docker Installation

```bash
# Run OpenCog in Docker
docker run -it opencog/opencog:latest

# With local filesystem access
docker run -it -v $(pwd):/workspace opencog/opencog:latest
```

### Configuration

#### Environment Setup

Add to your `.bashrc` or `.zshrc`:

```bash
export OPENCOG_PATH=/usr/local/share/opencog
export PYTHON_PATH=$PYTHON_PATH:/usr/local/lib/python3/dist-packages
export GUILE_LOAD_PATH=/usr/local/share/guile/site/3.0
```

#### CogServer Configuration

Create `~/.opencog/opencog.conf`:

```
# Basic CogServer configuration
SERVER_PORT           = 17001
LOG_FILE              = /tmp/cogserver.log
LOG_LEVEL             = info
PROMPT                = "opencog> "
MODULES               = opencog/cogserver/shell/libscheme-shell.so
                        opencog/cogserver/shell/libpy-shell.so
```

## Core Tutorials

### AtomSpace Basics

#### Creating Atoms

```python
from opencog.atomspace import AtomSpace
from opencog.type_constructors import *

# Initialize
atomspace = AtomSpace()

# Create nodes
person = ConceptNode("Alice")
animal = ConceptNode("cat")
pet = ConceptNode("Whiskers")

# Create links
ownership = InheritanceLink(
    pet,
    animal
)

relationship = EvaluationLink(
    PredicateNode("owns"),
    ListLink(person, pet)
)

print(f"AtomSpace contains {atomspace.size()} atoms")
```

#### Truth Values and Confidence

```python
# Create atoms with truth values
belief = InheritanceLink(
    ConceptNode("birds"),
    ConceptNode("can-fly"),
    TruthValue(0.9, 0.8)  # strength=0.9, confidence=0.8
)

# Update truth values
belief.set_tv(TruthValue(0.95, 0.9))

# Query truth values
tv = belief.get_tv()
print(f"Strength: {tv.mean}, Confidence: {tv.confidence}")
```

#### Pattern Matching

```scheme
;; Define a pattern
(define find-animals
  (BindLink
    (VariableNode "$x")
    (InheritanceLink
      (VariableNode "$x")
      (ConceptNode "animal"))
    (VariableNode "$x")))

;; Execute the pattern
(cog-bind find-animals)
```

### PLN Reasoning Tutorial

#### Basic Deduction

```python
from opencog.pln import *

# Create reasoning chain
atomspace = AtomSpace()
chainer = BackwardChainer(atomspace)

# Add knowledge
atomspace.add_link(INHERITANCE_LINK, [
    atomspace.add_node(CONCEPT_NODE, "Socrates"),
    atomspace.add_node(CONCEPT_NODE, "human")
], TruthValue(1.0, 0.9))

atomspace.add_link(INHERITANCE_LINK, [
    atomspace.add_node(CONCEPT_NODE, "human"),
    atomspace.add_node(CONCEPT_NODE, "mortal")
], TruthValue(0.95, 0.8))

# Define target
target = atomspace.add_link(INHERITANCE_LINK, [
    atomspace.add_node(CONCEPT_NODE, "Socrates"),
    atomspace.add_node(CONCEPT_NODE, "mortal")
])

# Execute reasoning
chainer.add_rule(DeductionRule())
result = chainer.do_chain(target)
print(f"Reasoning result: {result}")
```

### MOSES Learning Tutorial

#### Feature Selection

```python
from opencog.moses import moses
import pandas as pd

# Load data
data = pd.read_csv('dataset.csv')
target_column = 'target'

# Configure MOSES
moses_params = {
    'max_evals': 1000,
    'max_score': 1.0,
    'complexity_ratio': 3,
    'population_size': 500
}

# Run evolution
result = moses.run(
    input_table=data,
    target_feature=target_column,
    **moses_params
)

print(f"Best program: {result.best_program}")
print(f"Best score: {result.best_score}")
```

## Application Guides

### Building a Chatbot

#### Ghost-based Chatbot

1. **Create Rules File** (`my_bot.ghost`)
   ```scheme
   ; Basic greeting
   topic: ~greeting
   u: (hello hi hey) Hello there! How can I help you?
   
   ; Weather query
   topic: ~weather
   u: (* weather *) I don't have access to weather data, but it's always sunny in the digital world!
   
   ; Goodbye
   topic: ~goodbye
   u: (bye goodbye farewell) See you later! Have a great day!
   ```

2. **Load and Run**
   ```scheme
   (use-modules (opencog) (opencog ghost))
   
   ; Load rules
   (ghost-parse-file "my_bot.ghost")
   
   ; Process input
   (ghost-get-result "hello")
   ; Returns: "Hello there! How can I help you?"
   ```

#### LLM Integration Chatbot

```python
from opencog.atomspace import AtomSpace
from opencog.type_constructors import *
import requests

class CognitiveBot:
    def __init__(self):
        self.atomspace = AtomSpace()
        self.llm_url = "http://localhost:5001/api/v1/generate"
        
    def process_message(self, user_input):
        # Store conversation in AtomSpace
        user_atom = ConceptNode(f"user_input_{hash(user_input)}")
        input_atom = ConceptNode(user_input)
        
        self.atomspace.add_link(EVALUATION_LINK, [
            PredicateNode("said"),
            ListLink(user_atom, input_atom)
        ])
        
        # Generate response via LLM
        response = self.generate_llm_response(user_input)
        
        # Store response
        response_atom = ConceptNode(response)
        self.atomspace.add_link(EVALUATION_LINK, [
            PredicateNode("responded"),
            ListLink(user_atom, response_atom)
        ])
        
        return response
    
    def generate_llm_response(self, text):
        payload = {
            "prompt": f"User: {text}\nBot:",
            "max_length": 100,
            "temperature": 0.7
        }
        
        response = requests.post(self.llm_url, json=payload)
        return response.json()['results'][0]['text']

# Usage
bot = CognitiveBot()
response = bot.process_message("Hello!")
print(response)
```

### Knowledge Mining

#### Pattern Mining Example

```python
from opencog.miner import *

# Load knowledge base
atomspace = AtomSpace()

# Add sample data
for person in ["Alice", "Bob", "Charlie"]:
    atomspace.add_link(INHERITANCE_LINK, [
        ConceptNode(person),
        ConceptNode("person")
    ])
    
    atomspace.add_link(EVALUATION_LINK, [
        PredicateNode("likes"),
        ListLink(ConceptNode(person), ConceptNode("music"))
    ])

# Mine patterns
miner = PatternMiner(atomspace)
patterns = miner.mine(
    minimum_support=2,
    maximum_iterations=100
)

for pattern in patterns:
    print(f"Pattern: {pattern}")
    print(f"Support: {pattern.support}")
```

## Advanced Configuration

### Performance Tuning

#### Memory Optimization

```cpp
// In your C++ code
#include <opencog/atomspace/AtomSpace.h>

// Configure AtomSpace for large datasets
AtomSpace atomspace;
atomspace.set_max_size(10000000);  // 10M atoms max
atomspace.enable_copy_on_write(true);  // Memory efficiency
```

#### Concurrent Processing

```python
import threading
from opencog.atomspace import AtomSpace

# Thread-safe AtomSpace operations
atomspace = AtomSpace()

def worker_thread(thread_id):
    # Each thread works with same AtomSpace
    for i in range(1000):
        concept = ConceptNode(f"concept_{thread_id}_{i}")
        atomspace.add_atom(concept)

# Start multiple threads
threads = []
for i in range(4):
    t = threading.Thread(target=worker_thread, args=(i,))
    threads.append(t)
    t.start()

# Wait for completion
for t in threads:
    t.join()

print(f"Total atoms: {atomspace.size()}")
```

### Storage Configuration

#### PostgreSQL Backend

1. **Setup Database**
   ```sql
   CREATE DATABASE opencog;
   CREATE USER opencog_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE opencog TO opencog_user;
   ```

2. **Configure Connection**
   ```scheme
   (use-modules (opencog persist-sql))
   
   (sql-open "postgresql://opencog_user:your_password@localhost/opencog")
   (store-atomspace)  ; Save all atoms
   (load-atomspace)   ; Load atoms
   ```

#### RocksDB Backend

```scheme
(use-modules (opencog persist-rocks))

; Open RocksDB storage
(rocks-open "file:///path/to/database")

; Store individual atoms
(store-atom (ConceptNode "persistent-data"))

; Bulk operations
(store-atomspace)
(load-atomspace)
```

## Troubleshooting

### Common Issues

#### Build Failures

**Problem**: CMake can't find Boost
```bash
# Solution: Specify Boost location
cmake -DBOOST_ROOT=/usr/local ..
```

**Problem**: Guile version mismatch
```bash
# Check Guile version
guile --version

# Install correct version
sudo apt-get install guile-3.0-dev
```

#### Runtime Issues

**Problem**: CogServer won't start
```bash
# Check port availability
netstat -an | grep 17001

# Try different port
cogserver --port 17002
```

**Problem**: Python imports failing
```python
# Check Python path
import sys
print(sys.path)

# Add OpenCog path
sys.path.append('/usr/local/lib/python3/dist-packages')
```

### Performance Issues

#### Slow Pattern Matching

```scheme
; Use indexed queries
(cog-bind
  (BindLink
    (TypedVariable (Variable "$x") (Type "ConceptNode"))
    (InheritanceLink (Variable "$x") (Concept "animal"))
    (Variable "$x")))
```

#### Memory Usage

```python
# Monitor memory usage
import psutil
process = psutil.Process()
print(f"Memory usage: {process.memory_info().rss / 1024 / 1024} MB")

# Periodic garbage collection
import gc
gc.collect()
```

### Getting Help

#### Community Resources

- **GitHub Issues**: https://github.com/opencog/opencog/issues
- **Mailing List**: opencog@googlegroups.com
- **IRC**: #opencog on freenode
- **Discord**: OpenCog Community Server

#### Debug Tools

```bash
# Enable debug logging
export OPENCOG_LOG_LEVEL=DEBUG

# Valgrind for memory issues
valgrind --tool=memcheck cogserver

# GDB for crashes
gdb cogserver
(gdb) run
(gdb) bt  # on crash
```

## Next Steps

After completing these tutorials, explore:

1. **Advanced Topics**
   - [Technical Architecture](02-TECHNICAL-ARCHITECTURE.md)
   - [AI/ML Integration](05-AI-ML-INTEGRATION.md)

2. **Specialized Applications**
   - Biological modeling with agi-bio
   - Language learning systems
   - Robotics integration

3. **Contributing**
   - See [Developer Documentation](07-DEVELOPER-DOCUMENTATION.md)
   - Join community discussions
   - Submit pull requests
