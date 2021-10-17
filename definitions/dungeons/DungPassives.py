from typing import List

from pydantic import BaseModel

from helpers.CustomTypes import Numeric


class DungPassive(BaseModel):
	effect: str
	x1: Numeric
	x2: Numeric
	func: str
	type: str
	lvlUpText: str


class DungPassives(BaseModel):
	passives: List[DungPassive]
