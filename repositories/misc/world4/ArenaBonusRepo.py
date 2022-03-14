from typing import List

from definitions.misc.world4.ArenaBonus import ArenaBonus
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class ArenaBonusRepo(Repository[ArenaBonus]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["LabDesc"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())[0]
		for n, bonus in enumerate(data):
			bonus = bonus.title()
			cls.addList(ArenaBonus.fromList([bonus]))
			if cls.contains(bonus): continue
			cls.add(f"{n}", ArenaBonus.fromList([bonus]))
