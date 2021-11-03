from definitions.collections.Item import Item
from repositories.item.AnvilRepo import AnvilRepo
from repositories.item.DetDropsRepo import DetDropsRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.item.sources.ItemNoteRepo import ItemNoteRepo
from repositories.item.sources.SourceRepo import SourceRepo
from repositories.master.Repository import Repository


class ItemRepo(Repository[Item]):
	"""
	Dependent on: SpecificItemRepo, SourceRepo, RecipeRepo, VendorRepo, AnvilRepo, DetDropsRepo
	"""

	@classmethod
	def initDependencies(cls):
		SpecificItemRepo.initialise(cls.codeReader)
		SourceRepo.initialise(cls.codeReader)
		RecipeRepo.initialise(cls.codeReader)
		VendorRepo.initialise(cls.codeReader)
		AnvilRepo.initialise(cls.codeReader)
		DetDropsRepo.initialise(cls.codeReader)
		ItemNoteRepo.initialise(cls.codeReader)

	@classmethod
	def generateRepo(cls) -> None:
		cls.initDependencies()
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
				detDrops = DetDropsRepo.get(item)
			))

	@classmethod
	def _ignore(cls, name: str, data: Item) -> bool:
		if "Dung" in name:
			return True
		if name in {"EXP", "Blank", "LockedInvSpace", "COIN", "TalentBook1", "TalentBook2",
		            "TalentBook3", "TalentBook4", "TalentBook5", "SmithingRecipes1", "SmithingRecipes2",
		            "SmithingRecipes3", "SmithingRecipes4", "ExpSmith1", "Quest8", "EquipmentShirts8", "FoodHealth1d",
		            "FoodHealth2d", "FoodHealth3d", "PremiumGem"}:
			return True
		if name[:3] == "Gem":
			return True
		if data.item.displayName in {"Filler", "FILLER", "Blank"}:
			return True
		return False

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return SpecificItemRepo.getDisplayName(name)
