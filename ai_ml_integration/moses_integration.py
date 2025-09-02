
"""
MOSES Integration for Evolutionary Program Learning
Connects MOSES with neural networks and cognitive systems
"""

import subprocess
import tempfile
import json
from typing import Dict, List, Any, Optional
import torch
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class MOSESIntegration:
    """
    Integration layer for MOSES evolutionary program learning
    """
    
    def __init__(self, moses_path: str = "asmoses/build/moses/main/moses"):
        self.moses_path = moses_path
        self.programs = {}
        self.evolution_history = []
    
    def evolve_neural_program(self, 
                            training_data: torch.Tensor, 
                            target_data: torch.Tensor,
                            generations: int = 100,
                            population_size: int = 500) -> Dict[str, Any]:
        """
        Evolve a program using MOSES that mimics neural network behavior
        
        Args:
            training_data: Input training data
            target_data: Target outputs
            generations: Number of evolution generations
            population_size: Size of population
            
        Returns:
            Best evolved program and metadata
        """
        try:
            # Convert neural data to MOSES format
            moses_data = self._neural_to_moses_format(training_data, target_data)
            
            # Write temporary data file
            with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
                moses_data_file = f.name
                f.write(moses_data)
            
            # Run MOSES evolution
            result = self._run_moses_evolution(
                moses_data_file, 
                generations, 
                population_size
            )
            
            # Parse results
            evolved_program = self._parse_moses_output(result)
            
            # Store program
            program_id = f"neural_program_{len(self.programs)}"
            self.programs[program_id] = evolved_program
            
            # Record evolution history
            evolution_record = {
                'program_id': program_id,
                'generations': generations,
                'population_size': population_size,
                'fitness': evolved_program.get('fitness', 0.0),
                'complexity': evolved_program.get('complexity', 0)
            }
            self.evolution_history.append(evolution_record)
            
            # Clean up
            Path(moses_data_file).unlink()
            
            return {
                'program_id': program_id,
                'program': evolved_program,
                'evolution_record': evolution_record
            }
            
        except Exception as e:
            logger.error(f"MOSES evolution failed: {e}")
            return {'error': str(e)}
    
    def _neural_to_moses_format(self, inputs: torch.Tensor, targets: torch.Tensor) -> str:
        """Convert neural tensors to MOSES CSV format"""
        lines = []
        
        # Header
        input_dim = inputs.shape[-1]
        output_dim = targets.shape[-1] if len(targets.shape) > 1 else 1
        
        header = []
        for i in range(input_dim):
            header.append(f"input_{i}")
        if output_dim == 1:
            header.append("target")
        else:
            for i in range(output_dim):
                header.append(f"target_{i}")
        
        lines.append(",".join(header))
        
        # Data rows
        inputs_flat = inputs.view(-1, input_dim)
        targets_flat = targets.view(-1, output_dim) if output_dim > 1 else targets.view(-1, 1)
        
        for i in range(min(inputs_flat.shape[0], 1000)):  # Limit data size
            row = []
            
            # Input features
            for j in range(input_dim):
                row.append(str(float(inputs_flat[i, j])))
            
            # Target values
            for j in range(output_dim):
                row.append(str(float(targets_flat[i, j])))
            
            lines.append(",".join(row))
        
        return "\n".join(lines)
    
    def _run_moses_evolution(self, 
                           data_file: str, 
                           generations: int, 
                           population_size: int) -> str:
        """Run MOSES evolution process"""
        cmd = [
            self.moses_path,
            "--input-file", data_file,
            "--target-feature", "target",
            "--max-evals", str(generations * population_size),
            "--result-count", "10",
            "--output-format", "combo",
            "--log-level", "INFO"
        ]
        
        try:
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True, 
                timeout=300  # 5 minute timeout
            )
            
            if result.returncode != 0:
                raise RuntimeError(f"MOSES failed: {result.stderr}")
            
            return result.stdout
            
        except subprocess.TimeoutExpired:
            raise RuntimeError("MOSES evolution timed out")
        except FileNotFoundError:
            raise RuntimeError(f"MOSES executable not found at: {self.moses_path}")
    
    def _parse_moses_output(self, moses_output: str) -> Dict[str, Any]:
        """Parse MOSES output to extract best program"""
        lines = moses_output.strip().split('\n')
        
        if not lines:
            return {'error': 'No output from MOSES'}
        
        # Find best program (first line is usually the best)
        best_line = None
        for line in lines:
            if line.strip() and not line.startswith('#'):
                best_line = line
                break
        
        if not best_line:
            return {'error': 'No valid program found'}
        
        # Parse program line
        parts = best_line.split('\t') if '\t' in best_line else best_line.split()
        
        if len(parts) >= 2:
            fitness = float(parts[0]) if parts[0].replace('-', '').replace('.', '').isdigit() else 0.0
            program = parts[1] if len(parts) > 1 else parts[0]
        else:
            fitness = 0.0
            program = best_line
        
        return {
            'program': program,
            'fitness': fitness,
            'complexity': len(program.split()),
            'raw_output': moses_output
        }
    
    def evaluate_program(self, program_id: str, test_data: torch.Tensor) -> Dict[str, Any]:
        """
        Evaluate an evolved program on test data
        """
        if program_id not in self.programs:
            return {'error': f'Program {program_id} not found'}
        
        program = self.programs[program_id]
        
        try:
            # Convert test data to evaluable format
            # This is a simplified evaluation - in practice, would need
            # proper combo program interpreter
            
            predictions = self._evaluate_combo_program(
                program['program'], 
                test_data
            )
            
            return {
                'program_id': program_id,
                'predictions': predictions,
                'test_samples': test_data.shape[0]
            }
            
        except Exception as e:
            logger.error(f"Program evaluation failed: {e}")
            return {'error': str(e)}
    
    def _evaluate_combo_program(self, program: str, inputs: torch.Tensor) -> torch.Tensor:
        """
        Evaluate a combo program (simplified implementation)
        In practice, this would use proper combo interpreter
        """
        # Mock evaluation - replace with actual combo interpreter
        batch_size = inputs.shape[0]
        return torch.randn(batch_size, 1)  # Random predictions for now
    
    def get_best_programs(self, top_k: int = 5) -> List[Dict[str, Any]]:
        """Get the top-k best evolved programs"""
        programs_with_fitness = []
        
        for prog_id, program in self.programs.items():
            programs_with_fitness.append({
                'id': prog_id,
                'fitness': program.get('fitness', 0.0),
                'program': program
            })
        
        # Sort by fitness (higher is better)
        programs_with_fitness.sort(key=lambda x: x['fitness'], reverse=True)
        
        return programs_with_fitness[:top_k]
    
    def export_program_to_neural(self, program_id: str) -> Optional[torch.nn.Module]:
        """
        Convert evolved program to neural network (experimental)
        """
        if program_id not in self.programs:
            logger.error(f"Program {program_id} not found")
            return None
        
        program = self.programs[program_id]
        
        try:
            # This is a placeholder for program-to-neural conversion
            # In practice, would analyze combo program structure
            # and create equivalent neural architecture
            
            class EvolvedNeuralNet(torch.nn.Module):
                def __init__(self, program_str: str):
                    super().__init__()
                    self.program_str = program_str
                    # Simplified: create basic linear layers
                    self.layers = torch.nn.Sequential(
                        torch.nn.Linear(10, 20),
                        torch.nn.ReLU(),
                        torch.nn.Linear(20, 1)
                    )
                
                def forward(self, x):
                    return self.layers(x)
            
            neural_net = EvolvedNeuralNet(program['program'])
            logger.info(f"Converted program {program_id} to neural network")
            return neural_net
            
        except Exception as e:
            logger.error(f"Program to neural conversion failed: {e}")
            return None

def create_moses_integration(moses_path: str = None) -> MOSESIntegration:
    """Create MOSES integration instance"""
    if moses_path is None:
        # Try to find MOSES in standard locations
        possible_paths = [
            "asmoses/build/moses/main/moses",
            "moses/build/moses/main/moses",
            "moses"
        ]
        
        for path in possible_paths:
            if Path(path).exists() or subprocess.run(['which', path], capture_output=True).returncode == 0:
                moses_path = path
                break
        
        if moses_path is None:
            logger.warning("MOSES executable not found, some features may not work")
            moses_path = "moses"  # Fallback
    
    return MOSESIntegration(moses_path)
