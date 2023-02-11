import re
from typing import List

from definitions.enemy.SubTable import SubTables, SubTable
from helpers.HelperFunctions import formatStr, getFromArrayArray
from repositories.master.Repository import Repository


class SubTableRepo(Repository[SubTables]):

	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DropTables", "EnemyDropTables"]

	@classmethod
	def generateRepo(cls) -> None:
		reDropTables = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		droptableData = formatStr(cls.getSection(1), ["\n", "  "], replaceUnderscores = False)
		for name, dt in re.findall(reDropTables, droptableData):
			drops = getFromArrayArray(dt)
			drops = [drop for drop in drops if "DropTable" in drop[0]]
			for drop in drops:
				cls.addTo(drop[0], SubTable(
					name = name,
					chance = drop[1],
					quantity = drop[2]))

		reDropTables = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		droptableData = formatStr(cls.getSection(), ["\n", "  "])
		for name, dt in re.findall(reDropTables, droptableData):
			drops = getFromArrayArray(dt)
			drops = [drop for drop in drops if "SuperDropTable" in drop[0]]
			for drop in drops:
				if not cls.contains(name):
					continue
				for source in cls.get(name).sources:
					cls.addTo(drop[0], SubTable(
						name = source.name,
						chance = float(drop[1]) * source.chance,
						quantity = int(drop[2]) * source.quantity))

	@classmethod
	def addTo(cls, key: str, source: SubTable):
		if not cls.contains(key):
			cls.add(key, SubTables(sources = []))
		cls.get(key).sources.append(source)
