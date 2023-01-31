from typing import Union, Callable, Dict

from definitions.master.IdleonModel import IdleonModel
from helpers.Constants import Constants
from helpers.CustomTypes import Integer


class NpcHead(IdleonModel):
	location: str
	world: str
	noQuest: Integer
	repeatable: str
	type: str
	birthWeight: Union[float, Integer]
	starSign: str
	mothersMaidenName: str
	notes: str

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"world": "world",
			"location": "location",
			"noquest": "noQuest",
			"npcType": "type",
			"repeatable": "repeatable",
			"birthweight": "birthWeight",
			"starsign": "starSign",
			"mmm": "mothersMaidenName",
			"notes": self.getNotes,
		}

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{npc\n"
		res += super().writeWiki()
		res += "}}"
		return res

	def getNotes(self) -> str:
		return self.notes.replace(Constants.newLineRep, "\n")
