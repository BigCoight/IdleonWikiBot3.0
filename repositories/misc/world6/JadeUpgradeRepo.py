from typing import List

from definitions.misc.world6.JadeUpgrade import JadeUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class JadeUpgradeRepo(Repository[JadeUpgrade]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["JadeUpgrades"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(JadeUpgrade.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], JadeUpgrade.fromList(line))
