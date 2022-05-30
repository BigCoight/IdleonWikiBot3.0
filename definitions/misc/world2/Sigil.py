from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class Sigil(IdleonModel):
	name: str
	unlockCost: Integer
	boostCost: Integer
	unlockBonus: Numeric
	boostBonus: Numeric
	filler: str
	desc: str
