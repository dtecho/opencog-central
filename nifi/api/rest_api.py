
"""
NiFi REST API
Provides programmatic access to NiFi functionality
"""

import json
import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class NiFiRestAPI:
    """REST API interface for NiFi operations"""
    
    def __init__(self, flow_engine):
        self.flow_engine = flow_engine
        
    def get_processor_types(self) -> List[Dict[str, Any]]:
        """Get available processor types"""
        return [
            {
                "type": "GenerateFlowFile",
                "description": "Generates flowfiles with configurable content",
                "properties": [
                    {"name": "content", "type": "string", "description": "Content to generate"},
                    {"name": "format", "type": "string", "description": "Content format (text/json)"},
                    {"name": "interval_seconds", "type": "number", "description": "Generation interval"}
                ]
            },
            {
                "type": "LogAttribute", 
                "description": "Logs flowfile attributes and content",
                "properties": [
                    {"name": "log_level", "type": "string", "description": "Log level (DEBUG/INFO/WARNING/ERROR)"},
                    {"name": "log_content", "type": "boolean", "description": "Whether to log content"},
                    {"name": "max_content_length", "type": "number", "description": "Max content length to log"}
                ]
            },
            {
                "type": "AtomSpaceWriter",
                "description": "Writes data to OpenCog AtomSpace", 
                "properties": [
                    {"name": "atom_type", "type": "string", "description": "Type of atoms to create"},
                    {"name": "name_attribute", "type": "string", "description": "Attribute to use for atom name"}
                ]
            },
            {
                "type": "AtomSpaceReader",
                "description": "Reads data from OpenCog AtomSpace",
                "properties": [
                    {"name": "query_type", "type": "string", "description": "Type of query (concept/predicate)"},
                    {"name": "query_pattern", "type": "string", "description": "Query pattern"},
                    {"name": "max_results", "type": "number", "description": "Maximum results to return"}
                ]
            },
            {
                "type": "CognitiveProcessor",
                "description": "Performs cognitive operations on data",
                "properties": [
                    {"name": "operation", "type": "string", "description": "Cognitive operation (analyze/reason/pattern_match)"}
                ]
            }
        ]
        
    def create_flow_template(self, template_name: str) -> Dict[str, Any]:
        """Create a flow from a predefined template"""
        
        templates = {
            "simple_logging": {
                "name": "Simple Logging Flow",
                "description": "Generates data and logs it",
                "processors": [
                    {
                        "type": "GenerateFlowFile",
                        "config": {
                            "content": "Hello from NiFi!",
                            "format": "text",
                            "interval_seconds": 5
                        }
                    },
                    {
                        "type": "LogAttribute",
                        "config": {
                            "log_level": "INFO",
                            "log_content": True
                        }
                    }
                ]
            },
            "atomspace_integration": {
                "name": "AtomSpace Integration Flow",
                "description": "Reads from AtomSpace, processes, and writes back",
                "processors": [
                    {
                        "type": "AtomSpaceReader",
                        "config": {
                            "query_type": "concept",
                            "max_results": 50
                        }
                    },
                    {
                        "type": "CognitiveProcessor", 
                        "config": {
                            "operation": "analyze"
                        }
                    },
                    {
                        "type": "AtomSpaceWriter",
                        "config": {
                            "atom_type": "ConceptNode"
                        }
                    }
                ]
            },
            "cognitive_pipeline": {
                "name": "Cognitive Processing Pipeline",
                "description": "Full cognitive processing workflow",
                "processors": [
                    {
                        "type": "GenerateFlowFile",
                        "config": {
                            "content": "Input text for cognitive processing",
                            "format": "text"
                        }
                    },
                    {
                        "type": "CognitiveProcessor",
                        "config": {
                            "operation": "analyze"
                        }
                    },
                    {
                        "type": "CognitiveProcessor",
                        "config": {
                            "operation": "reason"
                        }
                    },
                    {
                        "type": "LogAttribute",
                        "config": {
                            "log_level": "INFO",
                            "log_content": True
                        }
                    }
                ]
            }
        }
        
        if template_name not in templates:
            raise ValueError(f"Unknown template: {template_name}")
            
        return templates[template_name]
