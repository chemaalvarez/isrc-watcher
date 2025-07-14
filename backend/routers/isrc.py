# backend/routers/isrc.py
from fastapi import APIRouter

router = APIRouter()

@router.post("/isrc/verify")
async def verify_isrc(code: dict):
    return {"status": "ok", "received": code}
