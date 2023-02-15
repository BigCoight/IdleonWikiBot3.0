from typing import Dict, Union, Callable

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class GemShopItem(IdleonModel):
	section: str
	name: str
	itemName: str
	desc: str
	cost: Integer
	no: Integer
	maxPurchases: Integer
	qty: Integer
	costIncrement: Integer

	def sortKey(self) -> str:
		return self.section

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		return "{{GemshopData\n" + super().writeWiki(newLine, ignoreZero) + "}}"

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"section": "section",
			"name": "name",
			"itemName": "itemName",
			"description": "desc",
			"cost": "cost",
			"maxPurchases": "maxPurchases",
			"costIncrement": "costIncrement",
		}
