from typing import List

from definitions.misc.equinox.DreamChallenge import DreamChallenge
from definitions.misc.weeklybosses.WeeklyAction import WeeklyAction, ActionType
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class DreamChallengeRepo(Repository[DreamChallenge]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc/Equinox"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DreamChallenge"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, challenge in enumerate(data):
			toAdd = DreamChallenge.fromList(challenge)
			cls.add(f"{n}", toAdd)
			cls.addList(toAdd)
