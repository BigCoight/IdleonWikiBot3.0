from pydantic import BaseModel

from helpers.CustomTypes import Numeric


class SaltLick(BaseModel):
	item: str
	desc: str
	baseCost: int
	increment: Numeric
	baseBonus: Numeric
	maxLevel: int
