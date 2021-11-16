from __future__ import annotations

from typing import Union, Dict, Callable

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from helpers.CustomTypes import Integer
from repositories.misc.StorageOrderRepo import StorageOrderRepo


class ChestItem(DescItem):
	order: Integer
	level: Integer

	@classmethod
	def fromItemDetails(cls, item: Union[EquipItem]) -> BaseItem:
		return cls(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			order = StorageOrderRepo.get(item.internalID).order + 1,
			description = cls.getDesc(item),
			level = item.lvReqToEquip, )

	@classmethod
	def getDesc(cls, item: EquipItem) -> str:
		return (f"Hold down to permanently add +{item.lvReqToCraft} Slots to your Storage Chest. Can only be used "
		        "once.")

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {"internalid": "order", "level": "level"}
		return {**base, **extra}
