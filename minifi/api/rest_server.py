
"""
MiniNiFi REST Server
Provides REST API endpoints for agent management
"""

import json
import logging
from aiohttp import web, web_request
from aiohttp_cors import setup as cors_setup, ResourceOptions
from typing import Dict, Any

logger = logging.getLogger(__name__)

class MiniNiFiRestServer:
    """REST API server for MiniNiFi agent"""
    
    def __init__(self, agent, port: int = 8081):
        self.agent = agent
        self.port = port
        self.app = None
        self.runner = None
        self.site = None
        
    async def start(self):
        """Start the REST server"""
        self.app = web.Application()
        
        # Setup CORS
        cors = cors_setup(self.app, defaults={
            "*": ResourceOptions(
                allow_credentials=True,
                expose_headers="*",
                allow_headers="*",
                allow_methods="*"
            )
        })
        
        # Add routes
        self.app.router.add_get('/status', self.get_status)
        self.app.router.add_get('/flows', self.get_flows)
        self.app.router.add_post('/flows', self.create_flow)
        self.app.router.add_delete('/flows/{flow_id}', self.delete_flow)
        self.app.router.add_get('/processors', self.get_processors)
        self.app.router.add_get('/health', self.health_check)
        
        # Add CORS to all routes
        for route in list(self.app.router.routes()):
            cors.add(route)
        
        # Start server
        self.runner = web.AppRunner(self.app)
        await self.runner.setup()
        
        self.site = web.TCPSite(self.runner, '0.0.0.0', self.port)
        await self.site.start()
        
        logger.info(f"REST API server started on port {self.port}")
    
    async def stop(self):
        """Stop the REST server"""
        if self.site:
            await self.site.stop()
        if self.runner:
            await self.runner.cleanup()
        
        logger.info("REST API server stopped")
    
    async def get_status(self, request: web_request.Request) -> web.Response:
        """Get agent status"""
        status = self.agent.get_status()
        return web.json_response(status)
    
    async def get_flows(self, request: web_request.Request) -> web.Response:
        """Get all flows"""
        flows = {fid: flow.get_status() for fid, flow in self.agent.flows.items()}
        return web.json_response(flows)
    
    async def create_flow(self, request: web_request.Request) -> web.Response:
        """Create a new flow"""
        try:
            flow_config = await request.json()
            flow_id = await self.agent.create_flow(flow_config)
            
            return web.json_response({
                'success': True,
                'flow_id': flow_id,
                'message': f'Flow {flow_id} created successfully'
            })
            
        except Exception as e:
            logger.error(f"Failed to create flow: {e}")
            return web.json_response({
                'success': False,
                'error': str(e)
            }, status=400)
    
    async def delete_flow(self, request: web_request.Request) -> web.Response:
        """Delete a flow"""
        flow_id = request.match_info['flow_id']
        
        try:
            await self.agent.remove_flow(flow_id)
            
            return web.json_response({
                'success': True,
                'message': f'Flow {flow_id} deleted successfully'
            })
            
        except Exception as e:
            logger.error(f"Failed to delete flow {flow_id}: {e}")
            return web.json_response({
                'success': False,
                'error': str(e)
            }, status=400)
    
    async def get_processors(self, request: web_request.Request) -> web.Response:
        """Get available processor types"""
        processors = {
            name: {
                'name': name,
                'class': cls.__name__,
                'description': cls.__doc__ or f'{name} processor'
            }
            for name, cls in self.agent.processors.items()
        }
        
        return web.json_response(processors)
    
    async def health_check(self, request: web_request.Request) -> web.Response:
        """Health check endpoint"""
        health_status = {
            'status': 'healthy' if self.agent.running else 'stopped',
            'agent_id': self.agent.config['agent']['id'],
            'timestamp': time.time(),
            'flows_running': sum(1 for flow in self.agent.flows.values() if flow.running)
        }
        
        return web.json_response(health_status)
