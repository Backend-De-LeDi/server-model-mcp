from configs.db.connection import Connection
from configs.env.env import Env
from pymongo.collection import Collection
from bson import ObjectId

class UserService:
    def __init__(self):
        status, database = Connection().getConnection(Env.getEnv("MONGO_URL"))
        self.collections: Collection | None = database["users"] if status else None

    def getUserPreferences(self, user_id: str):
        """
        Devuelve solo las preferencias del usuario (categoría y formato),
        ignorando campos sensibles.
        """
        if self.collections is None:
            return None
        return self.collections.find_one(
            {"_id": ObjectId(user_id)},
            {
                "_id": 0,
                "preference.category": 1,
                "preference.format": 1
            }
        )