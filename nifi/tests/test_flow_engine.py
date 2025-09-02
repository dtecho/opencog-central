
"""
Tests for NiFi Flow Engine
"""

import pytest
import asyncio
from nifi.core.flow_engine import FlowEngine
from nifi.core.processor import FlowFile

class TestFlowEngine:
    
    def setup_method(self):
        """Setup test environment"""
        self.engine = FlowEngine()
        
    def test_create_flow(self):
        """Test flow creation"""
        flow_id = self.engine.create_flow("Test Flow", "A test flow")
        assert flow_id in self.engine.flows
        assert self.engine.flows[flow_id].name == "Test Flow"
        
    def test_add_processor(self):
        """Test adding processor to flow"""
        flow_id = self.engine.create_flow("Test Flow")
        processor_id = self.engine.add_processor(flow_id, "GenerateFlowFile", {
            "content": "test content"
        })
        
        assert processor_id in self.engine.processors
        assert processor_id in self.engine.flows[flow_id].processor_ids
        
    def test_create_connection(self):
        """Test creating connections between processors"""
        flow_id = self.engine.create_flow("Test Flow")
        proc1_id = self.engine.add_processor(flow_id, "GenerateFlowFile", {})
        proc2_id = self.engine.add_processor(flow_id, "LogAttribute", {})
        
        conn_id = self.engine.create_connection(proc1_id, proc2_id)
        assert conn_id in self.engine.connections
        
    @pytest.mark.asyncio
    async def test_flow_execution(self):
        """Test flow start/stop"""
        flow_id = self.engine.create_flow("Test Flow")
        self.engine.add_processor(flow_id, "GenerateFlowFile", {"content": "test"})
        
        await self.engine.start_flow(flow_id)
        assert self.engine.flows[flow_id].status == "RUNNING"
        
        await self.engine.stop_flow(flow_id)
        assert self.engine.flows[flow_id].status == "STOPPED"
        
    def test_engine_stats(self):
        """Test engine statistics"""
        stats = self.engine.get_engine_stats()
        assert "flows_active" in stats
        assert "processors_running" in stats
        assert "uptime_seconds" in stats
        
    def test_flow_status(self):
        """Test flow status retrieval"""
        flow_id = self.engine.create_flow("Test Flow")
        processor_id = self.engine.add_processor(flow_id, "LogAttribute", {})
        
        status = self.engine.get_flow_status(flow_id)
        assert status["id"] == flow_id
        assert status["name"] == "Test Flow"
        assert processor_id in status["processors"]

if __name__ == "__main__":
    pytest.main([__file__])
