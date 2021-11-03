import re
from typing import List

from definitions.enemy.DropTable import DropTable
from definitions.common.DropTypes import Drop, ItemDrop
from definitions.enemy.EnemyTable import EnemyTable
from repositories.master.Repository import Repository


class EnemyTableRepo(Repository[EnemyTable]):

	@classmethod
	def parse(cls, value) -> DropTable:
		return DropTable.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["EnemyDropTables"]

	@classmethod
	def generateRepo(cls) -> None:
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection()
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			drops = re.findall(reDrops, droptables[i])

			drops = [Drop.arrayToDropType(drop) for drop in drops]
			cls.add(droptables[i + 1], EnemyTable(drops = drops.copy()))
		cls.insertMissing()

	@classmethod
	def insertMissing(cls):
		cls.get("wolfA").drops.insert(0, ItemDrop(
			item = "Crystal1",
			quantity = "1",
			chance = "1",
			questLink = "N/A",
		))
		cls.get("Boss2A").drops.insert(0, ItemDrop(
			item = "Crystal2",
			quantity = "1",
			chance = "1",
			questLink = "N/A",
		))
