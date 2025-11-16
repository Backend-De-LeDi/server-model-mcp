from configs.ai.llm import AgentBuilder
from langchain.agents import AgentExecutor
from validations.msgRequest import MsgRequest
from services.modelMemory import MemoryService

class ChatBotServices:
	model:AgentExecutor = None
	memoryService = MemoryService()

	def __init__(self):
		self.model = AgentBuilder.build_agent()


	async def run(self,body:MsgRequest):
		self.memoryService.saveMemory(body.userId,body.sessionId,"user",body.msg)
		response = await self.model.ainvoke({
			"input": body.msg,
			"userId":body.userId,
			"sessionId":body.sessionId
			})
		self.memoryService.saveMemory(body.userId,body.sessionId,"assistant",response["output"])
		return response