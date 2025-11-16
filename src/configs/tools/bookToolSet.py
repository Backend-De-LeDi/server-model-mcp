from langchain.tools import tool
from services.bookService import BookService
from rich import print

service = BookService()

class BookToolSet:

    @tool("countBooks")
    def countBooks():
        """
        Herramienta que devuelve la cantidad total de libros en la plataforma.
        """
        result = service.countBook()
        print(result)
        return result

    @tool("countByFormat")
    def countByFormat():
        """
        Herramienta que devuelve la cantidad de libros agrupados por formato.
        """
        result = service.countByFormat()
        print(result)
        return result

    @tool("countByGenre")
    def countByGenre():
        """
        Herramienta que devuelve la cantidad de libros agrupados por género.
        """
        result = service.countByGenre()
        print(result)
        return result

    @tool("countBySubgenre")
    def countBySubgenre():
        """
        Herramienta que devuelve la cantidad de libros agrupados por subgénero.
        """
        result = service.countBySubgenre()
        print(result)
        return result

    @tool("getFormats")
    def getFormats():
        """
        Herramienta que devuelve los formatos únicos de los libros.
        """
        result = service.getFormats()
        print(result)
        return result

    @tool("getGenres")
    def getGenres():
        """
        Herramienta que devuelve los géneros únicos de los libros.
        """
        result = service.getGenres()
        print(result)
        return result

    @tool("getSubgenres")
    def getSubgenres():
        """
        Herramienta que devuelve los subgéneros únicos de los libros.
        """
        result = service.getSubgenres()
        print(result)
        return result

    @tool("getLanguages")
    def getLanguages():
        """
        Herramienta que devuelve los idiomas únicos de los libros.
        """
        result = service.getLanguages()
        print(result)
        return result

    @tool("getLevels")
    def getLevels():
        """
        Herramienta que devuelve los niveles únicos de los libros.
        """
        result = service.getLevels()
        print(result)
        return result
    
    @tool("getBooksByTitle")
    def getBooksByTitle(title: str):
        """
        Herramienta que devuelve libros por título (case-insensitive, coincidencia parcial).
        """
        result = service.getBooksByTitle(title)
        print(result)
        return result

    @tool("getBooksByGenre")
    def getBooksByGenre(genre: str):
        """
        Herramienta que devuelve libros por género (case-insensitive, coincidencia parcial).
        """
        result = service.getBooksByGenre(genre)
        print(result)
        return result

    @tool("getBooksBySubgenre")
    def getBooksBySubgenre(subgenre: str):
        """
        Herramienta que devuelve libros por subgénero (case-insensitive, coincidencia parcial).
        """
        result = service.getBooksBySubgenre(subgenre)
        print(result)
        return result

    @tool("getBooksByLanguage")
    def getBooksByLanguage(language: str):
        """
        Herramienta que devuelve libros por idioma (case-insensitive, coincidencia parcial).
        """
        result = service.getBooksByLanguage(language)
        print(result)
        return result

    @tool("getBooksByLevel")
    def getBooksByLevel(level: str):
        """
        Herramienta que devuelve libros por nivel (case-insensitive, coincidencia parcial).
        """
        result = service.getBooksByLevel(level)
        print(result)
        return result

    @tool("getBooksByTheme")
    def getBooksByTheme(theme: str):
        """
        Herramienta que devuelve libros por tema (case-insensitive, coincidencia parcial).
        """
        result = service.getBooksByTheme(theme)
        print(result)
        return result

    @tool("getIntelligenceBook")
    def getIntelligenceBook(query: list[str], userLevel: str = None):
        """
        Herramienta que busca libros usando texto completo o regex,
        filtrando por nivel si se pasa. Evita campos sensibles.
        """
        result = service.getIntelligenceBook(query, userLevel)
        print(result)
        return result

    @tool("getAllBooksByLevel")
    def getAllBooksByLevel(level: str):
        """
        Herramienta que devuelve libros según jerarquía de nivel.
        """
        result = service.getAllBooksByLevel(level)
        print(result)
        return result

    @tool("getBooksByFiltering")
    def getBooksByFiltering(theme: list[str] = None,
                            subgenre: list[str] = None,
                            yearBook: list[str] = None,
                            genre: list[str] = None,
                            format: list[str] = None,
                            level: str = None):
        """
        Herramienta que filtra libros por múltiples criterios (tema, subgénero, año, género, formato, nivel).
        """
        result = service.getBooksByFiltering(theme or [],
                                             subgenre or [],
                                             yearBook or [],
                                             genre or [],
                                             format or [],
                                             level)
        print(result)
        return result
