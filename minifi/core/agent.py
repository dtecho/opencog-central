
"""
MiniNiFi Agent
Core agent implementation for lightweight data flow processing
"""

import asyncio
import yaml
import logging
from typing import Dict, Any, List, Optional
from pathlib import Path

from .flow import MiniNiFiFlow
from .processor import MiniNiFiProcessor

logger = logging.getLogger(__name__)

class MiniNiFiAgent:
    """Main MiniNiFi agent for managing flows and processors"""
    
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = {}
        self.flows = {}
        self.processors = {}
        self.atomspace_connector = None
        self.c2_client = None
        self.running = False
        self._tasks = []
        
    async def initialize(self):
        """Initialize the agent with configuration"""
        await self._load_config()
        await self._initialize_processors()
        logger.info(f"Agent {self.config['agent']['id']} initialized")
        
    async def _load_config(self):
        """Load configuration from YAML file"""
        try:
            with open(self.config_path, 'r') as f:
                self.config = yaml.safe_load(f)
        except Exception as e:
            logger.error(f"Failed to load config: {e}")
            # Use default config
            self.config = {
                'agent': {'id': 'default-agent', 'name': 'Default MiniNiFi Agent'},
                'server': {'port': 8081, 'host': '0.0.0.0'},
                'logging': {'level': 'INFO'}
            }
    
    async def _initialize_processors(self):
        """Initialize default processors"""
        from ..processors.generate_flowfile import GenerateFlowFileProcessor
        from ..processors.log_attribute import LogAttributeProcessor
        
        # Register default processors
        self.processors['GenerateFlowFile'] = GenerateFlowFileProcessor
        self.processors['LogAttribute'] = LogAttributeProcessor
        
        if self.atomspace_connector:
            from ..processors.atomspace_reader import AtomSpaceReaderProcessor
            from ..processors.atomspace_writer import AtomSpaceWriterProcessor
            self.processors['AtomSpaceReader'] = AtomSpaceReaderProcessor
            self.processors['AtomSpaceWriter'] = AtomSpaceWriterProcessor
    
    def register_atomspace(self, connector):
        """Register AtomSpace connector"""
        self.atomspace_connector = connector
        logger.info("AtomSpace connector registered")
    
    def register_c2_client(self, client):
        """Register C2 client for remote management"""
        self.c2_client = client
        logger.info("C2 client registered")
    
    async def start(self):
        """Start the agent and all flows"""
        self.running = True
        
        # Start heartbeat if C2 is enabled
        if self.c2_client:
            task = asyncio.create_task(self._heartbeat_loop())
            self._tasks.append(task)
        
        # Start monitoring task
        task = asyncio.create_task(self._monitoring_loop())
        self._tasks.append(task)
        
        logger.info("Agent started")
    
    async def stop(self):
        """Stop the agent and all flows"""
        self.running = False
        
        # Stop all flows
        for flow in self.flows.values():
            await flow.stop()
        
        # Cancel all tasks
        for task in self._tasks:
            task.cancel()
        
        # Wait for tasks to complete
        await asyncio.gather(*self._tasks, return_exceptions=True)
        
        logger.info("Agent stopped")
    
    async def _heartbeat_loop(self):
        """Send heartbeat to C2 server"""
        interval = self.config.get('c2', {}).get('heartbeat_interval', 30)
        
        while self.running:
            try:
                if self.c2_client:
                    await self.c2_client.send_heartbeat()
            except Exception as e:
                logger.warning(f"Heartbeat failed: {e}")
            
            await asyncio.sleep(interval)
    
    async def _monitoring_loop(self):
        """Monitor agent health and resources"""
        while self.running:
            try:
                # Basic health monitoring
                flow_count = len(self.flows)
                processor_count = sum(len(flow.processors) for flow in self.flows.values())
                
                logger.debug(f"Agent health: {flow_count} flows, {processor_count} processors")
                
                # Resource monitoring if enabled
                if self.config.get('edge', {}).get('resource_monitoring', False):
                    import psutil
                    cpu_percent = psutil.cpu_percent()
                    memory_percent = psutil.virtual_memory().percent
                    
                    if cpu_percent > 80 or memory_percent > 80:
                        logger.warning(f"High resource usage: CPU {cpu_percent}%, Memory {memory_percent}%")
                
            except Exception as e:
                logger.warning(f"Monitoring error: {e}")
            
            await asyncio.sleep(60)  # Monitor every minute
    
    async def create_flow(self, flow_config: Dict[str, Any]) -> str:
        """Create a new flow from configuration"""
        flow_id = flow_config.get('id', f'flow-{len(self.flows)}')
        
        flow = MiniNiFiFlow(flow_id, flow_config, self.processors)
        await flow.initialize()
        
        self.flows[flow_id] = flow
        
        if self.running:
            await flow.start()
        
        logger.info(f"Flow {flow_id} created")
        return flow_id
    
    async def remove_flow(self, flow_id: str):
        """Remove a flow"""
        if flow_id in self.flows:
            flow = self.flows[flow_id]
            await flow.stop()
            del self.flows[flow_id]
            logger.info(f"Flow {flow_id} removed")
    
    def get_status(self) -> Dict[str, Any]:
        """Get agent status"""
        return {
            'agent_id': self.config['agent']['id'],
            'running': self.running,
            'flows': {fid: flow.get_status() for fid, flow in self.flows.items()},
            'uptime': 0,  # TODO: implement uptime tracking
            'resource_usage': self._get_resource_usage()
        }
    
    def _get_resource_usage(self) -> Dict[str, Any]:
        """Get current resource usage"""
        try:
            import psutil
            return {
                'cpu_percent': psutil.cpu_percent(),
                'memory_percent': psutil.virtual_memory().percent,
                'disk_usage': psutil.disk_usage('.').percent
            }
        except ImportError:
            return {'cpu_percent': 0, 'memory_percent': 0, 'disk_usage': 0}
