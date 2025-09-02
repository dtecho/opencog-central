
"""
OpenCog Neural Network Framework (PyTorch)
==========================================

A comprehensive neural network implementation using PyTorch that integrates
with the OpenCog AtomSpace framework for cognitive computing applications.

This module provides:
- Core neural network building blocks
- AtomSpace integration layers
- Cognitive architectures (attention, memory, reasoning)
- Multi-scale modeling capabilities
- Visualization and analysis tools
"""

from .core import *
from .layers import *
from .models import *
from .training import *
from .utils import *
from .cognitive import *
from .atomspace_integration import *

__version__ = "1.0.0"
__author__ = "OpenCog Neural Network Team"

# Set default tensor types for consistency
import torch
torch.set_default_dtype(torch.float32)

# Main entry points
from .core.module import NeuralModule
from .models.cognitive_net import CognitiveNetwork
from .atomspace_integration.bridge import AtomSpaceBridge
