from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class PetUpgrade(IdleonModel):
	upgradeName: str
	filler: str
	material: str
	x1: Numeric
	baseCost: Numeric
	costScale: Numeric
	baseCost2: Numeric
	costScale2: Numeric
	maxLevel: Integer
	description: str
	boostEffect: str
	x2: Numeric
