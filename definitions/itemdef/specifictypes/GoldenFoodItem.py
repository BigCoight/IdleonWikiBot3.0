from __future__ import annotations

from typing import Union, List

from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import replaceUnderscores


class GoldenFoodData(IdleonModel):
	effect: str
	amount: Integer

	def writeWiki(self, newLine = True) -> str:
		res = "{{gfoodbonus|"
		res += f"{self.amount}|{self.effect}"
		res += "}}\n"
		return res


class GoldenFoodItem(DescItem):
	goldenFoodData: GoldenFoodData

	@classmethod
	def fromItemDetails(cls, item: ConsumableItem) -> GoldenFoodItem:
		effect = replaceUnderscores(item.desc_line1 + " " + item.desc_line2)
		return GoldenFoodItem(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			description = cls.getDesc(item),
			goldenFoodData = GoldenFoodData(
				effect = effect,
				amount = item.Amount
			)
		)

	@classmethod
	def getDesc(cls, item: Union[ConsumableItem, QuestItem]) -> str:
		effect = replaceUnderscores(item.desc_line1 + " " + item.desc_line2)
		desc = replaceUnderscores(effect.split(" by")[0])
		return f"{desc}. {replaceUnderscores(item.desc_line3)}"

	def writeAfter(self) -> List[IdleonModel]:
		return [self.goldenFoodData]
