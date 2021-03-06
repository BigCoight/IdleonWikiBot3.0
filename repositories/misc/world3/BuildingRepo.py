from typing import List

from definitions.component.ComponentFactory import ComponentFactory
from definitions.misc.world3.Building import Building
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class BuildingRepo(Repository[Building]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/3"

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
				ComponentFactory.getComponent(building[4], building[6]),
				ComponentFactory.getComponent(building[5], building[7]),
			]
			desc = building[1].split("@ Current Bonuses: @")
			cBuilding = Building(
				name = building[0],
				description = desc[0],
				bonus = "Filler" if len(desc) < 2 else desc[1],
				lvlUpReq = costs,
				maxLvl = building[8],
				bonusInc = building[2:4],
				costInc = building[9],
				misc = building[10],

			)
			cls.addList(cBuilding)
			if len(desc) < 2:
				continue
			cls.add(building[0], cBuilding)
