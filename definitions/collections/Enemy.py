from typing import Optional

from definitions.enemy.BossDetails import BossDetails
from definitions.enemy.EnemyDetails import EnemyDetails
from definitions.enemy.EnemyNav import EnemyNav
from definitions.enemy.EnemyTable import EnemyTable
from definitions.enemy.MapData import MapData
from definitions.master.IdleonModel import IdleonModel


class Enemy(IdleonModel):
	details: EnemyDetails
	drops: Optional[EnemyTable] = None
	mapData: Optional[MapData] = None
	navigation: Optional[EnemyNav] = None
	bossData: Optional[BossDetails] = None

	def wikiWriterKey(self) -> str:
		res = "{{InfoEnemy\n"
		res += self.details.wikiWriterKey()
		res += self.mapData.wikiWriterKey() if self.mapData else ""
		res += self.navigation.wikiWriterKey() if self.navigation else ""
		res += "|}\n"
		res += self.drops.wikiWriterKey()
		return res
