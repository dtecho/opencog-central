
#!/usr/bin/env python3
"""
Apache NiFi-like Data Flow Processing System for OpenCog
Main application entry point
"""

import asyncio
import logging
import argparse
from pathlib import Path

from nifi.core.flow_engine import FlowEngine
from nifi.web.server import NiFiWebServer
from nifi.api.rest_api import NiFiRestAPI
from nifi.atomspace.connector import AtomSpaceConnector

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NiFiApplication:
    def __init__(self, port=8080, atomspace_host="localhost", atomspace_port=17001):
        self.port = port
        self.atomspace_host = atomspace_host
        self.atomspace_port = atomspace_port
        
        # Initialize core components
        self.flow_engine = FlowEngine()
        self.atomspace_connector = AtomSpaceConnector(atomspace_host, atomspace_port)
        self.web_server = NiFiWebServer(self.flow_engine, port)
        self.rest_api = NiFiRestAPI(self.flow_engine)
        
    async def start(self):
        """Start the NiFi application"""
        logger.info("Starting Apache NiFi for OpenCog...")
        
        # Initialize AtomSpace connection
        await self.atomspace_connector.connect()
        
        # Register AtomSpace with flow engine
        self.flow_engine.register_atomspace(self.atomspace_connector)
        
        # Start web server
        await self.web_server.start()
        
        logger.info(f"NiFi Web UI available at http://0.0.0.0:{self.port}/nifi")
        logger.info(f"NiFi REST API available at http://0.0.0.0:{self.port}/api")
        
    async def stop(self):
        """Stop the NiFi application"""
        logger.info("Stopping Apache NiFi...")
        await self.web_server.stop()
        await self.atomspace_connector.disconnect()

async def main():
    parser = argparse.ArgumentParser(description="Apache NiFi for OpenCog")
    parser.add_argument("--port", type=int, default=8080, help="Web server port")
    parser.add_argument("--atomspace-host", default="localhost", help="AtomSpace host")
    parser.add_argument("--atomspace-port", type=int, default=17001, help="AtomSpace port")
    
    args = parser.parse_args()
    
    app = NiFiApplication(
        port=args.port,
        atomspace_host=args.atomspace_host,
        atomspace_port=args.atomspace_port
    )
    
    try:
        await app.start()
        # Keep running
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info("Received shutdown signal")
    finally:
        await app.stop()

if __name__ == "__main__":
    asyncio.run(main())
