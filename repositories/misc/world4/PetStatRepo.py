from typing import List

from definitions.misc.world4.PetStat import PetStat
from helpers.HelperFunctions import getFromSplitArray, getFromArrayArray, getFromSplit
from repositories.master.Repository import Repository


class PetStatRepo(Repository[PetStat]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/4"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["PetStats"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, world in enumerate(data):
			if n > 7: break
			for pet in world:
				petData = getFromSplit(pet) + [n]
				cls.addList(PetStat.fromList(petData))
				if cls.contains(petData[0]): continue
				cls.add(petData[0], PetStat.fromList(petData))
