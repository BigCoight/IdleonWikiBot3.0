from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class SummonUpgrade(IdleonModel):
	screenX: int
	screenY: int
	colour: int
	name: str
	cost: int
	costExponent: Numeric
	bonusQty: int
	summonLvlReq: int
	maxLvl: int
	idReq: int
	filler: str
	bonus: str
