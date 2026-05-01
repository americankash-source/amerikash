from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "AmeriKash running"}


def test_health_endpoint():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_database_health_endpoint():
    response = client.get("/health/db")
    assert response.status_code == 200
    assert response.json()["database"] == "connected"


def test_plan_endpoint():
    response = client.post(
        "/plan/",
        json={
            "user_id": "u1",
            "income": 8000,
            "expenses": 5000,
            "goals": ["invest"],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "cashflow" in data
    assert "risk" in data
    assert "investment" in data
