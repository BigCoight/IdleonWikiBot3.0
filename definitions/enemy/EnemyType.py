from enum import Enum
from typing import Callable

from definitions.common.EnumMeta import CheckIn


class EnemyType(str, Enum, metaclass = CheckIn):
	monsterType = "Monster Type"
	oreType = "Ore Type"
	treeType = "Tree Type"
	fishType = "Fish Type"
	bugType = "Bug Type"

	def detDropName(self) -> Callable[[str], str]:
		skillSources = {
			self.oreType: lambda x: f"Mining#Drops|Mining {x}",
			self.treeType: lambda x: f"Choppin#Drops|Choppin {x}",
			self.fishType: lambda x: f"Fishing#Drops|Fishing {x}",
			self.bugType: lambda x: f"Catching#Drops|Catching {x}",
		}
		return skillSources[self]
