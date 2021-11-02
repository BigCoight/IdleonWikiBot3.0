from typing import List

from definitions.Bribe import Bribe
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.ListRepository import ListRepository


class BribeRepo(ListRepository[Bribe]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Bribes"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bribe in data:
			cls.add(Bribe(
				name = replaceUnderscores(bribe[0]),
				desc = replaceUnderscores(bribe[1]),
				cost = bribe[2],
				type = replaceUnderscores(bribe[3]),
				intName = replaceUnderscores(bribe[4]),
				amount = bribe[5]
			))
