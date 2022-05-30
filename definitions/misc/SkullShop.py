from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class SkullShop(IdleonModel):
	description: str
	baseCost: Integer
	costInc: Integer
	rewardId: str
	qty: Integer
