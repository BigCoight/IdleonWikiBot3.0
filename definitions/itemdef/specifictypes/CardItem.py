from __future__ import annotations

from typing import Optional, Dict, Union, Callable

from definitions.itemdef.CardData import CardData
from definitions.itemdef.initialtypes.CommonItem import CommonItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.item.CardRepo import CardRepo
from repositories.item.ItemDetailRepo import ItemDetailRepo


class CardItem(BaseItem):
	cardData: Optional[CardData] = None

	@classmethod
	def fromItemDetails(cls, item: CommonItem) -> BaseItem:
		name = CardRepo.getName(item.internalID)
		if not name:
			dispName = "FILLER"
		elif name == "Crystal1":
			dispName = "Crystal Crabal Card"
		elif name == "Crystal2":
			dispName = "Crystal Cattle Card"
		elif name == "Crystal3":
			dispName = "Crystal Custard Card"

		#T
		elif ItemDetailRepo.contains(name):
			dispName = f"{ItemDetailRepo.getDisplayName(name)} Card"
		else:
			dispName = f"{EnemyDetailsRepo.get(name).Name} Card"

		cardData = CardRepo.get(name)

		return cls(
			internalName = item.internalID,
			displayName = dispName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			cardData = cardData,
		)

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = super().writeWiki()
		if self.cardData:
			res += self.cardData.writeWiki()
		return res

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {"title": "displayName"}
