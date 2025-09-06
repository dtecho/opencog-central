
"""
OpenCog Marduk Assistant Module

Marduk v15: The Systems Architect Mad Scientist
A brilliant cognitive systems architect specialized in orchestrating 
OpenCog's distributed cognitive processes.
"""

from .marduk_assistant import MardukAssistant, MardukOpenCogBridge, SubsystemType, CognitivePattern

__version__ = "15.0"
__author__ = "OpenCog Cognitive Architecture Team"

# Make key classes available at module level
__all__ = [
    "MardukAssistant",
    "MardukOpenCogBridge", 
    "SubsystemType",
    "CognitivePattern"
]
