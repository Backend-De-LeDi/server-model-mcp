from utils.centerLign import centerLog
from rich import print

class Log:
	@staticmethod
	def red(msg: str):
		print(f"\n ⛔ [red]{centerLog(msg)}[/red]\n")

	@staticmethod
	def green(msg: str):
		print(f"\n ✅ [green]{centerLog(msg)}[/green]\n")

	@staticmethod
	def magenta(msg: str):
		print(f"\n ❔ [magenta]{centerLog(msg)}[/magenta]\n")

	@staticmethod
	def yellow(msg: str):
		print(f"\n ⚠️ [yellow]{centerLog(msg)}[/yellow]\n")

	@staticmethod
	def blue(msg: str):
		print(f"\n 🛜 [blue]{centerLog(msg)}[/blue]\n")