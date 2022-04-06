import re
from typing import List

from definitions.itemdef.CardDropChance import CardDropChance
from helpers.HelperFunctions import reAll, strToArray
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
		#Enemies
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection()
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			rawDrops = re.findall(reDrops, droptables[i])
			for drop in rawDrops:
				if drop[0][:4] != "Card": continue
				cls.add(drop[0], CardDropChance(dropChance= drop[1]))

		#Fishies
		rePools = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reData = r'\[(?:"([^ ]*)", )?"([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		poolData = cls.getSection(1)
		fishPools = re.split(rePools, poolData)
		for i in range(0, len(fishPools) - 1, 2):
			rawData = re.findall(reData, fishPools[i])
			for i in range(4):
				cls.add(rawData[4][i], CardDropChance(dropChance = rawData[5][i]))

		#Dungeon Enemies
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reInner = fr'\[({reAll}*)\]'
		dungEnemy = re.split(reEnemies, cls.getSection(2))
		for i in range(0, len(dungEnemy) - 1, 2):
			data = re.findall(reInner, dungEnemy[i])
			dungData = strToArray(data[0])
			if dungEnemy[i + 1] not in CardRepo.nameToCard:
				continue
			cardName = CardRepo.nameToCard[dungEnemy[i + 1]]
			cls.add(cardName, CardDropChance(dropChance = dungData[7]))


		cls.addMissing()

	@classmethod
	def addMissing(cls):
		cls.add("CardsB14", CardDropChance(dropChance = 1))
