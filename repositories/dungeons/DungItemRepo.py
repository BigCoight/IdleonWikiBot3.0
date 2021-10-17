from typing import List

from definitions.dungeons.DungItem import DungItem
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.ListRepository import ListRepository


class DungItemRepo(ListRepository[DungItem]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungItems"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		rarity = ["Common", "Uncommon", "Rare", "Epic", "Legendary"]
		for item in data:
			cls.add(DungItem(
				name = item[0],
				bonus = item[1],
				increment = item[2],
				rarity = rarity[int(item[3])],
				desc = item[4],
				lvlText = item[5],
				baseValue = item[6],
				maxLevel = item[7]
			))
