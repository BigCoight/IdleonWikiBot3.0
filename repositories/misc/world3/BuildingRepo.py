from typing import List

from definitions.misc.world3.Building import Building
from definitions.common.Component import Component
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class BuildingRepo(Repository[Building]):

	@classmethod
	def parse(cls, value) -> Building:
		return Building.parse_obj(value)

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
			cBuilding = Building(
				name = building[0],
				description = desc[0],
				bonus = "Filler" if len(desc) < 2 else desc[1],
				lvlUpReq = costs,
				maxLvl = building[8],
				costIncrement = building[2:4],
				bonusInc = building[9],
				misc = building[10],

			)
			cls.addList(cBuilding)
			if len(desc) < 2:
				continue
			cls.add(building[0], cBuilding)
