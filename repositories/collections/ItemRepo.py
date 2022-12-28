from definitions.collections.Item import Item
from repositories.item.AnvilRepo import AnvilRepo
from repositories.item.DetDropsRepo import DetDropsRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.item.sources.ItemNoteRepo import ItemNoteRepo
from repositories.item.sources.SourceRepo import SourceRepo
from repositories.master.Repository import Repository
from repositories.misc.world5.SlabItemSortRepo import SlabItemSortRepo


class ItemRepo(Repository[Item]):
	"""
	Dependent on: SpecificItemRepo, SourceRepo, RecipeRepo, VendorRepo, AnvilRepo, DetDropsRepo
	"""

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def initDependencies(cls, log = True):
		SpecificItemRepo.initialise(cls.codeReader, log)
		SourceRepo.initialise(cls.codeReader, log)
		RecipeRepo.initialise(cls.codeReader, log)
		VendorRepo.initialise(cls.codeReader, log)
		AnvilRepo.initialise(cls.codeReader, log)
		DetDropsRepo.initialise(cls.codeReader, log)
		ItemNoteRepo.initialise(cls.codeReader)
		SlabItemSortRepo.initialise(cls.codeReader)

	@classmethod
	def generateRepo(cls) -> None:
		for item, data in SpecificItemRepo.items():
			if sources := SourceRepo.get(item):
				if sources.recipeFrom:
					RecipeRepo.get(item).recipeFrom = sources.recipeFrom
			cls.add(item, Item(
				item = SpecificItemRepo.get(item),
				sources = SourceRepo.get(item),
				notes = ItemNoteRepo.get(item),
				recipe = RecipeRepo.get(item),
				vendors = VendorRepo.getVendorFromItem(item),
				anvilProduction = AnvilRepo.get(item),
				detDrops = DetDropsRepo.get(item),
				order = SlabItemSortRepo.get(item)
			))

	@classmethod
	def _ignore(cls, name: str, data: Item) -> bool:
		return SpecificItemRepo._ignore(name, data.item)

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return SpecificItemRepo.getDisplayName(name)
