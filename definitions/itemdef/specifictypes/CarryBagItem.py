from __future__ import annotations

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from helpers.Constants import Constants


class CarryBagItem(DescItem):

	@classmethod
	def getDesc(cls, item: EquipItem) -> str:
		baseDesc = "Hold down on this bag to increase the Carry Capacity of the following items to"
		upgrades = ", ".join(Constants.pouches.get(item.Class))
		description = f"{baseDesc} {item.lvReqToEquip}: {upgrades}"
		return description
