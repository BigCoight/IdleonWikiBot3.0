from __future__ import annotations

from typing import Union, Dict, Callable

from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from helpers.HelperFunctions import replaceUnderscores


class DescItem(BaseItem):
	description: str

	@classmethod
	def fromItemDetails(cls, item: Union[ConsumableItem, QuestItem]) -> BaseItem:
		return cls(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			description = cls.getDesc(item))

	@classmethod
	def getDesc(cls, item: Union[ConsumableItem, QuestItem]) -> str:
		res = ""
		for line in [item.desc_line1, item.desc_line2, item.desc_line3, item.desc_line4, item.desc_line5,
		             item.desc_line6, item.desc_line7, item.desc_line8]:
			if line != "Filler":
				res += replaceUnderscores(line) + " "
		return res

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {"description": "description"}
		return {**base, **extra}
