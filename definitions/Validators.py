from helpers.HelperFunctions import scientificToInt


def validateInteger(v: str) -> int:
	if not v.isnumeric():
		return -1
	return scientificToInt(v)