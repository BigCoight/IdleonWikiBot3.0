from __future__ import annotations

from typing import Union, Dict, Callable

from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from helpers.HelperFunctions import replaceUnderscores


class StoneItem(DescItem):
	tier: str

	@classmethod
	def fromItemDetails(cls, item: Union[ConsumableItem, QuestItem]) -> BaseItem:
		try:
			tier = item.displayName.split("Upgrade Stone ")[1]
		except IndexError:
			tier = item.displayName.split(" Upgrade Stone")[0].split(" ")[0]
		return cls(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			description = cls.getDesc(item),
			tier = tier)

	@classmethod
	def getDesc(cls, item: ConsumableItem) -> str:
		baseDesc = super().getDesc(item)
		before, after = baseDesc.split(".", 1)
		effects = item.Effect.split(".")
		formattedEffects = []
		for effect in effects:
			e, n = effect.split(",")
			formattedEffects.append(f"+{n} {replaceUnderscores(e)}")
		formattedEffects = ", ".join(formattedEffects)
		after = after.replace("*", f"{item.Amount}").replace("#", f"{item.Trigger}")
		return f"{before}. {formattedEffects}.{after}"

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {"tier": "tier"}
		return {**base, **extra}
