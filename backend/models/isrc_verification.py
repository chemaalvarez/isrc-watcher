from sqlalchemy import Column, Integer, String, DateTime, func
from backend.services.db import Base

class ISRCVerification(Base):
    __tablename__ = "isrc_verifications"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, nullable=False)
    is_valid = Column(String, nullable=False)
    message = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
