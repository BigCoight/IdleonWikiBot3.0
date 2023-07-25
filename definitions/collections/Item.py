from typing import Optional, List

from definitions.common.Note import Note
from definitions.itemdef.AnvilProduce import AnvilProduce
from definitions.itemdef.DetDrops import DetDrops
from definitions.itemdef.ItemSet import ItemSet
from definitions.itemdef.Recipe import Recipe
from definitions.itemdef.Sources import Sources
from definitions.itemdef.Vendors import ItemVendors
from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.master.IdleonModel import IdleonModel
from definitions.misc.world5.SlabItemSort import SlabItemSort


class Item(IdleonModel):
	item: BaseItem
	sources: Optional[Sources] = None
	notes: Optional[Note] = None
	recipe: Optional[Recipe] = None
	vendors: Optional[ItemVendors] = None
	anvilProduction: Optional[AnvilProduce] = None
	detDrops: Optional[DetDrops] = None
	slabSort: Optional[SlabItemSort] = None
	itemSet: Optional[ItemSet] = None

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		before = self.writeBefore()
		after = self.writeAfter()
		for _, subModel in self:
			if not subModel:
				continue
			if not isinstance(subModel, IdleonModel):
				continue
			before += subModel.writeBefore()
			after += subModel.writeAfter()

		res = ""
		writeBefore = filter(lambda x: x, before)
		for subModel in writeBefore:
			res += subModel.writeWiki()

		res += self.getCorrectHead()
		res += self.item.writeWiki()
		if self.recipe:
			res += f"|sellprice={self.recipe.sellPrice}\n"
		else:
			res += f"|sellprice={self.item.sellPrice}\n"
		if self.itemSet:
			res += self.itemSet.writeWiki()
		# if self.slabSort:
		# 	res += f"|order={self.slabSort.order}\n"
		# if self.sources:
		# 	res += self.sources.writeWiki()
		if self.notes:
			res += self.notes.writeWiki()
		res += "}}\n"

		writeAfter = filter(lambda x: x, after)
		for subModel in writeAfter:
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
		return [self.anvilProduction, self.detDrops]

	def writeBefore(self) -> List[IdleonModel]:
		return []
