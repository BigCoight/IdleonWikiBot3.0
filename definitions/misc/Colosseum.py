from typing import List

from definitions.enemy.MapData import MapData
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class ColEnemy(IdleonModel):
	enemy: str
	qty: Integer
	platform: Integer
	baseScore: Integer

class ColWave(IdleonModel):
	enemies: List[ColEnemy]

class Colosseum(IdleonModel):
	name: str
	map: Integer
	node: Integer
	colMap: Integer
	keyCost: Integer
	infoX: Numeric
	infoY: Numeric
	bronzeScore: Numeric
	silverScore: Numeric
	goldScore: Numeric
	bronzeNode: Numeric
	silverNode: Numeric
	goldNode: Numeric
	bronzeX: Numeric
	silverX: Numeric
	goldX: Numeric
	waves: List[ColWave]

