from typing import List

from definitions.itemdef.StatueData import StatueData
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.ListRepository import ListRepository
from repositories.master.Repository import Repository


class StatueRepo(Repository[StatueData]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["StatueInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		statues = getFromArrayArray(cls.getSection())
		for n, statue in enumerate(statues):
			toAdd = StatueData(
				name = replaceUnderscores(statue[0]).title(),
				effect = replaceUnderscores(statue[1]).title(),
				dk = statue[2],
				bonus = statue[3]
			)
			cls.add(f"{n}", toAdd)
			cls.addList(toAdd)
