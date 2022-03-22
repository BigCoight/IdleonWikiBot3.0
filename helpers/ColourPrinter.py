
from rich.console import Console

console = Console(color_system = "windows")


def printGreen(txt: str) -> None:
	console.print(txt, style = "green")


def printRed(txt: str) -> None:
	console.print(txt, style = "red")


def printYellow(txt: str) -> None:
	console.print(txt, style = "yellow")


def printBlue(txt: str) -> None:
	console.print(txt, style = "blue")


def printPurple(txt: str) -> None:
	console.print(txt, style = "purple")