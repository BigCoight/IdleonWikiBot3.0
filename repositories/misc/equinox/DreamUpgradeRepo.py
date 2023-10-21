from typing import List

from definitions.misc.equinox.DreamUpgrade import DreamUpgrade
from helpers.HelperFunctions import getFromArrayArray
from repositories.master.Repository import Repository


class DreamUpgradeRepo(Repository[DreamUpgrade]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc/Equinox"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DreamUpg"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromArrayArray(cls.getSection())
		for n, challenge in enumerate(data):
			toAdd = DreamUpgrade.fromList(challenge)
			cls.add(f"{n}", toAdd)
			cls.addList(toAdd)
