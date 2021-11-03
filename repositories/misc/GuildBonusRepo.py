from typing import List

from definitions.misc.GuildBonus import GuildBonus
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GuildBonusRepo(Repository[GuildBonus]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GuidBonuses"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for bonus in data:
			cls.add(bonus[0], GuildBonus.fromList(bonus))
