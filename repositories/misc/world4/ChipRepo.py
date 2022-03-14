from typing import List

from definitions.common.Component import Component
from definitions.misc.world4.Chip import Chip
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class ChipRepo(Repository[Chip]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ChipDesc"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for line in data:
			components = []
			for i in range(3):
				start = 3 + i*2
				end = start + 2
				component = line[start:end]
				components.append(Component.fromList(component))
			toAdd = Chip(
				name =line[0],
				bonus =line[1],
				description =line[2],
				requirements =components.copy(),
				bool1 =line[9],
				stat = line[10],
				baseVal =line[11])
			cls.addList(toAdd)
			if cls.contains(line[0]): continue
			cls.add(line[0], toAdd)
