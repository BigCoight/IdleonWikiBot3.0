from __future__ import annotations

from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem


class ChestItem(DescItem):

	@classmethod
	def getDesc(cls, item: ConsumableItem) -> str:
		return (f"Hold down to permanently add +{item.lvReqToCraft} Slots to your Storage Chest. Can only be used "
		        "once.")
