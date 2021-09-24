import re

from definitions.DropTable import DropTable, Drop
from repositories.Repository import Repository
from typing import List


class DropTableRepo(Repository[DropTable]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DropTables"]

	@classmethod
	def generateRepo(cls) -> None:
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection()
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			drops = re.findall(reDrops, droptables[i])
			drops = [Drop(
				item = drop[0],
				quantity = drop[2],
				chance = drop[1],
				questLink = drop[3],
			) for drop in drops]
			cls.add(droptables[i + 1], DropTable(drops = drops))
