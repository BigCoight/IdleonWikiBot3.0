from typing import List

from definitions.misc.Tome import Tome
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class TomeRepo(Repository[Tome]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TomeInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, bonus in enumerate(data):
			cls.add(replaceUnderscores(bonus[0]), Tome.fromList(bonus, {"filler"}))
			cls.addList(Tome.fromList(bonus, {"filler"}))
