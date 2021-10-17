from __future__ import annotations

from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from helpers.HelperFunctions import replaceUnderscores


class StoneItem(DescItem):

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
