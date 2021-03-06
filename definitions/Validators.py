from helpers.HelperFunctions import scientificToInt


def validateInteger(v: str) -> int:
	if len(v) > 2 and v[-2] == "e" and v[-1].isnumeric():
		return scientificToInt(v)
	return int(v)
