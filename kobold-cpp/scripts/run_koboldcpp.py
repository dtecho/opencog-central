
#!/usr/bin/env python3
"""
KoboldCpp OpenCog Integration Script
"""

import os
import sys
import subprocess
import argparse
import requests
import json
from pathlib import Path

class KoboldCppManager:
    def __init__(self):
        self.base_dir = Path(__file__).parent.parent
        self.koboldcpp_dir = self.base_dir.parent / "3p" / "koboldcpp"
        
    def run_koboldcpp(self, model_path, port=5001, context_size=2048, gpu_layers=0, **kwargs):
        """Run KoboldCpp with specified parameters"""
        
        cmd = [
            "python", 
            str(self.koboldcpp_dir / "koboldcpp.py"),
            str(model_path),
            "--port", str(port),
            "--contextsize", str(context_size),
            "--hordeconfig", "main",
            "--smartcontext"
        ]
        
        if gpu_layers > 0:
            cmd.extend(["--gpulayers", str(gpu_layers)])
            
        if kwargs.get("usecuda"):
            cmd.append("--usecuda")
            
        if kwargs.get("usevulkan"):
            cmd.append("--usevulkan")
            
        print(f"Starting KoboldCpp: {' '.join(cmd)}")
        
        try:
            process = subprocess.Popen(cmd, cwd=str(self.koboldcpp_dir))
            print(f"KoboldCpp started on port {port}")
            print(f"Access the web interface at: http://0.0.0.0:{port}")
            return process
        except Exception as e:
            print(f"Error starting KoboldCpp: {e}")
            return None
    
    def test_api(self, port=5001):
        """Test the KoboldCpp API"""
        try:
            response = requests.get(f"http://localhost:{port}/api/v1/info")
            if response.status_code == 200:
                print("API is responding:", response.json())
                return True
        except Exception as e:
            print(f"API test failed: {e}")
        return False
    
    def generate_text(self, prompt, port=5001, max_length=100):
        """Generate text using the API"""
        try:
            payload = {
                "prompt": prompt,
                "max_length": max_length,
                "temperature": 0.7,
                "top_p": 0.9,
                "rep_pen": 1.1
            }
            
            response = requests.post(
                f"http://localhost:{port}/api/v1/generate",
                json=payload
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get("results", [{}])[0].get("text", "")
        except Exception as e:
            print(f"Generation failed: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="KoboldCpp OpenCog Integration")
    parser.add_argument("--model", required=True, help="Path to GGUF model file")
    parser.add_argument("--port", type=int, default=5001, help="Server port")
    parser.add_argument("--context", type=int, default=2048, help="Context size")
    parser.add_argument("--gpu-layers", type=int, default=0, help="GPU layers")
    parser.add_argument("--usecuda", action="store_true", help="Use CUDA")
    parser.add_argument("--usevulkan", action="store_true", help="Use Vulkan")
    parser.add_argument("--test", action="store_true", help="Test mode")
    
    args = parser.parse_args()
    
    manager = KoboldCppManager()
    
    if args.test:
        # Test with a simple prompt
        if manager.test_api(args.port):
            result = manager.generate_text("Hello, this is a test prompt.", args.port)
            print(f"Generated: {result}")
    else:
        # Start the server
        process = manager.run_koboldcpp(
            args.model,
            port=args.port,
            context_size=args.context,
            gpu_layers=args.gpu_layers,
            usecuda=args.usecuda,
            usevulkan=args.usevulkan
        )
        
        if process:
            try:
                process.wait()
            except KeyboardInterrupt:
                print("\nShutting down KoboldCpp...")
                process.terminate()

if __name__ == "__main__":
    main()
