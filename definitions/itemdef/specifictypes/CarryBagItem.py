from __future__ import annotations

from typing import Callable, Union, Dict

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from helpers.Constants import Constants
from helpers.CustomTypes import Integer


class CarryBagItem(DescItem):
	level: Integer

	@classmethod
	def getDesc(cls, item: EquipItem) -> str:
		baseDesc = "Hold down on this bag to increase the Carry Capacity of the following items to"
		upgrades = ", ".join(Constants.pouches.get(item.Class))
		description = f"{baseDesc} {item.lvReqToEquip}: {upgrades}"
		return description

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> CarryBagItem:
		return cls(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			description = cls.getDesc(item),
			level = item.ID)

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {"level": "level"}
		return {**base, **extra}
