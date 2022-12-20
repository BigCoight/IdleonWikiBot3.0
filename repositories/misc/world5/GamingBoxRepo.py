from typing import List

from definitions.misc.world5.GamingBox import GamingBox
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GamingBoxRepo(Repository[GamingBox]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GamingBoxes"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(GamingBox.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], GamingBox.fromList(line))
