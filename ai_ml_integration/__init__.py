
"""
OpenCog AI/ML Integration Package

This package provides comprehensive integration between:
- OpenCog AtomSpace and symbolic reasoning
- Neural networks and deep learning
- Evolutionary algorithms (MOSES)
- Large Language Models
- Cognitive architectures

Main components:
- core: Core integration framework
- moses_integration: Evolutionary program learning
- llm_integration: Large language model integration
- demo: Demonstration scripts
"""

from .core import OpenCogAIMLIntegration, AIMLIntegrationManager, get_integration_manager
from .moses_integration import MOSESIntegration, create_moses_integration
from .llm_integration import LLMCognitiveIntegration, CognitivePromptEnhancer, create_llm_integration

__version__ = "1.0.0"
__author__ = "OpenCog AI/ML Integration Team"

__all__ = [
    'OpenCogAIMLIntegration',
    'AIMLIntegrationManager', 
    'get_integration_manager',
    'MOSESIntegration',
    'create_moses_integration',
    'LLMCognitiveIntegration',
    'CognitivePromptEnhancer',
    'create_llm_integration'
]

# Initialize logging
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())
