from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class PostOfficeUpgrade(IdleonModel):
	bonus: str
	x1: Numeric
	x2: Numeric
	func: str
	bonusKey: str
	investmentReq: Numeric


class PostOfficeUpgrades(IdleonModel):
	name: str
	bonuses: List[PostOfficeUpgrade]
	maxLevel: Numeric
