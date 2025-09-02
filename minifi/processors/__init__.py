
"""
MiniNiFi Processors Module
Lightweight data processing components
"""

from .generate_flowfile import GenerateFlowFileProcessor
from .log_attribute import LogAttributeProcessor

__all__ = ['GenerateFlowFileProcessor', 'LogAttributeProcessor']
