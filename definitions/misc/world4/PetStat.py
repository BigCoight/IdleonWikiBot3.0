from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class PetStat(IdleonModel):
	petId: str
	x1: Numeric
	x2: Numeric
	x3: Numeric
	x4: Numeric
	unlockOrder: Numeric
	world: Integer
