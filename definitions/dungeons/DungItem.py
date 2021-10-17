from typing import Dict, Union, Callable

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class DungItem(IdleonModel):
	name: str
	bonus: str
	increment: float
	rarity: str
	desc: str
	lvlText: str
	baseValue: float
	maxLevel: Integer

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"name": "name",
			"desc": self.getDesc,
			"increment": self.getLvlText,
			"rarity": "rarity",
			"maxlvl": "maxLevel"
		}

	def writeWiki(self, newLine = True) -> str:
		res = "{{RNGItem"
		res += super().writeWiki(False)
		return res + "}}"

	def getDesc(self):
		return self.desc.replace("{", f"{self.baseValue:g}")

	def getLvlText(self):
		numAdded = self.lvlText.replace("{", f"{self.increment:g}")
		splitted = numAdded.split(": ")
		if len(splitted) > 1:
			return splitted[1]
		return numAdded
