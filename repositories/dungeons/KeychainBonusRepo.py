from typing import List

from definitions.dungeons.KeychainBonus import KeychainBonus
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.Repository import Repository


class KeychainBonusRepo(Repository[KeychainBonus]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungKeychain"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for item in data:
			cls.add(item[0], KeychainBonus(
				bonus = replaceUnderscores(item[1]).title(),
				lvl1 = item[2],
				lvl2 = item[3],
				lvl3 = item[4]))
