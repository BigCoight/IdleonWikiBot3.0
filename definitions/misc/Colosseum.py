from typing import List

from pydantic import validator

from definitions.enemy.MapData import MapData
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo


class ColEnemy(IdleonModel):
	enemy: str
	qty: Integer
	platform: Integer
	baseScore: Integer

	def shouldCompare(self) -> bool:
		return False

	def compareKey(self) -> str:
		return self.enemy

	def __str__(self) -> str:
		return f"{self.qty}x {EnemyDetailsRepo.get(self.enemy).Name} ({self.baseScore})"


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

