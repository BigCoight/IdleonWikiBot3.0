from typing import Optional, List

from definitions.itemdef.AnvilProduce import AnvilProduce
from definitions.itemdef.Recipe import Recipe
from definitions.itemdef.Sources import Sources
from definitions.itemdef.Vendors import Vendors
from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.master.IdleonModel import IdleonModel


class Item(IdleonModel):
	item: BaseItem
	sources: Optional[Sources] = None
	recipe: Optional[Recipe] = None
	vendors: Optional[Vendors] = None
	anvilProduction: Optional[AnvilProduce] = None

	def writeWiki(self, newLine = True) -> str:
		res = self.getCorrectHead()
		res += self.item.writeWiki()
		if self.recipe:
			res += f"|sellprice={self.recipe.sellPrice}"
		else:
			res += f"|sellprice={self.item.sellPrice}"
		if self.sources:
			res += self.sources.writeWiki()
		res += "}}\n"

		toWrite = filter(lambda x: x, self.item.writeAfter() + self.writeAfter())
		for subModel in toWrite:
			res += subModel.writeWiki()
		return res

	def getCorrectHead(self) -> str:
		if self.item.typeGen == TypeGen.dCard:
			return "{{InfoCard\n"
		if self.item.typeGen == TypeGen.dFishToolkit:
			return "{{Fishingaccessory\n"
		if self.item.typeGen == TypeGen.aStamp:
			return "{{InfoStamp\n"
		return "{{InfoItem\n"

	def writeAfter(self) -> List[IdleonModel]:
		return [self.recipe, self.vendors, self.anvilProduction]
