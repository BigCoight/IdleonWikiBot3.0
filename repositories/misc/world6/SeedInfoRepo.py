from typing import List

from definitions.misc.world6.SeedInfo import SeedInfo
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class SeedInfoRepo(Repository[SeedInfo]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SeedInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(SeedInfo.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], SeedInfo.fromList(line))
