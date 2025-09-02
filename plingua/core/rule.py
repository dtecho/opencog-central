
"""
Rule system for P-systems.
"""

from typing import List, Dict, Optional, Set, Any
from abc import ABC, abstractmethod
from .multiset import Multiset
from .configuration import Configuration


class RuleType:
    """Enumeration of rule types."""
    EVOLUTION = "evolution"
    COMMUNICATION = "communication" 
    DISSOLUTION = "dissolution"
    DIVISION = "division"


class Rule(ABC):
    """Abstract base class for P-system rules."""
    
    def __init__(self, rule_type: str):
        self.rule_type = rule_type
        self.priority = 0
        self.probability = 1.0
        self.label = ""
        
    @abstractmethod
    def is_applicable(self, configuration: 'Configuration') -> bool:
        """Check if this rule is applicable to the current configuration."""
        pass
    
    @abstractmethod
    def apply(self, configuration: 'Configuration') -> bool:
        """Apply this rule to the configuration."""
        pass
    
    @abstractmethod
    def get_objects(self) -> Set[str]:
        """Get all objects involved in this rule."""
        pass
    
    def __str__(self) -> str:
        return f"{self.rule_type}_rule"


class EvolutionRule(Rule):
    """
    Evolution rule: [u -> v]_i
    Objects evolve within a membrane.
    """
    
    def __init__(self, 
                 left_hand_side: Multiset,
                 right_hand_side: Multiset,
                 membrane_label: int):
        super().__init__(RuleType.EVOLUTION)
        self.lhs = left_hand_side
        self.rhs = right_hand_side
        self.membrane_label = membrane_label
    
    def is_applicable(self, configuration: 'Configuration') -> bool:
        """Check if rule can be applied."""
        membrane = configuration.find_membrane(self.membrane_label)
        if not membrane or membrane.dissolved:
            return False
        return membrane.multiset.contains(self.lhs)
    
    def apply(self, configuration: 'Configuration') -> bool:
        """Apply the evolution rule."""
        membrane = configuration.find_membrane(self.membrane_label)
        if not membrane or not self.is_applicable(configuration):
            return False
        
        # Remove left-hand side objects
        if membrane.multiset.subtract(self.lhs):
            # Add right-hand side objects
            membrane.multiset.add_multiset(self.rhs)
            return True
        return False
    
    def get_objects(self) -> Set[str]:
        """Get all objects in the rule."""
        objects = set(self.lhs.objects.keys())
        objects.update(self.rhs.objects.keys())
        return objects
    
    def __str__(self) -> str:
        return f"[{self.lhs} -> {self.rhs}]_{self.membrane_label}"


class CommunicationRule(Rule):
    """
    Communication rule: [u]_i (v, out) | [w]_j (x, in_j)
    Objects move between membranes.
    """
    
    def __init__(self,
                 consumed: Multiset,
                 source_label: int,
                 sent_out: Multiset,
                 target_label: int,
                 sent_in: Multiset):
        super().__init__(RuleType.COMMUNICATION)
        self.consumed = consumed
        self.source_label = source_label
        self.sent_out = sent_out
        self.target_label = target_label
        self.sent_in = sent_in
    
    def is_applicable(self, configuration: 'Configuration') -> bool:
        """Check if communication rule can be applied."""
        source = configuration.find_membrane(self.source_label)
        target = configuration.find_membrane(self.target_label)
        
        if not source or not target or source.dissolved or target.dissolved:
            return False
        
        return source.multiset.contains(self.consumed)
    
    def apply(self, configuration: 'Configuration') -> bool:
        """Apply the communication rule."""
        source = configuration.find_membrane(self.source_label)
        target = configuration.find_membrane(self.target_label)
        
        if not self.is_applicable(configuration):
            return False
        
        # Remove consumed objects from source
        if source.multiset.subtract(self.consumed):
            # Add objects to target
            target.multiset.add_multiset(self.sent_in)
            
            # Add objects sent out to parent of source
            if source.parent:
                source.parent.multiset.add_multiset(self.sent_out)
            
            return True
        return False
    
    def get_objects(self) -> Set[str]:
        """Get all objects in the rule."""
        objects = set(self.consumed.objects.keys())
        objects.update(self.sent_out.objects.keys())
        objects.update(self.sent_in.objects.keys())
        return objects
    
    def __str__(self) -> str:
        return f"[{self.consumed}]_{self.source_label} ({self.sent_out}, out) | [{self.sent_in}]_{self.target_label}"


