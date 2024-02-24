from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class MarketInfo(IdleonModel):
	name: str
	bonus: str
	cropId: int
	cropIdIncrement: Numeric
	cost: int
	costExponent: Numeric
	cropReq: int
	maxLvl: int
	bonusPerLvl: Numeric
