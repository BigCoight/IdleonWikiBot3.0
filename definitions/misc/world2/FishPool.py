from definitions.common.EnumMeta import CheckIn
from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class PoolType(str, IdleonEnum, metaclass = CheckIn):
	FishSmall = "FishSmall"
	FishMed = "FishMed"
	FishBig = "FishBig"


class FishPool(IdleonModel):
	fish: str
	expGiven: Integer
	damageDelt: Integer
	efficiency: Integer
	cardDrop: str
	cardChance: Numeric
	pool: PoolType
