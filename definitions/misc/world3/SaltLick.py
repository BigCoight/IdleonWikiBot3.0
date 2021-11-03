from pydantic import BaseModel

from helpers.CustomTypes import Numeric, Integer


class SaltLick(BaseModel):
	item: str
	desc: str
	baseCost: Integer
	increment: Numeric
	baseBonus: Numeric
	maxLevel: Integer
