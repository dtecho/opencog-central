
"""
Multiset implementation for P-systems.
"""

from typing import Dict, Iterator, Union, List
from collections import defaultdict


class Multiset:
    """
    A multiset implementation for representing collections of objects
    with multiplicities in P-systems.
    """
    
    def __init__(self, objects: Dict[str, int] = None):
        """Initialize multiset with optional objects dictionary."""
        self.objects: Dict[str, int] = defaultdict(int)
        if objects:
            for obj, count in objects.items():
                if count > 0:
                    self.objects[obj] = count
    
    def add(self, obj: str, count: int = 1):
        """Add objects to the multiset."""
        if count > 0:
            self.objects[obj] += count
    
    def remove(self, obj: str, count: int = 1) -> bool:
        """Remove objects from the multiset. Returns True if successful."""
        if obj in self.objects and self.objects[obj] >= count:
            self.objects[obj] -= count
            if self.objects[obj] == 0:
                del self.objects[obj]
            return True
        return False
    
    def count(self, obj: str) -> int:
        """Get the count of an object."""
        return self.objects.get(obj, 0)
    
    def contains(self, other: 'Multiset') -> bool:
        """Check if this multiset contains another multiset."""
        for obj, count in other.objects.items():
            if self.count(obj) < count:
                return False
        return True
    
    def subtract(self, other: 'Multiset') -> bool:
        """Subtract another multiset from this one. Returns True if successful."""
        if not self.contains(other):
            return False
        
        for obj, count in other.objects.items():
            self.remove(obj, count)
        return True
    
    def add_multiset(self, other: 'Multiset'):
        """Add another multiset to this one."""
        for obj, count in other.objects.items():
            self.add(obj, count)
    
    def union(self, other: 'Multiset') -> 'Multiset':
        """Return the union of this multiset with another."""
        result = Multiset()
        result.add_multiset(self)
        result.add_multiset(other)
        return result
    
    def intersection(self, other: 'Multiset') -> 'Multiset':
        """Return the intersection of this multiset with another."""
        result = Multiset()
        for obj in self.objects:
            if obj in other.objects:
                result.add(obj, min(self.count(obj), other.count(obj)))
        return result
    
    def copy(self) -> 'Multiset':
        """Create a copy of this multiset."""
        return Multiset(dict(self.objects))
    
    def is_empty(self) -> bool:
        """Check if the multiset is empty."""
        return len(self.objects) == 0
    
    def size(self) -> int:
        """Get the total number of objects (counting multiplicities)."""
        return sum(self.objects.values())
    
    def cardinality(self) -> int:
        """Get the number of distinct objects."""
        return len(self.objects)
    
    def clear(self):
        """Remove all objects from the multiset."""
        self.objects.clear()
    
    def __iter__(self) -> Iterator[str]:
        """Iterate over distinct objects."""
        return iter(self.objects.keys())
    
    def __len__(self) -> int:
        """Get the number of distinct objects."""
        return len(self.objects)
    
    def __str__(self) -> str:
        """String representation of the multiset."""
        if not self.objects:
            return "∅"
        
        parts = []
        for obj, count in sorted(self.objects.items()):
            if count == 1:
                parts.append(obj)
            else:
                parts.append(f"{obj}^{count}")
        
        return ", ".join(parts) if len(parts) > 1 else parts[0] if parts else "∅"
    
    def __repr__(self) -> str:
        return f"Multiset({dict(self.objects)})"
    
    def __eq__(self, other) -> bool:
        """Check equality with another multiset."""
        if not isinstance(other, Multiset):
            return False
        return self.objects == other.objects
    
    def __hash__(self) -> int:
        """Hash for use in sets and dictionaries."""
        return hash(tuple(sorted(self.objects.items())))


def parse_multiset(text: str) -> Multiset:
    """Parse a multiset from string representation."""
    multiset = Multiset()
    
    if not text or text.strip() == "∅":
        return multiset
    
    # Split by commas
    parts = [part.strip() for part in text.split(",")]
    
    for part in parts:
        if "^" in part:
            obj, count_str = part.split("^", 1)
            try:
                count = int(count_str)
                multiset.add(obj.strip(), count)
            except ValueError:
                multiset.add(part, 1)  # Treat as single object if count parsing fails
        else:
            multiset.add(part, 1)
    
    return multiset
