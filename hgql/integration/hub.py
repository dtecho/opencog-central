
"""
HGQL Integration Hub
Centralized system for managing API connections and data sources
"""

import asyncio
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod
import logging
from enum import Enum

class ConnectorType(Enum):
    REST_API = "rest_api"
    DATABASE = "database"
    MESSAGE_QUEUE = "message_queue"
    FILE_SYSTEM = "file_system"
    WEBSOCKET = "websocket"

@dataclass
class ConnectionConfig:
    name: str
    connector_type: ConnectorType
    endpoint: str
    authentication: Dict[str, Any]
    rate_limit: int
    timeout: int
    retry_policy: Dict[str, Any]
    transformation_rules: List[Dict[str, Any]]

class DataConnector(ABC):
    """Abstract base class for all data connectors"""
    
    def __init__(self, config: ConnectionConfig):
        self.config = config
        self.is_connected = False
        self.connection_stats = {
            'total_requests': 0,
            'successful_requests': 0,
            'failed_requests': 0,
            'avg_response_time': 0
        }
        
    @abstractmethod
    async def connect(self):
        """Establish connection to data source"""
        pass
        
    @abstractmethod
    async def disconnect(self):
        """Close connection to data source"""
        pass
        
    @abstractmethod
    async def fetch_data(self, query: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch data from source"""
        pass
        
    @abstractmethod
    async def push_data(self, data: Dict[str, Any]) -> bool:
        """Push data to source"""
        pass

class RESTAPIConnector(DataConnector):
    """Connector for REST API endpoints"""
    
    def __init__(self, config: ConnectionConfig):
        super().__init__(config)
        self.session = None
        
    async def connect(self):
        import aiohttp
        
        auth = self.config.authentication
        if auth.get('type') == 'bearer':
            headers = {'Authorization': f"Bearer {auth['token']}"}
        elif auth.get('type') == 'basic':
            auth_obj = aiohttp.BasicAuth(auth['username'], auth['password'])
        else:
            headers = {}
            auth_obj = None
            
        timeout = aiohttp.ClientTimeout(total=self.config.timeout)
        self.session = aiohttp.ClientSession(
            headers=headers,
            auth=auth_obj,
            timeout=timeout
        )
        self.is_connected = True
        
    async def disconnect(self):
        if self.session:
            await self.session.close()
            self.is_connected = False
            
    async def fetch_data(self, query: Dict[str, Any]) -> Dict[str, Any]:
        if not self.is_connected:
            await self.connect()
            
        try:
            async with self.session.get(
                f"{self.config.endpoint}/{query.get('path', '')}",
                params=query.get('params', {})
            ) as response:
                data = await response.json()
                self.connection_stats['successful_requests'] += 1
                return self._transform_data(data)
                
        except Exception as e:
            self.connection_stats['failed_requests'] += 1
            raise e
        finally:
            self.connection_stats['total_requests'] += 1
            
    async def push_data(self, data: Dict[str, Any]) -> bool:
        if not self.is_connected:
            await self.connect()
            
        try:
            async with self.session.post(
                self.config.endpoint,
                json=data
            ) as response:
                success = response.status < 400
                if success:
                    self.connection_stats['successful_requests'] += 1
                else:
                    self.connection_stats['failed_requests'] += 1
                return success
                
        except Exception as e:
            self.connection_stats['failed_requests'] += 1
            raise e
        finally:
            self.connection_stats['total_requests'] += 1
            
    def _transform_data(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Apply transformation rules to incoming data"""
        transformed = data
        
        for rule in self.config.transformation_rules:
            if rule['type'] == 'field_mapping':
                transformed = self._apply_field_mapping(transformed, rule)
            elif rule['type'] == 'data_filtering':
                transformed = self._apply_data_filtering(transformed, rule)
                
        return transformed
        
    def _apply_field_mapping(self, data: Dict, rule: Dict) -> Dict:
        """Map field names according to rule"""
        mapping = rule.get('mapping', {})
        result = {}
        
        for old_key, new_key in mapping.items():
            if old_key in data:
                result[new_key] = data[old_key]
                
        return result
        
    def _apply_data_filtering(self, data: Dict, rule: Dict) -> Dict:
        """Filter data according to rule"""
        filters = rule.get('filters', [])
        # Implementation would apply various filtering logic
        return data

class IntegrationHub:
    """Central hub for managing all data connections"""
    
    def __init__(self):
        self.connectors: Dict[str, DataConnector] = {}
        self.monitoring_enabled = True
        self.logger = logging.getLogger(__name__)
        
    def register_connector(self, name: str, connector: DataConnector):
        """Register a new data connector"""
        self.connectors[name] = connector
        self.logger.info(f"Registered connector: {name}")
        
    def remove_connector(self, name: str):
        """Remove a data connector"""
        if name in self.connectors:
            asyncio.create_task(self.connectors[name].disconnect())
            del self.connectors[name]
            self.logger.info(f"Removed connector: {name}")
            
    async def connect_all(self):
        """Connect to all registered data sources"""
        tasks = []
        for name, connector in self.connectors.items():
            tasks.append(self._safe_connect(name, connector))
            
        await asyncio.gather(*tasks, return_exceptions=True)
        
    async def _safe_connect(self, name: str, connector: DataConnector):
        """Safely connect to a data source with error handling"""
        try:
            await connector.connect()
            self.logger.info(f"Connected to {name}")
        except Exception as e:
            self.logger.error(f"Failed to connect to {name}: {e}")
            
    async def fetch_from_source(self, source_name: str, query: Dict[str, Any]) -> Dict[str, Any]:
        """Fetch data from a specific source"""
        if source_name not in self.connectors:
            raise ValueError(f"Unknown source: {source_name}")
            
        connector = self.connectors[source_name]
        return await connector.fetch_data(query)
        
    async def push_to_source(self, source_name: str, data: Dict[str, Any]) -> bool:
        """Push data to a specific source"""
        if source_name not in self.connectors:
            raise ValueError(f"Unknown source: {source_name}")
            
        connector = self.connectors[source_name]
        return await connector.push_data(data)
        
    def get_connection_status(self) -> Dict[str, Any]:
        """Get status of all connections"""
        status = {}
        
        for name, connector in self.connectors.items():
            status[name] = {
                'connected': connector.is_connected,
                'type': connector.config.connector_type.value,
                'stats': connector.connection_stats
            }
            
        return status
        
    async def health_check(self) -> Dict[str, Any]:
        """Perform health check on all connections"""
        health_status = {}
        
        for name, connector in self.connectors.items():
            try:
                # Simple ping test
                if connector.is_connected:
                    health_status[name] = 'healthy'
                else:
                    health_status[name] = 'disconnected'
            except Exception as e:
                health_status[name] = f'error: {str(e)}'
                
        return health_status

# Factory for creating connectors
class ConnectorFactory:
    @staticmethod
    def create_connector(config: ConnectionConfig) -> DataConnector:
        """Create appropriate connector based on type"""
        
        if config.connector_type == ConnectorType.REST_API:
            return RESTAPIConnector(config)
        elif config.connector_type == ConnectorType.DATABASE:
            # Would return DatabaseConnector(config)
            raise NotImplementedError("Database connector not yet implemented")
        elif config.connector_type == ConnectorType.MESSAGE_QUEUE:
            # Would return MessageQueueConnector(config)
            raise NotImplementedError("Message queue connector not yet implemented")
        else:
            raise ValueError(f"Unknown connector type: {config.connector_type}")
