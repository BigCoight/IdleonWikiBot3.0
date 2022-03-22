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

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{InfoEnemy\n"
		res += self.details.writeWiki()
		res += self.mapData.writeWiki() if self.mapData else ""
		res += self.navigation.writeWiki() if self.navigation else ""
		res += "}}\n"
		if self.drops:
			res += "{{DropTable/head|Droptable for " + self.details.Name + "}}\n"
			res += self.drops.writeWiki()
		return res
