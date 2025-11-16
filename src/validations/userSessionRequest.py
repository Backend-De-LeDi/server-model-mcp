from pydantic import BaseModel

class UserSessionRequest(BaseModel):
	userId: str
	sessionId: str
