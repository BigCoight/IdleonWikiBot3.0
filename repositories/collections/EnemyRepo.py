from typing import Set

from definitions.collections.Enemy import Enemy
from helpers.CodeReader import IdleonReader
from helpers.HelperFunctions import ignoreWorld6
from repositories.enemies.BossDetailRepo import BossDetailRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.enemies.EnemyNavRepo import EnemyNavRepo
from repositories.enemies.EnemyNoteRepo import EnemyNoteRepo
from repositories.enemies.EnemyTableRepo import EnemyTableRepo
from repositories.enemies.MapDataRepo import MapDataRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.master.Repository import Repository


class EnemyRepo(Repository[Enemy]):
	"""
	Required: EnemyDetailsRepo, EnemyNavRepo, BossDetailRepo, MapDataRepo, DropTableRepo
	"""

	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def initDependencies(cls, log = True):
		SpecificItemRepo.initialise(cls.codeReader, log)
		RecipeRepo.initialise(cls.codeReader, log)
		EnemyDetailsRepo.initialise(cls.codeReader, log)
		EnemyTableRepo.initialise(cls.codeReader, log)
		EnemyNavRepo.initialise(cls.codeReader, log)
		BossDetailRepo.initialise(cls.codeReader, log)
		MapDataRepo.initialise(cls.codeReader, log)
		DropTableRepo.initialise(cls.codeReader, log)
		EnemyNoteRepo.initialise(cls.codeReader)

	@classmethod
	def generateRepo(cls) -> None:
		tempSet = set()
		for enemy, data in EnemyDetailsRepo.items():
			cls.add(enemy, Enemy(
				details = data,
				drops = EnemyTableRepo.get(enemy),
				mapData = MapDataRepo.get(enemy),
				navigation = EnemyNavRepo.get(enemy),
				bossData = BossDetailRepo.get(enemy),
			))
			tempSet.add(data.AFKtype)

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.get(name).details.Name

	@classmethod
	def compareVersions(cls, v1: IdleonReader, v2: IdleonReader, ignored: Set[str] = set(), useIgnore = True):
		return super().compareVersions(v1, v2, ignored = {
			"bossData",
			"navigation",
			"note",
			"AFKtype",
			"MonsterFace",
			"MonsterOffsetX",
			"MonsterOffsetY",
			"HeightOfMonster",
			"MonsterMoving",
			"MovingFrame",
			"DeathFrame",
			"Type",
		},
		                               useIgnore = False)

	@classmethod
	def _ignore(cls, name: str, data: Enemy) -> bool:
		if data.bossData is not None:
			return True
		if data.mapData is None or data.navigation is None:
			return True
		return EnemyDetailsRepo._ignore(name, data.details) or ignoreWorld6(cls.getWikiName(name))
