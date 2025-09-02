
#!/usr/bin/env python3
"""
Simple runner script for LLM.txt generation
"""

import sys
import os
from pathlib import Path

def main():
    print("OpenCog LLM.txt Generator")
    print("=" * 40)
    
    # Check if ref directory exists
    ref_dir = Path("ref")
    if not ref_dir.exists():
        print("Creating ref/ directory...")
        ref_dir.mkdir()
        print("Please place your site folders in the ref/ directory and run again.")
        return
    
    # Count sites to process
    sites = [d for d in ref_dir.iterdir() if d.is_dir()]
    if not sites:
        print("No site folders found in ref/ directory.")
        print("Please add your site folders to ref/ and run again.")
        return
    
    print(f"Found {len(sites)} sites to process:")
    for site in sites:
        print(f"  - {site.name}")
    
    print("\nStarting generation...")
    
    # Import and run the generator
    try:
        from generate_llm_txt import LLMTxtGenerator
        generator = LLMTxtGenerator()
        generator.process_all_sites()
        generator.generate_master_index()
        
        print("\n" + "=" * 40)
        print("✓ Generation complete!")
        print(f"✓ llm.txt files created in each site folder")
        print(f"✓ AI-friendly markdown files created in llm/sites/")
        print(f"✓ Master index created at llm/index.md")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
