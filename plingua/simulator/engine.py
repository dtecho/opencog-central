
"""
Simulation engine for P-systems.
"""

from typing import List, Optional, Dict, Any, Callable
from dataclasses import dataclass
import time
from ..core.psystem import PSystem
from ..core.configuration import Configuration
from .trace import ExecutionTrace, TraceStep
from .statistics import SimulationStatistics


@dataclass
class SimulationResult:
    """Result of a P-system simulation."""
    success: bool
    steps: int
    final_configuration: Optional[Configuration]
    execution_time: float
    halting: bool
    trace: Optional[ExecutionTrace]
    statistics: Optional[SimulationStatistics]
    error_message: Optional[str] = None


class SimulationEngine:
    """
    Main simulation engine for P-systems.
    
    Supports various simulation modes and provides detailed execution traces.
    """
    
    def __init__(self, psystem: PSystem):
        self.psystem = psystem
        self.max_steps = 1000
        self.trace_enabled = True
        self.statistics_enabled = True
        self.step_callback: Optional[Callable[[Configuration], None]] = None
    
    def simulate(self, 
                 max_steps: Optional[int] = None,
                 trace: bool = True,
                 statistics: bool = True) -> SimulationResult:
        """
        Run a complete simulation of the P-system.
        
        Args:
            max_steps: Maximum number of steps (default: self.max_steps)
            trace: Whether to generate execution trace
            statistics: Whether to collect statistics
            
        Returns:
            SimulationResult with execution details
        """
        start_time = time.time()
        max_steps = max_steps or self.max_steps
        
        # Reset P-system to initial state
        self.psystem.reset()
        
        # Initialize trace and statistics
        execution_trace = ExecutionTrace() if trace else None
        stats = SimulationStatistics() if statistics else None
        
        try:
            config = self.psystem.get_configuration()
            
            if execution_trace:
                # Record initial configuration
                step = TraceStep(
                    step_number=0,
                    configuration=config.copy(),
                    applied_rules=[],
                    execution_time=0.0
                )
                execution_trace.add_step(step)
            
            # Main simulation loop
            for step_num in range(1, max_steps + 1):
                step_start = time.time()
                
                # Check if system has halted
                if self.psystem.is_halting():
                    break
                
                # Execute one step
                success = self.psystem.step()
                step_time = time.time() - step_start
                
                if not success:
                    break
                
                # Update configuration
                config = self.psystem.get_configuration()
                config.step_number = step_num
                
                # Record trace step
                if execution_trace:
                    step = TraceStep(
                        step_number=step_num,
                        configuration=config.copy(),
                        applied_rules=[],  # Would need to track applied rules
                        execution_time=step_time
                    )
                    execution_trace.add_step(step)
                
                # Update statistics
                if stats:
                    stats.record_step(config, step_time)
                
                # Call step callback if provided
                if self.step_callback:
                    self.step_callback(config)
            
            execution_time = time.time() - start_time
            
            return SimulationResult(
                success=True,
                steps=config.step_number,
                final_configuration=config,
                execution_time=execution_time,
                halting=self.psystem.is_halting(),
                trace=execution_trace,
                statistics=stats
            )
            
        except Exception as e:
            execution_time = time.time() - start_time
            return SimulationResult(
                success=False,
                steps=0,
                final_configuration=None,
                execution_time=execution_time,
                halting=False,
                trace=execution_trace,
                statistics=stats,
                error_message=str(e)
            )
    
    def step_by_step(self) -> bool:
        """Execute a single simulation step."""
        if self.psystem.is_halting():
            return False
        return self.psystem.step()
    
    def run_until_halt(self, max_steps: Optional[int] = None) -> int:
        """Run simulation until halting or max steps reached."""
        max_steps = max_steps or self.max_steps
        steps = 0
        
        while steps < max_steps and not self.psystem.is_halting():
            if not self.psystem.step():
                break
            steps += 1
        
        return steps
    
    def get_current_configuration(self) -> Configuration:
        """Get the current configuration."""
        return self.psystem.get_configuration()
    
    def reset(self):
        """Reset the P-system to initial state."""
        self.psystem.reset()
    
    def set_step_callback(self, callback: Callable[[Configuration], None]):
        """Set a callback function to be called after each step."""
        self.step_callback = callback
