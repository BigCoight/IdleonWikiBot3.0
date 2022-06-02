from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class SaltLick(IdleonModel):
	item: str
	desc: str
	baseCost: Integer
	baseBonus: Numeric
	maxLevel: Integer
	costInc: Numeric
