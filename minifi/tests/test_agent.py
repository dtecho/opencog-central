
"""
Test MiniNiFi Agent
Unit tests for the core agent functionality
"""

import pytest
import asyncio
import yaml
import tempfile
from pathlib import Path

from minifi.core.agent import MiniNiFiAgent

@pytest.fixture
def sample_config():
    """Sample configuration for testing"""
    return {
        'agent': {
            'id': 'test-agent',
            'name': 'Test Agent'
        },
        'server': {'port': 8081, 'host': '0.0.0.0'},
        'logging': {'level': 'DEBUG'}
    }

@pytest.fixture
async def test_agent(sample_config):
    """Create a test agent instance"""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        yaml.dump(sample_config, f)
        config_path = f.name
    
    agent = MiniNiFiAgent(config_path)
    await agent.initialize()
    
    yield agent
    
    await agent.stop()
    Path(config_path).unlink()

@pytest.mark.asyncio
async def test_agent_initialization(test_agent):
    """Test agent initialization"""
    assert test_agent.config['agent']['id'] == 'test-agent'
    assert test_agent.config['agent']['name'] == 'Test Agent'
    assert len(test_agent.processors) > 0

@pytest.mark.asyncio 
async def test_agent_start_stop(test_agent):
    """Test agent start and stop"""
    await test_agent.start()
    assert test_agent.running == True
    
    await test_agent.stop()
    assert test_agent.running == False

@pytest.mark.asyncio
async def test_flow_creation(test_agent):
    """Test flow creation"""
    flow_config = {
        'id': 'test-flow',
        'processors': [
            {
                'id': 'gen',
                'type': 'GenerateFlowFile',
                'properties': {'interval': '5.0'}
            }
        ],
        'connections': []
    }
    
    flow_id = await test_agent.create_flow(flow_config)
    assert flow_id == 'test-flow'
    assert 'test-flow' in test_agent.flows

@pytest.mark.asyncio
async def test_agent_status(test_agent):
    """Test agent status reporting"""
    status = test_agent.get_status()
    
    assert 'agent_id' in status
    assert 'running' in status
    assert 'flows' in status
    assert status['agent_id'] == 'test-agent'
