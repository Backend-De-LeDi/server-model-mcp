from configs.ai.llm import AgentBuilder
from langchain.agents import AgentExecutor
from validations.msgRequest import MsgRequest
from services.modelMemory import MemoryService
from services.userService import UserService
from services.bookService import BookService
from rich import print

class ChatBotServices:
	model:AgentExecutor = None
	memoryService = MemoryService()
	userService = UserService()
	bookService = BookService()

	def __init__(self):
		self.model = AgentBuilder.build_agent()


	async def run(self,body:MsgRequest):

		self.memoryService.saveMemory(body.userId,body.sessionId,"user",body.msg)
		result = self.userService.getUserPreferences(body.userId)
		
		formats = result.get("preference", {}).get("format", [])
		subgenres = result.get("preference", {}).get("subgenre", []) or result.get("preference", {}).get("category", [])

		formatStr = ", ".join(formats) if formats else ""
		subgenreStr = ", ".join(subgenres) if subgenres else ""

		memoryContext = self.memoryService.getMemoryByUserAndSession(body.userId, body.sessionId)
		memoryText = [
			    {"role": item.get("role"), "content": item.get("text")}
			    for doc in memoryContext
			    for item in doc.get("content", [])
		]

		print(memoryText)

		response = await self.model.ainvoke({
			"input": body.msg,
			"userId":body.userId,
			"sessionId":body.sessionId,
			"subgenre":subgenreStr,
			"format":formatStr,
			"memory_context": memoryText
			})
		
		self.memoryService.saveMemory(body.userId,body.sessionId,"assistant",response["output"])
		return response