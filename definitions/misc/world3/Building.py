from typing import List

from definitions.common.Component import Component
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class Building(IdleonModel):
	name: str
	description: str
	bonus: str
	lvlUpReq: List[Component]
	maxLvl: Integer
	costInc: Numeric
	bonusInc: List[Numeric]
	misc: Integer
