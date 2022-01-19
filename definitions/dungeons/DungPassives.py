from typing import List

from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class DungPassive(IdleonModel):
	effect: str
	x1: Numeric
	x2: Numeric
	func: str
	type: str
	lvlUpText: str


class DungPassives(IdleonModel):
	passives: List[DungPassive]
