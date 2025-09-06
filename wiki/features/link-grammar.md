
# Link Grammar Parser

## Overview
Link Grammar is a syntactic parsing system for natural language that identifies grammatical relationships between words in sentences. It serves as the foundation for many OpenCog language processing components.

## Key Features

### Parsing Capabilities
- Context-free grammar parsing
- Link-based grammatical analysis
- Robust handling of malformed input
- Multiple parse ranking

### Language Support
- Comprehensive English grammar
- Support for multiple languages (Russian, German, Arabic, etc.)
- Extensible dictionary format
- Morphological analysis

### Integration
- C/C++ library interface
- Python bindings
- Java interface
- Command-line tools

## Architecture

### Core Components
- **Dictionary System**: Grammar rules and word definitions
- **Parser Engine**: Core parsing algorithms
- **Link Analysis**: Grammatical relationship detection
- **Output Generation**: Parse tree and link formatting

### Grammar Framework
- Connector-based link formation
- Disjunctive grammar rules
- Cost-based parse ranking
- Morphological decomposition

## Usage Examples

### C++ Interface
```cpp
#include <link-grammar/link-includes.h>

Dictionary dict = dictionary_create_lang("en");
Parse_Options opts = parse_options_create();

Sentence sent = sentence_create("The cat sat on the mat.", dict);
sentence_split(sent, opts);

int num_linkages = sentence_parse(sent, opts);
for (int i = 0; i < num_linkages; i++) {
    Linkage linkage = linkage_create(i, sent, opts);
    char *diagram = linkage_print_diagram(linkage, true, 80);
    printf("%s", diagram);
    linkage_free_diagram(diagram);
    linkage_delete(linkage);
}
```

### Python Interface
```python
from linkgrammar import *

# Create parser
lg = clgParse()

# Parse sentence
result = lg.parse("Birds fly.")

# Get linkages
for linkage in result.links():
    print(linkage)
```

### Command Line
```bash
# Interactive parsing
link-parser

# Batch processing
echo "Dogs chase cats." | link-parser -batch

# Custom dictionary
link-parser -dict=/path/to/dict
```

## Grammar Format

### Dictionary Entries
```
cat dog mouse: A+ or (Ss*b+ & <noun-main-s>);
chase: Ss- & O+ & <verb-wall>;
the: Ds+;
```

### Link Types
- **S**: Subject links
- **O**: Object links
- **A**: Adjective links
- **D**: Determiner links
- **P**: Preposition links

## Configuration

### Parse Options
- Maximum sentence length
- Memory limits
- Timeout settings
- Cost thresholds

### Dictionary Settings
- Language selection
- Custom dictionary paths
- Morphology settings
- Affix handling

## Applications

### Natural Language Processing
- Syntactic parsing
- Grammatical analysis
- Sentence structure detection
- Language learning applications

### OpenCog Integration
- RelEx dependency extraction
- Semantic processing pipeline
- Knowledge representation
- Language learning systems

## Technical Details

### Performance
- Fast parsing algorithms
- Efficient memory usage
- Scalable to long sentences
- Multi-threaded processing

### Accuracy
- High precision for well-formed sentences
- Robust error handling
- Graceful degradation for malformed input
- Multiple parse alternatives

### Extensibility
- Custom dictionary creation
- New language support
- Morphology integration
- Rule customization

## Language Support

### Supported Languages
- **English**: Comprehensive grammar
- **Russian**: Extensive morphology
- **German**: Complex grammar rules
- **Arabic**: Right-to-left processing
- **Lithuanian**: Rich morphology
- **Persian**: Script handling
- **Turkish**: Agglutinative features

### Adding New Languages
1. Create dictionary files
2. Define morphological rules
3. Test with sample sentences
4. Integrate with build system

## Installation

### Dependencies
- Standard C library
- Optional: Java runtime
- Optional: Python development headers
- Optional: SWIG for bindings

### Build Process
```bash
./configure
make
make install

# With Python bindings
./configure --enable-python-bindings
```

## Current Status
Link Grammar is actively maintained with regular updates for improved accuracy and new language support. It remains a core component of OpenCog's language processing pipeline.
