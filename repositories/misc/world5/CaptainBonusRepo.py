from typing import List

from definitions.misc.world5.CaptainBonus import CaptainBonus
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class CaptainBonusRepo(Repository[CaptainBonus]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["CaptainBonuses"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, line in enumerate(data):
			cls.addList(CaptainBonus.fromList(line))
			cls.add(f"{n}", CaptainBonus.fromList(line))
