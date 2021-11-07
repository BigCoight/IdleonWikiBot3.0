from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class GuildBonus(IdleonModel):
	name: str
	xPos: Integer
	yPos: Integer
	bonus: str
	x1: Numeric
	x2: Numeric
	func: str
	maxLevel: Integer
	reqIndex: Integer
	reqLevel: Integer
	gpBaseCost: Integer
	gpIncrease: Integer
