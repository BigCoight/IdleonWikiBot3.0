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
			toAdd = SummonEnemy(
				enemyId = data[0][i],
				damage = data[1][i],
				health = data[2][i],
				x4 = data[3][i],
				territoryName = replaceUnderscores(data[4][i]),
				bonusId = data[5][i],
				bonus = SummonEnemyBonusRepo.getList(int(data[5][i]) - 1) if data[5][i] != "_" else None,
				x8 = data[7][i],
				x9 = data[8][i],
			)
			cls.addList(toAdd)
			if cls.contains(toAdd.enemyId): continue
			cls.add(toAdd.enemyId, toAdd)
