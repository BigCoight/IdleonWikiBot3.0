from pydantic import BaseModel


class GemShopItem(BaseModel):
	itemName: str
	desc: str
	cost: int
	no: int
	maxPurchases: int
	qty: int
	costIncrement: int
