from typing import List

from pydantic import BaseModel

from definitions.common.Component import Component
from helpers.CustomTypes import Numeric, Integer


class Building(BaseModel):
	description: str
	bonus: str
	lvlUpReq: List[Component]
	maxLvl: Integer
	costIncrement: List[Numeric]
	bonusInc: Numeric
	misc: Integer

