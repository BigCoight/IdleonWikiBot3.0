from enum import Enum

from definitions.common.EnumMeta import CheckIn


class AFKType(str, Enum, metaclass = CheckIn):
	Catching = 'Catching'
	Mining = 'Mining'
	Error = 'Error'
	Fishing = 'Fishing'
	Nothing = 'Nothing'
	Fighting = 'Fighting'
	Choppin = 'Choppin'
	Cooking = "Cooking"
	Laboratory = "Laboratory"
