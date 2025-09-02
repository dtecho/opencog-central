
"""
Core Flow Processing Engine
Manages data flows, processors, and execution
"""

import asyncio
import logging
import uuid
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from datetime import datetime

from .flow import Flow
from .processor import Processor
from .connection import Connection

logger = logging.getLogger(__name__)

@dataclass
class FlowEngineStats:
    flows_active: int = 0
    processors_running: int = 0
    connections_active: int = 0
    flowfiles_processed: int = 0
    total_bytes_processed: int = 0
    uptime_seconds: float = 0

class FlowEngine:
    """Core engine for managing and executing data flows"""
    
    def __init__(self):
        self.flows: Dict[str, Flow] = {}
        self.processors: Dict[str, Processor] = {}
        self.connections: Dict[str, Connection] = {}
        self.running = False
        self.atomspace_connector = None
        self.stats = FlowEngineStats()
        self.start_time = datetime.now()
        
    def register_atomspace(self, connector):
        """Register AtomSpace connector"""
        self.atomspace_connector = connector
        logger.info("AtomSpace connector registered")
        
    def create_flow(self, name: str, description: str = "") -> str:
        """Create a new data flow"""
        flow_id = str(uuid.uuid4())
        flow = Flow(flow_id, name, description)
        self.flows[flow_id] = flow
        logger.info(f"Created flow: {name} ({flow_id})")
        return flow_id
        
    def add_processor(self, flow_id: str, processor_type: str, config: Dict[str, Any]) -> str:
        """Add a processor to a flow"""
        if flow_id not in self.flows:
            raise ValueError(f"Flow {flow_id} not found")
            
        processor_id = str(uuid.uuid4())
        processor = Processor.create(processor_type, processor_id, config)
        
        # Set AtomSpace reference if available
        if self.atomspace_connector:
            processor.set_atomspace(self.atomspace_connector)
            
        self.processors[processor_id] = processor
        self.flows[flow_id].add_processor(processor_id)
        
        logger.info(f"Added processor {processor_type} to flow {flow_id}")
        return processor_id
        
    def create_connection(self, source_id: str, destination_id: str, 
                         source_relationship: str = "success") -> str:
        """Create a connection between processors"""
        connection_id = str(uuid.uuid4())
        connection = Connection(
            connection_id, 
            source_id, 
            destination_id, 
            source_relationship
        )
        
        self.connections[connection_id] = connection
        logger.info(f"Created connection from {source_id} to {destination_id}")
        return connection_id
        
    async def start_flow(self, flow_id: str):
        """Start executing a flow"""
        if flow_id not in self.flows:
            raise ValueError(f"Flow {flow_id} not found")
            
        flow = self.flows[flow_id]
        flow.status = "RUNNING"
        
        # Start all processors in the flow
        for processor_id in flow.processor_ids:
            processor = self.processors[processor_id]
            await processor.start()
            
        logger.info(f"Started flow: {flow.name}")
        
    async def stop_flow(self, flow_id: str):
        """Stop executing a flow"""
        if flow_id not in self.flows:
            raise ValueError(f"Flow {flow_id} not found")
            
        flow = self.flows[flow_id]
        flow.status = "STOPPED"
        
        # Stop all processors in the flow
        for processor_id in flow.processor_ids:
            processor = self.processors[processor_id]
            await processor.stop()
            
        logger.info(f"Stopped flow: {flow.name}")
        
    def get_flow_status(self, flow_id: str) -> Dict[str, Any]:
        """Get status information for a flow"""
        if flow_id not in self.flows:
            raise ValueError(f"Flow {flow_id} not found")
            
        flow = self.flows[flow_id]
        processors_status = {}
        
        for processor_id in flow.processor_ids:
            processor = self.processors[processor_id]
            processors_status[processor_id] = {
                "type": processor.processor_type,
                "status": processor.status,
                "flowfiles_processed": processor.flowfiles_processed,
                "bytes_processed": processor.bytes_processed
            }
            
        return {
            "id": flow_id,
            "name": flow.name,
            "status": flow.status,
            "processors": processors_status,
            "created": flow.created.isoformat(),
            "last_modified": flow.last_modified.isoformat()
        }
        
    def get_engine_stats(self) -> Dict[str, Any]:
        """Get overall engine statistics"""
        self.stats.flows_active = len([f for f in self.flows.values() if f.status == "RUNNING"])
        self.stats.processors_running = len([p for p in self.processors.values() if p.status == "RUNNING"])
        self.stats.connections_active = len(self.connections)
        self.stats.uptime_seconds = (datetime.now() - self.start_time).total_seconds()
        
        return {
            "flows_active": self.stats.flows_active,
            "processors_running": self.stats.processors_running,
            "connections_active": self.stats.connections_active,
            "flowfiles_processed": self.stats.flowfiles_processed,
            "total_bytes_processed": self.stats.total_bytes_processed,
            "uptime_seconds": self.stats.uptime_seconds,
            "atomspace_connected": self.atomspace_connector is not None
        }
        
    def list_flows(self) -> List[Dict[str, Any]]:
        """List all flows with basic information"""
        return [
            {
                "id": flow.id,
                "name": flow.name,
                "status": flow.status,
                "processor_count": len(flow.processor_ids),
                "created": flow.created.isoformat()
            }
            for flow in self.flows.values()
        ]
