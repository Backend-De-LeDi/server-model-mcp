from pydantic import BaseModel

class MsgRequest(BaseModel):
    userId: str
    sessionId: str
    msg: str