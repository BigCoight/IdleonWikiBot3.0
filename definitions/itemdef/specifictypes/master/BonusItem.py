from __future__ import annotations

from typing import Union, Dict, Callable

from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem


class BonusItem(DescItem):
	bonus: str

	@classmethod
	def fromItemDetails(cls, item: Union[ConsumableItem, QuestItem]) -> BaseItem:
		return cls(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			description = cls.getDesc(item),
			bonus = cls.getBonus(item))

	@classmethod
	def getBonus(cls, item: Union[ConsumableItem, QuestItem]) -> str:
		raise NotImplementedError

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {"bonus": "bonus"}
		return {**base, **extra}
