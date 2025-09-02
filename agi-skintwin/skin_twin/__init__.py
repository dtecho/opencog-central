
"""
SkinTwin-ASI: OpenCog-based Skin Modeling System

This package provides a comprehensive multiscale computational model of human skin
that integrates biological and chemical data within the OpenCog AtomSpace framework.
"""

__version__ = "0.1.0"
__author__ = "SkinTwin-ASI Development Team"

from .core import SkinTwinCore
from .atomspace_integration import AtomSpaceManager
from .multiscale_model import MultiscaleModel

__all__ = [
    "SkinTwinCore",
    "AtomSpaceManager", 
    "MultiscaleModel"
]
