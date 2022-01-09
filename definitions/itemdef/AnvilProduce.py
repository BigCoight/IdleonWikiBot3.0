from typing import Dict, Union, Callable

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class AnvilProduce(IdleonModel):
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
