from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class GodInfo(IdleonModel):
	name: str
	majorBonus: str
	passiveBonus: str
	passiveMax: int
	blessingBaseCost: int
	blessingIncrement: Numeric
	blessingBonus: str
	preUnlockMessage: str
	x: int
	y: int
	linkX: int
	linkY: int
	hueAdjust: int
	bonusIndex: int
	blessingPerLevel: int
