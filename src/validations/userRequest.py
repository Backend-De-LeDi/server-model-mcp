from pydantic import BaseModel

class UserRequest(BaseModel):
    userId: str