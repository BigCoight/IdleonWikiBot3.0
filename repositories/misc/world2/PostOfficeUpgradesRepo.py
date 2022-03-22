from typing import List

from definitions.postoffice.PostOfficeUpgrades import PostOfficeUpgrades, PostOfficeUpgrade
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class PostOfficeUpgradesRepo(Repository[PostOfficeUpgrades]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/2"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["PostOfficeUpgrades"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for box in data:
			upgrades = []
			for i in range(3):
				upgrades.append(
					PostOfficeUpgrade(
						bonus = box[i * 4 + 4],
						x1 = box[i * 4 + 1],
						x2 = box[i * 4 + 2],
						func = box[i * 4 + 3])
				)
			cls.add(box[0], PostOfficeUpgrades(
				name = box[0],
				bonuses = upgrades.copy()))
