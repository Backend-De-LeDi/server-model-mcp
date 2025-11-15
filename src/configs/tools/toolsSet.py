from langchain.tools import tool

class Toolset:
	@tool
	def get_weather(city: str) -> str:
		"""Returns weather info for a given city"""
		return f"In {city}, it's 27°C with 5.54 km/h wind"