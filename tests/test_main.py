from fastapi.testclient import TestClient
from app.main import app, ITEMS, API_PREFIX, API_VERSION

client = TestClient(app)

def setup_function():
    ITEMS.clear()

def test_docs_available():
    r = client.get("/docs")
    assert r.status_code == 200
    assert "Swagger UI" in r.text  # basic signal it loaded

def test_openapi_available_and_versioned():
    r = client.get("/openapi.json")
    assert r.status_code == 200
    data = r.json()
    assert data["info"]["title"] == "Dockerized FastAPI"
    assert data["info"]["version"] == API_VERSION

def test_health_versioned():
    r = client.get(f"{API_PREFIX}/health")
    assert r.status_code == 200
    body = r.json()
    assert body["status"] == "ok"
    assert body["api_version"] == API_VERSION

def test_items_flow_versioned():
    r = client.get(f"{API_PREFIX}/items")
    assert r.status_code == 200
    assert r.json() == []

    r2 = client.post(f"{API_PREFIX}/items", json={"name": "apple"})
    assert r2.status_code == 201
    assert r2.json() == {"name": "apple"}

    r3 = client.get(f"{API_PREFIX}/items")
    assert r3.status_code == 200
    assert r3.json() == [{"name": "apple"}]

def test_metrics_counts_items_versioned():
    client.post(f"{API_PREFIX}/items", json={"name": "a"})
    client.post(f"{API_PREFIX}/items", json={"name": "b"})
    r = client.get(f"{API_PREFIX}/metrics")
    assert r.status_code == 200
    data = r.json()
    assert "uptime_seconds" in data
    assert data["items_count"] == 2
