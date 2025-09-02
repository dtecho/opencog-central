
"""
MiniNiFi Connection
Manages connections between processors
"""

from typing import Dict, Any, Optional
from enum import Enum

class Relationship(Enum):
    """Standard relationships between processors"""
    SUCCESS = "success"
    FAILURE = "failure"
    RETRY = "retry"
    ORIGINAL = "original"

class Connection:
    """Represents a connection between processors"""
    
    def __init__(self, source_id: str, destination_id: str, 
                 relationship: Relationship = Relationship.SUCCESS):
        self.source_id = source_id
        self.destination_id = destination_id
        self.relationship = relationship
        self.statistics = {
            'flowfiles_queued': 0,
            'flowfiles_transferred': 0,
            'bytes_transferred': 0
        }
    
    def get_status(self) -> Dict[str, Any]:
        """Get connection status"""
        return {
            'source_id': self.source_id,
            'destination_id': self.destination_id,
            'relationship': self.relationship.value,
            'statistics': self.statistics.copy()
        }
