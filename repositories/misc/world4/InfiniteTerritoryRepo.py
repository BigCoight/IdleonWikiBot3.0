from typing import List

from definitions.misc.world4.InfiniteTerritory import InfiniteTerritory
from definitions.misc.world4.TerritoryEnemy import TerritoryEnemy
from definitions.misc.world4.TerritoryFight import TerritoryFight
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class InfiniteTerritoryRepo(Repository[InfiniteTerritory]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TerrINF"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, bonus in enumerate(data):
			enemies = []
			for i in range(5):
				dataStart = i*4
				dataEnd = dataStart + 4
				enemyData = bonus[dataStart:dataEnd]
				enemies.append(TerritoryEnemy.fromList(enemyData))
			toAdd = InfiniteTerritory(enemies = enemies.copy())
			cls.add(f"{n}", toAdd)
			cls.addList(toAdd)

