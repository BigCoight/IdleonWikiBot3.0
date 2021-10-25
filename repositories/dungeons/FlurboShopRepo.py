from typing import List

from definitions.dungeons.FlurboShop import FlurboShop
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.Repository import Repository


class FlurboShopRepo(Repository[FlurboShop]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungFlurbo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for item in data:
			cls.add(item[0], FlurboShop(
				intId = item[0],
				cost = item[1],
				noPurchases = item[2],
				displayName = replaceUnderscores(item[3]),
				description = replaceUnderscores(item[4])
			))
