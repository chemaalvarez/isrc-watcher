import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_verify_isrc():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/api/isrc/verify", json={"isrc_code": "TEST123"})
        print("Response body:", response.json())
        assert response.status_code == 200
