import re
from typing import List

from definitions.enemy.EnemyDetails import EnemyDetails
from helpers.HelperFunctions import strToArray, formatStr, changeChestNames
from repositories.master.Repository import Repository


class EnemyDetailsRepo(Repository[EnemyDetails]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Enemies"]

	@classmethod
	def generateRepo(cls) -> None:
		reName = r'..\.addNewMonster\("([a-zA-Z0-9_]*)", {'
		reData = r'([a-zA-Z0-9_]*): "?([a-zA-Z0-9_.\]\[, \$]*)"?,'
		enemiesText = cls.getSection(0)
		enemiesData = re.split(reName, enemiesText)

		for i in range(1, len(enemiesData), 2):
			intName = enemiesData[i]
			data = enemiesData[i + 1]
			splitData = re.findall(reData, data)
			enemy = {}
			for atr, val in splitData:
				if atr == "Name":
					if "Chest" in val:
						val = changeChestNames(intName, val)
				val = strToArray(val) if "[" in val else formatStr(val, [","], replaceUnderscores = True)
				enemy[atr.strip()] = val
			if enemy.get("Name") == "Error":
				continue
			enemy["Type"] = enemy.get("Type").split(".")[1].title()

			cls.add(intName, EnemyDetails.parse_obj(enemy))

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.get(name).Name
