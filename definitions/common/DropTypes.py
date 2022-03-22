from __future__ import annotations

import string
from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import formatFloat, isTalent, isRecipe
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.npc.NpcRepo import NpcRepo
from repositories.talents.TalentNameRepo import TalentNameRepo


class Drop(IdleonModel):
	item: str
	quantity: Numeric
	chance: float
	questLink: str

	def hasDropTableExtra(self) -> bool:
		return True

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = self.writeDrop()
		if self.questLink != "N/A":
			questName = NpcRepo.getQuestByName(self.questLink)
			npcName = self.questLink.rstrip(string.digits)
			displayed = f"[[{npcName}#{questName}|{npcName}]]"
			res += f"|special=({displayed})"
		return res

	def __str__(self) -> str:
		res = ""
		if self.quantity != 1:
			res += f"{self.quantity}x "
		res += "{{CraftReq|"
		res += SpecificItemRepo.getDisplayName(self.item) + "}}"
		res += f" ({formatFloat(self.chance)})"
		return res

	def shouldCompare(self) -> bool:
		return False

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

	def hasDropTableExtra(self) -> bool:
		return False

	def writeDrop(self):
		res = "{{DropTable/append|"
		res += f"{self.item}|{formatFloat(self.chance)}|{self.quantity}"
		return res

	def __str__(self) -> str:
		return f"{self.quantity}x " + self.item + f" {self.chance:g}"


class CardDrop(Drop):

	def writeDrop(self):
		res = "{{DropTable"
		res += f"/card|{formatFloat(self.chance)}"
		return res


class CoinDrop(Drop):

	def writeDrop(self):
		res = "{{DropTable"
		res += f"/coin|{self.quantity}|{formatFloat(self.chance)}"
		return res

	def __str__(self) -> str:
		return f"{self.quantity}x " + "Coins" + f" {self.chance:g}"


class TalentDrop(Drop):

	def writeDrop(self):
		qty = str(self.quantity)
		no = int(qty[0])
		index = int(qty[1: no + 1])
		res = "{{DropTable/talent|"
		talent = TalentNameRepo.getList(index).name
		res += f"{talent}|{formatFloat(self.chance)}"
		return res

	def __str__(self) -> str:
		qty = str(self.quantity)
		no = int(qty[0])
		index = int(qty[1: no + 1])
		talent = TalentNameRepo.getList(index).name
		return f"{self.quantity}x " + f"{talent} Talent Book" + f" {self.chance:g}"


class RecipeDrop(Drop):

	def writeDrop(self):
		tab = int(self.item[-1]) - 1
		index = int(self.quantity)
		item = ItemDetailRepo.getDisplayName(RecipeRepo.getItemAtIndex(tab, index))
		res = "{{DropTable/recipe|"
		res += f"{tab + 1}|{item}|{formatFloat(self.chance)}"
		return res

	def __str__(self) -> str:
		tab = int(self.item[-1]) - 1
		index = int(self.quantity)
		item = ItemDetailRepo.getDisplayName(RecipeRepo.getItemAtIndex(tab, index))
		res = "{{CraftReq|" + item + "}}"
		return f"{self.quantity}x " + f"{res} Recipe" + f" {self.chance:g}"


class ItemDrop(Drop):

	def writeDrop(self):
		res = "{{DropTable"
		displayName = ItemDetailRepo.getDisplayName(self.item)
		res += f"|{displayName}|{formatFloat(self.chance)}|{self.quantity}"
		return res
