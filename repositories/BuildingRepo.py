from definitions.Building import Building
from definitions.common.Component import Component
from helpers.HelperFunctions import getFromSplitArray
from repositories.Repository import Repository
from typing import List


class BuildingRepo(Repository[Building]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["BuildingData"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for building in data:
			costs = [
				Component(item = building[4], quantity = building[6]),
				Component(item = building[5], quantity = building[7])
			]
			desc = building[1].split("@ Current Bonuses: @")
			if len(desc) < 2:
				continue
			cls.add(building[0], Building(
				description = desc[0],
				bonus = desc[1],
				lvlUpReq = costs,
				maxLvl =building[8],
				costIncrement = building[2:4],
				bonusInc =building[9],
				misc =building[10],

			))
