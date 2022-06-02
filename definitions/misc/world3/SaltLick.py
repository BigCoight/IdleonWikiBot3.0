from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class SaltLick(IdleonModel):
	item: str
	desc: str
	baseCost: Integer
	increment: Numeric
	maxLevel: Integer
	baseBonus: Numeric
