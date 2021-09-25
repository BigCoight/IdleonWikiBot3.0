import re
from typing import List

from definitions.Enemy import Enemy
from definitions.common.Drop import Drop
from helpers.HelperFunctions import strToArray, formatStr
from repositories.Repository import Repository


class EnemyRepo(Repository[Enemy]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Enemies", "EnemyDropTables"]

	@classmethod
	def generateRepo(cls) -> None:
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection(1)
		droptables = re.split(reEnemies, droptableData)
		tables = {}
		for i in range(0, len(droptables) - 1, 2):

			drops = re.findall(reDrops, droptables[i])
			drops = [Drop(
				item = drop[0],
				quantity = drop[2],
				chance = drop[1],
				questLink = drop[3],
			) for drop in drops]
			tables[droptables[i + 1]] = drops.copy()
		# tables["wolfA"].insert(0, ["Crystal1", "1", "1", "N/A"])
		# tables["Boss2A"].insert(0, ["Crystal2", "1", "1", "N/A"])

		reName = r'..\.addNewMonster\("([a-zA-Z0-9_]*)", {'
		reData = r'([a-zA-Z0-9_]*): "?([a-zA-Z0-9_.\]\[, \$]*)"?,'
		enemiesText = cls .getSection(0)
		enemiesData = re.split(reName, enemiesText)

		for i in range(1, len(enemiesData), 2):
			intName = enemiesData[i]
			data = enemiesData[i + 1]
			splitData = re.findall(reData, data)
			enemy = {}
			for atr, val in splitData:
				val = strToArray(val) if "[" in val else formatStr(val, [","], replaceUnderscores = True)
				enemy[atr.strip()] = val
			# IF the enemy has a drotpable, it should but lava (tm)
			if droptable := tables.get(intName):
				enemy["Drops"] = droptable.copy()
			else:
				enemy["Drops"] = []

			if enemy.get("Name") == "Error":
				continue
			cls.add(intName, Enemy.parse_obj(enemy))

		cls.get("wolfA").Drops.insert(0, Drop(
			item = "Crystal1",
			quantity = "1",
			chance = "1",
			questLink = "N/A",
		))
		cls.get("Boss2A").Drops.insert(0, Drop(
			item = "Crystal2",
			quantity = "1",
			chance = "1",
			questLink = "N/A",
		))

