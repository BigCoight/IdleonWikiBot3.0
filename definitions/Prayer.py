from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class Prayer(IdleonModel):
	id: Integer
	bonus: str
	curse: str
	x1: Numeric
	x2: Numeric
	soul: str
	costMult: Integer
	unlockZone: str
	unlockWave: Integer
