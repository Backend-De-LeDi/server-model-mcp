from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor,create_openai_functions_agent
from configs.env.env import Env
from configs.prompts.promptTemplate import build_prompt_template
from configs.tools.allTools import mainTools
from rich import print
class AgentBuilder:


    @staticmethod
    def build_agent() -> AgentExecutor:
        tools = mainTools

        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0.0 ,
            api_key=Env.getEnv("GEMINI_API_KEY"),
        )

        prompt = build_prompt_template()
        

        agent = create_openai_functions_agent(
            llm=model,
            tools=tools,
            prompt=prompt
        )

        return AgentExecutor(agent=agent, tools=tools,verbose=True)