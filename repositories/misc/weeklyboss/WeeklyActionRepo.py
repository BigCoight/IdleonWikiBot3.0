from typing import List

from definitions.misc.weeklybosses.WeeklyAction import WeeklyAction, ActionType
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class WeeklyActionRepo(Repository[WeeklyAction]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc/WeeklyTask"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["WeeklyAction"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, action in enumerate(data):
			actionType = action[0].split(" ", 1)[0].replace("(", "").replace(")", "")
			desc = action[0].split(" ", 1)[1]
			actionEnum = ActionType(actionType)
			toAdd = WeeklyAction(
				actionType = actionEnum,
				desc = desc,
				scaling = action[1],
				max = action[2],
				key = action[3],
			)
			cls.add(f"{n}", toAdd)
			cls.addList(toAdd)
