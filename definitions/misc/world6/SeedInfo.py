from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class SeedInfo(IdleonModel):
	name: str
	seedId: int
	cropIdMin: int
	cropIdMax: int
	lvlReq: int
	nextCropChance: Numeric
	nextCropDecay: Numeric
