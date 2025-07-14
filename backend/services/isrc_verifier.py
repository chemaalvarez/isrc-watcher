# backend/services/isrc_verifier.py

from backend.schemas.isrc import ISRCRequest, ISRCResponse
from backend.models.isrc_verification import ISRCVerification
from backend.services.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

# 1. Función de lógica pura
def verify_isrc_code(isrc_code: str) -> tuple[bool, str]:
    is_valid = isrc_code.startswith("ISRC")
    message = "Valid ISRC" if is_valid else "Invalid ISRC"
    return is_valid, message

# 2. Función que usa la lógica + guarda
async def verify_and_store_isrc(isrc_code: str) -> dict:
    is_valid, message = verify_isrc_code(isrc_code)

    async for session in get_db():  # get_db es un generador async
        verification = ISRCVerification(
            code=isrc_code,
            is_valid=str(is_valid),
            message=message,
        )
        session.add(verification)
        await session.commit()
        await session.refresh(verification)

    return {
        "is_valid": is_valid,
        "message": message,
    }
