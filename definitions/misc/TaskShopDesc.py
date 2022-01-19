from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class TaskShopDesc(IdleonModel):
	descLine1: str
	descLine2: str
	number1: Integer
	number2: Integer
	number3: Integer
	totalLevels: Integer
	meritCost: Integer
	text1: str
	text2: str
	extraStr: str
	icon: str
	bonusPerLevel: Integer