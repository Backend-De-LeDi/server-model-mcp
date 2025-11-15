from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from configs.tools.toolsSet import Toolset
from configs.env.env import Env
from configs.prompts.promptTemplate import build_prompt_template
from langchain.memory import ConversationBufferMemory

class AgentBuilder:
    @staticmethod
    def build_agent() -> AgentExecutor:
        tools = [Toolset.get_weather]

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
        
        memory = ConversationBufferMemory(
           memory_key="chat_history",
           return_messages=True
	   )

        return AgentExecutor(agent=agent, tools=tools, memory=memory,verbose=True)