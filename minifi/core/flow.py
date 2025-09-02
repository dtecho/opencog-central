
"""
MiniNiFi Flow
Represents a data flow with connected processors
"""

import asyncio
import logging
from typing import Dict, Any, List
from .processor import MiniNiFiProcessor

logger = logging.getLogger(__name__)

class MiniNiFiFlow:
    """Represents a data processing flow"""
    
    def __init__(self, flow_id: str, config: Dict[str, Any], available_processors: Dict[str, type]):
        self.flow_id = flow_id
        self.config = config
        self.available_processors = available_processors
        self.processors = {}
        self.connections = []
        self.running = False
        self._tasks = []
    
    async def initialize(self):
        """Initialize the flow from configuration"""
        # Create processors
        for proc_config in self.config.get('processors', []):
            await self._create_processor(proc_config)
        
        # Create connections
        for conn_config in self.config.get('connections', []):
            self._create_connection(conn_config)
        
        logger.info(f"Flow {self.flow_id} initialized with {len(self.processors)} processors")
    
    async def _create_processor(self, proc_config: Dict[str, Any]):
        """Create a processor instance"""
        proc_id = proc_config['id']
        proc_type = proc_config['type']
        
        if proc_type not in self.available_processors:
            raise ValueError(f"Unknown processor type: {proc_type}")
        
        processor_class = self.available_processors[proc_type]
        processor = processor_class(proc_id, proc_config)
        
        await processor.initialize()
        self.processors[proc_id] = processor
    
    def _create_connection(self, conn_config: Dict[str, Any]):
        """Create a connection between processors"""
        source_id = conn_config['source']
        destination_id = conn_config['destination']
        
        if source_id not in self.processors or destination_id not in self.processors:
            raise ValueError(f"Invalid connection: {source_id} -> {destination_id}")
        
        source = self.processors[source_id]
        destination = self.processors[destination_id]
        
        # Connect processors
        source.add_connection(destination)
        
        self.connections.append({
            'source': source_id,
            'destination': destination_id,
            'relationship': conn_config.get('relationship', 'success')
        })
    
    async def start(self):
        """Start the flow"""
        self.running = True
        
        # Start all processors
        for processor in self.processors.values():
            task = asyncio.create_task(processor.run())
            self._tasks.append(task)
        
        logger.info(f"Flow {self.flow_id} started")
    
    async def stop(self):
        """Stop the flow"""
        self.running = False
        
        # Stop all processors
        for processor in self.processors.values():
            await processor.stop()
        
        # Cancel all tasks
        for task in self._tasks:
            task.cancel()
        
        await asyncio.gather(*self._tasks, return_exceptions=True)
        self._tasks.clear()
        
        logger.info(f"Flow {self.flow_id} stopped")
    
    def get_status(self) -> Dict[str, Any]:
        """Get flow status"""
        return {
            'flow_id': self.flow_id,
            'running': self.running,
            'processors': {pid: proc.get_status() for pid, proc in self.processors.items()},
            'connections': self.connections
        }
