from pymongo import MongoClient

class Connection:
	_instancia = None

	def __new__(cls):
		if cls._instancia is None:
			cls._instancia = super(Connection, cls).__new__(cls)
			cls._instancia.cliente = None  
		return cls._instancia

	def getConnection(self, url: str) -> tuple[bool, MongoClient | None]:
		if self.cliente is not None:
			return True, self.cliente
		try:
			self.cliente = MongoClient(url)
			return True, self.cliente
		except Exception as error:
			print(error)
			return False, None