from fastapi import APIRouter
from backend.schemas.isrc import ISRCRequest, ISRCResponse
from backend.services.isrc_verifier import verify_and_store_isrc

router = APIRouter()

@router.post("/verify", response_model=ISRCResponse)
async def verify_isrc(data: ISRCRequest):
    result = await verify_and_store_isrc(data.isrc_code)
    return ISRCResponse(**result)

