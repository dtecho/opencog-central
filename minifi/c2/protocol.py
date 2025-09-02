
"""
C2 Protocol
Defines the Command and Control protocol messages and operations
"""

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Any, Optional

class C2OperationType(Enum):
    """Types of C2 operations"""
    HEARTBEAT = "heartbeat"
    UPDATE_CONFIG = "update_config"
    START_FLOW = "start_flow"
    STOP_FLOW = "stop_flow"
    GET_STATUS = "get_status"
    RESTART = "restart"
    SHUTDOWN = "shutdown"

@dataclass
class C2Message:
    """C2 protocol message"""
    operation: C2OperationType
    agent_id: str
    timestamp: float
    payload: Dict[str, Any]
    operation_id: Optional[str] = None

@dataclass
class C2Response:
    """C2 protocol response"""
    operation_id: str
    success: bool
    message: str
    payload: Dict[str, Any]
    timestamp: float

class C2Protocol:
    """Handles C2 protocol serialization and deserialization"""
    
    @staticmethod
    def serialize_message(message: C2Message) -> Dict[str, Any]:
        """Serialize C2 message to dict"""
        return {
            'operation': message.operation.value,
            'agent_id': message.agent_id,
            'timestamp': message.timestamp,
            'payload': message.payload,
            'operation_id': message.operation_id
        }
    
    @staticmethod
    def deserialize_message(data: Dict[str, Any]) -> C2Message:
        """Deserialize dict to C2 message"""
        return C2Message(
            operation=C2OperationType(data['operation']),
            agent_id=data['agent_id'],
            timestamp=data['timestamp'],
            payload=data['payload'],
            operation_id=data.get('operation_id')
        )
    
    @staticmethod
    def serialize_response(response: C2Response) -> Dict[str, Any]:
        """Serialize C2 response to dict"""
        return {
            'operation_id': response.operation_id,
            'success': response.success,
            'message': response.message,
            'payload': response.payload,
            'timestamp': response.timestamp
        }
    
    @staticmethod
    def deserialize_response(data: Dict[str, Any]) -> C2Response:
        """Deserialize dict to C2 response"""
        return C2Response(
            operation_id=data['operation_id'],
            success=data['success'],
            message=data['message'],
            payload=data['payload'],
            timestamp=data['timestamp']
        )
