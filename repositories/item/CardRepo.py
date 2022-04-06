import re
from typing import List, Dict

from definitions.itemdef.CardData import CardData
from helpers.Constants import Constants
from helpers.HelperFunctions import formatStr, wrap, strToArray
from repositories.master.Repository import Repository


class CardRepo(Repository[CardData]):
	orderMap: Dict[str, str] = {}
	cardToName: Dict[str, str] = {}
	nameToCard: Dict[str, str] = {}
	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["CardInfo"]

	@classmethod
	def generateRepo(cls) -> None:

		cardData = formatStr(cls.getSection(), ["\n", "  "])
		for n, section in enumerate([wrap(x) for x in re.split(r",?],?],\[\[", cardData)]):
			for m, data in enumerate([wrap(x) for x in re.split(r",?],\[", section)]):
				arrayData = strToArray(data)
				temp = CardData(
					cardID = arrayData[1],
					category = Constants.cardNames[n],
					perTier = arrayData[2],
					effect = arrayData[3],
					bonus = arrayData[4],
					order = m + 1,
				)
				cls.cardToName[f"Cards{arrayData[1]}"] = arrayData[0]
				cls.nameToCard[arrayData[0]] = f"Cards{arrayData[1]}"

				if Constants.cardNames[n] in Constants.navCategories:
					cls.orderMap[f"{Constants.cardNames[n]}{m + 1}"] = arrayData[0]
				cls.add(arrayData[0], temp)
		cls.cardToName["CardsA0"] = "mushG"
		cls.cardToName["mushG"] = "CardsA0"


	@classmethod
	def getOrder(cls, world: str, order: int) -> str:
		return cls.orderMap.get(f"{world}{order}")

	@classmethod
	def getName(cls, cardID: str) -> str:
		return cls.cardToName.get(cardID)
