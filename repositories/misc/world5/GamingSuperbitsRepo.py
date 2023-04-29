from typing import List

from definitions.misc.world5.GamingSuperbit import GamingSuperbit
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class GamingSuperbitsRepo(Repository[GamingSuperbit]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GamingSuperbits"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for line in data:
			cls.addList(GamingSuperbit.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], GamingSuperbit.fromList(line))
