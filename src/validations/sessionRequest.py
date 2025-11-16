from pydantic import BaseModel

class SessionRequest(BaseModel):
    sessionId: str