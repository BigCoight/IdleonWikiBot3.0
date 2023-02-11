import re
from typing import List

from definitions.dungeons.DungEnemy import DungEnemy
from helpers.HelperFunctions import strToArray
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.master.Repository import Repository


class DungEnemyRepo(Repository[DungEnemy]):

	@classmethod
	def getCategory(cls) -> str:
		return "Dungeon"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		EnemyDetailsRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungEnemies"]

	@classmethod
	def generateRepo(cls) -> None:
		reEnemies = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		dungEnemy = re.findall(reEnemies, cls.getSection())
		for enemy in dungEnemy:
			dungData = strToArray(enemy[1])
			cls.add(enemy[0], DungEnemy(
				intName = enemy[0],
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
