from typing import List

from pydantic import BaseModel, validator

from definitions.Validators import validateInteger


class BossAttack(BaseModel):
	name: str
	damage: int
	_convertInts = validator("damage", pre = True, allow_reuse = True)(validateInteger)


class BossDetails(BaseModel):
	health: int
	defence: int
	exp: int
	keys: int
	attacks: List[BossAttack]

	_convertInts = validator("health", "defence", "exp", pre = True, allow_reuse = True)(validateInteger)
