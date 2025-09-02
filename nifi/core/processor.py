
"""
Base Processor class and processor factory
"""

import asyncio
import logging
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any, List, Optional

logger = logging.getLogger(__name__)

@dataclass
class FlowFile:
    """Represents a data unit flowing through the system"""
    
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    attributes: Dict[str, str] = field(default_factory=dict)
    content: bytes = b""
    size: int = 0
    created: datetime = field(default_factory=datetime.now)
    
    def __post_init__(self):
        if self.content:
            self.size = len(self.content)

class Processor(ABC):
    """Base class for all processors"""
    
    def __init__(self, processor_id: str, config: Dict[str, Any]):
        self.id = processor_id
        self.config = config
        self.status = "STOPPED"
        self.flowfiles_processed = 0
        self.bytes_processed = 0
        self.atomspace = None
        self.processor_type = self.__class__.__name__
        
    def set_atomspace(self, atomspace_connector):
        """Set AtomSpace connector reference"""
        self.atomspace = atomspace_connector
        
    async def start(self):
        """Start the processor"""
        self.status = "RUNNING"
        logger.info(f"Started processor {self.id} ({self.processor_type})")
        
    async def stop(self):
        """Stop the processor"""
        self.status = "STOPPED"
        logger.info(f"Stopped processor {self.id} ({self.processor_type})")
        
    @abstractmethod
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """Process a flowfile and return result flowfiles"""
        pass
        
    def update_stats(self, flowfile: FlowFile):
        """Update processing statistics"""
        self.flowfiles_processed += 1
        self.bytes_processed += flowfile.size
        
    @staticmethod
    def create(processor_type: str, processor_id: str, config: Dict[str, Any]) -> 'Processor':
        """Factory method to create processors"""
        from nifi.processors.generate_flowfile import GenerateFlowFileProcessor
        from nifi.processors.log_attribute import LogAttributeProcessor
        from nifi.processors.atomspace_writer import AtomSpaceWriterProcessor
        from nifi.processors.atomspace_reader import AtomSpaceReaderProcessor
        from nifi.processors.cognitive_processor import CognitiveProcessor
        
        processor_classes = {
            "GenerateFlowFile": GenerateFlowFileProcessor,
            "LogAttribute": LogAttributeProcessor,
            "AtomSpaceWriter": AtomSpaceWriterProcessor,
            "AtomSpaceReader": AtomSpaceReaderProcessor,
            "CognitiveProcessor": CognitiveProcessor
        }
        
        if processor_type not in processor_classes:
            raise ValueError(f"Unknown processor type: {processor_type}")
            
        return processor_classes[processor_type](processor_id, config)
