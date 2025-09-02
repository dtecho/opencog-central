
#!/usr/bin/env python3
"""
SkinTwin-ASI: Comprehensive Skin Modeling System
Main entry point for the multiscale computational skin model
"""

import sys
import os
import logging
from pathlib import Path

# Add project paths
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root / "agi-bio"))
sys.path.insert(0, str(project_root / "cheminformatics"))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def main():
    """Main entry point for SkinTwin-ASI system"""
    logger = logging.getLogger(__name__)
    logger.info("Initializing SkinTwin-ASI Comprehensive Skin Modeling System")
    
    try:
        # Import core modules
        from skin_twin.core import SkinTwinCore
        from skin_twin.atomspace_integration import AtomSpaceManager
        from skin_twin.multiscale_model import MultiscaleModel
        
        # Initialize core system
        logger.info("Starting AtomSpace integration...")
        atomspace_manager = AtomSpaceManager()
        
        logger.info("Initializing multiscale skin model...")
        multiscale_model = MultiscaleModel(atomspace_manager)
        
        logger.info("Starting SkinTwin core system...")
        skin_twin = SkinTwinCore(atomspace_manager, multiscale_model)
        
        # Start the system
        skin_twin.start()
        
    except ImportError as e:
        logger.error(f"Missing dependencies: {e}")
        logger.info("Please ensure OpenCog AtomSpace and related components are installed")
        sys.exit(1)
    except Exception as e:
        logger.error(f"System initialization failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
