from langchain.tools import tool
from services.modelMemory import MemoryService

memoryService = MemoryService()

class Toolset:
	@tool
	def get_weather(city: str) -> str:
		"""Returns weather info for a given city"""
		return f"In {city}, it's 27°C with 5.54 km/h wind"

	@tool
	def getMemoryContext(userId: str, sessionId: str) -> str:
		"""
		Devuelve el historial de conversación para un usuario y sesión como texto plano.
		
		"""
		docs = memoryService.getMemory(userId)
		session_docs = [d for d in docs if d.get("sessionId") == sessionId]

		if not session_docs:
			return "No hay historial para este usuario y sesión."

		lines = []
		for doc in session_docs:
			for item in doc.get("content", []):
				role = item.get("role")
				text = item.get("text")
				prefix = "Usuario:" if role == "user" else "Asistente:"
				lines.append(f"{prefix} {text}")
		return "\n".join(lines)