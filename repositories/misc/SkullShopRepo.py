from typing import List

from definitions.misc.SkullShop import SkullShop
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class SkullShopRepo(Repository[SkullShop]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["SkullShop"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, bonus in enumerate(data):
			cls.add(f"{n}", SkullShop.fromList(bonus))
			cls.addList(SkullShop.fromList(bonus))
