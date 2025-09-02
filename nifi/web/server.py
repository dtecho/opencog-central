
"""
NiFi Web Server
Provides HTTP server for web UI and API endpoints
"""

import asyncio
import logging
import json
from pathlib import Path
from typing import Dict, Any

try:
    from aiohttp import web, WSMsgType
    from aiohttp_cors import setup as cors_setup, ResourceOptions
except ImportError:
    # Fallback for basic HTTP server
    import http.server
    import socketserver
    from urllib.parse import parse_qs, urlparse

logger = logging.getLogger(__name__)

class NiFiWebServer:
    """Web server for NiFi interface"""
    
    def __init__(self, flow_engine, port=8080):
        self.flow_engine = flow_engine
        self.port = port
        self.app = None
        self.server = None
        
    async def start(self):
        """Start the web server"""
        try:
            # Try to use aiohttp if available
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
            self.app.router.add_get('/', self._serve_index)
            self.app.router.add_get('/nifi', self._serve_nifi_ui)
            self.app.router.add_get('/api/flows', self._api_list_flows)
            self.app.router.add_post('/api/flows', self._api_create_flow)
            self.app.router.add_get('/api/flows/{flow_id}', self._api_get_flow)
            self.app.router.add_post('/api/flows/{flow_id}/start', self._api_start_flow)
            self.app.router.add_post('/api/flows/{flow_id}/stop', self._api_stop_flow)
            self.app.router.add_get('/api/stats', self._api_get_stats)
            self.app.router.add_static('/static', Path(__file__).parent / 'static')
            
            # Start server
            runner = web.AppRunner(self.app)
            await runner.setup()
            site = web.TCPSite(runner, '0.0.0.0', self.port)
            await site.start()
            
            logger.info(f"NiFi Web Server started on port {self.port}")
            
        except ImportError:
            # Fallback to simple HTTP server
            logger.warning("aiohttp not available, using basic HTTP server")
            await self._start_basic_server()
            
    async def _start_basic_server(self):
        """Start basic HTTP server as fallback"""
        class NiFiHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/' or self.path == '/nifi':
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b"""
                    <!DOCTYPE html>
                    <html>
                    <head><title>Apache NiFi for OpenCog</title></head>
                    <body>
                        <h1>Apache NiFi for OpenCog</h1>
                        <p>NiFi integration is running. Full web UI requires aiohttp.</p>
                        <p>Install with: pip install aiohttp aiohttp-cors</p>
                    </body>
                    </html>
                    """)
                else:
                    super().do_GET()
                    
        with socketserver.TCPServer(("0.0.0.0", self.port), NiFiHandler) as httpd:
            logger.info(f"Basic HTTP server started on port {self.port}")
            await asyncio.sleep(3600)  # Keep running
            
    async def stop(self):
        """Stop the web server"""
        if self.server:
            await self.server.stop()
            
    async def _serve_index(self, request):
        """Serve the main index page"""
        return web.Response(text="""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Apache NiFi for OpenCog</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .header { background: #326dd6; color: white; padding: 20px; margin: -40px -40px 20px -40px; }
                .nav { margin: 20px 0; }
                .nav a { margin-right: 20px; color: #326dd6; text-decoration: none; }
                .stats { background: #f5f5f5; padding: 15px; border-radius: 5px; }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Apache NiFi for OpenCog</h1>
                <p>Data Flow Processing and Cognitive Integration</p>
            </div>
            
            <div class="nav">
                <a href="/nifi">Flow Designer</a>
                <a href="/api/flows">API</a>
                <a href="/api/stats">Statistics</a>
            </div>
            
            <div class="stats" id="stats">
                Loading statistics...
            </div>
            
            <script>
                fetch('/api/stats')
                    .then(r => r.json())
                    .then(data => {
                        document.getElementById('stats').innerHTML = 
                            '<h3>System Statistics</h3>' +
                            '<p>Active Flows: ' + data.flows_active + '</p>' +
                            '<p>Running Processors: ' + data.processors_running + '</p>' +
                            '<p>AtomSpace Connected: ' + data.atomspace_connected + '</p>' +
                            '<p>Uptime: ' + Math.round(data.uptime_seconds) + ' seconds</p>';
                    });
            </script>
        </body>
        </html>
        """, content_type='text/html')
        
    async def _serve_nifi_ui(self, request):
        """Serve the NiFi flow designer UI"""
        return web.Response(text="""
        <!DOCTYPE html>
        <html>
        <head>
            <title>NiFi Flow Designer</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 0; }
                .toolbar { background: #326dd6; color: white; padding: 10px; }
                .canvas { width: 100%; height: 80vh; background: #f0f0f0; border: 1px solid #ccc; }
                .sidebar { position: fixed; right: 0; top: 50px; width: 300px; background: white; border-left: 1px solid #ccc; height: calc(100vh - 50px); padding: 10px; }
            </style>
        </head>
        <body>
            <div class="toolbar">
                <h2>NiFi Flow Designer</h2>
                <button onclick="createFlow()">New Flow</button>
                <button onclick="loadFlows()">Load Flows</button>
            </div>
            
            <div class="canvas" id="canvas">
                <p style="text-align: center; margin-top: 100px; color: #666;">
                    Drag processors here to build your data flow
                </p>
            </div>
            
            <div class="sidebar">
                <h3>Processors</h3>
                <div draggable="true" data-type="GenerateFlowFile">📄 Generate FlowFile</div>
                <div draggable="true" data-type="LogAttribute">📝 Log Attribute</div>
                <div draggable="true" data-type="AtomSpaceWriter">🧠 AtomSpace Writer</div>
                <div draggable="true" data-type="AtomSpaceReader">🔍 AtomSpace Reader</div>
                <div draggable="true" data-type="CognitiveProcessor">🤖 Cognitive Processor</div>
                
                <h3>Flows</h3>
                <div id="flows-list">Loading...</div>
            </div>
            
            <script>
                function createFlow() {
                    const name = prompt('Flow name:');
                    if (name) {
                        fetch('/api/flows', {
                            method: 'POST',
                            headers: {'Content-Type': 'application/json'},
                            body: JSON.stringify({name: name, description: ''})
                        }).then(() => loadFlows());
                    }
                }
                
                function loadFlows() {
                    fetch('/api/flows')
                        .then(r => r.json())
                        .then(flows => {
                            const list = document.getElementById('flows-list');
                            list.innerHTML = flows.map(f => 
                                '<div onclick="loadFlow(\'' + f.id + '\')">' + f.name + ' (' + f.status + ')</div>'
                            ).join('');
                        });
                }
                
                function loadFlow(flowId) {
                    console.log('Loading flow:', flowId);
                }
                
                // Load flows on page load
                loadFlows();
            </script>
        </body>
        </html>
        """, content_type='text/html')
        
    async def _api_list_flows(self, request):
        """API endpoint to list flows"""
        flows = self.flow_engine.list_flows()
        return web.json_response(flows)
        
    async def _api_create_flow(self, request):
        """API endpoint to create a new flow"""
        data = await request.json()
        flow_id = self.flow_engine.create_flow(
            data.get('name', 'Untitled Flow'),
            data.get('description', '')
        )
        return web.json_response({"id": flow_id, "status": "created"})
        
    async def _api_get_flow(self, request):
        """API endpoint to get flow details"""
        flow_id = request.match_info['flow_id']
        try:
            flow_status = self.flow_engine.get_flow_status(flow_id)
            return web.json_response(flow_status)
        except ValueError as e:
            return web.json_response({"error": str(e)}, status=404)
            
    async def _api_start_flow(self, request):
        """API endpoint to start a flow"""
        flow_id = request.match_info['flow_id']
        try:
            await self.flow_engine.start_flow(flow_id)
            return web.json_response({"status": "started"})
        except ValueError as e:
            return web.json_response({"error": str(e)}, status=404)
            
    async def _api_stop_flow(self, request):
        """API endpoint to stop a flow"""
        flow_id = request.match_info['flow_id']
        try:
            await self.flow_engine.stop_flow(flow_id)
            return web.json_response({"status": "stopped"})
        except ValueError as e:
            return web.json_response({"error": str(e)}, status=404)
            
    async def _api_get_stats(self, request):
        """API endpoint to get engine statistics"""
        stats = self.flow_engine.get_engine_stats()
        return web.json_response(stats)
