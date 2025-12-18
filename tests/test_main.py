from fastapi.testclient import TestClient
from app.main import app, ITEMS

client = TestClient(app)

def setup_function():
    # Reset global state before each test
    ITEMS.clear()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_items_empty_initially():
    r = client.get("/items")
    assert r.status_code == 200
    assert r.json() == []

def test_add_item_then_list():
    r = client.post("/items", json={"name": "apple"})
    assert r.status_code == 201
    assert r.json() == {"name": "apple"}

    r2 = client.get("/items")
    assert r2.status_code == 200
    assert r2.json() == [{"name": "apple"}]

def test_metrics_counts_items():
    client.post("/items", json={"name": "a"})
    client.post("/items", json={"name": "b"})
    r = client.get("/metrics")
    assert r.status_code == 200
    data = r.json()
    assert "uptime_seconds" in data
    assert data["items_count"] == 2
