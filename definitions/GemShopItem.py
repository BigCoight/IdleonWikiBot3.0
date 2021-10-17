from pydantic import BaseModel

from helpers.CustomTypes import Integer


class GemShopItem(BaseModel):
	itemName: str
	desc: str
	cost: Integer
	no: Integer
	maxPurchases: Integer
	qty: Integer
	costIncrement: Integer
