from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class BossAttack(IdleonModel):
	name: str
	damage: Integer

	def shouldCompare(self) -> bool:
		return False

	def __str__(self) -> str:
		return f"{self.name} {self.damage}"


class BossDetails(IdleonModel):
	health: Integer
	defence: Integer
	exp: Integer
	keys: Integer
	attacks: List[BossAttack]
