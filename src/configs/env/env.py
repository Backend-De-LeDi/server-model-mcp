from dotenv import load_dotenv
import os
from utils.logers import Log

ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
ENV_PATH = os.path.join(ROOT_PATH, ".env")
load_dotenv(dotenv_path=ENV_PATH)

class Env:
    @staticmethod
    def getEnv(key: str) -> str:
        value = os.getenv(key)
        if value is None:
            raise EnvironmentError(Log.red(f"Variable de entorno '{key}' no encontrada."))
        return value