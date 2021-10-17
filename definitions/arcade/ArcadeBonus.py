from pydantic import BaseModel

from helpers.CustomTypes import Numeric


class ArcadeBonus(BaseModel):
	effect: str
	x1: Numeric
	x2: Numeric
	func: str
	type: str
	lvlUpText: str
