from typing import List

from definitions.misc.world5.hole.CosmoUpgrade import CosmoUpgrade
from helpers.HelperFunctions import getFrom4dArray
from repositories.master.Repository import Repository


class CosmoUpgradeRepo(Repository[CosmoUpgrade]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["CosmoUpgrades"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFrom4dArray(cls.getSection())
		for n, colour in enumerate(data[0]):
			for upgrade in colour:
				upgrade.append(n + 1)
				cls.addList(CosmoUpgrade.fromList(upgrade))
				if cls.contains(upgrade[2]): continue
				cls.add(upgrade[2], CosmoUpgrade.fromList(upgrade))