class DissolutionRule(Rule):
    """
    Dissolution rule: [u -> v δ]_i
    Membrane dissolves and contents move to parent.
    """
    
    def __init__(self,
                 left_hand_side: Multiset,
                 right_hand_side: Multiset,
                 membrane_label: int):
        super().__init__(RuleType.DISSOLUTION)
        self.lhs = left_hand_side
        self.rhs = right_hand_side
        self.membrane_label = membrane_label
    
    def is_applicable(self, configuration: 'Configuration') -> bool:
        """Check if dissolution rule can be applied."""
        membrane = configuration.find_membrane(self.membrane_label)
        if not membrane or membrane.dissolved:
            return False
        return membrane.multiset.contains(self.lhs)
    
    def apply(self, configuration: 'Configuration') -> bool:
        """Apply the dissolution rule."""
        membrane = configuration.find_membrane(self.membrane_label)
        if not self.is_applicable(configuration):
            return False
        
        # Remove left-hand side objects
        if membrane.multiset.subtract(self.lhs):
            # Add right-hand side objects
            membrane.multiset.add_multiset(self.rhs)
            
            # Dissolve the membrane
            membrane.dissolve()
            return True
        return False
    
    def get_objects(self) -> Set[str]:
        """Get all objects in the rule."""
        objects = set(self.lhs.objects.keys())
        objects.update(self.rhs.objects.keys())
        return objects
    
    def __str__(self) -> str:
        return f"[{self.lhs} -> {self.rhs} δ]_{self.membrane_label}"


class DivisionRule(Rule):
    """
    Division rule: [a]'i -> [b]'j [c]'k
    Membrane divides into two membranes.
    """
    
    def __init__(self,
                 catalyst: str,
                 membrane_label: int,
                 label1: int,
                 label2: int,
                 content1: Multiset,
                 content2: Multiset):
        super().__init__(RuleType.DIVISION)
        self.catalyst = catalyst
        self.membrane_label = membrane_label
        self.label1 = label1
        self.label2 = label2
        self.content1 = content1
        self.content2 = content2
    
    def is_applicable(self, configuration: 'Configuration') -> bool:
        """Check if division rule can be applied."""
        membrane = configuration.find_membrane(self.membrane_label)
        if not membrane or membrane.dissolved:
            return False
        return membrane.multiset.count(self.catalyst) > 0
    
    def apply(self, configuration: 'Configuration') -> bool:
        """Apply the division rule."""
        membrane = configuration.find_membrane(self.membrane_label)
        if not self.is_applicable(configuration):
            return False
        
        # Remove catalyst
        if membrane.multiset.remove(self.catalyst, 1):
            # Divide the membrane
            mem1, mem2 = membrane.divide(self.label1, self.label2)
            
            # Set contents
            mem1.multiset = self.content1.copy()
            mem2.multiset = self.content2.copy()
            
            return True
        return False
    
    def get_objects(self) -> Set[str]:
        """Get all objects in the rule."""
        objects = {self.catalyst}
        objects.update(self.content1.objects.keys())
        objects.update(self.content2.objects.keys())
        return objects
    
    def __str__(self) -> str:
        return f"[{self.catalyst}]_{self.membrane_label} -> [{self.content1}]_{self.label1} [{self.content2}]_{self.label2}"
