from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class NinjaInfo(IdleonModel):
	bossXoff: int
	bossYoff: Integer
	doorXoff: int
	baseDoorHp: int
	hatXoff: int
	hatYoff: int
	tiedXpos: int
	tiedFloor: int
	untiedQtyReq: Integer
	stealReq45: Numeric
	baseCoinPerAction: int
	baseXpPerAction: int
