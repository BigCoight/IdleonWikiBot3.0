from typing import List

from definitions.misc.world6.SummonUnit import SummonUnit
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class SummonUnitRepo(Repository[SummonUnit]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SummonUnits"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, line in enumerate(data):
			cls.addList(SummonUnit.fromList(line))
			if cls.contains(f"{n}"): continue
			cls.add(f"{n}", SummonUnit.fromList(line))
