from typing import List

from definitions.dungeons.DungTrait import DungTrait
from helpers.HelperFunctions import replaceUnderscores, getFromSplit
from repositories.master.ListRepository import ListRepository


class DungTraitRepo(ListRepository[DungTrait]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungTraits"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplit(cls.getSection())
		for trait in data:
			cls.add(DungTrait(
				name = replaceUnderscores(trait)
			))
