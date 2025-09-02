
"""
P-System base class and related functionality.
"""

from typing import Dict, List, Optional, Set, Any
from abc import ABC, abstractmethod
from .membrane import Membrane
from .multiset import Multiset
from .rule import Rule
from .configuration import Configuration


class PSystemType:
    """Enumeration of P-system types."""
    TRANSITION = "transition"
    TISSUE = "tissue"
    NEURAL = "neural"
    POPULATION = "population"
    PROBABILISTIC = "probabilistic"


class PSystem(ABC):
    """
    Abstract base class for P-systems.
    
    A P-system consists of:
    - A membrane structure
    - Initial multisets
    - A set of rules
    - An environment (optional)
    """
    
    def __init__(self, system_type: str):
        self.system_type = system_type
        self.membrane_structure: Optional[Membrane] = None
        self.initial_multisets: Dict[int, Multiset] = {}
        self.rules: List[Rule] = []
        self.environment: Optional[Multiset] = None
        self.alphabet: Set[str] = set()
        self.configuration: Optional[Configuration] = None
        
    def add_membrane(self, label: int, parent: Optional[int] = None) -> Membrane:
        """Add a membrane to the system."""
        if self.membrane_structure is None:
            self.membrane_structure = Membrane(label)
            return self.membrane_structure
        
        # Find parent membrane and add child
        parent_membrane = self.find_membrane(parent) if parent else self.membrane_structure
        if parent_membrane:
            child = Membrane(label, parent_membrane)
            parent_membrane.add_child(child)
            return child
        
        raise ValueError(f"Parent membrane {parent} not found")
    
    def find_membrane(self, label: int) -> Optional[Membrane]:
        """Find a membrane by its label."""
        if not self.membrane_structure:
            return None
        return self.membrane_structure.find_by_label(label)
    
    def set_initial_multiset(self, membrane_label: int, multiset: Multiset):
        """Set the initial multiset for a membrane."""
        self.initial_multisets[membrane_label] = multiset
        self.alphabet.update(multiset.objects.keys())
    
    def add_rule(self, rule: Rule):
        """Add a rule to the system."""
        self.rules.append(rule)
        self.alphabet.update(rule.get_objects())
    
    def get_configuration(self) -> Configuration:
        """Get the current configuration of the system."""
        if not self.configuration:
            self.configuration = Configuration(self)
        return self.configuration
    
    @abstractmethod
    def step(self) -> bool:
        """Execute one computation step. Returns True if step was successful."""
        pass
    
    @abstractmethod
    def is_halting(self) -> bool:
        """Check if the system has reached a halting configuration."""
        pass
    
    def reset(self):
        """Reset the system to its initial configuration."""
        self.configuration = Configuration(self)
        for label, multiset in self.initial_multisets.items():
            membrane = self.find_membrane(label)
            if membrane:
                membrane.multiset = multiset.copy()


class TransitionPSystem(PSystem):
    """Standard transition P-system implementation."""
    
    def __init__(self):
        super().__init__(PSystemType.TRANSITION)
        self.halting = False
    
    def step(self) -> bool:
        """Execute one computation step using maximal parallelism."""
        if self.halting:
            return False
            
        config = self.get_configuration()
        applicable_rules = []
        
        # Find all applicable rules
        for rule in self.rules:
            if rule.is_applicable(config):
                applicable_rules.append(rule)
        
        if not applicable_rules:
            self.halting = True
            return False
        
        # Apply rules with maximal parallelism
        for rule in applicable_rules:
            rule.apply(config)
        
        return True
    
    def is_halting(self) -> bool:
        """Check if system has halted."""
        return self.halting


class TissuePSystem(PSystem):
    """Tissue P-system with cell-like structure."""
    
    def __init__(self):
        super().__init__(PSystemType.TISSUE)
        self.cell_connections: Dict[int, Set[int]] = {}
    
    def add_connection(self, cell1: int, cell2: int):
        """Add a connection between two cells."""
        if cell1 not in self.cell_connections:
            self.cell_connections[cell1] = set()
        if cell2 not in self.cell_connections:
            self.cell_connections[cell2] = set()
        
        self.cell_connections[cell1].add(cell2)
        self.cell_connections[cell2].add(cell1)
    
    def step(self) -> bool:
        """Execute one computation step."""
        # Implementation for tissue P-system semantics
        return True
    
    def is_halting(self) -> bool:
        """Check if system has halted."""
        return False
