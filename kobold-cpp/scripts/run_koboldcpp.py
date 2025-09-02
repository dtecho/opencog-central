
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
    
    def test_cognitive_features(self, port=5001):
        """Test cognitive enhancement features"""
        try:
            payload = {
                "test_type": "cognitive_features",
                "include_memory": True,
                "include_attention": True,
                "include_reasoning": True
            }
            
            response = requests.post(
                f"http://localhost:{port}/api/v1/test/cognitive",
                json=payload,
                timeout=10
            )
            
            if response.status_code == 200:
                return response.json().get("result", "Cognitive test completed")
            else:
                return f"Cognitive test failed: {response.status_code}"
        except Exception as e:
            return f"Cognitive test error: {e}"
    
    def test_atomspace_integration(self, port=5001):
        """Test AtomSpace integration"""
        try:
            # Test knowledge injection
            test_knowledge = "Artificial intelligence exhibits emergent behavior through complex interactions."
            
            inject_payload = {"knowledge_text": test_knowledge}
            inject_response = requests.post(
                f"http://localhost:{port}/api/v1/atomspace/inject",
                json=inject_payload,
                timeout=10
            )
            
            if inject_response.status_code != 200:
                return f"Knowledge injection failed: {inject_response.status_code}"
            
            # Test query
            query_payload = {"query": "emergent behavior"}
            query_response = requests.post(
                f"http://localhost:{port}/api/v1/atomspace/query",
                json=query_payload,
                timeout=10
            )
            
            if query_response.status_code == 200:
                result = query_response.json()
                return f"AtomSpace integration working: {result.get('result', 'No result')[:50]}..."
            else:
                return f"AtomSpace query failed: {query_response.status_code}"
                
        except Exception as e:
            return f"AtomSpace test error: {e}"
    
    def test_pln_reasoning(self, port=5001):
        """Test PLN reasoning capabilities"""
        try:
            payload = {
                "premises": "Intelligence involves information processing. Consciousness involves awareness.",
                "target": "Intelligent systems can potentially develop awareness",
                "reasoning_depth": 3
            }
            
            response = requests.post(
                f"http://localhost:{port}/api/v1/pln/reason",
                json=payload,
                timeout=15
            )
            
            if response.status_code == 200:
                result = response.json()
                truth_value = result.get("truth_value", 0.0)
                reasoning = result.get("reasoning_chain", "No reasoning provided")
                return f"PLN reasoning successful: TV={truth_value:.3f}, Chain={reasoning[:50]}..."
            else:
                return f"PLN reasoning failed: {response.status_code}"
                
        except Exception as e:
            return f"PLN test error: {e}"
    
    def run_koboldcpp(self, model_path, port=5001, context_size=2048, gpu_layers=0, **kwargs):
        """Run KoboldCpp with cognitive enhancements"""
        
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
        
        # Add cognitive enhancement flags
        if kwargs.get("cognitive"):
            cmd.append("--cognitive-mode")
            
        if kwargs.get("atomspace"):
            cmd.append("--enable-atomspace")
            
        if kwargs.get("pln"):
            cmd.append("--enable-pln")
            
        if kwargs.get("monitor"):
            cmd.append("--cognitive-monitor")
        
        print(f"🚀 Starting Enhanced KoboldCpp: {' '.join(cmd)}")
        
        try:
            process = subprocess.Popen(cmd, cwd=str(self.koboldcpp_dir))
            print(f"✅ KoboldCpp-OpenCog hybrid started on port {port}")
            print(f"🌐 Web interface: http://0.0.0.0:{port}")
            print(f"🧠 Cognitive API: http://0.0.0.0:{port}/api/v1/cognitive")
            return process
        except Exception as e:
            print(f"❌ Error starting KoboldCpp: {e}")
            return None

def main():
    parser = argparse.ArgumentParser(description="KoboldCpp OpenCog Cognitive Integration")
    parser.add_argument("--model", required=True, help="Path to GGUF model file")
    parser.add_argument("--port", type=int, default=5001, help="Server port")
    parser.add_argument("--context", type=int, default=2048, help="Context size")
    parser.add_argument("--gpu-layers", type=int, default=0, help="GPU layers")
    parser.add_argument("--usecuda", action="store_true", help="Use CUDA")
    parser.add_argument("--usevulkan", action="store_true", help="Use Vulkan")
    parser.add_argument("--test", action="store_true", help="Test mode")
    parser.add_argument("--cognitive", action="store_true", help="Enable cognitive features")
    parser.add_argument("--demo", action="store_true", help="Run cognitive demo")
    parser.add_argument("--monitor", action="store_true", help="Enable cognitive monitoring")
    parser.add_argument("--atomspace", action="store_true", help="Enable AtomSpace integration")
    parser.add_argument("--pln", action="store_true", help="Enable PLN reasoning")
    
    args = parser.parse_args()
    
    manager = KoboldCppManager()
    
    if args.demo:
        # Run cognitive integration demo
        print("🧠 Starting KoboldCpp-OpenCog Cognitive Demo...")
        import subprocess
        import sys
        
        demo_script = Path(__file__).parent / "cognitive_demo.py"
        if demo_script.exists():
            subprocess.run([sys.executable, str(demo_script), "--url", f"http://0.0.0.0:{args.port}"])
        else:
            print("❌ Cognitive demo script not found")
        return
    
    if args.test:
        print("🔬 Testing KoboldCpp-OpenCog Integration...")
        if manager.test_api(args.port):
            # Test basic generation
            result = manager.generate_text("Explain consciousness in AI systems.", args.port)
            print(f"Basic Generation: {result}")
            
            # Test cognitive features if enabled
            if args.cognitive:
                print("\n🧠 Testing Cognitive Features...")
                cognitive_result = manager.test_cognitive_features(args.port)
                print(f"Cognitive Test: {cognitive_result}")
            
            if args.atomspace:
                print("\n🌐 Testing AtomSpace Integration...")
                atomspace_result = manager.test_atomspace_integration(args.port)
                print(f"AtomSpace Test: {atomspace_result}")
                
            if args.pln:
                print("\n🔬 Testing PLN Reasoning...")
                pln_result = manager.test_pln_reasoning(args.port)
                print(f"PLN Test: {pln_result}")
    else:
        # Start the enhanced server
        print("🚀 Starting KoboldCpp-OpenCog Hybrid Server...")
        
        if args.cognitive:
            print("🧠 Cognitive enhancement enabled")
        if args.atomspace:
            print("🌐 AtomSpace integration enabled")
        if args.pln:
            print("🔬 PLN reasoning enabled")
        if args.monitor:
            print("📊 Cognitive monitoring enabled")
        
        process = manager.run_koboldcpp(
            args.model,
            port=args.port,
            context_size=args.context,
            gpu_layers=args.gpu_layers,
            usecuda=args.usecuda,
            usevulkan=args.usevulkan,
            cognitive=args.cognitive,
            atomspace=args.atomspace,
            pln=args.pln,
            monitor=args.monitor
        )
        
        if process:
            try:
                print(f"✅ Server running on http://0.0.0.0:{args.port}")
                print("🧠 Cognitive features active - Try the demo: python cognitive_demo.py")
                print("Press Ctrl+C to shutdown...")
                process.wait()
            except KeyboardInterrupt:
                print("\n🛑 Shutting down KoboldCpp-OpenCog hybrid server...")
                process.terminate()
                print("✅ Server shutdown complete")

if __name__ == "__main__":
    main()
