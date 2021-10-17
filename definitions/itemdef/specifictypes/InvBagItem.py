from __future__ import annotations

from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem


class InvBagItem(DescItem):

	@classmethod
	def getDesc(cls, item: ConsumableItem) -> str:
		return f"Hold down to permanently add +{item.lvReqToCraft} Slots to your Inventory. Can only be used once."
