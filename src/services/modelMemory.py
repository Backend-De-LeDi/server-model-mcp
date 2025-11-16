from configs.db.connection import Connection
from configs.env.env import Env
from datetime import datetime, timezone
from pymongo.collection import Collection
from utils.serializeDocument import serializeDocument

class MemoryService:
    def __init__(self):
        status, database = Connection().getConnection(Env.getEnv("MONGO_URL"))
        self.collections: Collection | None = database["vectorMemorys"] if status else None


    def getMemory(self, idUser: str):
        if self.collections is None:
            return []

        query = {
            "userId": idUser,
        }

        result = list(self.collections.find(query))

        return [serializeDocument(doc) for doc in result]

    def saveMemory(self, userId: str, sessionId: str, role: str, content: str):
        if self.collections is None:
            return False

        query = {
            "userId": userId,
            "sessionId": sessionId
        }

        update = {
            "$push": {
                "content": {
                    "role": role,
                    "text": content
                }
            },
            "$setOnInsert": {
                "timestamp": datetime.now(timezone.utc)
            }
        }

        result = self.collections.update_one(query, update, upsert=True)
        return result.upserted_id or "updated"

    def getMemoryBySession(self, sessionId: str):
        if self.collections is None:
            return []

        query = {
            "sessionId": sessionId
        }

        result = list(self.collections.find(query))
        return [serializeDocument(doc) for doc in result]

    def getMemoryByUserAndSession(self, userId: str, sessionId: str):
        if self.collections is None:
            return []

        query = {
            "userId": userId,
            "sessionId": sessionId
        }

        result = list(self.collections.find(query))
        return [serializeDocument(doc) for doc in result]