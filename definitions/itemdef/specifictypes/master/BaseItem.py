from __future__ import annotations

from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.CommonItem import CommonItem
from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from repositories.item.CardRepo import CardRepo


class BaseItem(IdleonModel):
	internalName: str
	displayName: str
	sellPrice: Integer
	typeGen: TypeGen
	Type: str

	@classmethod
	def fromItemDetails(cls, item: CommonItem) -> BaseItem:
		return cls(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
		)

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"type": "Type",
			"hascard": self.doHasCard,
		}

	def doHasCard(self):
		return "yes" if CardRepo.contains(self.internalName) else ""

	def isFiller(self) -> bool:
		return self.displayName.lower() == 'filler'
