from colorama import Fore, Style


def printGreen(txt: str) -> None:
	print(Fore.GREEN + txt + Style.RESET_ALL)


def printRed(txt: str) -> None:
	print(Fore.RED + txt + Style.RESET_ALL)


def printYellow(txt: str) -> None:
	print(Fore.YELLOW + txt + Style.RESET_ALL)


def printBlue(txt: str) -> None:
	print(Fore.BLUE + txt + Style.RESET_ALL)
