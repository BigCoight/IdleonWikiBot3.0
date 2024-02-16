from typing import List

from definitions.misc.world6.SummonEnemyBonus import SummonEnemyBonus
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class SummonEnemyBonusRepo(Repository[SummonEnemyBonus]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SummonEnemies"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection(), replaceUnderscores = False)
		numBonuses = len(data[6])

		for i in range(numBonuses):
			toAdd = SummonEnemyBonus(
				bonusId = i + 1,
				bonus = replaceUnderscores(data[6][i])
			)
			cls.addList(toAdd)
			if cls.contains(f"{toAdd.bonusId}"): continue
			cls.add(f"{toAdd.bonusId}", toAdd)
