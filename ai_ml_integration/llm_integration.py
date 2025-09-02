
"""
Large Language Model Integration with OpenCog
Connects LLMs (llama.cpp, koboldcpp) with cognitive architectures
"""

import subprocess
import requests
import json
from typing import Dict, List, Any, Optional, Union
import torch
import logging
from pathlib import Path
import threading
import time

logger = logging.getLogger(__name__)

class LLMCognitiveIntegration:
    """
    Integration between LLMs and OpenCog cognitive systems
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or self._default_config()
        self.llm_services = {}
        self.cognitive_context = {}
        self.conversation_history = []
        
        # Initialize available LLM services
        self._init_llm_services()
    
    def _default_config(self) -> Dict[str, Any]:
        """Default configuration for LLM integration"""
        return {
            'llama_cpp': {
                'executable': '3p/llama.cpp/main',
                'model_path': 'models/llama-7b.gguf',
                'context_size': 2048,
                'threads': 4
            },
            'koboldcpp': {
                'executable': '3p/koboldcpp/koboldcpp.py',
                'model_path': 'models/llama-7b.gguf',
                'port': 5001,
                'host': '0.0.0.0'
            },
            'cognitive': {
                'enable_reasoning': True,
                'enable_memory': True,
                'context_window': 10
            }
        }
    
    def _init_llm_services(self):
        """Initialize available LLM services"""
        # Check for llama.cpp
        llama_path = Path(self.config['llama_cpp']['executable'])
        if llama_path.exists():
            self.llm_services['llama_cpp'] = {
                'available': True,
                'type': 'local_executable'
            }
            logger.info("llama.cpp service available")
        
        # Check for KoboldCpp
        kobold_path = Path(self.config['koboldcpp']['executable'])
        if kobold_path.exists():
            self.llm_services['koboldcpp'] = {
                'available': True,
                'type': 'server',
                'status': 'stopped'
            }
            logger.info("KoboldCpp service available")
    
    def start_koboldcpp_server(self) -> bool:
        """Start KoboldCpp server in background"""
        if 'koboldcpp' not in self.llm_services:
            logger.error("KoboldCpp not available")
            return False
        
        try:
            cmd = [
                'python',
                self.config['koboldcpp']['executable'],
                '--model', self.config['koboldcpp']['model_path'],
                '--port', str(self.config['koboldcpp']['port']),
                '--host', self.config['koboldcpp']['host'],
                '--quiet'
            ]
            
            # Start server process
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Store process reference
            self.llm_services['koboldcpp']['process'] = process
            self.llm_services['koboldcpp']['status'] = 'starting'
            
            # Wait for server to start
            time.sleep(5)
            
            # Test connection
            if self._test_koboldcpp_connection():
                self.llm_services['koboldcpp']['status'] = 'running'
                logger.info("KoboldCpp server started successfully")
                return True
            else:
                self.llm_services['koboldcpp']['status'] = 'failed'
                logger.error("KoboldCpp server failed to start properly")
                return False
                
        except Exception as e:
            logger.error(f"Failed to start KoboldCpp server: {e}")
            return False
    
    def _test_koboldcpp_connection(self) -> bool:
        """Test connection to KoboldCpp server"""
        try:
            url = f"http://{self.config['koboldcpp']['host']}:{self.config['koboldcpp']['port']}/api/v1/model"
            response = requests.get(url, timeout=10)
            return response.status_code == 200
        except:
            return False
    
    def stop_koboldcpp_server(self):
        """Stop KoboldCpp server"""
        if 'koboldcpp' in self.llm_services and 'process' in self.llm_services['koboldcpp']:
            try:
                process = self.llm_services['koboldcpp']['process']
                process.terminate()
                process.wait(timeout=10)
                self.llm_services['koboldcpp']['status'] = 'stopped'
                logger.info("KoboldCpp server stopped")
            except Exception as e:
                logger.error(f"Error stopping KoboldCpp server: {e}")
    
    def cognitive_chat(self, 
                      message: str, 
                      integration: 'OpenCogAIMLIntegration',
                      service: str = 'koboldcpp') -> Dict[str, Any]:
        """
        Chat with LLM enhanced by cognitive processing
        
        Args:
            message: User message
            integration: OpenCog AI/ML integration instance
            service: LLM service to use
            
        Returns:
            Enhanced response with cognitive analysis
        """
        try:
            # Process message through cognitive system
            cognitive_results = integration.process_input(message)
            
            # Enhance prompt with cognitive context
            enhanced_prompt = self._create_cognitive_prompt(
                message, 
                cognitive_results,
                integration
            )
            
            # Generate LLM response
            llm_response = self._generate_llm_response(enhanced_prompt, service)
            
            # Process LLM response through cognitive system
            response_analysis = integration.process_input(llm_response)
            
            # Learn from interaction
            integration.learn_from_interaction(
                {'user_message': message, 'llm_response': llm_response},
                feedback=0.8  # Positive feedback for successful interaction
            )
            
            # Store conversation
            conversation_entry = {
                'user_message': message,
                'cognitive_processing': cognitive_results,
                'enhanced_prompt': enhanced_prompt,
                'llm_response': llm_response,
                'response_analysis': response_analysis
            }
            self.conversation_history.append(conversation_entry)
            
            return {
                'response': llm_response,
                'cognitive_analysis': response_analysis,
                'conversation_id': len(self.conversation_history) - 1
            }
            
        except Exception as e:
            logger.error(f"Cognitive chat failed: {e}")
            return {'error': str(e)}
    
    def _create_cognitive_prompt(self, 
                               message: str, 
                               cognitive_results: Dict[str, Any],
                               integration: 'OpenCogAIMLIntegration') -> str:
        """Create enhanced prompt with cognitive context"""
        
        # Get cognitive state
        cognitive_state = integration.get_cognitive_state()
        
        # Get relevant memories
        working_memory = integration.memory_systems['working']
        relevant_memories, _ = working_memory.retrieve(
            working_memory.memories[0] if working_memory.memories else torch.randn(512),
            k=3
        )
        
        # Build enhanced prompt
        prompt_parts = [
            "You are an AI assistant integrated with cognitive processing systems.",
            f"Current cognitive state: {cognitive_state.get('neural_state', {})}",
            f"Relevant memories: {len(relevant_memories)} items retrieved",
        ]
        
        # Add symbolic context if available
        if cognitive_results.get('symbolic_output'):
            symbolic_info = cognitive_results['symbolic_output']
            prompt_parts.append(f"Symbolic concepts identified: {symbolic_info.get('concepts', [])}")
        
        # Add conversation context
        if self.conversation_history:
            recent_context = self.conversation_history[-self.config['cognitive']['context_window']:]
            prompt_parts.append("Recent conversation context:")
            for entry in recent_context[-3:]:  # Last 3 exchanges
                prompt_parts.append(f"User: {entry['user_message']}")
                prompt_parts.append(f"Assistant: {entry['llm_response']}")
        
        prompt_parts.extend([
            "",
            f"User message: {message}",
            "",
            "Please provide a thoughtful response considering the cognitive context above:"
        ])
        
        return "\n".join(prompt_parts)
    
    def _generate_llm_response(self, prompt: str, service: str) -> str:
        """Generate response using specified LLM service"""
        if service == 'koboldcpp':
            return self._koboldcpp_generate(prompt)
        elif service == 'llama_cpp':
            return self._llama_cpp_generate(prompt)
        else:
            raise ValueError(f"Unknown LLM service: {service}")
    
    def _koboldcpp_generate(self, prompt: str) -> str:
        """Generate text using KoboldCpp API"""
        if self.llm_services.get('koboldcpp', {}).get('status') != 'running':
            if not self.start_koboldcpp_server():
                return "KoboldCpp server is not available"
        
        try:
            url = f"http://{self.config['koboldcpp']['host']}:{self.config['koboldcpp']['port']}/api/v1/generate"
            
            payload = {
                "prompt": prompt,
                "max_length": 200,
                "temperature": 0.7,
                "top_p": 0.9,
                "top_k": 40,
                "rep_pen": 1.1
            }
            
            response = requests.post(url, json=payload, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                return result.get('results', [{}])[0].get('text', '').strip()
            else:
                return f"KoboldCpp API error: {response.status_code}"
                
        except Exception as e:
            logger.error(f"KoboldCpp generation failed: {e}")
            return f"Generation failed: {str(e)}"
    
    def _llama_cpp_generate(self, prompt: str) -> str:
        """Generate text using llama.cpp executable"""
        try:
            cmd = [
                self.config['llama_cpp']['executable'],
                '--model', self.config['llama_cpp']['model_path'],
                '--prompt', prompt,
                '--n-predict', '200',
                '--temp', '0.7',
                '--threads', str(self.config['llama_cpp']['threads']),
                '--ctx-size', str(self.config['llama_cpp']['context_size'])
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            
            if result.returncode == 0:
                # Extract generated text (after the prompt)
                output = result.stdout
                if prompt in output:
                    generated = output.split(prompt, 1)[1].strip()
                    return generated
                return output.strip()
            else:
                return f"llama.cpp error: {result.stderr}"
                
        except Exception as e:
            logger.error(f"llama.cpp generation failed: {e}")
            return f"Generation failed: {str(e)}"
    
    def analyze_conversation_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in conversation history"""
        if not self.conversation_history:
            return {'message': 'No conversation history available'}
        
        analysis = {
            'total_conversations': len(self.conversation_history),
            'avg_message_length': 0,
            'avg_response_length': 0,
            'common_topics': [],
            'cognitive_insights': {}
        }
        
        # Calculate averages
        total_msg_len = sum(len(entry['user_message']) for entry in self.conversation_history)
        total_resp_len = sum(len(entry['llm_response']) for entry in self.conversation_history)
        
        analysis['avg_message_length'] = total_msg_len / len(self.conversation_history)
        analysis['avg_response_length'] = total_resp_len / len(self.conversation_history)
        
        # Extract common words/topics (simplified)
        all_messages = ' '.join([entry['user_message'] for entry in self.conversation_history])
        words = all_messages.lower().split()
        word_freq = {}
        for word in words:
            if len(word) > 3:  # Skip short words
                word_freq[word] = word_freq.get(word, 0) + 1
        
        # Get top 10 most common words
        analysis['common_topics'] = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        return analysis
    
    def export_conversation_for_training(self, filepath: str):
        """Export conversation history for model training"""
        training_data = []
        
        for entry in self.conversation_history:
            training_data.append({
                'input': entry['user_message'],
                'output': entry['llm_response'],
                'cognitive_features': entry.get('cognitive_processing', {}),
                'quality_score': 1.0  # Placeholder for quality assessment
            })
        
        with open(filepath, 'w') as f:
            json.dump(training_data, f, indent=2)
        
        logger.info(f"Exported {len(training_data)} conversation entries to {filepath}")

