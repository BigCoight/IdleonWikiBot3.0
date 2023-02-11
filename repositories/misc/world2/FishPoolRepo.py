import re
from typing import List

from definitions.misc.world2.FishPool import FishPool
from helpers.HelperFunctions import formatStr, getFromArrayArray
from repositories.master.Repository import Repository


class FishPoolRepo(Repository[FishPool]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/2"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["FishPools"]

	@classmethod
	def generateRepo(cls) -> None:
		reDropTables = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		fishPoolData = formatStr(cls.getSection(), ["\n", "  "])
		for name, fishPool in re.findall(reDropTables, fishPoolData):
			pool = getFromArrayArray(fishPool)
			pool[3].insert(0, "0")
			for i in range(4):
				toAdd = FishPool(
					fish = pool[0][i],
					expGiven = pool[1][i],
					damageDelt = pool[2][i],
					efficiency = pool[3][i],
					cardDrop = pool[4][i],
					cardChance = pool[5][i],
					pool = name)
				cls.add(pool[0][i], toAdd)
				cls.addList(toAdd)
