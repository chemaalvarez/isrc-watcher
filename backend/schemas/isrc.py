from pydantic import BaseModel, Field

class ISRCRequest(BaseModel):
    isrc_code: str = Field(min_length=1)

class ISRCResponse(BaseModel):
    is_valid: bool
    message: str
