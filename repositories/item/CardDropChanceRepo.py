import re
from typing import List

from definitions.itemdef.CardDropChance import CardDropChance
from repositories.master.Repository import Repository


class CardDropChanceRepo(Repository[CardDropChance]):

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["EnemyDropTables", "FishPools"]

	@classmethod
	def generateRepo(cls) -> None:
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection()
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			intName = droptables[i + 1]
			rawDrops = re.findall(reDrops, droptables[i])
			for drop in rawDrops:
				if drop[0][:4] != "Card": continue
				cls.add(drop[0], CardDropChance(dropChance= drop[1]))

		rePools = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reData = r'\[(?:"([^ ]*)", )?"([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		poolData = cls.getSection(1)
		fishPools = re.split(rePools, poolData)
		for i in range(0, len(fishPools) - 1, 2):
			rawData = re.findall(reData, fishPools[i])
			for i in range(4):
				cls.add(rawData[4][i], CardDropChance(dropChance = rawData[5][i]))

		cls.addMissing()

	@classmethod
	def addMissing(cls):
		cls.add("CardsB14", CardDropChance(dropChance = 1))
