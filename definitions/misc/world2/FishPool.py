from enum import Enum

from definitions.common.EnumMeta import CheckIn
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class PoolType(str, Enum, metaclass=CheckIn):
	FishSmall = "FishSmall"
	FishMed = "FishMed"

class FishPool(IdleonModel):
	fish: str
	expGiven: Integer
	damageDelt: Integer
	efficiency: Integer
	cardDrop: str
	cardChance: Numeric
	pool: PoolType