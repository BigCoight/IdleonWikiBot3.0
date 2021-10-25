from typing import List

from definitions.dungeons.DungItem import DungItem
from helpers.Constants import Constants
from helpers.HelperFunctions import getFromSplitArray, getFromArrayArray
from repositories.AchievementRepo import AchievementRepo
from repositories.master.ListRepository import ListRepository


class DungItemRepo(ListRepository[DungItem]):
	"""
	Depends on AchievementRepo
	"""

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
			cls.add(DungItem(
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
			))

	@classmethod
	def getCorrespondingAchieve(cls, n):
		if n == 0:
			return ""
		if n == -1:
			return "Unobtainable"
		return AchievementRepo.get(n).name
