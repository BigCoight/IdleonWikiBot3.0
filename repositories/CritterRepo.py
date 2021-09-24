from definitions.Critter import Critter
from helpers.HelperFunctions import getFromSplitArray
from repositories.MapNameRepo import MapNameRepo
from repositories.Repository import Repository
from typing import List


class CritterRepo(Repository[Critter]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TrappingInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		critters = getFromSplitArray(cls.getSection())
		for critter in critters:
			cls.add(critter[2], Critter(
				location = MapNameRepo.get(int(critter[0])),
				baseExp = critter[5],
				baseShinyRate = critter[6],
				shiny = critter[2] + "A",
				effForBonus = critter[4],
			))
