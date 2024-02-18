from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class SummonUnit(IdleonModel):
	height: int
	speed: Numeric
	colRadius: int
	qtyText: int
	minQty: int
	maxQty: int
	baseCost: int
	baseHp: int
	baseDamage: Numeric
