from typing import List

from definitions.common.Component import Component
from definitions.misc.world4.Chip import Chip
from definitions.misc.world4.Jewel import Jewel
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class JewelRepo(Repository[Jewel]):
	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/4"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["JewelDesc"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			components = []
			for i in range(3):
				start = 5 + i*2
				end = start + 2
				component = line[start:end]
				components.append(Component.fromList(component))
			toAdd = Jewel(
				x =line[0],
				y =line[1],
				range =line[2],
				effect =line[3],
				description =line[4],
				requirements =components.copy(),
				name =line[11],
				bonusGiven =line[12])
			cls.addList(toAdd)
			if cls.contains(line[11]): continue
			cls.add(line[11], toAdd)
