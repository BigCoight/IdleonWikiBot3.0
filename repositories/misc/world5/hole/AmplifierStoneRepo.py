from typing import List

from definitions.misc.world5.hole.AmplifierStone import AmplifierStone
from definitions.misc.world5.hole.HoleOrder import HoleOrder
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import getFromMixedArray
from repositories.master.Repository import Repository


class AmplifierStoneRepo(Repository[AmplifierStone]):

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/5/Hole"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["HoleInfo"]

	@classmethod
	def hardcodedValues(cls, index: int) -> List[Numeric]:
		# Thanks to lava, this is (perLv, maxLvl)
		return [
			[0.11, 100],
			[0.09, 100],
			[0.08, 20],
			[0.10, 100],
			[0.08, 30],
			[0.07, 20],
			[0.10, 24],
			[0.07, 40]
		][index]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromMixedArray(cls.getSection())
		ampStones = data[HoleOrder.Amplifiers.value]
		print(ampStones)
		for n, i in enumerate(range(0, len(ampStones), 2)):
			name = ampStones[i]
			desc = ampStones[i + 1]
			hcVal = cls.hardcodedValues(n)
			toAdd = AmplifierStone(
				name = name,
				desc = desc,
				perLvl = hcVal[0],
				maxVal = hcVal[1]
			)
			cls.addList(toAdd)
			if cls.contains(name): continue
			cls.add(name, toAdd)