class CognitivePromptEnhancer:
    """
    Enhances prompts with cognitive context and reasoning
    """
    
    def __init__(self, integration: 'OpenCogAIMLIntegration'):
        self.integration = integration
    
    def enhance_prompt(self, 
                      base_prompt: str, 
                      enhancement_type: str = 'reasoning') -> str:
        """
        Enhance prompt with cognitive capabilities
        
        Args:
            base_prompt: Original prompt
            enhancement_type: Type of enhancement (reasoning, memory, attention)
            
        Returns:
            Enhanced prompt
        """
        if enhancement_type == 'reasoning':
            return self._add_reasoning_context(base_prompt)
        elif enhancement_type == 'memory':
            return self._add_memory_context(base_prompt)
        elif enhancement_type == 'attention':
            return self._add_attention_context(base_prompt)
        else:
            return base_prompt
    
    def _add_reasoning_context(self, prompt: str) -> str:
        """Add reasoning capabilities to prompt"""
        reasoning_context = """
You have access to advanced reasoning capabilities:
1. Deductive reasoning: Draw logical conclusions from premises
2. Inductive reasoning: Identify patterns and make generalizations
3. Analogical reasoning: Find similarities between different domains
4. Causal reasoning: Understand cause-and-effect relationships

When responding, explicitly show your reasoning process.
"""
        return reasoning_context + "\n" + prompt
    
    def _add_memory_context(self, prompt: str) -> str:
        """Add memory context to prompt"""
        # Get relevant memories
        working_memory = self.integration.memory_systems['working']
        episodic_memory = self.integration.memory_systems['episodic']
        
        memory_context = f"""
You have access to memory systems:
- Working memory: {len(working_memory.memories)} active items
- Episodic memory: {len(episodic_memory.episodes)} stored episodes

Consider relevant past experiences when responding.
"""
        return memory_context + "\n" + prompt
    
    def _add_attention_context(self, prompt: str) -> str:
        """Add attention mechanism context"""
        attention_context = """
Use focused attention to:
1. Identify the most important parts of the input
2. Maintain focus on relevant information
3. Filter out irrelevant details

Explain what you're focusing on and why.
"""
        return attention_context + "\n" + prompt

def create_llm_integration(config: Dict[str, Any] = None) -> LLMCognitiveIntegration:
    """Create LLM cognitive integration instance"""
    return LLMCognitiveIntegration(config)
