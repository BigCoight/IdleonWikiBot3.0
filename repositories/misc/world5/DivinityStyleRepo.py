from typing import List

from definitions.misc.world5.DivinityStyle import DivinityStyle
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class DivinityStyleRepo(Repository[DivinityStyle]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DivStyle"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for line in data:
			cls.addList(DivinityStyle.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], DivinityStyle.fromList(line))
