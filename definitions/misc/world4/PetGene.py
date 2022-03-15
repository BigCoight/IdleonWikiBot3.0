from enum import Enum

from definitions.common.EnumMeta import CheckIn
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer

class AbilityType(Enum, metaclass=CheckIn):
	Red = 0
	Green = 1
	Special = 2


class PetGene(IdleonModel):
	name: str
	abilityType: AbilityType
	x2: Numeric
	lowerLetter: str
	upperLetter: str
	description: str
	combatDescription: str
