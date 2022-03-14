from typing import List

from definitions.master.IdleonModel import IdleonModel
from definitions.misc.world4.TerritoryEnemy import TerritoryEnemy


class InfiniteTerritory(IdleonModel):
	enemies: List[TerritoryEnemy]
