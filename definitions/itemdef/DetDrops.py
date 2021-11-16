from typing import List

from definitions.enemy.EnemyType import EnemyType
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import formatFloat
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo


class DetDrop(IdleonModel):
	source: str
	quantity: Numeric
	chance: float

	def writeWiki(self, newLine = True) -> str:
		res = "{{detdrops|"
		res += f"[[{self.detDropName()}]]|{formatFloat(self.chance)}|{self.quantity}"
		res += "}}"
		return res

	def detDropName(self) -> str:
		enemy = EnemyDetailsRepo.get(self.source)
		enemName = enemy.Name
		if enemy.Type == EnemyType.monsterType:
			return enemName
		return enemy.Type.detDropName()(enemName)


class DetDrops(IdleonModel):
	sources: List[DetDrop]

	def writeWiki(self, newLine = True) -> str:
		res = "{{detdrops/head}}\n"
		for detDrop in self.sources:
			res += detDrop.writeWiki() + "\n"
		res += "|}"
		return res
