from definitions.collections.Enemy import Enemy
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
		EnemyNavRepo.initialise(cls.codeReader)
		BossDetailRepo.initialise(cls.codeReader)
		MapDataRepo.initialise(cls.codeReader)
		DropTableRepo.initialise(cls.codeReader)

	@classmethod
	def generateRepo(cls) -> None:
		cls.initDependencies()
		for enemy, data in EnemyDetailsRepo.items():
			cls.add(enemy, Enemy(
				details = data,
				drops = EnemyTableRepo.get(enemy),
				mapData = MapDataRepo.get(enemy),
				navigation = EnemyNavRepo.get(enemy),
				bossData = BossDetailRepo.get(enemy),
			))
