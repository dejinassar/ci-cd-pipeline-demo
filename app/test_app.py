from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_create_todo():
    response = client.post("/todos", json={"id": 1, "title": "Learn CI/CD"})
    assert response.status_code == 200
    data = response.json()
    assert data["todo"]["title"] == "Learn CI/CD"
