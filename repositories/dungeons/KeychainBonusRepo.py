import string
from typing import List

from definitions.dungeons.KeychainBonus import KeychainBonus, KeychainBonuses
from helpers.HelperFunctions import getFromArrayArray, replaceUnderscores
from repositories.master.Repository import Repository


class KeychainBonusRepo(Repository[KeychainBonuses]):

	@classmethod
	def getCategory(cls) -> str:
		return "Dungeon"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungKeychain"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for item in data:
			if not cls.contains(item[0]):
				cls.add(item[0], KeychainBonuses(bonuses = []))
			cls.get(item[0]).bonuses.append(KeychainBonus(
				bonus = string.capwords(replaceUnderscores(item[1])),
				lvl1 = item[2],
				lvl2 = item[3],
				lvl3 = item[4]
			))

	@classmethod
	def _extractWikiSingle(cls) -> str:
		res = "{|class = \"wikitable\"\n!Bonus !! Tier 1 !! Tier 2 !! Tier 3\n|-\n"
		res += super()._extractWikiSingle()
		res += "|}"
		return res
