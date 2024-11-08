from definitions.common.EnumMeta import CheckIn
from definitions.master.IdleonEnum import IdleonEnum


class AFKType(str, IdleonEnum, metaclass = CheckIn):
	Catching = 'Catching'
	Mining = 'Mining'
	Error = 'Error'
	Fishing = 'Fishing'
	Nothing = 'Nothing'
	Fighting = 'Fighting'
	Choppin = 'Choppin'
	Cooking = "Cooking"
	Laboratory = "Laboratory"
	Divinity = "Divinity"
	PayingRespect = "Paying Respect"
