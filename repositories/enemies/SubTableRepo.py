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
		droptableData = cls.getSection()
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			drops = re.findall(reDrops, droptables[i])
			drops = [drop for drop in drops if "DropTable" in drop[0]]
			mega = []
			for drop in drops:
				mega.append(SubTable(
					name = drop[0],
					chance = drop[1],
					quantity = drop[2]))
			cls.add(droptables[i + 1], SubTables(
				rare = [],
				mega = mega.copy()
			))

		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection(1)
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			drops = re.findall(reDrops, droptables[i])
			drops = [drop for drop in drops if "DropTable" in drop[0]]
			rare = []
			mega = []

			for drop in drops:
				rare.append(SubTable(
					name = drop[0],
					chance = drop[1],
					quantity = drop[2]))
				mega += cls.get(drop[0]).mega.copy()
			cls.add(droptables[i + 1], SubTables(
				rare = rare.copy(),
				mega = mega.copy()
			))
