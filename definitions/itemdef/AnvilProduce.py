from typing import Dict, Union, Callable

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class AnvilProduce(IdleonModel):
	item: str
	no: Integer
	time: Integer
	levelReq: Integer
	exp: Integer

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{ProductionSlot" + "\n"
		res += super().writeWiki(False)
		res += "}}"
		return res

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"lvlreq": "levelReq",
			"num": "no",
			"expcraft": "exp",
			"time": "time"
		}

	def isFiller(self) -> bool:
		return ItemDetailRepo.get(self.item).displayName == "Filler"
