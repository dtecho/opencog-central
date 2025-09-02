
"""
AtomSpaceWriter Processor
Writes flowfile data to OpenCog AtomSpace
"""

import json
import logging
from typing import List, Dict, Any

from nifi.core.processor import Processor, FlowFile

logger = logging.getLogger(__name__)

class AtomSpaceWriterProcessor(Processor):
    """Writes data to AtomSpace"""
    
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """Write flowfile content to AtomSpace"""
        
        if not self.atomspace:
            logger.error("AtomSpace not available")
            return [flowfile]
            
        try:
            # Parse content based on format
            content_type = flowfile.attributes.get("mime.type", "text/plain")
            
            if content_type == "application/json":
                data = json.loads(flowfile.content.decode('utf-8'))
                await self._write_json_to_atomspace(data, flowfile)
            else:
                # Treat as text and create a ConceptNode
                text_content = flowfile.content.decode('utf-8')
                await self._write_text_to_atomspace(text_content, flowfile)
                
            # Add success attribute
            flowfile.attributes["atomspace.write.status"] = "success"
            
        except Exception as e:
            logger.error(f"Error writing to AtomSpace: {e}")
            flowfile.attributes["atomspace.write.status"] = "failed"
            flowfile.attributes["atomspace.write.error"] = str(e)
            
        self.update_stats(flowfile)
        return [flowfile]
        
    async def _write_json_to_atomspace(self, data: Dict[str, Any], flowfile: FlowFile):
        """Write JSON data as structured atoms"""
        
        # Create a ConceptNode for the main data
        concept_name = data.get("concept", f"FlowFile_{flowfile.id}")
        
        # In a real implementation, this would use the actual AtomSpace API
        logger.info(f"Would create ConceptNode: {concept_name}")
        logger.info(f"Would create attributes: {data}")
        
        # Simulate AtomSpace operations
        await asyncio.sleep(0.01)  # Simulate I/O
        
    async def _write_text_to_atomspace(self, text: str, flowfile: FlowFile):
        """Write text content as ConceptNode"""
        
        concept_name = f"TextConcept_{flowfile.id}"
        
        # In a real implementation, this would use the actual AtomSpace API
        logger.info(f"Would create ConceptNode: {concept_name} with text: {text[:100]}...")
        
        # Simulate AtomSpace operations
        await asyncio.sleep(0.01)  # Simulate I/O
