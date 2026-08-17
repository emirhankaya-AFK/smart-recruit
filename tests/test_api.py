from fastapi.testclient import TestClient

from app.main import create_app, match


def test_match_returns_missing_skills() -> None:
    result = match("Python FastAPI PostgreSQL", "Python FastAPI Docker Kubernetes")
    assert result.score > 0
    assert "docker" in result.missing_skills


def test_match_endpoint_requires_real_text() -> None:
    with TestClient(create_app()) as client:
        response = client.post(
            "/api/v1/matches",
            json={"resume": "short", "job_description": "short"},
        )
    assert response.status_code == 422
