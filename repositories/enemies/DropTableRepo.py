import re
from typing import List

from definitions.enemy.DropTable import DropTable
from definitions.common.DropTypes import Drop, ItemDrop
from repositories.master.Repository import Repository


class DropTableRepo(Repository[DropTable]):

	@classmethod
	def parse(cls, value) -> DropTable:
		return DropTable.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["DropTables"]

	@classmethod
	def generateRepo(cls) -> None:
		cls.subDroptables()

	@classmethod
	def subDroptables(cls):
		reEnemies = r'.\.setReserved\("([a-zA-Z0-9_]*)", [a-zA-Z0-9_$]*\)'
		reDrops = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		droptableData = cls.getSection()
		droptables = re.split(reEnemies, droptableData)
		for i in range(0, len(droptables) - 1, 2):
			drops = re.findall(reDrops, droptables[i])
			drops = [Drop.arrayToDropType(drop) for drop in drops]
			cls.add(droptables[i + 1], DropTable(drops = drops.copy(), subTable = droptables[i + 1]))
		cls.insertObols()

	@classmethod
	def insertObols(cls):
		obols = []
		for i in range(12):  # Obols1
			if i < 4:
				obols.append(ItemDrop(
					item = f"ObolBronze{i}",
					quantity = 1,
					chance = 0.0006 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i < 8:
				obols.append(ItemDrop(
					item = f"ObolSilver{i - 4}",
					quantity = 1,
					chance = 0.0006 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i == 8:
				obols.append(ItemDrop(
					item = f"ObolSilverMoney",
					quantity = 1,
					chance = 0.027 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i == 9:
				obols.append(ItemDrop(
					item = f"ObolSilverDamage",
					quantity = 1,
					chance = 0.027 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i == 10:
				obols.append(ItemDrop(
					item = f"ObolGold3",
					quantity = 1,
					chance = 0.021 * (1 + 1 / 20),
					questLink = "N/A",
				))
			elif i == 11:
				obols.append(ItemDrop(
					item = f"ObolSilverLuck",
					quantity = 1,
					chance = 0.021 * (1 + 1 / 20),
					questLink = "N/A",
				))
			if i < 4:
				cls.get(f"DropTable{i + 1}").drops.insert(-1, obols[i])
			elif i < 8:
				cls.get(f"DropTable{i + 2}").drops.insert(-1, obols[i])
			elif i < 10:
				cls.get(f"SuperDropTable1").drops.insert(-1, obols[i])
			elif i < 12:
				cls.get(f"SuperDropTable2").drops.insert(-1, obols[i])

		cls.get("DropTable14").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeWorship",
			quantity = 1,
			chance = 0.021 * (1 + 1 / 20),
			questLink = "N/A",
		))
		cls.get("DropTable15").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeTrapping",
			quantity = 1,
			chance = 0.021 * (1 + 1 / 20),
			questLink = "N/A",
		))
		cls.get("DropTable16").drops.insert(-1, ItemDrop(
			item = f"ObolBronzeCons",
			quantity = 1,
			chance = 0.021 * (1 + 1 / 20),
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
