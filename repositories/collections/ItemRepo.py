from definitions.collections.Item import Item
from repositories.item.AnvilRepo import AnvilRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SourceRepo import SourceRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.master.Repository import Repository


class ItemRepo(Repository[Item]):
	"""
	Dependent on: SpecificItemRepo, SourceRepo, RecipeRepo, VendorRepo, AnvilRepo
	"""

	@classmethod
	def generateRepo(cls) -> None:
		for item, data in SpecificItemRepo.items():
			if sources := SourceRepo.get(item):
				if sources.recipeFrom:
					RecipeRepo.get(item).recipeFrom = sources.recipeFrom

			cls.add(item, Item(
				item = SpecificItemRepo.get(item),
				sources = SourceRepo.get(item),
				recipe = RecipeRepo.get(item),
				vendors = VendorRepo.get(item),
				anvilProduction = AnvilRepo.get(item)
			))

	@classmethod
	def getWikiName(cls, name: str, data: Item) -> str:
		return data.item.displayName
