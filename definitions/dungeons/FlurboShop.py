from pydantic import BaseModel

from helpers.CustomTypes import Integer


class FlurboShop(BaseModel):
	cost: Integer
	noPurchases: Integer
	displayName: str
	description: str
