from typing import List

from definitions.dungeons.DungPassives import DungPassives, DungPassive
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository


class DungPassivesRepo(Repository[DungPassives]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DungPassiveI", "DungPassiveF"]

	@classmethod
	def generateRepo(cls) -> None:
		sources = ["Dungeon", "Flurbo"]
		for i in range(len(cls.getSections())):
			data = getFromSplitArray(cls.getSection(i))
			temp = []
			for bonus in data:
				name = bonus[0].replace("@", " ")
				temp.append(DungPassive(
					effect = name,
					x1 = bonus[1],
					x2 = bonus[2],
					func = bonus[3],
					type = bonus[4],
					lvlUpText = bonus[5]
				))
			cls.add(sources[i], DungPassives(
				passives = temp.copy()
			))
