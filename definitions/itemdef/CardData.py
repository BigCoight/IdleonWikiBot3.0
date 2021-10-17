from typing import Dict, Union, Callable

from pydantic import validator

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer
from helpers.HelperFunctions import replaceUnderscores


class CardData(IdleonModel):
	cardID: str
	category: str
	perTier: float
	effect: str
	bonus: Numeric
	order: Integer

	@validator("effect", pre = True)
	def repU(cls, v: str) -> str:
		return replaceUnderscores(v)

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"order": "order",
			"category": "category",
			"effect": "effect",
			"bonus": "bonus",
			"reqtier": "perTier"
		}
