
"""
GenerateFlowFile Processor
Generates synthetic data for testing and demonstration
"""

import asyncio
import json
import time
from typing import List

from ..core.processor import MiniNiFiProcessor, FlowFile

class GenerateFlowFileProcessor(MiniNiFiProcessor):
    """Generates flowfiles with synthetic data"""
    
    async def initialize(self):
        await super().initialize()
        self.interval = float(self.properties.get('interval', '5.0'))
        self.data_format = self.properties.get('format', 'json')
        
        # Start generation task
        if not hasattr(self, '_generation_task'):
            self._generation_task = asyncio.create_task(self._generate_loop())
    
    async def _generate_loop(self):
        """Continuously generate flowfiles"""
        counter = 0
        
        while self.running:
            try:
                # Generate synthetic data
                if self.data_format == 'json':
                    data = {
                        'timestamp': time.time(),
                        'counter': counter,
                        'agent_id': 'minifi-agent',
                        'message': f'Generated data item {counter}'
                    }
                    content = json.dumps(data).encode('utf-8')
                else:
                    content = f"Generated data item {counter}\n".encode('utf-8')
                
                # Create flowfile
                flowfile = FlowFile(
                    content=content,
                    attributes={
                        'filename': f'generated-{counter}.{self.data_format}',
                        'generator': self.processor_id,
                        'format': self.data_format
                    }
                )
                
                # Send to connections
                await self._send_to_connections(flowfile)
                
                counter += 1
                await asyncio.sleep(self.interval)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Generation error: {e}")
                await asyncio.sleep(1)
    
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """This processor generates data, doesn't process incoming flowfiles"""
        return [flowfile]  # Pass through
    
    async def stop(self):
        """Stop the processor"""
        await super().stop()
        if hasattr(self, '_generation_task'):
            self._generation_task.cancel()
