
"""
C2 Client
Handles communication with Command and Control server
"""

import asyncio
import aiohttp
import json
import logging
import time
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

class C2Client:
    """Client for communicating with C2 server"""
    
    def __init__(self, c2_url: str, agent_id: str):
        self.c2_url = c2_url
        self.agent_id = agent_id
        self.session = None
        self.connected = False
        self.last_heartbeat = 0
        
    async def connect(self):
        """Connect to C2 server"""
        try:
            self.session = aiohttp.ClientSession()
            
            # Test connection with initial heartbeat
            await self.send_heartbeat()
            self.connected = True
            
            logger.info(f"Connected to C2 server: {self.c2_url}")
            
        except Exception as e:
            logger.error(f"Failed to connect to C2 server: {e}")
            self.connected = False
    
    async def disconnect(self):
        """Disconnect from C2 server"""
        if self.session:
            await self.session.close()
        self.connected = False
        logger.info("Disconnected from C2 server")
    
    async def send_heartbeat(self) -> Optional[Dict[str, Any]]:
        """Send heartbeat to C2 server"""
        if not self.session:
            return None
        
        heartbeat_data = {
            'agent_id': self.agent_id,
            'timestamp': time.time(),
            'status': 'running',
            'uptime': time.time() - self.last_heartbeat if self.last_heartbeat else 0
        }
        
        try:
            async with self.session.post(
                f"{self.c2_url}/heartbeat",
                json=heartbeat_data,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                
                if response.status == 200:
                    self.last_heartbeat = time.time()
                    result = await response.json()
                    
                    # Check for configuration updates
                    if 'config_update' in result:
                        await self._handle_config_update(result['config_update'])
                    
                    return result
                else:
                    logger.warning(f"Heartbeat failed with status {response.status}")
                    
        except Exception as e:
            logger.warning(f"Heartbeat error: {e}")
        
        return None
    
    async def _handle_config_update(self, config_update: Dict[str, Any]):
        """Handle configuration update from C2 server"""
        logger.info(f"Received configuration update: {config_update}")
        
        # Placeholder for configuration update handling
        # In a real implementation, this would update the agent's configuration
        # and potentially restart flows/processors
    
    async def get_configuration(self) -> Optional[Dict[str, Any]]:
        """Get configuration from C2 server"""
        if not self.session:
            return None
        
        try:
            async with self.session.get(
                f"{self.c2_url}/config/{self.agent_id}",
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                
                if response.status == 200:
                    return await response.json()
                else:
                    logger.warning(f"Config fetch failed with status {response.status}")
                    
        except Exception as e:
            logger.warning(f"Config fetch error: {e}")
        
        return None
    
    async def acknowledge_operation(self, operation_id: str, success: bool, message: str = ""):
        """Acknowledge completion of an operation"""
        if not self.session:
            return
        
        ack_data = {
            'agent_id': self.agent_id,
            'operation_id': operation_id,
            'success': success,
            'message': message,
            'timestamp': time.time()
        }
        
        try:
            async with self.session.post(
                f"{self.c2_url}/acknowledge",
                json=ack_data,
                timeout=aiohttp.ClientTimeout(total=10)
            ) as response:
                
                if response.status != 200:
                    logger.warning(f"Acknowledgment failed with status {response.status}")
                    
        except Exception as e:
            logger.warning(f"Acknowledgment error: {e}")
