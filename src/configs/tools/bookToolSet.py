from langchain.tools import tool
from services.bookService import BookService
from rich import print

service = BookService()

class BookToolSet:

    @tool("countBooks")
    def countBooks():
        """
        Devuelve la cantidad total de libros disponibles en la plataforma.
        No recibe parámetros.
        """

        result = service.countBook()
        print(result)
        return result

    @tool("countByFormat")
    def countByFormat():
        """
        Devuelve la cantidad de libros agrupados por formato (ejemplo: PDF, EPUB, físico).
        No recibe parámetros.
        """

        result = service.countByFormat()
        print(result)
        return result

    @tool("countByGenre")
    def countByGenre():
        """
        Devuelve la cantidad de libros agrupados por género literario (ejemplo: ficción, historia).
        No recibe parámetros.
        """

        result = service.countByGenre()
        print(result)
        return result

    @tool("countBySubgenre")
    def countBySubgenre():
        """
        Devuelve la cantidad de libros agrupados por subgénero (ejemplo: ciencia ficción, biografía).
        No recibe parámetros.
        """

        result = service.countBySubgenre()
        print(result)
        return result

    @tool("getFormats")
    def getFormats():
        """
        Devuelve la lista de formatos únicos disponibles en los libros.
        No recibe parámetros.
        """

        result = service.getFormats()
        print(result)
        return result

    @tool("getGenres")
    def getGenres():
        """
        Devuelve la lista de géneros únicos disponibles en los libros.
        No recibe parámetros.
        """

        result = service.getGenres()
        print(result)
        return result

    @tool("getSubgenres")
    def getSubgenres():
        """
        Devuelve la lista de subgéneros únicos disponibles en los libros.
        No recibe parámetros.
        """

        result = service.getSubgenres()
        print(result)
        return result

    @tool("getLanguages")
    def getLanguages():
        """
        Devuelve la lista de idiomas únicos disponibles en los libros.
        No recibe parámetros.
        """

        result = service.getLanguages()
        print(result)
        return result

    @tool("getLevels")
    def getLevels():
        """
        Devuelve la lista de niveles únicos de los libros (ejemplo: básico, intermedio, avanzado).
        No recibe parámetros.
        """

        result = service.getLevels()
        print(result)
        return result
    
    @tool("getBooksByTitle")
    def getBooksByTitle(title: str):
        """
        Devuelve los libros cuyo título coincide parcial o totalmente con el texto ingresado.
        Parámetros:
        - title (str): texto del título a buscar. Insensible a mayúsculas/minúsculas.
        """

        result = service.getBooksByTitle(title)
        print(result)
        return result

    @tool("getBooksByGenre")
    def getBooksByGenre(genre: str):
        """
        Devuelve los libros que pertenecen a un género específico.
        Parámetros:
        - genre (str): nombre del género. Coincidencia parcial, insensible a mayúsculas/minúsculas valores aceptados(Narrativo y Poesía).
        """

        result = service.getBooksByGenre(genre)
        print(result)
        return result

    @tool("getBooksBySubgenre")
    def getBooksBySubgenre(subgenre: str):
        """
        Devuelve los libros que pertenecen a un subgénero específico.
        Parámetros:
        - subgenre (str): nombre del subgénero. Coincidencia parcial, insensible a mayúsculas/minúsculas.
        """

        result = service.getBooksBySubgenre(subgenre)
        print(result)
        return result

    @tool("getBooksByLanguage")
    def getBooksByLanguage(language: str):
        """
        Devuelve los libros escritos en un idioma específico.
        Parámetros:
        - language (str): idioma a buscar. Coincidencia parcial, insensible a mayúsculas/minúsculas.
        """

        result = service.getBooksByLanguage(language)
        print(result)
        return result

    @tool("getBooksByLevel")
    def getBooksByLevel(level: str):
        """
        Devuelve los libros que corresponden a un nivel específico.
        Parámetros:
        - level (str): nivel de dificultad (ejemplo: básico, intermedio, avanzado).
        """

        result = service.getBooksByLevel(level)
        print(result)
        return result

    @tool("getBooksByTheme")
    def getBooksByTheme(theme: str):
        """
        Devuelve los libros que coinciden con un tema específico.
        Parámetros:
        - theme (str): tema o palabra clave. Coincidencia parcial, insensible a mayúsculas/minúsculas.
        """

        result = service.getBooksByTheme(theme)
        print(result)
        return result

    @tool("getIntelligenceBook")
    def getIntelligenceBook(query: list[str], userLevel: str = None):
        """
        Busca libros usando coincidencia avanzada (texto completo o regex).
        Permite filtrar por nivel si se especifica.
        Parámetros:
        - query (list[str]): lista de palabras clave o expresiones regulares.
        - userLevel (str, opcional): nivel adecuado para el usuario (Inicial, Secundario, Joven Adulto y Adulto Mayor) .
        """

        result = service.getIntelligenceBook(query, userLevel)
        print(result)
        return result

    @tool("getAllBooksByLevel")
    def getAllBooksByLevel(level: str):
        """
        Devuelve todos los libros correspondientes a un nivel y su jerarquía asociada.
        Parámetros:
        - level (str): nivel adecuado para el usuario (Inicial, Secundario, Joven Adulto y Adulto Mayor).
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
        Filtra libros aplicando múltiples criterios de búsqueda.
        Parámetros:
        - theme (list[str], opcional): lista de temas.
        - subgenre (list[str], opcional): lista de subgéneros.
        - yearBook (list[str], opcional): lista de años de publicación.
        - genre (list[str], opcional): lista de géneros.
        - format (list[str], opcional): lista de formatos.
        - level (str, opcional): nivel de dificultad.
        """

        result = service.getBooksByFiltering(theme or [],
                                             subgenre or [],
                                             yearBook or [],
                                             genre or [],
                                             format or [],
                                             level)
        print(result)
        return result
