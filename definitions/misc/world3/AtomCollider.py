from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class AtomCollider(IdleonModel):
	name: str
	growthFactor: int
	baseExponent: Numeric
	baseCost: int
	bonusPerLv: int
	desc: str
