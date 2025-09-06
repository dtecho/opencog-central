
# HGQL API Reference

## HyperGraph Query Language (HGQL) API Documentation

### Overview

HGQL provides a comprehensive interface for querying and manipulating hypergraph data structures with advanced cognitive reasoning capabilities. This API combines traditional graph query functionality with probabilistic logic networks (PLN) and attention-based processing.

### Core Query Types

#### MATCH Queries
```hgql
MATCH cognitive_pattern IN atomspace 
WHERE synergy_potential > 0.75
BIND learning_context TO embodiment_layer
RETURN nodes, edges, confidence
```

**Parameters:**
- `pattern`: Hypergraph pattern to match
- `conditions`: Filter conditions
- `confidence_threshold`: Minimum confidence level (0.0-1.0)

**Response:**
```json
{
  "matches": [
    {
      "nodes": ["concept:human", "concept:mortal"],
      "edges": [{"type": "inheritance", "strength": 0.9}],
      "confidence": 0.85
    }
  ],
  "count": 1,
  "query_time": 1640995200.123
}
```

#### INFER Queries
```hgql
INFER probabilistic_consequences 
USING pln_reasoning(confidence=0.85)
FROM matched_patterns
WHERE evidence_strength > 0.6
```

**Parameters:**
- `inference_rules`: List of PLN rules to apply
- `confidence_threshold`: Minimum inference confidence
- `max_steps`: Maximum reasoning steps

**Response:**
```json
{
  "inferences": [
    {
      "conclusion": "Socrates is mortal",
      "confidence": 0.92,
      "rule_chain": ["deduction", "modus_ponens"],
      "premises": ["Socrates is human", "Humans are mortal"]
    }
  ],
  "rule_applications": 2,
  "confidence_threshold": 0.85
}
```

### REST API Endpoints

#### Query Execution
- **POST** `/api/execute_query`
- **Content-Type**: `application/json`

```json
{
  "type": "MATCH|BIND|INFER|UPDATE|TRIGGER",
  "pattern": "hypergraph pattern string",
  "conditions": ["condition1", "condition2"],
  "rules": ["rule1", "rule2"],
  "confidence": 0.75
}
```

#### Schema Information
- **GET** `/api/schema`

Returns available node types, edge types, and inference rules.

#### Integration Management
- **GET** `/api/integrations`
- Returns status of all data source connections

```json
{
  "atomspace": {
    "connected": true,
    "type": "rest_api",
    "stats": {
      "total_requests": 150,
      "successful_requests": 147,
      "failed_requests": 3,
      "avg_response_time": 0.045
    }
  }
}
```

#### Health Check
- **GET** `/api/integrations/health`

Returns health status of all integrations.

### Authentication & Authorization

HGQL supports multiple authentication mechanisms:

1. **Bearer Token Authentication**
   ```http
   Authorization: Bearer your-jwt-token
   ```

2. **Basic Authentication**
   ```http
   Authorization: Basic base64(username:password)
   ```

3. **API Key Authentication**
   ```http
   X-API-Key: your-api-key
   ```

### Rate Limiting

Default rate limits:
- 100 requests per minute for authenticated users
- 10 requests per minute for unauthenticated users
- 1000 requests per hour for premium accounts

### Error Handling

All API errors follow this format:

```json
{
  "error": {
    "code": "INVALID_QUERY",
    "message": "Pattern syntax error at position 15",
    "details": {
      "position": 15,
      "expected": "closing parenthesis",
      "received": "end of input"
    }
  },
  "timestamp": "2024-01-01T12:00:00Z",
  "request_id": "req_123456789"
}
```

### Integration Connectors

#### Available Connector Types

1. **REST API Connector**
   - HTTP/HTTPS endpoints
   - JSON data exchange
   - OAuth2 and Bearer token support

2. **Database Connector** (Coming Soon)
   - PostgreSQL, MySQL, MongoDB
   - SQL and NoSQL queries
   - Connection pooling

3. **Message Queue Connector** (Coming Soon)
   - RabbitMQ, Apache Kafka
   - Real-time data streaming
   - Event-driven processing

4. **File System Connector** (Coming Soon)
   - Local and network file systems
   - CSV, JSON, XML formats
   - Batch processing

### Configuration Examples

#### REST API Integration
```json
{
  "name": "external_kb",
  "connector_type": "rest_api",
  "endpoint": "https://api.example.com/v1",
  "authentication": {
    "type": "bearer",
    "token": "your-token"
  },
  "rate_limit": 100,
  "timeout": 30,
  "transformation_rules": [
    {
      "type": "field_mapping",
      "mapping": {
        "concept_id": "id",
        "concept_name": "label"
      }
    }
  ]
}
```

### Performance Optimization

#### Query Optimization Tips

1. **Use Specific Patterns**: Avoid overly broad patterns that match large subgraphs
2. **Set Confidence Thresholds**: Filter low-confidence results early
3. **Limit Result Sets**: Use appropriate limits to prevent memory issues
4. **Cache Frequent Queries**: Enable query caching for repeated operations

#### Monitoring & Metrics

The system provides comprehensive metrics:

- Query execution time
- Memory usage
- Connection pool status
- Error rates and types
- Attention allocation efficiency

### SDKs and Client Libraries

#### Python Client
```python
from hgql_client import HGQLClient

client = HGQLClient(
    endpoint="http://localhost:5000",
    api_key="your-api-key"
)

result = await client.match(
    pattern="(Concept Human) -> (Predicate Mortal)",
    confidence=0.8
)
```

#### JavaScript Client
```javascript
import { HGQLClient } from 'hgql-client';

const client = new HGQLClient({
  endpoint: 'http://localhost:5000',
  apiKey: 'your-api-key'
});

const results = await client.infer({
  rules: ['deduction', 'modus_ponens'],
  confidence: 0.75
});
```

### Best Practices

1. **Query Design**
   - Start with simple patterns and add complexity gradually
   - Use appropriate confidence thresholds
   - Consider attention allocation in query design

2. **Integration Management**
   - Monitor connection health regularly
   - Implement proper retry logic
   - Use connection pooling for high-traffic scenarios

3. **Security**
   - Use HTTPS in production
   - Implement proper authentication
   - Validate all input data
   - Monitor for unusual query patterns

### Troubleshooting

#### Common Issues

1. **Query Timeout**
   - Reduce query complexity
   - Increase timeout settings
   - Check system resources

2. **Connection Failures**
   - Verify network connectivity
   - Check authentication credentials
   - Review rate limiting settings

3. **Memory Issues**
   - Limit result set sizes
   - Optimize query patterns
   - Monitor hypergraph size

#### Debug Mode

Enable debug mode for detailed logging:

```python
app.run(debug=True, log_level='DEBUG')
```

### Version Compatibility

- **Current Version**: 1.0.0
- **API Version**: v1
- **Minimum Python**: 3.8+
- **Compatible with**: OpenCog 5.x, AtomSpace 5.x

### Support & Community

- **Documentation**: https://hgql.docs.org
- **GitHub**: https://github.com/opencog/hgql
- **Issues**: https://github.com/opencog/hgql/issues
- **Discussions**: https://github.com/opencog/hgql/discussions
