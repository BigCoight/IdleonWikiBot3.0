from __future__ import annotations

from typing import Union

from definitions.itemdef.FishingToolkit import FishingToolkit
from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from repositories.item.FishingToolkitRepo import FishingToolkitRepo


class FishingTKItem(DescItem):
	fishingToolkit: FishingToolkit

	@classmethod
	def fromItemDetails(cls, item: Union[ConsumableItem, QuestItem]) -> BaseItem:
		fishingToolkit = FishingToolkitRepo.get(item.internalID)
		return cls(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			description = cls.getDesc(item),
			fishingToolkit = fishingToolkit)

	def writeWiki(self, newLine = True) -> str:
		res = super().writeWiki()
		res += self.fishingToolkit.writeWiki()
		return res
