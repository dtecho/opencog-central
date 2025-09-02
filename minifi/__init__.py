
"""
Apache MiniNiFi for OpenCog
Lightweight data flow processing for edge computing
"""

__version__ = "1.0.0"
__author__ = "OpenCog Foundation"

from .core.agent import MiniNiFiAgent
from .core.processor import MiniNiFiProcessor
from .core.flow import MiniNiFiFlow

__all__ = [
    'MiniNiFiAgent',
    'MiniNiFiProcessor', 
    'MiniNiFiFlow'
]
