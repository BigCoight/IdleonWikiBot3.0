from typing import List

from definitions.arcade.ArcadeBonus import ArcadeBonus
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class ArcadeBonusRepo(Repository[ArcadeBonus]):

	@classmethod
	def getCategory(cls) -> str:
		return "Arcade"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ArcadeBonus"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, bonus in enumerate(data):
			toAdd = ArcadeBonus.fromList(bonus)
			cls.add(f"{n}", toAdd)
			cls.addList(toAdd)
