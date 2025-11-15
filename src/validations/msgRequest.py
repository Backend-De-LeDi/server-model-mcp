from pydantic import BaseModel
class MsgRequest(BaseModel):
	msg: str
