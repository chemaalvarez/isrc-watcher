from pydantic import BaseModel

class ISRCRequest(BaseModel):
    isrc_code: str

class ISRCResponse(BaseModel):
    is_valid: bool
    message: str
