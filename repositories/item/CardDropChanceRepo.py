import re
from typing import List

from definitions.itemdef.CardDropChance import CardDropChance
from helpers.HelperFunctions import strToArray, formatStr, getFromArrayArray
from repositories.item.CardRepo import CardRepo
from repositories.master.Repository import Repository


class CardDropChanceRepo(Repository[CardDropChance]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		CardRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["EnemyDropTables", "FishPools", "DungEnemies"]

	@classmethod
	def generateRepo(cls) -> None:
		# Enemies
		reDropTables = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		droptableData = formatStr(cls.getSection(), ["\n", "  "], replaceUnderscores = False)
		for name, dt in re.findall(reDropTables, droptableData):
			drops = getFromArrayArray(dt, repU = False)
			for drop in drops:
				if drop[0][:4] != "Card": continue
				cls.add(drop[0], CardDropChance(dropChance = drop[1]))

		# Fishies
		reDropTables = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		fishPoolData = formatStr(cls.getSection(1), ["\n", "  "])
		for name, fishPool in re.findall(reDropTables, fishPoolData):
			pool = getFromArrayArray(fishPool)
			pool[3].insert(0, "0")
			for i in range(4):
				cls.add(pool[4][i], CardDropChance(dropChance = pool[5][i]))

		# Dungeon Enemies
		reEnemies = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		dungEnemy = re.findall(reEnemies, cls.getSection(2))
		for enemy, data in dungEnemy:
			dungData = strToArray(data)
			if enemy not in CardRepo.nameToCard:
				continue
			cardName = CardRepo.nameToCard[enemy]
			cls.add(cardName, CardDropChance(dropChance = dungData[7]))
		cls.addMissing()

	@classmethod
	def addMissing(cls):
		cls.add("CardsB14", CardDropChance(dropChance = 1))
