
"""
Reasoning Processor
Applies logical reasoning to flowfile data
"""

import json
import logging
from typing import List, Dict, Any

from nifi.core.processor import Processor, FlowFile

logger = logging.getLogger(__name__)

class ReasoningProcessor(Processor):
    """Applies PLN reasoning to flowfile content"""
    
    async def process(self, flowfile: FlowFile) -> List[FlowFile]:
        """Apply reasoning operations"""
        
        try:
            reasoning_type = self.config.get("reasoning_type", "deduction")
            confidence_threshold = self.config.get("confidence_threshold", 0.5)
            
            # Parse input data
            if flowfile.attributes.get("mime.type") == "application/json":
                input_data = json.loads(flowfile.content.decode('utf-8'))
            else:
                input_data = {"text": flowfile.content.decode('utf-8')}
                
            # Apply reasoning based on type
            if reasoning_type == "deduction":
                result = await self._apply_deduction(input_data, confidence_threshold)
            elif reasoning_type == "induction":
                result = await self._apply_induction(input_data, confidence_threshold)
            elif reasoning_type == "abduction":
                result = await self._apply_abduction(input_data, confidence_threshold)
            else:
                raise ValueError(f"Unknown reasoning type: {reasoning_type}")
                
            # Create result flowfile
            result_flowfile = FlowFile()
            result_flowfile.content = json.dumps(result).encode('utf-8')
            result_flowfile.attributes.update({
                "mime.type": "application/json",
                "filename": f"reasoning_result_{result_flowfile.id}.json",
                "reasoning.type": reasoning_type,
                "reasoning.confidence": str(result.get("confidence", 0))
            })
            result_flowfile.size = len(result_flowfile.content)
            
            self.update_stats(result_flowfile)
            return [result_flowfile]
            
        except Exception as e:
            logger.error(f"Error in reasoning processor: {e}")
            flowfile.attributes["reasoning.error"] = str(e)
            return [flowfile]
            
    async def _apply_deduction(self, data: Dict[str, Any], threshold: float) -> Dict[str, Any]:
        """Apply deductive reasoning"""
        return {
            "reasoning_type": "deduction",
            "premises": data.get("premises", []),
            "conclusions": ["deduced_conclusion_1", "deduced_conclusion_2"],
            "confidence": 0.8,
            "rules_applied": ["modus_ponens", "universal_instantiation"]
        }
        
    async def _apply_induction(self, data: Dict[str, Any], threshold: float) -> Dict[str, Any]:
        """Apply inductive reasoning"""
        return {
            "reasoning_type": "induction",
            "observations": data.get("observations", []),
            "generalizations": ["induced_pattern_1", "induced_pattern_2"],
            "confidence": 0.6,
            "sample_size": len(data.get("observations", []))
        }
        
    async def _apply_abduction(self, data: Dict[str, Any], threshold: float) -> Dict[str, Any]:
        """Apply abductive reasoning"""
        return {
            "reasoning_type": "abduction",
            "observations": data.get("observations", []),
            "explanations": ["hypothesis_1", "hypothesis_2"],
            "confidence": 0.7,
            "plausibility_scores": [0.8, 0.6]
        }
