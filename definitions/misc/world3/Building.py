from typing import List

from definitions.component.ComponentBase import ComponentBase
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class Building(IdleonModel):
	name: str
	description: str
	bonus: str
	lvlUpReq: List[ComponentBase]
	maxLvl: Integer
	costInc: Numeric
	bonusInc: List[Numeric]
	misc: Integer
