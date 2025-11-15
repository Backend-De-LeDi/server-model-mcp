import shutil

def centerLog(msg: str) -> str:
	ancho = shutil.get_terminal_size().columns
	return msg.center(ancho)