from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class SaltLick(IdleonModel):
	item: str
	desc: str
	baseCost: Integer
	increment: Numeric
	baseBonus: Numeric
	maxLevel: Integer
