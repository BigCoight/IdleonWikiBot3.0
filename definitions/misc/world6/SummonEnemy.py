from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from definitions.misc.world6.SummonEnemyBonus import SummonEnemyBonus
from helpers.CustomTypes import Integer


class SummonEnemy(IdleonModel):
	enemyId: str
	damage: Integer
	health: int
	x4: int
	territoryName: str
	bonusId: int | str
	bonus: Optional[SummonEnemyBonus]
	x8: int | str
	x9: int | str
