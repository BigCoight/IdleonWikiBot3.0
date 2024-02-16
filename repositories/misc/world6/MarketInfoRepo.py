from typing import List

from definitions.misc.world6.MarketInfo import MarketInfo
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class MarketInfoRepo(Repository[MarketInfo]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MarketInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(MarketInfo.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], MarketInfo.fromList(line))
