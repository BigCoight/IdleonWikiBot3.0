from typing import Union, Callable, Dict

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class NpcHead(IdleonModel):
	location: str
	world: str
	noQuest: Integer
	repeatable: str
	birthWeight: Union[float, Integer]
	starSign: str
	mothersMaidenName: str
	notes: str

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"world": "world",
			"location": "location",
			"noquest": "noQuest",
			"repeatable": "repeatable",
			"birthweight": "birthWeight",
			"starsign": "starSign",
			"mmm": "mothersMaidenName",
			"notes": "notes",
		}

	def writeWiki(self, newLine = True) -> str:
		res = "{{npc\n"
		res += super().writeWiki()
		res += "}}"
		return res
