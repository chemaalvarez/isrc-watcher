# backend/services/isrc_verifier.py

import re
from backend.schemas.isrc import ISRCRequest, ISRCResponse
from backend.models.isrc_verification import ISRCVerification
from backend.services.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

# CC (2 alpha) + registrant (3 alphanumeric) + year (2 digits) + designation (5 digits)
_ISRC_RE = re.compile(r"^[A-Z]{2}[A-Z0-9]{3}[0-9]{7}$")

# 1. Función de lógica pura
def verify_isrc_code(isrc_code: str) -> tuple[bool, str]:
    normalized = isrc_code.upper().replace("-", "")
    is_valid = bool(_ISRC_RE.match(normalized))
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
