from typing import List

from definitions.misc.Achievement import Achievement
from definitions.misc.CardSet import CardSet
from helpers.Constants import Constants
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.Repository import Repository


class CardSetRepo(Repository[CardSet]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["CardSets"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, cardSet in enumerate(data):
			toAdd = CardSet.fromList(cardSet)
			cls.addList(toAdd)
			if n >= len(Constants.cardNames):
				continue
			cls.add(Constants.cardNames[n], toAdd)

