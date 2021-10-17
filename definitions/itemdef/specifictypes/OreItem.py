from __future__ import annotations

from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem


class OreItem(DescItem):

	@classmethod
	def getDesc(cls, item: ConsumableItem) -> str:
		baseDesc = super().getDesc(item)
		baseDesc = baseDesc.replace("[", f"{item.Amount}").replace("]", f"{item.Cooldown} Seconds")
		return baseDesc
