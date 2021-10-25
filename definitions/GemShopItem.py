from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class GemShopItem(IdleonModel):
	itemName: str
	desc: str
	cost: Integer
	no: Integer
	maxPurchases: Integer
	qty: Integer
	costIncrement: Integer
