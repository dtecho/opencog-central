
"""
AtomSpace Reader Processor
Reads data from OpenCog AtomSpace
"""

import json
import logging
from typing import List

from ..core.processor import MiniNiFiProcessor, FlowFile

logger = logging.getLogger(__name__)

class AtomSpaceReaderProcessor(MiniNiFiProcessor):
    """Reads atoms and values from AtomSpace"""
    
    async def initialize(self):
        await super().initialize()
        self.query_type = self.properties.get('query_type', 'get_atoms')
        self.atom_type = self.properties.get('atom_type', 'Node')
        self.query_interval = float(self.properties.get('query_interval', '10.0'))
        
        # Start query task
        if not hasattr(self, '_query_task'):
            self._query_task = asyncio.create_task(self._query_loop())
    
    async def _query_loop(self):
        """Continuously query AtomSpace"""
        while self.running:
            try:
                # Get AtomSpace connector from agent
                atomspace = getattr(self, 'atomspace_connector', None)
                if not atomspace:
                    await asyncio.sleep(self.query_interval)
                    continue
                
                # Perform query (simplified - would need actual AtomSpace integration)
                if self.query_type == 'get_atoms':
                    # Placeholder for actual AtomSpace query
                    data = {
                        'query_type': self.query_type,
                        'atom_type': self.atom_type,
                        'timestamp': time.time(),
                        'result_count': 0,  # Would be actual count
                        'atoms': []  # Would contain actual atoms
                    }
                
                # Create flowfile with query results
                content = json.dumps(data).encode('utf-8')
                flowfile = FlowFile(
                    content=content,
                    attributes={
                        'source': 'atomspace',
                        'query_type': self.query_type,
                        'atom_type': self.atom_type,
                        'format': 'json'
                    }
                )
                
                await self._send_to_connections(flowfile)
                await asyncio.sleep(self.query_interval)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"AtomSpace query error: {e}")
                await asyncio.sleep(1)
    
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """Process incoming flowfiles (pass through)"""
        return [flowfile]
    
    async def stop(self):
        """Stop the processor"""
        await super().stop()
        if hasattr(self, '_query_task'):
            self._query_task.cancel()
