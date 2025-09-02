
"""
AtomSpaceReader Processor
Reads data from OpenCog AtomSpace
"""

import json
import logging
from typing import List

from nifi.core.processor import Processor, FlowFile

logger = logging.getLogger(__name__)

class AtomSpaceReaderProcessor(Processor):
    """Reads data from AtomSpace"""
    
    async def process(self, flowfile: FlowFile = None) -> List[FlowFile]:
        """Read data from AtomSpace and create flowfiles"""
        
        if not self.atomspace:
            logger.error("AtomSpace not available")
            return []
            
        try:
            # Get query parameters from config
            query_type = self.config.get("query_type", "concept")
            query_pattern = self.config.get("query_pattern", "*")
            max_results = self.config.get("max_results", 100)
            
            # Execute query (simulated)
            results = await self._execute_atomspace_query(query_type, query_pattern, max_results)
            
            # Create flowfiles from results
            result_flowfiles = []
            for result in results:
                new_flowfile = FlowFile()
                new_flowfile.content = json.dumps(result).encode('utf-8')
                new_flowfile.attributes.update({
                    "mime.type": "application/json",
                    "filename": f"atomspace_result_{new_flowfile.id}.json",
                    "atomspace.query.type": query_type,
                    "atomspace.query.pattern": query_pattern
                })
                new_flowfile.size = len(new_flowfile.content)
                
                result_flowfiles.append(new_flowfile)
                self.update_stats(new_flowfile)
                
            return result_flowfiles
            
        except Exception as e:
            logger.error(f"Error reading from AtomSpace: {e}")
            return []
            
    async def _execute_atomspace_query(self, query_type: str, pattern: str, max_results: int) -> List[Dict]:
        """Execute query against AtomSpace"""
        
        # Simulate AtomSpace query
        await asyncio.sleep(0.05)  # Simulate query time
        
        # Return mock results
        if query_type == "concept":
            return [
                {
                    "type": "ConceptNode",
                    "name": f"Concept_{i}",
                    "tv": {"strength": 0.8, "confidence": 0.9}
                }
                for i in range(min(max_results, 10))
            ]
        elif query_type == "predicate":
            return [
                {
                    "type": "PredicateNode", 
                    "name": f"Predicate_{i}",
                    "tv": {"strength": 0.7, "confidence": 0.8}
                }
                for i in range(min(max_results, 5))
            ]
        else:
            return []
