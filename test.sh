curl http://localhost:8000/health
curl http://localhost:8000/items
curl -X POST http://localhost:8000/items -H "Content-Type: application/json" -d '{"name":"apple"}'
curl http://localhost:8000/metrics
