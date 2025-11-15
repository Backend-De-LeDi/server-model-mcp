from configs.ai.llm import AgentBuilder
from langchain.agents import AgentExecutor
from validations.msgRequest import MsgRequest

class ChatBotServices:
	model:AgentExecutor = None

	def __init__(self):
		self.model = AgentBuilder.build_agent()


	async def run(self,msg:MsgRequest):
		response = await self.model.ainvoke({"input": msg.msg})
		return response