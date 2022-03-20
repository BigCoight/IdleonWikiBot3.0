from __future__ import annotations

from typing import Union, List

from definitions.itemdef.StatueData import StatueData
from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.BonusItem import BonusItem
from definitions.master.IdleonModel import IdleonModel
from repositories.item.StatueRepo import StatueRepo


class StatueItem(BonusItem):
	@classmethod
	def getBonus(cls, item: Union[ConsumableItem, QuestItem]) -> str:
		statueData = StatueRepo.get(f"{item.ID}")
		return statueData.effect.replace("@", "")

	statueData: StatueData

	@classmethod
	def fromItemDetails(cls, item: Union[ConsumableItem, QuestItem]) -> BaseItem:
		statueData = StatueRepo.get(f"{item.ID}")
		return cls(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			description = cls.getDesc(item),
			statueData = statueData,
			bonus = cls.getBonus(item)
		)

	def writeAfter(self) -> List[IdleonModel]:
		return [self.statueData]
