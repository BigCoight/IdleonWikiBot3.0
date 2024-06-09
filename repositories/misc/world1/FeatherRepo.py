from typing import List

from definitions.misc.world1.Feather import Feather
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class FeatherRepo(Repository[Feather]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/1"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Owlz"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for feather in data:
			toAdd = Feather.fromList(feather)
			cls.add(replaceUnderscores(feather[0]), toAdd)
			cls.addList(toAdd)
