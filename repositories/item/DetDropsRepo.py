from definitions.itemdef.DetDrops import DetDrops, DetDrop
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.enemies.SubTableRepo import SubTableRepo
from repositories.master.Repository import Repository


class DetDropsRepo(Repository[DetDrops]):

	@classmethod
	def generateRepo(cls) -> None:
		for table, drops in DropTableRepo.items():
			if not SubTableRepo.contains(table):
				continue
			for drop in drops.drops:
				for source in SubTableRepo.get(table).sources:
					if not EnemyDetailsRepo.contains(source.name):
						continue
					cls.addTo(drop.item, DetDrop(
						source = source.name,
						quantity = source.quantity * drop.quantity,
						chance = source.chance * drop.chance))

	@classmethod
	def addTo(cls, key: str, detDrop: DetDrop):
		if not cls.contains(key):
			cls.add(key, DetDrops(sources = []))
		cls.get(key).sources.append(detDrop)
