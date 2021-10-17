from definitions.SaltLick import SaltLick
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.ListRepository import ListRepository
from typing import List


class SaltLickRepo(ListRepository[SaltLick]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SaltLicks"]

	@classmethod
	def generateRepo(cls) -> None:
		saltLicks = getFromSplitArray(cls.getSection())
		for saltLick in saltLicks:
			cls.add(SaltLick(
				item = saltLick[0],
				desc = saltLick[1],
				baseCost = saltLick[2],
				baseBonus = saltLick[3],
				maxLevel = saltLick[4],
				increment = saltLick[5]
			))
