from typing import List

from definitions.misc.world6.SummonUpgrade import SummonUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class SummonUpgradeRepo(Repository[SummonUpgrade]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SummonUpgrades"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(SummonUpgrade.fromList(line))
			if cls.contains(line[3]): continue
			cls.add(line[3], SummonUpgrade.fromList(line))
