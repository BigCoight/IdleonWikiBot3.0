from typing import List

from definitions.misc.Achievement import Achievement
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.ListRepository import ListRepository


class AchievementRepo(ListRepository[Achievement]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Achieve"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for achieve in data:
			cls.add(Achievement(
				name = replaceUnderscores(achieve[0]),
				qty = achieve[1],
				desc = replaceUnderscores(achieve[2]),
				rewards = replaceUnderscores(achieve[3])
			))
