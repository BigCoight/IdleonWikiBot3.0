from typing import List

from definitions.misc.world5.IslandInfo import IslandInfo
from helpers.Constants import Constants
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class IslandInfoRepo(Repository[IslandInfo]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["IslandInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, line in enumerate(data):
			if n < len(Constants.sailingIslands):
				line[0] = Constants.sailingIslands[n]
			cls.addList(IslandInfo.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], IslandInfo.fromList(line))