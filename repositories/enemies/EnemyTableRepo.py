import re
from typing import List

from definitions.common.DropTypes import Drop, ItemDrop, RecipeDrop
from definitions.enemy.EnemyTable import EnemyTable
from helpers.HelperFunctions import formatStr, getFromArrayArray
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.master.Repository import Repository
from repositories.talents.TalentNameRepo import TalentNameRepo


class EnemyTableRepo(Repository[EnemyTable]):

	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		TalentNameRepo.initialise(cls.codeReader, log)
		SpecificItemRepo.initialise(cls.codeReader, log)
		RecipeRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["EnemyDropTables"]

	@classmethod
	def generateRepo(cls) -> None:
		reDropTables = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		droptableData = formatStr(cls.getSection(), ["\n", "  "], replaceUnderscores = False)
		for name, dt in re.findall(reDropTables, droptableData):
			drops = getFromArrayArray(dt, repU = False)
			drops = [Drop.arrayToDropType(drop) for drop in drops]
			cls.add(name, EnemyTable(drops = drops.copy()))
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
		# DNA Guns
		pincerDrops = cls.get("pincermin").drops
		pincerDrops.insert(len(pincerDrops) - 1, RecipeDrop(
			item = "SmithingRecipes4",
			quantity = "53",
			chance = "0.000003",
			questLink = "(Enter World 4)",
		))
		thermoDrops = cls.get("thermostat").drops
		thermoDrops.insert(len(thermoDrops) - 1, RecipeDrop(
			item = "SmithingRecipes4",
			quantity = "54",
			chance = "0.0000008",
			questLink = "(Enter World 4)",
		))
