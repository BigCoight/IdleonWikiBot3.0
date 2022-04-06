import re
from typing import List

from definitions.common.LiquidComponent import LiquidComponent
from definitions.misc.world2.Bubble import Bubble
from definitions.common.Component import Component
from definitions.misc.world2.FishPool import FishPool
from helpers.HelperFunctions import replaceUnderscores, camelCaseToTitle
from repositories.master.Repository import Repository


class FishPoolRepo(Repository[FishPool]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/2"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["FishPools"]

	@classmethod
	def generateRepo(cls) -> None:
		rePools = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reData = r'\[(?:"([^ ]*)", )?"([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		poolData = cls.getSection()
		fishPools = re.split(rePools, poolData)
		for i in range(0, len(fishPools) - 1, 2):
			intName = fishPools[i + 1]
			rawData = re.findall(reData, fishPools[i])
			for i in range(4):
				toAdd = FishPool(
					fish = rawData[0][i],
					x1 = rawData[1][i],
					x2 = rawData[2][i],
					efficiency = rawData[3][i] if rawData[3][i] else 0,
					cardDrop = rawData[4][i],
					cardChance = rawData[5][i],
					pool = intName)
				cls.add(rawData[0][i], toAdd)
				cls.addList(toAdd)