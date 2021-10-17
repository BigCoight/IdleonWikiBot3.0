from typing import List

from definitions.arcade.ArcadeBonus import ArcadeBonus
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.ListRepository import ListRepository


class ArcadeBonusRepo(ListRepository[ArcadeBonus]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ArcadeBonus"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bonus in data:
			cls.add(ArcadeBonus(
				effect = bonus[0],
				x1 = bonus[1],
				x2 = bonus[2],
				func = bonus[3],
				type = bonus[4],
				lvlUpText = bonus[5]
			))
