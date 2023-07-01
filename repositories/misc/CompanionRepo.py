from typing import List

from definitions.misc.Companion import Companion
from helpers.HelperFunctions import getFromSplitArray
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.master.Repository import Repository


class CompanionRepo(Repository[Companion]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Companion"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, bonus in enumerate(data):
			toAdd = Companion.fromList(bonus)
			cls.add(toAdd.id, Companion.fromList(bonus))
			cls.addList(Companion.fromList(bonus))

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return EnemyDetailsRepo.getWikiName(name)
