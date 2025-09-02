
"""
MiniNiFi C2 (Command and Control) Module
Handles remote configuration and management
"""

from .client import C2Client
from .protocol import C2Protocol

__all__ = ['C2Client', 'C2Protocol']
