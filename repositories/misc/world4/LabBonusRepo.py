from typing import List

from definitions.misc.world4.LabBonus import LabBonus
from helpers.Constants import Constants
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class LabBonusRepo(Repository[LabBonus]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/4"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["LabBonus", "NinjaInfo"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection(0))
		ninjaData = getFromSplitArray(cls.getSection(1))

		labInsertsStart = Constants.ninjaInfo + Constants.ninjaFloors + Constants.ninjaJadeOrder - 1  # -1 comes from the getFromSplitArray not recoginising the actual array
		labInsertsEnd = labInsertsStart + Constants.labInserts

		# for x in ninjaData[labInsertsStart: labInsertsEnd]:
		# 	print(x)

		if ninjaData:
			data.extend(ninjaData[labInsertsStart: labInsertsEnd])

		for bonus in data:
			cls.addList(LabBonus.fromList(bonus))
			if cls.contains(bonus[6]): continue
			cls.add(bonus[6], LabBonus.fromList(bonus))
