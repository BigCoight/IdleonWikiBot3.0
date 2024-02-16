from typing import List

from definitions.misc.world6.NinjaUpgrade import NinjaUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class NinjaUpgradeRepo(Repository[NinjaUpgrade]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["NinjaUpgrades"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(NinjaUpgrade.fromList(line))
			if cls.contains(line[4]): continue
			cls.add(line[4], NinjaUpgrade.fromList(line))
