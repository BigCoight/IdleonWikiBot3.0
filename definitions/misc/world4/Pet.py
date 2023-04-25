from definitions.master.IdleonModel import IdleonModel
from definitions.misc.world4.PetGene import PetGene
from definitions.misc.world4.PetStat import PetStat
from helpers.CustomTypes import Integer


class ShinyBonus(IdleonModel):
	shinyIndex: Integer
	shinyBonusDesc: str
	bonusPerLvl: Integer


class Pet(IdleonModel):
	stats: PetStat
	gene: PetGene
	shinyBonus: ShinyBonus
