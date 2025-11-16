from configs.db.connection import Connection
from configs.env.env import Env
from datetime import datetime, timezone
from pymongo.collection import Collection
from utils.serializeDocument import serializeDocument

class BookService:
    def __init__(self):
        status, database = Connection().getConnection(Env.getEnv("MONGO_URL"))
        self.collections: Collection | None = database["books"] if status else None


    def countBook(self):
        if self.collections is None:
            return []

        result = self.collections.count_documents({})

        return result

    def countByGenre(self):
        if self.collections is None:
            return {}
        pipeline = [
            {"$group": {"_id": "$genre", "count": {"$sum": 1}}}
        ]
        return list(self.collections.aggregate(pipeline))

    def countBySubgenre(self):
        if self.collections is None:
            return {}
        pipeline = [
            {"$unwind": "$subgenre"},
            {"$group": {"_id": "$subgenre", "count": {"$sum": 1}}}
        ]
        return list(self.collections.aggregate(pipeline))

    def countByFormat(self):
        if self.collections is None:
            return {}
        pipeline = [
            {"$group": {"_id": "$format", "count": {"$sum": 1}}}
        ]
        return list(self.collections.aggregate(pipeline))

    def getFormats(self):
        if self.collections is None:
            return []
        return self.collections.distinct("format")

    def getGenres(self):
        if self.collections is None:
            return []
        return self.collections.distinct("genre")

    def getSubgenres(self):
        if self.collections is None:
            return []
        return self.collections.distinct("subgenre")

    def getLanguages(self):
        if self.collections is None:
            return []
        return self.collections.distinct("language")

    def getLevels(self):
        if self.collections is None:
            return []
        return self.collections.distinct("level")

    def getBooksByTitle(self, title: str):
        if self.collections is None:
            return []
        return list(self.collections.find(
            {"title": {"$regex": title, "$options": "i"}},
            {
                "_id": 0,
                "title": 1,
                "summary": 1,
                "subgenre": 1,
                "language": 1,
                "available": 1,
                "yearBook": 1,
                "synopsis": 1,
                "theme": 1,
                "totalPages": 1,
                "genre": 1,
                "level": 1,
                "format": 1,
                "fileExtension": 1,
                "anthology": 1
            }
        ))

    def getBooksByGenre(self, genre: str):
        if self.collections is None:
            return []
        return list(self.collections.find(
            {"genre": {"$regex": genre, "$options": "i"}},
            {
                "_id": 0,
                "title": 1,
                "summary": 1,
                "genre": 1,
                "subgenre": 1,
                "language": 1,
                "level": 1,
                "format": 1,
                "theme": 1,
                "yearBook": 1
            }
        ))

    def getBooksBySubgenre(self, subgenre: str):
        if self.collections is None:
            return []
        return list(self.collections.find(
            {"subgenre": {"$regex": subgenre, "$options": "i"}},
            {
                "_id": 0,
                "title": 1,
                "summary": 1,
                "subgenre": 1,
                "genre": 1,
                "language": 1,
                "level": 1,
                "format": 1,
                "theme": 1
            }
        ))

    def getBooksByLanguage(self, language: str):
        if self.collections is None:
            return []
        return list(self.collections.find(
            {"language": {"$regex": language, "$options": "i"}},
            {
                "_id": 0,
                "title": 1,
                "summary": 1,
                "language": 1,
                "genre": 1,
                "level": 1,
                "format": 1,
                "yearBook": 1
            }
        ))

    def getBooksByLevel(self, level: str):
        if self.collections is None:
            return []
        return list(self.collections.find(
            {"level": {"$regex": level, "$options": "i"}},
            {
                "_id": 0,
                "title": 1,
                "summary": 1,
                "level": 1,
                "genre": 1,
                "subgenre": 1,
                "language": 1,
                "format": 1,
                "yearBook": 1
            }
        ))

    def getBooksByTheme(self, theme: str):
        if self.collections is None:
            return []
        return list(self.collections.find(
            {"theme": {"$regex": theme, "$options": "i"}},
            {
                "_id": 0,
                "title": 1,
                "summary": 1,
                "theme": 1,
                "genre": 1,
                "subgenre": 1,
                "language": 1,
                "level": 1,
                "format": 1
            }
        ))

    def getIntelligenceBook(self, query: list[str], userLevel: str | None = None):
        """
        Busca libros usando texto completo o regex, filtrando por nivel si se pasa.
        """
        if self.collections is None:
            return []

        searchText = " ".join(query)
        matchText = {"$text": {"$search": searchText}}
        if userLevel:
            matchText["level"] = userLevel

        pipeline = [
            {"$match": matchText},
            {"$addFields": {"matchScore": {"$meta": "textScore"}}},
            {"$sort": {"matchScore": -1, "createdAt": -1}},
            {"$project": {
                "_id": 0,
                "title": 1,
                "summary": 1,
                "synopsis": 1,
                "subgenre": 1,
                "theme": 1,
                "genre": 1,
                "yearBook": 1,
                "language": 1,
                "available": 1,
                "level": 1,
                "format": 1,
                "fileExtension": 1,
                "totalPages": 1,
                "createdAt": 1,
                "updatedAt": 1,
                "matchScore": 1,
                "author": 1
            }}
        ]

        orderedBooks = list(self.collections.aggregate(pipeline))

        # fallback con regex si no hay resultados
        if not orderedBooks:
            regex = {"$regex": "|".join(query), "$options": "i"}
            regexMatch = {}
            if userLevel:
                regexMatch["level"] = userLevel

            pipeline = [
                {"$match": {
                    **regexMatch,
                    "$or": [
                        {"title": regex},
                        {"summary": regex},
                        {"synopsis": regex},
                        {"genre": regex},
                        {"theme": regex},
                        {"subgenre": regex}
                    ]
                }},
                {"$addFields": {"matchScore": 0.1}},
                {"$project": {
                    "_id": 0,
                    "title": 1,
                    "summary": 1,
                    "synopsis": 1,
                    "subgenre": 1,
                    "theme": 1,
                    "genre": 1,
                    "yearBook": 1,
                    "language": 1,
                    "available": 1,
                    "level": 1,
                    "format": 1,
                    "fileExtension": 1,
                    "totalPages": 1,
                    "createdAt": 1,
                    "updatedAt": 1,
                    "matchScore": 1,
                    "author": 1
                }},
                {"$sort": {"createdAt": -1}}
            ]
            orderedBooks = list(self.collections.aggregate(pipeline))

        return orderedBooks

    def getAllBooksByLevel(self, nivel: str):
        """
        Devuelve libros según jerarquía de nivel.
        """
        if self.collections is None:
            return []

        levelHierarchy = {
            "Inicial": ["Inicial"],
            "Secundario": ["Secundario", "Inicial"],
            "Joven Adulto": ["Joven Adulto", "Secundario", "Inicial"],
            "Adulto Mayor": ["Adulto Mayor", "Joven Adulto", "Secundario", "Inicial"]
        }

        allowedLevels = levelHierarchy.get(nivel, ["Inicial", "Secundario", "Joven Adulto", "Adulto Mayor"])

        return list(self.collections.find(
            {"level": {"$in": allowedLevels}},
            {
                "_id": 0,
                "title": 1,
                "summary": 1,
                "genre": 1,
                "subgenre": 1,
                "theme": 1,
                "language": 1,
                "level": 1,
                "format": 1,
                "yearBook": 1,
                "totalPages": 1
            }
        ).sort("createdAt", -1))

    def getBooksByFiltering(self, theme: list[str], subgenre: list[str], yearBook: list[str],
                            genre: list[str], format: list[str], level: str | None = None):
        """
        Filtra libros por múltiples criterios, con jerarquía de nivel.
        """
        if self.collections is None:
            return []

        levelHierarchy = {
            "inicial": ["Inicial"],
            "secundario": ["Secundario", "Inicial"],
            "joven adulto": ["Joven Adulto", "Secundario", "Inicial"],
            "adulto mayor": ["Adulto Mayor", "Joven Adulto", "Secundario", "Inicial"]
        }

        filters = {}
        if yearBook: filters["yearBook"] = {"$in": yearBook}
        if theme: filters["theme"] = {"$in": theme}
        if subgenre: filters["subgenre"] = {"$in": subgenre}
        if genre: filters["genre"] = {"$in": genre}
        if format: filters["format"] = {"$in": format}
        if level and levelHierarchy.get(level): filters["level"] = {"$in": levelHierarchy[level]}

        pipeline = []
        if filters:
            pipeline.append({"$match": filters})

        pipeline.append({"$sort": {"createdAt": -1}})
        pipeline.append({"$project": {
            "_id": 0,
            "title": 1,
            "summary": 1,
            "genre": 1,
            "subgenre": 1,
            "theme": 1,
            "language": 1,
            "level": 1,
            "format": 1,
            "yearBook": 1,
            "totalPages": 1
        }})

        return list(self.collections.aggregate(pipeline))


