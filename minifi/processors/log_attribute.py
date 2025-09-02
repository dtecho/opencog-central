
"""
LogAttribute Processor
Logs flowfile attributes and content
"""

import logging
from typing import List

from ..core.processor import MiniNiFiProcessor, FlowFile

logger = logging.getLogger(__name__)

class LogAttributeProcessor(MiniNiFiProcessor):
    """Logs flowfile attributes and optionally content"""
    
    async def initialize(self):
        await super().initialize()
        self.log_level = self.properties.get('log_level', 'INFO').upper()
        self.log_content = self.properties.get('log_content', 'false').lower() == 'true'
        self.max_content_length = int(self.properties.get('max_content_length', '1024'))
    
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """Log flowfile information"""
        
        # Prepare log message
        log_msg = f"FlowFile[{flowfile.uuid}] attributes: {flowfile.attributes}"
        
        if self.log_content and flowfile.content:
            content_preview = flowfile.content[:self.max_content_length]
            if len(flowfile.content) > self.max_content_length:
                content_preview += b"... (truncated)"
            
            try:
                content_str = content_preview.decode('utf-8', errors='replace')
                log_msg += f" content: {content_str}"
            except Exception:
                log_msg += f" content: <binary data, {len(flowfile.content)} bytes>"
        
        # Log at specified level
        if self.log_level == 'DEBUG':
            logger.debug(log_msg)
        elif self.log_level == 'WARNING':
            logger.warning(log_msg)
        elif self.log_level == 'ERROR':
            logger.error(log_msg)
        else:  # INFO
            logger.info(log_msg)
        
        return [flowfile]  # Pass through unchanged
