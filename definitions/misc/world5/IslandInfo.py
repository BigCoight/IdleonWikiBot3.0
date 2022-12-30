from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class IslandInfo(IdleonModel):
	name: str
	distance: int
	relic1: int
	relic2: int
	relic3: int
	unlockQty: int
	cloudsUnlocked: Numeric
	xYPointer: str
	expPerTrip: int
	artifactsPerIsland: int
