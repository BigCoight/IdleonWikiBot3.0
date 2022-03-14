from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class Meal(IdleonModel):
	name: str
	x1: Numeric
	x2: Numeric
	bonusText: str
	description: str
	bonusKey: str
