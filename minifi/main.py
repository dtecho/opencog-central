
#!/usr/bin/env python3
"""
Apache MiniNiFi - Lightweight Data Flow Processing Agent for OpenCog
Main application entry point
"""

import asyncio
import logging
import argparse
import signal
import sys
from pathlib import Path

from minifi.core.agent import MiniNiFiAgent
from minifi.c2.client import C2Client
from minifi.atomspace.connector import AtomSpaceConnector
from minifi.api.rest_server import MiniNiFiRestServer

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MiniNiFiApplication:
    def __init__(self, config_path="minifi/config/minifi.yaml"):
        self.config_path = config_path
        self.agent = None
        self.c2_client = None
        self.atomspace_connector = None
        self.rest_server = None
        self.running = False
        
    async def start(self):
        """Start the MiniNiFi agent"""
        logger.info("Starting Apache MiniNiFi Agent...")
        
        # Initialize core components
        self.agent = MiniNiFiAgent(self.config_path)
        await self.agent.initialize()
        
        # Initialize AtomSpace connection if configured
        if self.agent.config.get('atomspace', {}).get('enabled', False):
            self.atomspace_connector = AtomSpaceConnector(
                self.agent.config['atomspace'].get('host', 'localhost'),
                self.agent.config['atomspace'].get('port', 17001)
            )
            await self.atomspace_connector.connect()
            self.agent.register_atomspace(self.atomspace_connector)
        
        # Initialize C2 client if configured
        if self.agent.config.get('c2', {}).get('enabled', False):
            self.c2_client = C2Client(
                self.agent.config['c2'].get('url'),
                self.agent.config['c2'].get('agent_id', 'minifi-agent-001')
            )
            await self.c2_client.connect()
            self.agent.register_c2_client(self.c2_client)
        
        # Start REST API if configured
        if self.agent.config.get('api', {}).get('enabled', False):
            self.rest_server = MiniNiFiRestServer(
                self.agent,
                self.agent.config['api'].get('port', 8081)
            )
            await self.rest_server.start()
        
        # Start the agent
        await self.agent.start()
        self.running = True
        
        logger.info("MiniNiFi Agent started successfully")
        if self.rest_server:
            logger.info(f"REST API available at http://0.0.0.0:{self.rest_server.port}")
        
    async def stop(self):
        """Stop the MiniNiFi agent"""
        logger.info("Stopping MiniNiFi Agent...")
        self.running = False
        
        if self.agent:
            await self.agent.stop()
        if self.c2_client:
            await self.c2_client.disconnect()
        if self.atomspace_connector:
            await self.atomspace_connector.disconnect()
        if self.rest_server:
            await self.rest_server.stop()
            
        logger.info("MiniNiFi Agent stopped")

async def main():
    parser = argparse.ArgumentParser(description="Apache MiniNiFi Agent for OpenCog")
    parser.add_argument("--config", default="minifi/config/minifi.yaml", 
                       help="Configuration file path")
    parser.add_argument("--agent-id", help="Override agent ID from config")
    
    args = parser.parse_args()
    
    app = MiniNiFiApplication(args.config)
    
    # Setup signal handlers
    def signal_handler(signum, frame):
        logger.info(f"Received signal {signum}, shutting down...")
        asyncio.create_task(app.stop())
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    try:
        await app.start()
        # Keep running until shutdown
        while app.running:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")
    except Exception as e:
        logger.error(f"Application error: {e}")
    finally:
        await app.stop()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Application interrupted")
        sys.exit(0)
