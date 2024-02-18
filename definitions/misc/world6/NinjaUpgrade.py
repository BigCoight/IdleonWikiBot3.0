from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class NinjaUpgrade(IdleonModel):
	screenX: int
	screenY: int
	width: int
	height: int
	name: str
	bonusPerLvl: int | str
	bonus: str
	costBase: Integer
	costExponent: Numeric
	unlockId: int
	iconX: int
	iconY: int
