
"""
Configuration management for P-systems.
"""

from typing import Dict, List, Optional, Set
from .membrane import Membrane
from .multiset import Multiset


class Configuration:
    """
    Represents a configuration (instantaneous description) of a P-system.
    """
    
    def __init__(self, psystem):
        self.psystem = psystem
        self.step_number = 0
        self.halting = False
        self.computation_result: Optional[Multiset] = None
        
        # Initialize membranes with their initial multisets
        self._initialize_from_psystem()
    
    def _initialize_from_psystem(self):
        """Initialize configuration from P-system definition."""
        if not self.psystem.membrane_structure:
            return
            
        # Set initial multisets for each membrane
        for label, multiset in self.psystem.initial_multisets.items():
            membrane = self.find_membrane(label)
            if membrane:
                membrane.multiset = multiset.copy()
    
    def find_membrane(self, label: int) -> Optional[Membrane]:
        """Find a membrane by its label."""
        if not self.psystem.membrane_structure:
            return None
        return self.psystem.membrane_structure.find_by_label(label)
    
    def get_all_membranes(self) -> List[Membrane]:
        """Get all membranes in the current configuration."""
        if not self.psystem.membrane_structure:
            return []
        return self.psystem.membrane_structure.get_all_membranes()
    
    def get_membrane_multisets(self) -> Dict[int, Multiset]:
        """Get multisets for all membranes."""
        result = {}
        for membrane in self.get_all_membranes():
            if not membrane.dissolved:
                result[membrane.label] = membrane.multiset.copy()
        return result
    
    def get_total_objects(self) -> Multiset:
        """Get total objects across all membranes."""
        total = Multiset()
        for membrane in self.get_all_membranes():
            if not membrane.dissolved:
                total.add_multiset(membrane.multiset)
        return total
    
    def get_output_membrane_content(self) -> Optional[Multiset]:
        """Get contents of the output membrane (usually membrane 0)."""
        output_membrane = self.find_membrane(0)
        if output_membrane and not output_membrane.dissolved:
            return output_membrane.multiset.copy()
        return None
    
    def is_deterministic(self) -> bool:
        """Check if the current configuration allows deterministic evolution."""
        # This would require checking rule conflicts
        # Simplified implementation
        return True
    
    def copy(self) -> 'Configuration':
        """Create a deep copy of this configuration."""
        # This would require deep copying the entire membrane structure
        # Simplified implementation
        new_config = Configuration(self.psystem)
        new_config.step_number = self.step_number
        new_config.halting = self.halting
        return new_config
    
    def __str__(self) -> str:
        """String representation of the configuration."""
        if not self.psystem.membrane_structure:
            return "Empty configuration"
        
        return f"Step {self.step_number}: {self.psystem.membrane_structure}"
    
    def __repr__(self) -> str:
        return f"Configuration(step={self.step_number}, membranes={len(self.get_all_membranes())})"
