from typing import List

from definitions.misc.world4.PetGene import PetGene
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class PetGeneRepo(Repository[PetGene]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/4"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["PetGenes"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for petGene in data:
			petGene[1] = int(petGene[1])
			cls.addList(PetGene.fromList(petGene))
			if cls.contains(petGene[0]): continue
			cls.add(petGene[0], PetGene.fromList(petGene))
