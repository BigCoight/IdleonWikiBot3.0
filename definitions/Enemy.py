from typing import List, Tuple

from pydantic import BaseModel, validator

from definitions.Validators import validateInteger
from definitions.common.Drop import Drop


class Enemy(BaseModel):
    Name: str
    AFKtype: str
    MonsterFace: int
    MonsterOffsetX: int
    MonsterOffsetY: int
    HeightOfMonster: int
    MonsterMoving: int
    MovingFrame: int
    RespawnTime: int
    DeathFrame: int
    MonsterHPTotal: int
    Type: str
    SpecialType: str
    ExpGiven: int
    ExpType: int
    Defence: int
    MoveSPEED: int
    Damages: Tuple[int, int]
    Drops: List[Drop]

    _intValidator = validator("ExpGiven", "Defence", "RespawnTime", "MonsterHPTotal",  allow_reuse = True,
                              pre = True)(validateInteger)

    @validator("Damages", each_item = True, pre = True)
    def valDamages(cls, v: str) -> int:
        return validateInteger(v)
