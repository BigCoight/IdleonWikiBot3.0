from definitions.itemdef.StatueData import StatueData
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.ListRepository import ListRepository
from repositories.Repository import Repository
from typing import List


class StatueRepo(ListRepository[StatueData]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["StatueInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		statues = getFromArrayArray(cls.getSection())
		for statue in statues:
			cls.add(StatueData(
				name =replaceUnderscores(statue[0]).title(),
				effect =replaceUnderscores(statue[1]).title(),
				dk = statue[2],
				bonus =statue[3]
			))
