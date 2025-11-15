from langchain.prompts import PromptTemplate
from configs.prompts.promptSystem import PromptSystem

def build_prompt_template() -> PromptTemplate:
    ps = PromptSystem()
    ps.add_instruction("Eres un bibliotecario virtual")
    ps.add_task("Responder preguntas")
    ps.set_response_style("Responder Consultas")
    base = ps.build()

    template_str = f"""{base}

	Usuario: {{input}}
	
	Pasos del agente: {{agent_scratchpad}}"""

    return PromptTemplate.from_template(template_str)