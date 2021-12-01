from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class BossAttack(IdleonModel):
	name: str
	damage: Integer


class BossDetails(IdleonModel):
	health: Integer
	defence: Integer
	exp: Integer
	keys: Integer
	attacks: List[BossAttack]
