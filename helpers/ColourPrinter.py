from colorama import Fore, Style


def printGreen(txt: str) -> None:
	print(Fore.GREEN + txt + Style.RESET_ALL)


def printRed(txt: str) -> None:
	print(Fore.RED + txt + Style.RESET_ALL)
