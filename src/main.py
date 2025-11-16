from fastapi import FastAPI
import uvicorn
from configs.env.env import Env
from configs.db.connection import Connection
from utils.logers import Log
from routers.chatBotRouter import ChatBotRouter
from routers.memoryRouter import MemoryRouter

app = FastAPI()
chatBotRouters = ChatBotRouter()
memoryRouter = MemoryRouter()

app.include_router(chatBotRouters.router)
app.include_router(memoryRouter.router)

connectionMongo = Connection()

port = int(Env.getEnv(key="PORT"))

mongo_url = Env.getEnv(key="MONGO_URL")


if(__name__=="__main__"):

	ok, cliente = connectionMongo.getConnection(mongo_url)

	if ok:
		Log.blue("Conexión Mongo OK")
	
	else:
		Log.red("Error de conexión")

	uvicorn.run("main:app",host="0.0.0.0",port=port,reload=True)