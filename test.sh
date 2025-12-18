curl http://localhost:8000/v1/health
curl http://localhost:8000/v1/items
curl -X POST http://localhost:8000/v1/items -H "Content-Type: application/json" -d '{"name":"apple"}'
curl http://localhost:8000/v1/metrics
curl http://localhost:8000/docs
curl http://localhost:8000/openapi.json | head
