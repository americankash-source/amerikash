from uuid import uuid4

from fastapi.testclient import TestClient

from app.main import app


def test_root_endpoint():
    with TestClient(app) as client:
        response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "AmeriKash running"}


def test_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_database_health_endpoint():
    with TestClient(app) as client:
        response = client.get("/health/db")
    assert response.status_code == 200
    assert response.json()["database"] == "connected"


def test_plan_endpoint():
    with TestClient(app) as client:
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


def test_register_user_does_not_return_password_hash():
    email = f"user-{uuid4().hex}@example.com"
    with TestClient(app) as client:
        response = client.post("/auth/register", json={"email": email, "password": "securepass123"})
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == email
    assert "password" not in data
    assert "password_hash" not in data


def test_login_returns_bearer_token():
    email = f"login-{uuid4().hex}@example.com"
    password = "securepass123"
    with TestClient(app) as client:
        register_response = client.post("/auth/register", json={"email": email, "password": password})
        login_response = client.post("/auth/login", json={"email": email, "password": password})

    assert register_response.status_code == 201
    assert login_response.status_code == 200
    data = login_response.json()
    assert data["token_type"] == "bearer"
    assert data["access_token"]
    assert data["user"]["email"] == email
    assert "password" not in data
    assert "password_hash" not in data
