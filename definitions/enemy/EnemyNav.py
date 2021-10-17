from typing import Optional, Dict, Union, Callable

from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo


class EnemyNav(IdleonModel):
	prev: Optional[str] = None
	next: Optional[str] = None
	hasCrystal: bool = False
	crystalName: Optional[str] = None
	hasCard: bool = False

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			# "world": "World",
			# "defence0": "defFor0",
			"crystal": self.getHasCrystal,
			"crystalname": self.getCrystalname,
			"hascard": self.getHasCard,
			"nextenemy": self.getNext,
			"prevenemy": self.getPrev,
		}

	def getPrev(self):
		if self.prev:
			return EnemyDetailsRepo.get(self.prev).Name
		return ""

	def getNext(self):
		if self.next:
			return EnemyDetailsRepo.get(self.next).Name
		return ""

	def getHasCard(self):
		return "yes" if self.hasCard else "no"

	def getHasCrystal(self):
		return "yes" if self.hasCrystal else "no"

	def getCrystalname(self):
		if self.crystalName:
			return EnemyDetailsRepo.get(self.crystalName).Name
		return ""

