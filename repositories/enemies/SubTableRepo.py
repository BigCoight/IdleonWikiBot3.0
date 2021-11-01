import re
from typing import List

from definitions.enemy.SubTable import SubTables, SubTable
from repositories.master.Repository import Repository


class SubTableRepo(Repository[SubTables]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DropTables", "EnemyDropTables"]

	@classmethod
	def generateRepo(cls) -> None:
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection(1)
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			drops = re.findall(reDrops, droptables[i])
			drops = [drop for drop in drops if "DropTable" in drop[0]]
			for drop in drops:
				cls.addTo(drop[0], SubTable(
					name = droptables[i + 1],
					chance = drop[1],
					quantity = drop[2]))

		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection()
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			drops = re.findall(reDrops, droptables[i])
			drops = [drop for drop in drops if "SuperDropTable" in drop[0]]
			for drop in drops:
				if not cls.contains(droptables[i + 1]):
					continue
				for source in cls.get(droptables[i + 1]).sources:
					cls.addTo(drop[0], SubTable(
						name = source.name,
						chance = float(drop[1]) * source.chance,
						quantity = int(drop[2]) * source.quantity))

	@classmethod
	def addTo(cls, key: str, source: SubTable):
		if not cls.contains(key):
			cls.add(key, SubTables(sources = []))
		cls.get(key).sources.append(source)
