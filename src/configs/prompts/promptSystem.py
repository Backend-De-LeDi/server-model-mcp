class PromptSystem:
	def __init__(self):
		self.instructions = []
		self.rules = []
		self.tasks = []
		self.response_style = []
		self.toolsDescription = []

	def add_instruction(self, text: str):
		self.instructions.append(text)

	def add_rule(self, text: str):
		self.rules.append(text)

	def add_task(self, text: str):
		self.tasks.append(text)
	
	def tools_description(self, text: str):
		self.toolsDescription.append(text)

	def set_response_style(self, text: str):
		self.response_style = [text]

	def build(self) -> str:
		parts = []

		if self.instructions:
			parts.append("Instructions:\n" + "\n".join(f"- {i}" for i in self.instructions))

		if self.toolsDescription:
			parts.append("tools description:\n" + "\n".join(f"- {i}" for i in self.toolsDescription))

		if self.rules:
			parts.append("Rules:\n" + "\n".join(f"- {r}" for r in self.rules))

		if self.tasks:
			parts.append("Tasks:\n" + "\n".join(f"- {t}" for t in self.tasks))

		if self.response_style:
			parts.append("Response Style:\n" + self.response_style[0])

		return "\n\n".join(parts)