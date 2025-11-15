from dotenv import load_dotenv
import os

load_dotenv()

class Env:
	
	@staticmethod
	def getEnv(key:str):
		return os.getenv(key)
