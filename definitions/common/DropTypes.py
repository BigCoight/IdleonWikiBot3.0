from __future__ import annotations

from typing import List

from definitions.master.CollectionModel import CollectionModel
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import formatFloat, isTalent, isRecipe
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.talents.TalentNameRepo import TalentNameRepo


class Drop(CollectionModel):
	item: str
	quantity: Numeric
	chance: float
	questLink: str

	def wikiWriterKey(self):
		res = self.writeDrop()
		if self.questLink != "N/A":
			res += f"|special={self.questLink}"
		return res

	def writeDrop(self) -> str:
		raise NotImplementedError

	@classmethod
	def arrayToDropType(cls, drop: List[str]) -> Drop:
		currentType = ItemDrop
		if isRecipe(drop[0]):
			currentType = RecipeDrop
		elif isTalent(drop[0]):
			currentType = TalentDrop
		elif drop[0] == "COIN":
			currentType = CoinDrop
		elif drop[0][:5] == "Cards":
			currentType = CardDrop
		elif "DropTable" in drop[0]:
			currentType = SubTableDrop
		return currentType(
			item = drop[0],
			quantity = drop[2],
			chance = drop[1],
			questLink = drop[3])


class SubTableDrop(Drop):

	def writeDrop(self):
		res = "{{DropTable/append|"
		res += f"{self.item}|{formatFloat(self.chance)}|{self.quantity}"
		return res


class CardDrop(Drop):

	def writeDrop(self):
		res = "{{DropTable"
		res += f"/card|{formatFloat(self.chance)}"
		return res


class CoinDrop(Drop):

	def writeDrop(self):
		res = "{{DropTable"
		res += f"/coin|{formatFloat(self.chance)}|{self.quantity}"
		return res


class TalentDrop(Drop):

	def writeDrop(self):
		qty = str(self.quantity)
		no = int(qty[0])
		index = int(qty[1: no + 1])
		res = "{{DropTable/talent|"
		talent = TalentNameRepo.get(index).name
		res += f"{talent}|{formatFloat(self.chance)}"
		return res


class RecipeDrop(Drop):

	def writeDrop(self):
		tab = int(self.item[-1]) - 1
		index = int(self.quantity) + 1
		item = ItemDetailRepo.getDisplayName(RecipeRepo.getItemAtIndex(tab, index))
		res = "{{DropTable/recipe|"
		res += f"{item}|{formatFloat(self.chance)}"
		return res


class ItemDrop(Drop):

	def writeDrop(self):
		res = "{{DropTable"
		displayName = ItemDetailRepo.getDisplayName(self.item)
		res += f"|{displayName}|{formatFloat(self.chance)}|{self.quantity}"
		return res
