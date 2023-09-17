from typing import List

from definitions.misc.weeklybosses.WeeklyTask import WeeklyTask
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class WeeklyTaskRepo(Repository[WeeklyTask]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc/WeeklyTask"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["WeeklyTask"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, task in enumerate(data):
			toAdd = WeeklyTask.fromList(task)
			cls.add(f"{n}", toAdd)
			cls.addList(toAdd)
