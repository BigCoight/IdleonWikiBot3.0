from typing import Set

from pywikibot import Site, Page

from definitions.collections.Enemy import Enemy
from definitions.enemy.AFKType import AFKType
from definitions.enemy.EnemyType import EnemyType
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
		print(tempSet)

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.get(name).details.Name

	@classmethod
	def compareVersions(cls, v1: IdleonReader, v2: IdleonReader, ignored: Set[str] = set()):
		return super().compareVersions(v1, v2, ignored = {"bossData", "navigation", "note"})

	@classmethod
	def _ignore(cls, name: str, data: Enemy) -> bool:
		if "Dung" in name:
			return True
		if name in {"EXP", "Blank", "LockedInvSpace", "COIN", "TalentBook1", "TalentBook2",
		            "TalentBook3", "TalentBook4", "TalentBook5", "SmithingRecipes1", "SmithingRecipes2",
		            "SmithingRecipes3", "SmithingRecipes4", "ExpSmith1", "Quest8", "EquipmentShirts8", "FoodHealth1d",
		            "FoodHealth2d", "FoodHealth3d", "PremiumGem", "Quest49"}:
			return True
		if name[:3] == "Gem":
			return True
		if data.details.Type != EnemyType.monsterType:
			return True
		if data.details.AFKtype != AFKType.Fighting:
			return True
		if data.bossData is not None:
			return True
		if data.mapData is None:
			return True
		if data.navigation is None:
			return True
		if cls._ignoreW4(name, data):
			return True
		return False

	@classmethod
	def _ignoreW4(cls, name: str, data: Enemy) -> bool:
		website = Site()
		page = Page(website, data.details.Name)
		return not page.exists()
