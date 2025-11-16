from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from configs.tools.MemoryToolsSet import MemoryToolset
from configs.env.env import Env
from configs.prompts.promptTemplate import build_prompt_template

class AgentBuilder:
    @staticmethod
    def build_agent() -> AgentExecutor:
        tools = [
            MemoryToolset.getMemoryContext
			]

        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.5,
            api_key=Env.getEnv("GEMINI_API_KEY"),
        )

        prompt = build_prompt_template()

        agent = create_tool_calling_agent(
            llm=model,
            tools=tools,
            prompt=prompt
        )

        return AgentExecutor(agent=agent, tools=tools,verbose=True)