from typing import Set

from definitions.collections.Enemy import Enemy
from helpers.CodeReader import IdleonReader
from repositories.enemies.BossDetailRepo import BossDetailRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.enemies.EnemyNavRepo import EnemyNavRepo
from repositories.enemies.EnemyTableRepo import EnemyTableRepo
from repositories.enemies.MapDataRepo import MapDataRepo
from repositories.master.Repository import Repository


class EnemyRepo(Repository[Enemy]):
	"""
	Required: EnemyDetailsRepo, EnemyNavRepo, BossDetailRepo, MapDataRepo, DropTableRepo
	"""

	@classmethod
	def initDependencies(cls):
		EnemyDetailsRepo.initialise(cls.codeReader)
		EnemyTableRepo.initialise(cls.codeReader)
		EnemyNavRepo.initialise(cls.codeReader)
		BossDetailRepo.initialise(cls.codeReader)
		MapDataRepo.initialise(cls.codeReader)
		DropTableRepo.initialise(cls.codeReader)

	@classmethod
	def generateRepo(cls) -> None:
		for enemy, data in EnemyDetailsRepo.items():
			drops = EnemyTableRepo.get(enemy)
			cls.add(enemy, Enemy(
				details = data,
				drops = drops.drops if drops else [],
				mapData = MapDataRepo.get(enemy),
				navigation = EnemyNavRepo.get(enemy),
				bossData = BossDetailRepo.get(enemy),
			))

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.get(name).details.Name

	@classmethod
	def compareVersions(cls, v1: IdleonReader, v2: IdleonReader, ignored: Set[str] = set()):
		return super().compareVersions(v1, v2, ignored = {"bossData", "navigation", "note"})
