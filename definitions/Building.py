from typing import List

from pydantic import BaseModel

from definitions.common.Component import Component
from helpers.CustomTypes import Numeric


class Building(BaseModel):
	description: str
	bonus: str
	lvlUpReq: List[Component]
	maxLvl: int
	costIncrement: List[Numeric]
	bonusInc: Numeric
	misc: int

