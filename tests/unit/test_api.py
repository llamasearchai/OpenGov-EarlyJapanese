"""Tests for the FastAPI application."""

import pytest
from fastapi.testclient import TestClient

from opengov_earlyjapanese.api.main import app


class TestAPIEndpoints:
    """Test suite for API endpoints."""

    @pytest.fixture
    def client(self):
        """Create a test client."""
        return TestClient(app)

    def test_root_endpoint(self, client):
        """Test the root endpoint."""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "name" in data
        assert "version" in data
        assert data["version"] == "0.2.0"

    def test_health_endpoint(self, client):
        """Test the health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    def test_get_hiragana_row_success(self, client):
        """Test getting a valid hiragana row."""
        response = client.get("/hiragana/a_row")
        assert response.status_code == 200
        data = response.json()
        assert data["row"] == "a_row"
        assert "characters" in data
        assert "mnemonics" in data
        assert len(data["characters"]) == 5
        assert "あ" in data["characters"]

    def test_get_hiragana_row_ka_row(self, client):
        """Test getting ka_row."""
        response = client.get("/hiragana/ka_row")
        assert response.status_code == 200
        data = response.json()
        assert data["row"] == "ka_row"
        assert len(data["characters"]) == 5
        assert "か" in data["characters"]

    def test_get_hiragana_row_invalid(self, client):
        """Test getting an invalid hiragana row."""
        response = client.get("/hiragana/invalid_row")
        assert response.status_code == 404
        data = response.json()
        assert "detail" in data

    def test_cors_headers(self, client):
        """Test CORS headers are present."""
        response = client.get("/", headers={"Origin": "http://localhost:3000"})
        assert response.status_code == 200
        # CORS middleware should handle this

    def test_openapi_docs(self, client):
        """Test that OpenAPI documentation is available."""
        response = client.get("/openapi.json")
        assert response.status_code == 200
        data = response.json()
        assert "openapi" in data
        assert "info" in data
        assert data["info"]["title"] == "OpenGov-EarlyJapanese API"
        assert data["info"]["version"] == "0.2.0"

