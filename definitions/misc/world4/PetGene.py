from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class PetGene(IdleonModel):
	name: str
	x1: Numeric
	x2: Numeric
	lowerLetter: str
	upperLetter: str
	description: str
	combatDescription: str
