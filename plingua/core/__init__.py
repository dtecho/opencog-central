
"""
P-Lingua Core Module

This module provides the fundamental classes and interfaces for P-Lingua
membrane computing framework.
"""

from .psystem import PSystem
from .membrane import Membrane
from .multiset import Multiset
from .rule import Rule, EvolutionRule, CommunicationRule, DissolutionRule
from .environment import Environment
from .configuration import Configuration

__all__ = [
    'PSystem',
    'Membrane',
    'Multiset', 
    'Rule',
    'EvolutionRule',
    'CommunicationRule',
    'DissolutionRule',
    'Environment',
    'Configuration'
]
