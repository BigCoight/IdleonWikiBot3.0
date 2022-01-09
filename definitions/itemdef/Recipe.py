from typing import List, Optional, Dict, Union, Callable

from definitions.common.Component import Component
from definitions.common.Source import Source
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class DetRecipeComponent(IdleonModel):
	indent: Integer
	item: str
	quantity: Integer


class DetailedRecipe(IdleonModel):
	detRecipe: List[DetRecipeComponent]
	detRecipeTotals: List[Component] = []

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{detrecipe/tab\n|reci=\n"
		for comp in self.detRecipe:
			indent = 3 if comp.indent == 0 else comp.indent * 40
			res += "{{detrecipe" + f"|{indent}|{ItemDetailRepo.getDisplayName(comp.item)}|{comp.quantity}" + "}}\n"
		res += "|tot=\n"
		for comp in self.detRecipeTotals:
			res += "{{detrecipe/totals" + f"|{ItemDetailRepo.getDisplayName(comp.item)}|{comp.quantity}" + "}}\n"
		res += "}}\n"
		return res


class Recipe(IdleonModel):
	intID: str
	recipe: List[Component]
	levelReqToCraft: Integer
	expGiven: Integer
	no: Integer
	tab: Integer
	sellPrice: Integer = 0
	recipeFrom: List[Source] = []
	detailedRecipe: Optional[DetailedRecipe] = None

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{ForgeSlot\n"
		res += super().writeWiki()
		res += self.writeRecipe()
		res += "}}\n"
		res += self.detailedRecipe.writeWiki()
		return res

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"anvtab": self.getTab,
			"craftnum": "no",
			"levelreq": "levelReqToCraft",
			"expgiven": "expGiven",
			"recipefrom": self.getRecipeFrom
		}

	def getTab(self) -> str:
		return f"Anvil Tab {self.tab}"

	def writeRecipe(self) -> str:
		res = ""
		for i, comp in enumerate(self.recipe, 1):
			res += f"|resource{i}={ItemDetailRepo.getDisplayName(comp.item)}|quantity{i}={comp.quantity}\n"
		return res

	def getRecipeFrom(self) -> str:
		if not self.recipeFrom:
			return "Start"
		return ", ".join(map(lambda x: x.wikiName, self.recipeFrom))
