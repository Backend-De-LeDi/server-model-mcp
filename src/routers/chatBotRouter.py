from fastapi import APIRouter,Body
from fastapi.responses import JSONResponse
from services.chatBotService import ChatBotServices
from validations.msgRequest import MsgRequest
from rich import print

class ChatBotRouter:

	botServices = ChatBotServices()

	def __init__(self):
		self.router = APIRouter()

		self.router.post("/chatBot",tags=["ChatBotRouter"])(self.chatBot)

	async def chatBot(self,body:MsgRequest):

		respone = await self.botServices.run(body)
		
		return JSONResponse(content={"msg": respone["output"]})