from typing import Dict, Union, Callable

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class ActiveTalent(IdleonModel):
	name: str
	K: Numeric
	D: Numeric
	s: Numeric
	cooldown: Integer
	castTime: Numeric
	manaCost: Integer
	inputReq: Integer
	AFKrange: Integer
	AFKtype: str
	AFKactivity: Integer

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"cooldown": "cooldown",
			"actiontime": "castTime",
			"manacost": "manaCost",
		}
