from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class PetUpgrade(IdleonModel):
	upgradeName: str
	filler: str
	material: str
	cost: Numeric
	baseMatCost: Numeric
	costMatScale: Numeric
	baseCost: Numeric
	costScale: Numeric
	maxLevel: Integer
	description: str
	boostEffect: str
	bonusQty: Numeric
