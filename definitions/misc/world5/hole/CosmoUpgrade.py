from enum import auto

from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class CosmoType(IdleonEnum):
	Hole = auto()
	Village = auto()
	Idleon = auto()


class CosmoUpgrade(IdleonModel):
	perLvl: Integer
	zero: Integer
	name: str
	desc: str
	cosmoType: CosmoType
