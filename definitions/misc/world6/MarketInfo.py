from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class MarketInfo(IdleonModel):
	name: str
	bonus: str
	x1: int
	x2: Numeric
	x3: int
	x4: Numeric
	x5: int
	x6: int
	x7: int
