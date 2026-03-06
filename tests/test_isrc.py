import sys
import os
import pytest
from unittest.mock import patch, AsyncMock
from httpx import AsyncClient, ASGITransport

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend")))
from main import app
from backend.services.isrc_verifier import verify_isrc_code


def test_verify_isrc_code_valid():
    is_valid, message = verify_isrc_code("USRC17607839")
    assert is_valid is True
    assert message == "Valid ISRC"


def test_verify_isrc_code_invalid():
    is_valid, message = verify_isrc_code("TEST123")
    assert is_valid is False
    assert message == "Invalid ISRC"


@pytest.mark.asyncio
async def test_verify_isrc_endpoint_invalid():
    mock_result = {"is_valid": False, "message": "Invalid ISRC"}
    with patch(
        "backend.api.routes.isrc.verify_and_store_isrc",
        new=AsyncMock(return_value=mock_result),
    ):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/api/isrc/verify", json={"isrc_code": "TEST123"})

        assert response.status_code == 200
        assert response.json() == {"is_valid": False, "message": "Invalid ISRC"}


@pytest.mark.asyncio
async def test_verify_isrc_endpoint_valid():
    mock_result = {"is_valid": True, "message": "Valid ISRC"}
    with patch(
        "backend.api.routes.isrc.verify_and_store_isrc",
        new=AsyncMock(return_value=mock_result),
    ):
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.post("/api/isrc/verify", json={"isrc_code": "ISRC123456789"})

        assert response.status_code == 200
        assert response.json() == {"is_valid": True, "message": "Valid ISRC"}


@pytest.mark.asyncio
async def test_verify_isrc_endpoint_rejects_empty_string():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/isrc/verify", json={"isrc_code": ""})

    assert response.status_code == 422