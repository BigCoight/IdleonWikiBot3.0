from typing import List

from definitions.misc.world5.hole.LampWish import LampWish
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class LampWishRepo(Repository[LampWish]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["LampWishes"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())

		for line in data:
			cls.addList(LampWish.fromList(line))
			if cls.contains(line[0]): continue
			cls.add(line[0], LampWish.fromList(line))
