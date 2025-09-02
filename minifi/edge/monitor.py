
"""
Resource Monitor
Monitors system resources for edge optimization
"""

import asyncio
import logging
import time
from typing import Dict, Any

logger = logging.getLogger(__name__)

class ResourceMonitor:
    """Monitors system resources and provides optimization recommendations"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.monitoring_enabled = config.get('resource_monitoring', True)
        self.alert_thresholds = {
            'cpu_percent': 80,
            'memory_percent': 80,
            'disk_percent': 90
        }
        self.metrics_history = []
        
    async def start_monitoring(self):
        """Start resource monitoring loop"""
        if not self.monitoring_enabled:
            return
        
        while True:
            try:
                metrics = await self.collect_metrics()
                self.metrics_history.append(metrics)
                
                # Keep only last 100 entries
                if len(self.metrics_history) > 100:
                    self.metrics_history = self.metrics_history[-100:]
                
                # Check for alerts
                await self._check_alerts(metrics)
                
                await asyncio.sleep(30)  # Monitor every 30 seconds
                
            except Exception as e:
                logger.error(f"Resource monitoring error: {e}")
                await asyncio.sleep(60)
    
    async def collect_metrics(self) -> Dict[str, Any]:
        """Collect current system metrics"""
        try:
            import psutil
            
            metrics = {
                'timestamp': time.time(),
                'cpu_percent': psutil.cpu_percent(interval=1),
                'memory': {
                    'percent': psutil.virtual_memory().percent,
                    'available_mb': psutil.virtual_memory().available // (1024 * 1024),
                    'used_mb': psutil.virtual_memory().used // (1024 * 1024)
                },
                'disk': {
                    'percent': psutil.disk_usage('.').percent,
                    'free_mb': psutil.disk_usage('.').free // (1024 * 1024)
                },
                'network': {
                    'bytes_sent': psutil.net_io_counters().bytes_sent,
                    'bytes_recv': psutil.net_io_counters().bytes_recv
                }
            }
            
            return metrics
            
        except ImportError:
            # Fallback metrics if psutil not available
            return {
                'timestamp': time.time(),
                'cpu_percent': 0,
                'memory': {'percent': 0, 'available_mb': 1024, 'used_mb': 0},
                'disk': {'percent': 0, 'free_mb': 10240},
                'network': {'bytes_sent': 0, 'bytes_recv': 0}
            }
    
    async def _check_alerts(self, metrics: Dict[str, Any]):
        """Check if any metrics exceed alert thresholds"""
        
        if metrics['cpu_percent'] > self.alert_thresholds['cpu_percent']:
            logger.warning(f"High CPU usage: {metrics['cpu_percent']}%")
        
        if metrics['memory']['percent'] > self.alert_thresholds['memory_percent']:
            logger.warning(f"High memory usage: {metrics['memory']['percent']}%")
        
        if metrics['disk']['percent'] > self.alert_thresholds['disk_percent']:
            logger.warning(f"High disk usage: {metrics['disk']['percent']}%")
    
    def get_current_metrics(self) -> Optional[Dict[str, Any]]:
        """Get the most recent metrics"""
        return self.metrics_history[-1] if self.metrics_history else None
    
    def get_recommendations(self) -> List[str]:
        """Get optimization recommendations based on current metrics"""
        recommendations = []
        
        current = self.get_current_metrics()
        if not current:
            return recommendations
        
        if current['cpu_percent'] > 70:
            recommendations.append("Consider reducing processor concurrency")
        
        if current['memory']['percent'] > 70:
            recommendations.append("Consider reducing flow file queue sizes")
        
        if current['disk']['percent'] > 80:
            recommendations.append("Consider enabling data compression")
        
        return recommendations
