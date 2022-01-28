from definitions.misc.TaskShopDesc import TaskShopDesc
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from repositories.master.ListRepository import ListRepository
from typing import List


class TaskShopDescRepo(ListRepository[TaskShopDesc]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TaskShopDesc"]

	@classmethod
	def generateRepo(cls) -> None:
		sections = getFromSplitArray(cls.getSection())
		for section in sections:
			cls.add(TaskShopDesc(
				descLine1 = section[0],
				descLine2 = section[1],
				number1 = section[2],
				number2 = section[3],
				number3 = section[4],
				totalLevels = section[5],
				meritCost = section[6],
				text1 = section[7],
				text2 = section[8],
				extraStr = section[9],
				icon = section[10],
				bonusPerLevel = section[11],
			))


