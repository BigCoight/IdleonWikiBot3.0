from typing import List

from definitions.misc.Achievement import Achievement
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.Repository import Repository


class AchievementRepo(Repository[Achievement]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Achieve"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for achieve in data:
			toAdd = Achievement(
				name = replaceUnderscores(achieve[0]),
				qty = achieve[1],
				desc = replaceUnderscores(achieve[2]),
				rewards = replaceUnderscores(achieve[3])
			)
			cls.add(replaceUnderscores(achieve[0]), toAdd)
			cls.addList(toAdd)
