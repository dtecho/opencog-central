
#!/usr/bin/env python3
"""
HGQL Startup Script
Launch the HyperGraph Query Language interface system
"""

import sys
import os

# Add HGQL to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'hgql'))

from hgql.main import main

if __name__ == "__main__":
    print("Starting HGQL (HyperGraph Query Language) Interface System...")
    print("=" * 60)
    print("🧠 OpenCog Cognitive Synergy Engine")
    print("🔗 Hypergraph Query & Integration Hub")
    print("🚀 Advanced Reasoning Interface")
    print("=" * 60)
    
    main()
