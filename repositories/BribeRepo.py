from typing import List

from definitions.Bribe import Bribe
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class BribeRepo(Repository[Bribe]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Bribes"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bribe in data:
			cls.add(replaceUnderscores(bribe[0]), Bribe(
				name = replaceUnderscores(bribe[0]),
				desc = replaceUnderscores(bribe[1]),
				cost = bribe[2],
				type = replaceUnderscores(bribe[3]),
				intName = replaceUnderscores(bribe[4]),
				amount = bribe[5]
			))
