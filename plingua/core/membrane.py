
"""
Membrane structure classes for P-systems.
"""

from typing import List, Optional, Dict, Any
from .multiset import Multiset


class Membrane:
    """
    Represents a membrane in a P-system.
    
    A membrane has:
    - A unique label
    - A multiset of objects
    - Optional parent and children membranes
    - Optional charge
    - Optional dissolution state
    """
    
    def __init__(self, label: int, parent: Optional['Membrane'] = None):
        self.label = label
        self.parent = parent
        self.children: List['Membrane'] = []
        self.multiset = Multiset()
        self.charge = 0  # 0: neutral, +1: positive, -1: negative
        self.dissolved = False
        self.properties: Dict[str, Any] = {}
    
    def add_child(self, child: 'Membrane'):
        """Add a child membrane."""
        if child not in self.children:
            self.children.append(child)
            child.parent = self
    
    def remove_child(self, child: 'Membrane'):
        """Remove a child membrane."""
        if child in self.children:
            self.children.remove(child)
            child.parent = None
    
    def dissolve(self):
        """Dissolve this membrane."""
        self.dissolved = True
        
        # Move objects to parent if it exists
        if self.parent:
            self.parent.multiset.add_multiset(self.multiset)
            self.parent.remove_child(self)
        
        # Move children to parent
        for child in self.children[:]:
            if self.parent:
                self.parent.add_child(child)
            else:
                child.parent = None
    
    def divide(self, label1: int, label2: int) -> tuple['Membrane', 'Membrane']:
        """Divide this membrane into two new membranes."""
        # Create two new membranes
        membrane1 = Membrane(label1, self.parent)
        membrane2 = Membrane(label2, self.parent)
        
        # Copy multiset to both (membrane division semantics)
        membrane1.multiset = self.multiset.copy()
        membrane2.multiset = self.multiset.copy()
        
        # Update parent
        if self.parent:
            self.parent.remove_child(self)
            self.parent.add_child(membrane1)
            self.parent.add_child(membrane2)
        
        return membrane1, membrane2
    
    def find_by_label(self, label: int) -> Optional['Membrane']:
        """Find a membrane by label in this subtree."""
        if self.label == label:
            return self
        
        for child in self.children:
            result = child.find_by_label(label)
            if result:
                return result
        
        return None
    
    def get_all_membranes(self) -> List['Membrane']:
        """Get all membranes in this subtree."""
        result = [self]
        for child in self.children:
            result.extend(child.get_all_membranes())
        return result
    
    def depth(self) -> int:
        """Get the depth of this membrane."""
        if not self.parent:
            return 0
        return self.parent.depth() + 1
    
    def is_elementary(self) -> bool:
        """Check if this is an elementary membrane (no children)."""
        return len(self.children) == 0
    
    def __str__(self) -> str:
        """String representation of membrane structure."""
        if not self.children:
            charge_str = "+" if self.charge > 0 else "-" if self.charge < 0 else ""
            return f"[{self.multiset}]{charge_str}'{self.label}"
        
        children_str = " ".join(str(child) for child in self.children)
        charge_str = "+" if self.charge > 0 else "-" if self.charge < 0 else ""
        return f"[{self.multiset} {children_str}]{charge_str}'{self.label}"
    
    def __repr__(self) -> str:
        return f"Membrane(label={self.label}, charge={self.charge}, objects={len(self.multiset)})"
