from typing import List

from definitions.misc.world4.LabBonus import LabBonus
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class LabBonusRepo(Repository[LabBonus]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/4"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["LabBonus"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bonus in data:
			cls.addList(LabBonus.fromList(bonus))
			if cls.contains(bonus[6]): continue
			cls.add(bonus[6], LabBonus.fromList(bonus))
