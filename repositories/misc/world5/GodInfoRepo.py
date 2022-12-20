from typing import List

from definitions.misc.world5.GodInfo import GodInfo
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class GodInfoRepo(Repository[GodInfo]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GodsInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			cls.addList(GodInfo.fromList(line))
			bonusIndex = int(line[13])
			actualBonus = data[bonusIndex]
			cls.add(line[0], GodInfo(
				name = line[0],
				majorBonus = actualBonus[1],
				passiveBonus = actualBonus[2],
				passiveMax = actualBonus[3],
				blessingBaseCost = line[4],
				blessingIncrement = line[5],
				blessingBonus = line[6],
				preUnlockMessage = line[7],
				x = line[8],
				y = line[9],
				linkX = line[10],
				linkY = line[11],
				hueAdjust = line[12],
				bonusIndex = line[13],
				blessingPerLevel = line[14]
			)
			        )
