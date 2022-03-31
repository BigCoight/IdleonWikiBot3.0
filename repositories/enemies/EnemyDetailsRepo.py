import re
from typing import List

from definitions.enemy.AFKType import AFKType
from definitions.enemy.EnemyDetails import EnemyDetails
from definitions.enemy.EnemyType import EnemyType
from helpers.Constants import Constants
from helpers.HelperFunctions import strToArray, formatStr, changeChestNames
from repositories.master.Repository import Repository


class EnemyDetailsRepo(Repository[EnemyDetails]):

	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

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
					val = Constants.nameConflicts.get(val, val)
				val = strToArray(val) if "[" in val else formatStr(val, [","], replaceUnderscores = True)
				enemy[atr.strip()] = val
			if enemy.get("Name") == "Error":
				continue
			enemy["Type"] = enemy.get("Type").split(".")[1].title()
			enemy["AFKtype"] = enemy.get("AFKtype").title()
			cls.add(intName, EnemyDetails.parse_obj(enemy))

	@classmethod
	def getWikiName(cls, name: str) -> str:
		if not cls.contains(name):
			return name
		return cls.get(name).Name

	@classmethod
	def _ignore(cls, name: str, data: EnemyDetails) -> bool:
		if "Dung" in name:
			return True
		if name in {"EXP", "Blank", "LockedInvSpace", "COIN", "TalentBook1", "TalentBook2",
		            "TalentBook3", "TalentBook4", "TalentBook5", "SmithingRecipes1", "SmithingRecipes2",
		            "SmithingRecipes3", "SmithingRecipes4", "ExpSmith1", "Quest8", "EquipmentShirts8", "FoodHealth1d",
		            "FoodHealth2d", "FoodHealth3d", "PremiumGem", "Quest49"}:
			return True
		if name[:3] == "Gem":
			return True
		if data.Type != EnemyType.monsterType:
			return True
		if data.AFKtype != AFKType.Fighting:
			return True
		return False
