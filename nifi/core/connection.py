
"""
Connection between processors
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

@dataclass
class Connection:
    """Represents a connection between processors"""
    
    id: str
    source_id: str
    destination_id: str
    source_relationship: str = "success"
    flowfiles_queued: int = 0
    bytes_queued: int = 0
    created: datetime = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert connection to dictionary representation"""
        return {
            "id": self.id,
            "source_id": self.source_id,
            "destination_id": self.destination_id,
            "source_relationship": self.source_relationship,
            "flowfiles_queued": self.flowfiles_queued,
            "bytes_queued": self.bytes_queued,
            "created": self.created.isoformat()
        }
