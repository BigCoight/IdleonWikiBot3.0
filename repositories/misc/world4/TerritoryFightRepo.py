from typing import List

from definitions.misc.world4.TerritoryEnemy import TerritoryEnemy
from definitions.misc.world4.TerritoryFight import TerritoryFight
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class TerritoryFightRepo(Repository[TerritoryFight]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/4"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TerrInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bonus in data:
			enemies = []
			for i in range(5):
				dataStart = 8 + i*4
				dataEnd = dataStart + 4
				enemyData = bonus[dataStart:dataEnd]
				enemies.append(TerritoryEnemy.fromList(enemyData))
			toAdd = TerritoryFight(
				img =bonus[0],
				trekReq =bonus[1],
				fightPower =bonus[2],
				enemyAttack =bonus[3],
				battleName =bonus[4],
				filler1 =bonus[5],
				filler2 =bonus[6],
				filler3 =bonus[7],
				enemies = enemies.copy())
			if cls.contains(bonus[4]) or bonus[4] == "FILLER_FILLER_FILLER": continue
			cls.add(bonus[4], toAdd)
			cls.addList(toAdd)

