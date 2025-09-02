
#!/usr/bin/env python3

import sys
import time
from typing import Dict, List, Optional
from ..core.atomspace_psystem import AtomSpacePSystem
from ..core.atom_membrane import AtomMembrane, NodeAtomMembrane, LinkAtomMembrane

class AtomSpaceSimulator:
    """
    Simulator for AtomSpace P-Systems that demonstrates cognitive processes
    through membrane computing with atoms as membranes.
    """
    
    def __init__(self):
        self.psystem = AtomSpacePSystem()
        self.simulation_log = []
        self.step_delay = 0.1  # seconds between steps
        
    def create_demo_knowledge_base(self):
        """Create a demonstration knowledge base."""
        print("Creating demo knowledge base...")
        
        # Create concept nodes
        dog_id = self.psystem.create_node_atom("ConceptNode", "dog", 0.8, 0.9)
        animal_id = self.psystem.create_node_atom("ConceptNode", "animal", 0.9, 0.85)
        mammal_id = self.psystem.create_node_atom("ConceptNode", "mammal", 0.9, 0.8)
        furry_id = self.psystem.create_node_atom("ConceptNode", "furry", 0.7, 0.75)
        
        # Create inheritance relationships
        inh1_id = self.psystem.create_link_atom("InheritanceLink", [dog_id, animal_id], 0.9, 0.8)
        inh2_id = self.psystem.create_link_atom("InheritanceLink", [dog_id, mammal_id], 0.85, 0.8)
        inh3_id = self.psystem.create_link_atom("InheritanceLink", [mammal_id, animal_id], 0.95, 0.9)
        
        # Create similarity relationships
        sim1_id = self.psystem.create_link_atom("SimilarityLink", [dog_id, furry_id], 0.6, 0.7)
        
        # Create implication for inference
        impl_id = self.psystem.create_link_atom("ImplicationLink", [furry_id, mammal_id], 0.7, 0.6)
        
        print(f"Created {len(self.psystem.atom_membranes)} atoms in knowledge base")
        return [dog_id, animal_id, mammal_id, furry_id]
    
    def demonstrate_attention_dynamics(self, focus_atoms: List[int]):
        """Demonstrate attention spreading and focus."""
        print("\n=== Attention Dynamics Demo ===")
        
        # Set initial attention focus
        self.psystem.set_attention_focus(focus_atoms, 200)
        print(f"Set attention focus on atoms: {focus_atoms}")
        
        # Show initial attention state
        self.print_attention_state()
        
        # Spread activation
        if focus_atoms:
            print(f"\nSpreading activation from atom {focus_atoms[0]}...")
            self.psystem.spread_activation(focus_atoms[0], 100, 3)
            
        # Show updated attention state
        print("\nAfter activation spreading:")
        self.print_attention_state()
    
    def demonstrate_inference(self):
        """Demonstrate inference through membrane evolution."""
        print("\n=== Inference Demo ===")
        
        # Create inference rules
        self.psystem.create_inference_rules()
        print(f"Created {len(self.psystem.rules)} inference rules")
        
        # Run inference steps
        for step in range(10):
            print(f"\nInference step {step + 1}:")
            
            # Show state before step
            state = self.psystem.get_atomspace_state()
            print(f"  Focus atoms: {len(state['attention_focus'])}")
            print(f"  Average STI: {state['average_sti']:.1f}")
            
            # Execute step
            active = self.psystem.step()
            
            if not active:
                print("  No more active inference")
                break
                
            # Show inference trails
            if self.psystem.inference_trails:
                recent_trail = self.psystem.inference_trails[-1]
                print(f"  Applied rule: {recent_trail[2]} on atom {recent_trail[0]}")
            
            time.sleep(self.step_delay)
    
    def demonstrate_forgetting(self):
        """Demonstrate memory decay and forgetting."""
        print("\n=== Forgetting Demo ===")
        
        initial_count = len(self.psystem.atom_membranes)
        print(f"Initial atom count: {initial_count}")
        
        # Show atoms before forgetting
        self.print_atom_summary()
        
        # Apply aggressive forgetting
        print("\nApplying forgetting (decay rate 0.2)...")
        self.psystem.apply_forgetting(0.2)
        
        final_count = len(self.psystem.atom_membranes)
        print(f"Final atom count: {final_count}")
        print(f"Atoms forgotten: {initial_count - final_count}")
        
        # Show remaining atoms
        if final_count > 0:
            print("\nRemaining atoms:")
            self.print_atom_summary()
    
    def print_attention_state(self):
        """Print current attention state of all atoms."""
        print("\nAttention State:")
        print("ID  | Type           | Name    | STI  | Truth (S,C)")
        print("-" * 50)
        
        for atom_id, membrane in sorted(self.psystem.atom_membranes.items()):
            sti = membrane.attention_value["sti"]
            strength = membrane.truth_value["strength"]
            confidence = membrane.truth_value["confidence"]
            name = getattr(membrane, 'atom_name', 'Link')[:8]
            
            print(f"{atom_id:3d} | {membrane.atom_type:14s} | {name:7s} | {sti:4d} | ({strength:.2f},{confidence:.2f})")
    
    def print_atom_summary(self):
        """Print summary of atoms by type."""
        state = self.psystem.get_atomspace_state()
        
        print("\nAtom Type Summary:")
        for atom_type, count in state['type_counts'].items():
            print(f"  {atom_type}: {count}")
    
    def run_full_demo(self):
        """Run complete demonstration of AtomSpace P-System."""
        print("AtomSpace P-System Demonstration")
        print("=" * 50)
        
        # Create knowledge base
        focus_atoms = self.create_demo_knowledge_base()
        
        # Demonstrate attention dynamics
        self.demonstrate_attention_dynamics(focus_atoms[:2])
        
        # Demonstrate inference
        self.demonstrate_inference()
        
        # Demonstrate forgetting
        self.demonstrate_forgetting()
        
        # Final state
        print("\n=== Final State ===")
        final_state = self.psystem.get_atomspace_state()
        print(f"Total simulation steps: {final_state['step_count']}")
        print(f"Total inference trails: {final_state['inference_trails']}")
        print(f"Remaining atoms: {final_state['total_atoms']}")
        
        # Export to Atomese
        print("\n=== Atomese Export ===")
        atomese = self.psystem.to_atomese()
        if atomese:
            print("Final AtomSpace in Atomese format:")
            print(atomese[:500] + "..." if len(atomese) > 500 else atomese)
    
    def interactive_mode(self):
        """Run interactive simulation mode."""
        print("AtomSpace P-System Interactive Mode")
        print("Commands: step, focus <atom_id>, spread <atom_id>, state, forget, quit")
        
        while True:
            try:
                cmd = input("\n> ").strip().split()
                if not cmd:
                    continue
                    
                if cmd[0] == "quit":
                    break
                elif cmd[0] == "step":
                    active = self.psystem.step()
                    print(f"Step executed. Active: {active}")
                elif cmd[0] == "focus" and len(cmd) > 1:
                    atom_id = int(cmd[1])
                    self.psystem.set_attention_focus([atom_id], 200)
                    print(f"Set focus on atom {atom_id}")
                elif cmd[0] == "spread" and len(cmd) > 1:
                    atom_id = int(cmd[1])
                    self.psystem.spread_activation(atom_id, 100)
                    print(f"Spread activation from atom {atom_id}")
                elif cmd[0] == "state":
                    self.print_attention_state()
                elif cmd[0] == "forget":
                    self.psystem.apply_forgetting()
                    print("Applied forgetting")
                else:
                    print("Unknown command")
                    
            except (ValueError, IndexError, KeyboardInterrupt):
                print("Invalid command or interrupted")
                break

def main():
    """Main entry point for the simulator."""
    simulator = AtomSpaceSimulator()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        # Create basic knowledge base first
        simulator.create_demo_knowledge_base()
        simulator.interactive_mode()
    else:
        # Run full demonstration
        simulator.run_full_demo()

if __name__ == "__main__":
    main()
