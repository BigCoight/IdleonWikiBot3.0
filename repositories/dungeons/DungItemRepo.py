from typing import List

from definitions.dungeons.DungItem import DungItem
from helpers.Constants import Constants
from helpers.HelperFunctions import getFromSplitArray, getFromArrayArray
from repositories.misc.AchievementRepo import AchievementRepo
from repositories.master.Repository import Repository


class DungItemRepo(Repository[DungItem]):
	"""
	Depends on AchievementRepo
	"""

	@classmethod
	def getCategory(cls) -> str:
		return "Dungeon"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		AchievementRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungItems", "UnlockRNG"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		achieveUn = getFromArrayArray(cls.getSection(1))[0]
		rarity = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
		for n, item in enumerate(data):
			worldIndex = int(achieveUn[n]) // 70
			world = Constants.worlds[worldIndex]
			addition = DungItem(
				name = item[0],
				bonus = item[1],
				increment = item[2],
				rarity = rarity[int(item[3])],
				desc = item[4],
				lvlText = item[5],
				baseValue = item[6],
				maxLevel = item[7],
				achieve = cls.getCorrespondingAchieve(int(achieveUn[n])),
				world = world
			)
			cls.add(item[0], addition)
			cls.addList(addition)


	@classmethod
	def getCorrespondingAchieve(cls, n: int):
		if n == 0:
			return ""
		if n == -1:
			return "Unobtainable"
		return AchievementRepo.getList(n).name
