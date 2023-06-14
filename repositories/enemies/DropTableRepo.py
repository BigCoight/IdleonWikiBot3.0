import re
from typing import List

from definitions.common.DropTypes import Drop, ItemDrop
from definitions.enemy.DropTable import DropTable
from helpers.HelperFunctions import formatStr, getFromArrayArray
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.master.Repository import Repository
from repositories.talents.TalentNameRepo import TalentNameRepo


class DropTableRepo(Repository[DropTable]):

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
		return ["DropTables"]

	@classmethod
	def generateRepo(cls) -> None:
		reDropTables = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
		droptableData = formatStr(cls.getSection(), ["\n", "  "], replaceUnderscores = False)
		for name, dt in re.findall(reDropTables, droptableData):
			drops = getFromArrayArray(dt, repU = False)
			drops = [Drop.arrayToDropType(drop) for drop in drops]
			cls.add(name, DropTable(drops = drops.copy(), subTable = name))
		cls.insertObols()

	@classmethod
	def insertObols(cls):
		obols = []
		for i in range(12):  # Obols1
			if i < 4:
				obols.append(ItemDrop(
					item = f"ObolBronze{i}",
					quantity = 1,
					chance = 0.0011 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i < 8:
				obols.append(ItemDrop(
					item = f"ObolSilver{i - 4}",
					quantity = 1,
					chance = 0.0007 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i == 8:
				obols.append(ItemDrop(
					item = f"ObolSilverMoney",
					quantity = 1,
					chance = 0.03 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i == 9:
				obols.append(ItemDrop(
					item = f"ObolSilverDamage",
					quantity = 1,
					chance = 0.031 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i == 10:
				obols.append(ItemDrop(
					item = f"ObolGold3",
					quantity = 1,
					chance = 0.015 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i == 11:
				obols.append(ItemDrop(
					item = f"ObolSilverLuck",
					quantity = 1,
					chance = 0.025 * (1 + 1 / 20),
					questLink = "N/A",
				))
			if i < 4:
				cls.get(f"DropTable{i + 1}").drops.insert(-1, obols[i])
			if i < 8:
				cls.get(f"DropTable{i + 1}").drops.insert(-1, obols[i])
			elif i < 10:
				cls.get(f"SuperDropTable1").drops.insert(-1, obols[i])
			elif i < 12:
				cls.get(f"SuperDropTable2").drops.insert(-1, obols[i])

		cls.get("DropTable14").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeWorship",
			quantity = 1,
			chance = 0.0009 * (1 + 1 / 20),
			questLink = "N/A",
		))
		cls.get("DropTable15").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeTrapping",
			quantity = 1,
			chance = 0.0009 * (1 + 1 / 20),
			questLink = "N/A",
		))
		cls.get("DropTable16").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeCons",
			quantity = 1,
			chance = 0.0009 * (1 + 1 / 20),
			questLink = "N/A",
		))
		cls.get("SuperDropTable1").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeEXP",
			quantity = 1,
			chance = 0.029 * (1 + 1 / 20),
			questLink = "N/A",
		))
		cls.get("SuperDropTable3").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeKill",
			quantity = 1,
			chance = 0.029 * (1 + 1 / 20),
			questLink = "N/A",
		))
		cls.get("SuperDropTable2").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeDef",
			quantity = 1,
			chance = 0.029 * (1 + 1 / 20),
			questLink = "N/A",
		))
