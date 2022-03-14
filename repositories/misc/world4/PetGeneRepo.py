from typing import List

from definitions.misc.world4.PetGene import PetGene
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class PetGeneRepo(Repository[PetGene]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["PetGenes"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bonus in data:
			cls.addList(PetGene.fromList(bonus))
			if cls.contains(bonus[0]): continue
			cls.add(bonus[0], PetGene.fromList(bonus))
