from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class WeeklyShopSection(IdleonEnum):
	UI = "UI"
	Items = "Items"


class WeeklyShop(IdleonModel):
	name: str
	section: WeeklyShopSection
	cost: Numeric
	intName: str
	desc: str
	itemType: Integer
