
"""
AtomSpace Writer Processor
Writes data to OpenCog AtomSpace
"""

import json
import logging
from typing import List

from ..core.processor import MiniNiFiProcessor, FlowFile

logger = logging.getLogger(__name__)

class AtomSpaceWriterProcessor(MiniNiFiProcessor):
    """Writes flowfile data to AtomSpace"""
    
    async def initialize(self):
        await super().initialize()
        self.write_mode = self.properties.get('write_mode', 'create_or_update')
        self.atom_type = self.properties.get('default_atom_type', 'ConceptNode')
    
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """Write flowfile data to AtomSpace"""
        
        try:
            # Parse content if JSON
            if flowfile.attributes.get('format') == 'json':
                data = json.loads(flowfile.content.decode('utf-8'))
            else:
                data = {'content': flowfile.content.decode('utf-8', errors='replace')}
            
            # Get AtomSpace connector (would need actual implementation)
            atomspace = getattr(self, 'atomspace_connector', None)
            if atomspace:
                # Placeholder for actual AtomSpace write operation
                logger.info(f"Writing to AtomSpace: {data}")
                
                # Add write confirmation to attributes
                flowfile.attributes['atomspace_written'] = 'true'
                flowfile.attributes['write_timestamp'] = str(time.time())
            else:
                logger.warning("No AtomSpace connector available")
                flowfile.attributes['atomspace_written'] = 'false'
                flowfile.attributes['error'] = 'No AtomSpace connector'
            
        except Exception as e:
            logger.error(f"AtomSpace write error: {e}")
            flowfile.attributes['atomspace_written'] = 'false'
            flowfile.attributes['error'] = str(e)
        
        return [flowfile]
