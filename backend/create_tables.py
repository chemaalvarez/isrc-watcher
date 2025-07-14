import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio
from backend.services.db import engine, Base
from backend.models.isrc_verification import ISRCVerification

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Tablas creadas con éxito.")

if __name__ == "__main__":
    asyncio.run(create_db())
