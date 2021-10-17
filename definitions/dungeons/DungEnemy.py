from typing import Dict, Callable, Union

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo


class DungEnemy(IdleonModel):
	intName: str
	health: Integer
	damage: Integer
	credit1DR: float
	credit2DR: float
	cardVal: Integer
	coins: Integer
	itemDropChance: float
	cardDropChance: float

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"name": self.getEnemyName,
			"hp": "health",
			"dmg": "damage",
			"dcred": "credit1DR",
			"fcred": "credit2DR",
			"itemdr": "itemDropChance",
			"cdc": "cardDropChance",
			"coins": "coins",
		}

	def writeWiki(self, newLine = True) -> str:
		res = "{{DungeonEnemy"
		return res + super().writeWiki(False) + "}}"

	def getEnemyName(self):
		if not EnemyDetailsRepo.contains(self.intName):
			return ""
		return EnemyDetailsRepo.get(self.intName).Name

	def getCardDropChance(self):
		return "" if self.cardVal == -1 else self.cardDropChance
