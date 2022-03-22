from typing import List

from definitions.dungeons.DungEnhance import DungEnhance, MiscUpgrade
from helpers.HelperFunctions import getFrom4dArray, replaceUnderscores
from repositories.master.Repository import Repository


class DungEnhanceRepo(Repository[DungEnhance]):

	@classmethod
	def getCategory(cls) -> str:
		return "Dungeon"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungEnhance"]

	@classmethod
	def generateRepo(cls) -> None:
		secNames = ["Weapon", "Armor", "Jewelery"]
		data = getFrom4dArray(cls.getSection())[0]
		for n, section in enumerate(data):
			temp = []
			for bonus in section:
				temp.append(MiscUpgrade(
					upgrade = replaceUnderscores(bonus[0]).title(),
					min = bonus[1],
					max = bonus[2]))
			cls.add(secNames[n], DungEnhance(
				enhancements = temp.copy()
			))
