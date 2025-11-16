from langchain.tools import tool
from services.userService import UserService
from rich import print

service = UserService()

class UserToolSet:

    @tool("getUserPreferences")
    def getUserPreferences(user_id: str):
        """
        Herramienta que devuelve las preferencias del usuario (categoría y formato),
        ignorando campos sensibles.
        """
        result = service.getUserPreferences(user_id)
        print(result)
        return result

    @tool("getUserCategories")
    def getUserCategories(user_id: str):
        """
        Herramienta que devuelve solo las categorías preferidas del usuario.
        """
        result = service.getUserPreferences(user_id)
        categories = result.get("preference", {}).get("category", []) if result else []
        print(categories)
        return categories

    @tool("getUserFormats")
    def getUserFormats(user_id: str):
        """
        Herramienta que devuelve solo los formatos preferidos del usuario.
        """
        result = service.getUserPreferences(user_id)
        formats = result.get("preference", {}).get("format", []) if result else []
        print(formats)
        return formats