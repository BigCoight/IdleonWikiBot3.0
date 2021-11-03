from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class ArcadeBonus(IdleonModel):
	effect: str
	x1: Numeric
	x2: Numeric
	func: str
	type: str
	lvlUpText: str
