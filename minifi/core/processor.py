
"""
MiniNiFi Processor Base Class
Base class for all data processing components
"""

import asyncio
import logging
import time
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)

@dataclass
class FlowFile:
    """Represents a unit of data flowing through the system"""
    content: bytes = b""
    attributes: Dict[str, str] = field(default_factory=dict)
    size: int = 0
    uuid: str = ""
    created_time: float = field(default_factory=time.time)
    
    def __post_init__(self):
        if not self.uuid:
            import uuid
            self.uuid = str(uuid.uuid4())
        if self.size == 0:
            self.size = len(self.content)

class MiniNiFiProcessor(ABC):
    """Base class for all MiniNiFi processors"""
    
    def __init__(self, processor_id: str, config: Dict[str, Any]):
        self.processor_id = processor_id
        self.config = config
        self.properties = config.get('properties', {})
        self.connections = []
        self.input_queue = asyncio.Queue(maxsize=100)
        self.running = False
        self.statistics = {
            'flowfiles_received': 0,
            'flowfiles_sent': 0,
            'bytes_received': 0,
            'bytes_sent': 0,
            'processing_time_ms': 0
        }
    
    async def initialize(self):
        """Initialize the processor"""
        logger.info(f"Processor {self.processor_id} ({self.__class__.__name__}) initialized")
    
    def add_connection(self, destination_processor):
        """Add a connection to another processor"""
        self.connections.append(destination_processor)
    
    async def run(self):
        """Main processing loop"""
        self.running = True
        logger.info(f"Processor {self.processor_id} started")
        
        while self.running:
            try:
                # Get flowfile from input queue with timeout
                try:
                    flowfile = await asyncio.wait_for(
                        self.input_queue.get(), 
                        timeout=1.0
                    )
                except asyncio.TimeoutError:
                    continue
                
                # Process the flowfile
                start_time = time.time()
                result_flowfiles = await self.process(flowfile)
                processing_time = (time.time() - start_time) * 1000
                
                # Update statistics
                self.statistics['flowfiles_received'] += 1
                self.statistics['bytes_received'] += flowfile.size
                self.statistics['processing_time_ms'] += processing_time
                
                # Send to connected processors
                for result_flowfile in result_flowfiles:
                    await self._send_to_connections(result_flowfile)
                    self.statistics['flowfiles_sent'] += 1
                    self.statistics['bytes_sent'] += result_flowfile.size
                
                self.input_queue.task_done()
                
            except Exception as e:
                logger.error(f"Processing error in {self.processor_id}: {e}")
    
    async def _send_to_connections(self, flowfile: FlowFile):
        """Send flowfile to all connected processors"""
        for connection in self.connections:
            try:
                await connection.receive_flowfile(flowfile)
            except Exception as e:
                logger.error(f"Failed to send flowfile to {connection.processor_id}: {e}")
    
    async def receive_flowfile(self, flowfile: FlowFile):
        """Receive a flowfile for processing"""
        try:
            await self.input_queue.put(flowfile)
        except asyncio.QueueFull:
            logger.warning(f"Input queue full for processor {self.processor_id}")
    
    @abstractmethod
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """Process a flowfile and return result flowfiles"""
        pass
    
    async def stop(self):
        """Stop the processor"""
        self.running = False
        logger.info(f"Processor {self.processor_id} stopped")
    
    def get_status(self) -> Dict[str, Any]:
        """Get processor status"""
        return {
            'processor_id': self.processor_id,
            'type': self.__class__.__name__,
            'running': self.running,
            'queue_size': self.input_queue.qsize(),
            'statistics': self.statistics.copy()
        }
