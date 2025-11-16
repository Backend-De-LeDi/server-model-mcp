from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from services.modelMemory import MemoryService
from validations.userRequest import UserRequest
from validations.userRequest import UserRequest
from validations.sessionRequest import SessionRequest
from validations.userSessionRequest import UserSessionRequest

class MemoryRouter:

	memoryService = MemoryService()

	def __init__(self):
		self.router = APIRouter()

		self.router.get("/memory", tags=["MemoryRouter"])(self.getMyMemory)
		self.router.get("/memoryBySession", tags=["MemoryRouter"])(self.getMemoryBySession)
		self.router.get("/memoryByUserAndSession", tags=["MemoryRouter"])(self.getMemoryByUserAndSession)

	def getMyMemory(self, body: UserRequest):
		result = self.memoryService.getMemory(body.userId)
		return JSONResponse(content={"sessions": result})

	def getMemoryBySession(self, body: SessionRequest):
		result = self.memoryService.getMemoryBySession(body.sessionId)
		return JSONResponse(content={"session": result})

	def getMemoryByUserAndSession(self, body: UserSessionRequest):
		result = self.memoryService.getMemoryByUserAndSession(body.userId, body.sessionId)
		return JSONResponse(content={"session": result})