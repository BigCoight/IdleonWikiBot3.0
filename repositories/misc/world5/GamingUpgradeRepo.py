from typing import List

from definitions.misc.world5.GamingUpgrade import GamingUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GamingUpgradeRepo(Repository[GamingUpgrade]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GamingUpgrades"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(GamingUpgrade.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], GamingUpgrade.fromList(line))
