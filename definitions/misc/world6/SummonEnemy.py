from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from definitions.misc.world6.SummonEnemyBonus import SummonEnemyBonus
from helpers.CustomTypes import Integer


class SummonEnemy(IdleonModel):
	enemyId: str
	xOff: Integer
	yOff: int
	width: int
	territoryName: str
	bonusId: int | str
	bonus: Optional[SummonEnemyBonus]
	bonusQty: int | str
	difficulty: int | str
