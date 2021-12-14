import re
from typing import List

from definitions.dungeons.DungEnemy import DungEnemy
from helpers.HelperFunctions import reAll, strToArray
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.master.Repository import Repository


class DungEnemyRepo(Repository[DungEnemy]):

	@classmethod
	def initDependencies(cls) -> None:
		EnemyDetailsRepo.initialise(cls.codeReader)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungEnemies"]

	@classmethod
	def generateRepo(cls) -> None:
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reInner = fr'\[({reAll}*)\]'
		dungEnemy = re.split(reEnemies, cls.getSection())
		for i in range(0, len(dungEnemy) - 1, 2):
			data = re.findall(reInner, dungEnemy[i])
			dungData = strToArray(data[0])
			cls.add(dungEnemy[i + 1], DungEnemy(
				intName = dungEnemy[i + 1],
				health = dungData[0],
				damage = dungData[1],
				credit1DR = dungData[2],
				credit2DR = dungData[3],
				cardVal = dungData[4],
				coins = dungData[5],
				itemDropChance = dungData[6],
				cardDropChance = dungData[7],
			))

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return EnemyDetailsRepo.getWikiName(name)
