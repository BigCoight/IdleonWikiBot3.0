from definitions.misc.world3.SaltLick import SaltLick
from helpers.HelperFunctions import getFromSplitArray
from typing import List

from repositories.master.Repository import Repository


class SaltLickRepo(Repository[SaltLick]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/3"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SaltLicks"]

	@classmethod
	def generateRepo(cls) -> None:
		saltLicks = getFromSplitArray(cls.getSection())
		for saltLick in saltLicks:
			toAdd = SaltLick.fromList(saltLick)
			cls.add(saltLick[0], toAdd)
			cls.addList(toAdd)
