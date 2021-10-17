from typing import List

from pydantic import BaseModel

from helpers.CustomTypes import Integer


class BossAttack(BaseModel):
	name: str
	damage: Integer


class BossDetails(BaseModel):
	health: Integer
	defence: Integer
	exp: Integer
	keys: Integer
	attacks: List[BossAttack]
