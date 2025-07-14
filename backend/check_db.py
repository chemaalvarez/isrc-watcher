# check_db.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import asyncio
from backend.services.db import get_db

from sqlalchemy import text



async def test_connection():
    async for session in get_db():
        result = await session.execute(text("SELECT 1"))
        print("DB result:", result.scalar())

asyncio.run(test_connection())
