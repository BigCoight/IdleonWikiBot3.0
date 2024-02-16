from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class SeedInfo(IdleonModel):
	name: str
	seedId: int
	x1: int
	x2: int
	x3: int
	x5: Numeric
	x6: Numeric
