from definitions.misc.world3.Shrine import Shrine
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.Repository import Repository
from typing import List


class ShrineRepo(Repository[Shrine]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/3"

	@classmethod
	def parse(cls, value) -> Shrine:
		return Shrine.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ShrineInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		shrines = getFromArrayArray(cls.getSection())
		for shrine in shrines:
			toAdd = Shrine(
				name = replaceUnderscores(shrine[0]),
				desc = shrine[1],
				baseBonus = shrine[2],
				increment = shrine[3],
				misc = shrine[4]
			)
			cls.add(replaceUnderscores(shrine[0]), toAdd)
			cls.addList(toAdd)
