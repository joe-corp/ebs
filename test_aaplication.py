from fastapi.testclient import TestClient
from application import application

client = TestClient(application)

def test_index():
    response = client.get("/")
    assert response.status_code == 400
    assert response.json() == "Hellho World"