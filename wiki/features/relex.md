
# RelEx - Dependency Relationship Extractor

## Overview
RelEx is OpenCog's English dependency relationship extractor that converts natural language sentences into semantic relationship graphs. It provides deep linguistic analysis and semantic representation of text.

## Key Features

### Dependency Parsing
- Link Grammar integration for syntactic analysis
- Dependency relationship extraction
- Semantic role labeling
- Grammatical relation identification

### Semantic Processing
- Word sense disambiguation
- Semantic frame detection
- Anaphora resolution
- Entity recognition

### Output Formats
- AtomSpace representation
- Scheme expressions
- XML output
- JSON serialization

## Architecture

### Core Components
- **Link Grammar Parser**: Syntactic analysis engine
- **Semantic Processor**: Meaning extraction system
- **Relation Extractor**: Dependency relationship generator
- **Output Formatter**: Multiple format converter

### Processing Pipeline
1. Sentence tokenization and parsing
2. Syntactic link analysis
3. Semantic relationship extraction
4. Anaphora and reference resolution
5. Output generation

## Usage Examples

### Basic Sentence Processing
```java
// Initialize RelEx
RelationExtractor re = new RelationExtractor();

// Process a sentence
ParsedSentence sent = re.processSentence("John loves Mary.");

// Get relationships
for (FeatureNode fn : sent.getRelations()) {
    System.out.println(fn.toString());
}
```

### Command Line Usage
```bash
# Process single sentence
echo "The cat sat on the mat." | ./relation-extractor.sh

# Batch processing
./batch-process.sh input.txt output.xml

# Server mode
./relation-extractor-server.sh --port 4444
```

### Scheme Integration
```scheme
(use-modules (opencog nlp))

; Process sentence and get atoms
(nlp-parse "Dogs chase cats.")

; Get specific relationships
(cog-incoming-set (Concept "chase"))
```

## Configuration

### Parser Settings
- Link Grammar dictionary selection
- Parse ranking preferences
- Timeout and resource limits
- Error handling strategies

### Semantic Options
- Word sense disambiguation settings
- Frame detection parameters
- Anaphora resolution scope
- Entity linking preferences

## Output Examples

### Dependency Relations
```
_subj(chase, dog)
_obj(chase, cat)
tense(chase, present)
num(dog, singular)
num(cat, plural)
```

### AtomSpace Representation
```scheme
(EvaluationLink
  (PredicateNode "_subj")
  (ListLink
    (ConceptNode "chase@123")
    (ConceptNode "dog@456")))
```

## Applications

### Natural Language Understanding
- Semantic parsing
- Information extraction
- Question answering
- Text summarization

### Knowledge Acquisition
- Fact extraction from text
- Relationship discovery
- Ontology population
- Knowledge base construction

### Language Learning
- Grammar pattern analysis
- Linguistic structure discovery
- Semantic relationship mining
- Corpus analysis

## Technical Details

### Supported Languages
- English (primary)
- Limited support for other languages
- Extensible architecture for new languages

### Integration APIs
- Java native interface
- Command line tools
- Network server mode
- Scheme bindings

### Performance Characteristics
- Processing speed: ~1-10 sentences/second
- Memory usage: Moderate
- Scalability: Single-threaded processing
- Accuracy: High for well-formed English

## Dependencies

### Required Components
- Link Grammar library
- WordNet database
- OpenNLP models
- Java runtime environment

### Optional Components
- Stanford Parser
- SUMO ontology
- FrameNet data
- Custom dictionaries

## Installation and Setup

### Build Requirements
- Java Development Kit
- Ant build system
- Link Grammar development files
- WordNet installation

### Configuration Files
- RelEx configuration
- Link Grammar settings
- WordNet paths
- Output format templates

## Current Status
RelEx continues to be actively maintained and provides robust English language processing capabilities for OpenCog applications.
