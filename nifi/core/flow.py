
"""
Data Flow representation
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict, Any

@dataclass
class Flow:
    """Represents a data processing flow"""
    
    id: str
    name: str
    description: str = ""
    status: str = "STOPPED"  # STOPPED, RUNNING, INVALID
    processor_ids: List[str] = field(default_factory=list)
    created: datetime = field(default_factory=datetime.now)
    last_modified: datetime = field(default_factory=datetime.now)
    variables: Dict[str, str] = field(default_factory=dict)
    
    def add_processor(self, processor_id: str):
        """Add a processor to this flow"""
        if processor_id not in self.processor_ids:
            self.processor_ids.append(processor_id)
            self.last_modified = datetime.now()
            
    def remove_processor(self, processor_id: str):
        """Remove a processor from this flow"""
        if processor_id in self.processor_ids:
            self.processor_ids.remove(processor_id)
            self.last_modified = datetime.now()
            
    def set_variable(self, name: str, value: str):
        """Set a flow variable"""
        self.variables[name] = value
        self.last_modified = datetime.now()
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert flow to dictionary representation"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "status": self.status,
            "processor_ids": self.processor_ids,
            "created": self.created.isoformat(),
            "last_modified": self.last_modified.isoformat(),
            "variables": self.variables
        }
