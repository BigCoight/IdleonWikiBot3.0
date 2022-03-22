from definitions.itemdef.DetDrops import DetDrops, DetDrop
from helpers.Constants import Constants
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.enemies.EnemyTableRepo import EnemyTableRepo
from repositories.enemies.SubTableRepo import SubTableRepo
from repositories.master.Repository import Repository


class DetDropsRepo(Repository[DetDrops]):

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		DropTableRepo.initialise(cls.codeReader, log)
		EnemyDetailsRepo.initialise(cls.codeReader, log)
		EnemyTableRepo.initialise(cls.codeReader, log)
		SubTableRepo.initialise(cls.codeReader, log)

	@classmethod
	def generateRepo(cls) -> None:
		for table, drops in DropTableRepo.items():
			if not SubTableRepo.contains(table):
				continue
			for drop in drops.drops:
				for source in SubTableRepo.get(table).sources:
					if source.name in Constants.ignoredEnemies:
						continue
					if not EnemyDetailsRepo.contains(source.name):
						continue
					cls.addTo(drop.item, DetDrop(
						source = source.name,
						quantity = source.quantity * drop.quantity,
						chance = source.chance * drop.chance))
		for enemy, drops in EnemyTableRepo.items():
			if enemy in Constants.ignoredEnemies:
				continue
			if not EnemyDetailsRepo.contains(enemy):
				continue
			for drop in drops.drops:
				cls.addTo(drop.item, DetDrop(
					source = enemy,
					quantity = drop.quantity,
					chance = drop.chance))

	@classmethod
	def addTo(cls, key: str, detDrop: DetDrop):
		if not cls.contains(key):
			cls.add(key, DetDrops(sources = []))
		cls.get(key).sources.append(detDrop)
