
"""
GenerateFlowFile Processor
Creates flowfiles with configurable content
"""

import asyncio
import json
from typing import List, Dict, Any

from nifi.core.processor import Processor, FlowFile

class GenerateFlowFileProcessor(Processor):
    """Generates flowfiles with specified content"""
    
    async def process(self, flowfile: FlowFile = None) -> List[FlowFile]:
        """Generate a new flowfile"""
        
        # Get configuration
        content = self.config.get("content", "Generated content")
        file_format = self.config.get("format", "text")
        attributes = self.config.get("attributes", {})
        
        # Create new flowfile
        new_flowfile = FlowFile()
        
        # Set content based on format
        if file_format == "json":
            new_flowfile.content = json.dumps({
                "message": content,
                "timestamp": new_flowfile.created.isoformat(),
                "processor": self.id
            }).encode('utf-8')
            new_flowfile.attributes["mime.type"] = "application/json"
        else:
            new_flowfile.content = content.encode('utf-8')
            new_flowfile.attributes["mime.type"] = "text/plain"
            
        # Add configured attributes
        new_flowfile.attributes.update(attributes)
        new_flowfile.attributes["filename"] = f"generated_{new_flowfile.id}.{file_format}"
        new_flowfile.size = len(new_flowfile.content)
        
        self.update_stats(new_flowfile)
        
        return [new_flowfile]
        
    async def start(self):
        """Start the processor with periodic generation if configured"""
        await super().start()
        
        # Check if this is a periodic generator
        interval = self.config.get("interval_seconds", 0)
        if interval > 0:
            asyncio.create_task(self._periodic_generation(interval))
            
    async def _periodic_generation(self, interval: float):
        """Generate flowfiles periodically"""
        while self.status == "RUNNING":
            try:
                flowfiles = await self.process()
                # In a real implementation, these would be sent to downstream processors
                # For now, we just log the generation
                for ff in flowfiles:
                    logger.info(f"Generated flowfile {ff.id} with {ff.size} bytes")
            except Exception as e:
                logger.error(f"Error in periodic generation: {e}")
                
            await asyncio.sleep(interval)
