from langchain.tools import tool
from services.modelMemory import MemoryService

memoryService = MemoryService()

class MemoryToolset:

	@tool
	def getMemoryContext(userId: str, sessionId: str) -> str:
		"""
		 Devuelve el historial de conversación para un usuario y sesión como texto plano.
		solo se usa si no tenes contexto pero debes usarlo para responer cosas que no saber.
		
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