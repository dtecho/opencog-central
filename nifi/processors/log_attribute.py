
"""
LogAttribute Processor
Logs flowfile attributes and content for debugging
"""

import logging
from typing import List

from nifi.core.processor import Processor, FlowFile

logger = logging.getLogger(__name__)

class LogAttributeProcessor(Processor):
    """Logs flowfile attributes and optionally content"""
    
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """Log flowfile information and pass it through"""
        
        log_level = self.config.get("log_level", "INFO").upper()
        log_content = self.config.get("log_content", False)
        max_content_length = self.config.get("max_content_length", 1000)
        
        # Prepare log message
        log_msg = f"FlowFile {flowfile.id}:"
        log_msg += f"\n  Size: {flowfile.size} bytes"
        log_msg += f"\n  Created: {flowfile.created}"
        log_msg += f"\n  Attributes: {flowfile.attributes}"
        
        if log_content and flowfile.content:
            content_preview = flowfile.content[:max_content_length]
            if len(flowfile.content) > max_content_length:
                content_preview += b"... (truncated)"
            log_msg += f"\n  Content: {content_preview.decode('utf-8', errors='ignore')}"
            
        # Log at specified level
        if log_level == "DEBUG":
            logger.debug(log_msg)
        elif log_level == "INFO":
            logger.info(log_msg)
        elif log_level == "WARNING":
            logger.warning(log_msg)
        elif log_level == "ERROR":
            logger.error(log_msg)
            
        # Update processing stats
        self.update_stats(flowfile)
        
        # Pass flowfile through unchanged
        return [flowfile]
