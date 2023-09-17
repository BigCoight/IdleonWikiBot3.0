from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class WeeklyShop(IdleonModel):
	name: str
	cost: Numeric
	intName: str
	desc: str
	itemType: Integer
