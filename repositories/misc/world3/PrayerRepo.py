from typing import List

from definitions.misc.world3.Prayer import Prayer
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.Repository import Repository


class PrayerRepo(Repository[Prayer]):

	@classmethod
	def parse(cls, value) -> Prayer:
		return Prayer.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["PrayerInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		zones = ["Goblin Gorefest", "Wakawaka War", "Acorn Assault", "Frosty Firefight", "FILLER", "FILLER"]
		prayers = getFromSplitArray(cls.getSection())
		for prayer in prayers:
			cls.add(replaceUnderscores(prayer[0]), Prayer(
				bonus = prayer[1],
				curse = prayer[2],
				x1 = prayer[3],
				x2 = prayer[4],
				soul = f"Soul{int(prayer[8]) + 1}",
				id = prayer[5],
				costMult = prayer[6],
				unlockZone = zones[int(prayer[8])],
				unlockWave = prayer[7],
			))
