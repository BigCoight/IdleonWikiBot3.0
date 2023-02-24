import string
from typing import List

from definitions.misc.GemShopItem import GemShopItem
from helpers.Constants import Constants
from helpers.HelperFunctions import getFrom4dArray, getFromSplit, replaceUnderscores
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
		gemShopItems = getFrom4dArray(cls.getSection())[0]
		for n, parentSection in enumerate(gemShopItems):
			for m, childSection in enumerate(parentSection):
				for gemShopSlot in childSection:
					gemShop = getFromSplit(gemShopSlot)
					gemShop = [replaceUnderscores(x) for x in gemShop]
					section = Constants.gemShopSections[n][m]
					toAdd = GemShopItem(
						section = section,
						name = gemShop[0],
						itemName = string.capwords(gemShop[1]),
						desc = gemShop[2],
						cost = gemShop[3],
						no = gemShop[4],
						maxPurchases = gemShop[5],
						qty = gemShop[6],
						costIncrement = gemShop[7]
					)
					cls.addList(toAdd)
					if gemShop[3] == "GemCostNum":
						continue
					cls.add(gemShop[0], toAdd)

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.get(name).itemName
