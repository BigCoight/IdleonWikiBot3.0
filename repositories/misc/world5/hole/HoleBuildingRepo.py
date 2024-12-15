from typing import List

from definitions.misc.world5.hole.HoleBuilding import HoleBuilding
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.HelperFunctions import getFromSplitArray, getFromMixedArray
from repositories.master.Repository import Repository


class HoleBuildingRepo(Repository[HoleBuilding]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleBuilding", "HoleInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		holeInfo = getFromMixedArray(cls.getSection(1))
		order = holeInfo[HoleOrder.BuildingOrder.value]

		for line, o in zip(data, order):
			line.append(o)
			cls.addList(HoleBuilding.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], HoleBuilding.fromList(line))
