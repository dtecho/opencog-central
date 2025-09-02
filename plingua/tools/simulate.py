
#!/usr/bin/env python3
"""
P-Lingua Simulation Tool

Command-line interface for simulating P-systems.
"""

import argparse
import sys
import json
from pathlib import Path
from typing import Optional

from ..parser.parser import PLinguaParser
from ..simulator.engine import SimulationEngine
from ..serialization.json_format import JSONSerializer


def main():
    """Main entry point for the simulation tool."""
    parser = argparse.ArgumentParser(
        description="Simulate P-Lingua programs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python -m plingua.tools.simulate input.pli
  python -m plingua.tools.simulate input.pli --max-steps 100 --output result.json
  python -m plingua.tools.simulate input.pli --trace --verbose
        """
    )
    
    parser.add_argument(
        "input",
        help="Input P-Lingua file (.pli)"
    )
    
    parser.add_argument(
        "--max-steps", "-s",
        type=int,
        default=1000,
        help="Maximum number of simulation steps (default: 1000)"
    )
    
    parser.add_argument(
        "--output", "-o",
        help="Output file for simulation results (JSON format)"
    )
    
    parser.add_argument(
        "--trace", "-t",
        action="store_true",
        help="Generate execution trace"
    )
    
    parser.add_argument(
        "--statistics",
        action="store_true",
        help="Collect simulation statistics"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    
    parser.add_argument(
        "--format",
        choices=["json", "xml", "csv"],
        default="json",
        help="Output format (default: json)"
    )
    
    args = parser.parse_args()
    
    try:
        # Parse input file
        input_path = Path(args.input)
        if not input_path.exists():
            print(f"Error: Input file '{args.input}' not found", file=sys.stderr)
            sys.exit(1)
        
        if args.verbose:
            print(f"Parsing P-Lingua file: {args.input}")
        
        with open(input_path, 'r') as f:
            content = f.read()
        
        # Parse P-system
        plingua_parser = PLinguaParser()
        psystem = plingua_parser.parse(content)
        
        if args.verbose:
            print(f"P-system type: {psystem.system_type}")
            print(f"Number of rules: {len(psystem.rules)}")
            print(f"Alphabet size: {len(psystem.alphabet)}")
        
        # Run simulation
        if args.verbose:
            print(f"Running simulation (max {args.max_steps} steps)...")
        
        engine = SimulationEngine(psystem)
        result = engine.simulate(
            max_steps=args.max_steps,
            trace=args.trace,
            statistics=args.statistics
        )
        
        # Display results
        if result.success:
            print(f"Simulation completed successfully")
            print(f"Steps executed: {result.steps}")
            print(f"Execution time: {result.execution_time:.3f}s")
            print(f"Halting: {result.halting}")
            
            if result.final_configuration:
                output_content = result.final_configuration.get_output_membrane_content()
                if output_content:
                    print(f"Output: {output_content}")
        else:
            print(f"Simulation failed: {result.error_message}", file=sys.stderr)
            sys.exit(1)
        
        # Save results if output file specified
        if args.output:
            if args.verbose:
                print(f"Saving results to: {args.output}")
            
            serializer = JSONSerializer()
            output_data = serializer.serialize_simulation_result(result)
            
            with open(args.output, 'w') as f:
                json.dump(output_data, f, indent=2)
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
