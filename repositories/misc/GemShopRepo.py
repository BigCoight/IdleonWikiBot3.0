from typing import List

from definitions.misc.GemShopItem import GemShopItem
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GemShopRepo(Repository[GemShopItem]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def parse(cls, value) -> GemShopItem:
		return GemShopItem.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GemShop"]

	@classmethod
	def generateRepo(cls) -> None:
		gemShopItems = getFromSplitArray(cls.getSection())
		for item in gemShopItems:
			toAdd = GemShopItem(
				name = item[0],
				itemName = item[1].title(),
				desc = item[2],
				cost = item[3],
				no = item[4],
				maxPurchases = item[5],
				qty = item[6],
				costIncrement = item[7]
			)
			cls.addList(toAdd)
			if item[3] == "GemCostNum":
				continue
			cls.add(item[0], toAdd)

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.get(name).itemName
