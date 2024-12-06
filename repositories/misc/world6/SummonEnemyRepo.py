from typing import List

from definitions.misc.world6.SummonEnemy import SummonEnemy
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository
from repositories.misc.world6.SummonEnemyBonusRepo import SummonEnemyBonusRepo


class SummonEnemyRepo(Repository[SummonEnemy]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		SummonEnemyBonusRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SummonEnemies"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection(), replaceUnderscores = False)
		numEnemies = len(data[1])

		for i in range(numEnemies):
			# Some enemies (namely endless summoning battles enemies) don't have bonus information.
			# So add them with dummy bonus information.
			if i >= len(data[5]):
				toAdd = SummonEnemy(
					enemyId = data[0][i],
					xOff = data[1][i],
					yOff = data[2][i],
					width = data[3][i],
					territoryName = replaceUnderscores(data[4][i]),
					bonusId = 0,
					bonus = None,
					bonusQty = 0,
					difficulty = 0,
				)
			else:
				toAdd = SummonEnemy(
					enemyId = data[0][i],
					xOff = data[1][i],
					yOff = data[2][i],
					width = data[3][i],
					territoryName = replaceUnderscores(data[4][i]),
					bonusId = data[5][i],
					bonus = SummonEnemyBonusRepo.getList(int(data[5][i]) - 1) if data[5][i] != "_" else None,
					bonusQty = data[7][i],
					difficulty = data[8][i],
				)
			cls.addList(toAdd)
			if cls.contains(toAdd.enemyId): continue
			cls.add(toAdd.enemyId, toAdd)
