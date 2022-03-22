from typing import List

from definitions.misc.world4.PetUpgrade import PetUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class PetUpgradeRepo(Repository[PetUpgrade]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/4"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["PetUpgrade"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bonus in data:
			cls.addList(PetUpgrade.fromList(bonus))
			if cls.contains(bonus[0]): continue
			cls.add(bonus[0], PetUpgrade.fromList(bonus))
