from definitions.common.Component import Component
from definitions.common.Source import Source
from definitions.itemdef.Sources import Sources
from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.questdef.QuestType import QuestType
from helpers.Constants import Constants
from helpers.HelperFunctions import isRecipe
from repositories.GemShopRepo import GemShopRepo
from repositories.PostOfficeRepo import PostOfficeRepo
from repositories.TaskUnlocksRepo import TaskUnlocksRepo
from repositories.dungeons.FlurboShopRepo import FlurboShopRepo
from repositories.dungeons.KeychainBonusRepo import KeychainBonusRepo
from repositories.enemies.DropTableRepo import DropTableRepo
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.enemies.EnemyTableRepo import EnemyTableRepo
from repositories.item.AnvilRepo import AnvilRepo
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.RefineryCostRepo import RefineryCostRepo
from repositories.item.VendorRepo import VendorRepo
from repositories.item.sources.CustomSourceRepo import CustomSourceRepo
from repositories.master.Repository import Repository
from repositories.npc.NpcRepo import NpcRepo


class SourceRepo(Repository[Sources]):
	"""
	Dependent On: DropTableRepo, EnemyDetailsRepo, PostOfficeRepo, GemShopRepo, EnemyTableRepo, ITemDetailRepo,
	RecipeRepo, RefineryCostRepo, VendorRepo, FlurboShopRepo, KeychainBonusRepo
	"""

	@classmethod
	def excludeDefaults(cls) -> bool:
		return True

	@classmethod
	def generateRepo(cls) -> None:
		cls.addRecipes()
		cls.addEnemyDroptables()
		cls.addRefinery()
		cls.addPostOffice()
		cls.addVendors()
		cls.addDroptables()
		cls.addQuestRewards()
		cls.addTaskUnlocks()
		cls.addGemShop()
		cls.addSkilling()
		cls.addAnvil()
		cls.addFlurboShop()
		cls.addKeychains()

		for item, sources in CustomSourceRepo.items():
			for source in sources.sources:
				cls.addToSource(item, source)
			for source in sources.recipeFrom:
				cls.addToRecipeFrom(item, source)
			for source in sources.questAss:
				cls.addToQuestAss(item, source)

	@classmethod
	def addAnvil(cls):
		for item, _ in AnvilRepo.items():
			if not ItemDetailRepo.contains(item):
				continue
			cls.addToSource(item, Source(
				wikiName = "[[Smithing#Production items|Anvil Production]]",
				txtName = "Anvil Production"
			))

	@classmethod
	def addFlurboShop(cls):
		for item, _ in FlurboShopRepo.items():
			if not ItemDetailRepo.contains(item):
				continue
			if "Key" == item[:3]:
				continue
			cls.addToSource(item, Source(
				wikiName = "[[Dungeons#Flurbo Shop|Flurbo Shop]]",
				txtName = "Flurbo Shop"
			))

	@classmethod
	def addKeychains(cls):
		for item, _ in KeychainBonusRepo.items():
			if not ItemDetailRepo.contains(item):
				continue
			cls.addToSource(item, Source(
				wikiName = "[[Dungeons#Flurbo Shop|Flurbo Shop]]",
				txtName = "Flurbo Shop"
			))
			cls.addToSource(item, Source(
				wikiName = "[[Dungeons#Loot Rolls|Dungeon Loot Rolls]]",
				txtName = "Flurbo Shop"
			))

	@classmethod
	def addSkilling(cls):
		for item, data in ItemDetailRepo.items():
			if data.typeGen == TypeGen.bOre:
				cls.addToSource(item, Source(
					wikiName = "[[Mining]]",
					txtName = "Mining"
				))
			elif data.typeGen == TypeGen.bBar:
				cls.addToSource(item, Source(
					wikiName = "[[Forging]]",
					txtName = "Forging"
				))
			elif data.typeGen == TypeGen.bLog:
				cls.addToSource(item, Source(
					wikiName = "[[Choppin]]",
					txtName = "Choppin"
				))
			elif data.typeGen == TypeGen.dFish:
				cls.addToSource(item, Source(
					wikiName = "[[Fishing]]",
					txtName = "Fishing"
				))
			elif data.typeGen == TypeGen.dCritters:
				cls.addToSource(item, Source(
					wikiName = "[[Trapping]]",
					txtName = "Trapping"
				))
			elif data.typeGen == TypeGen.dSouls:
				cls.addToSource(item, Source(
					wikiName = "[[Worship]]",
					txtName = "Worship"
				))
			elif data.typeGen == TypeGen.dBugs:
				cls.addToSource(item, Source(
					wikiName = "[[Catching]]",
					txtName = "Catching"
				))

	@classmethod
	def addGemShop(cls):
		for item, _ in GemShopRepo.items():
			if not ItemDetailRepo.contains(item):
				continue
			cls.addToSource(item, Source(
				wikiName = "[[Gem Shop]]",
				txtName = "Gem Shop"
			))

	@classmethod
	def addTaskUnlocks(cls):
		for sec, unlocks in enumerate(TaskUnlocksRepo.items()):
			for unlock in unlocks.unlocks:
				for item in unlock:
					if item.item == "PremiumGem":
						continue
					cls.addToRecipeFrom(item.item, Source(
						wikiName = f"[[Tasks/Unlocks|Task Unlocks Tab {sec + 1}]]",
						txtName = f"Task Unlocks Tab {sec + 1}"
					))
					cls.addToSource(item.item, Source(
						wikiName = f"[[Tasks/Unlocks|Recipe from Task Unlocks Tab {sec + 1}]]",
						txtName = f"Task Unlocks Tab {sec + 1}"
					))

	@classmethod
	def addQuestRewards(cls):
		for npc, data in NpcRepo.items():
			for questN, quest in data.quests.items():
				for reward in quest.Rewards:
					if not isinstance(reward, Component):
						continue
					if reward.item[:-1] == "SmithingRecipes":
						cls.addToRecipeFrom(RecipeRepo.getFromComponent(reward), Source(
							txtName = f"{npc}: {quest.Name}",
							wikiName = f"[[{npc}#{quest.Name}|{quest.Name}]]"
						))
						cls.addToSource(RecipeRepo.getFromComponent(reward), Source(
							txtName = f"{npc}: {quest.Name}",
							wikiName = f"[[{npc}#{quest.Name}|Recipe from {quest.Name}]]"
						))
						continue
					cls.addToSource(reward.item, Source(
						txtName = f"{npc}: {quest.Name}",
						wikiName = f"[[{npc}#{quest.Name}|{quest.Name}]]"
					))
				if quest.Type == QuestType.ItemsAndSpaceRequired:
					for req in quest.getRequirements():
						if ItemDetailRepo.isItemOfTypeGen(req.item, TypeGen.dQuest) or \
								ItemDetailRepo.isItemOfTypeGen(req.item, TypeGen.dCurrency):
							cls.addToQuestAss(req.item, Source(
								txtName = f"{npc}: {quest.Name}",
								wikiName = f"[[{npc}#{quest.Name}|{quest.Name}]]"
							))

	@classmethod
	def addDroptables(cls):
		for droptable, drops in DropTableRepo.items():
			for drop in drops.drops:
				if isRecipe(drop.item):
					cls.addToRecipeFrom(RecipeRepo.getFromItemStr(drop.item, drop.quantity), Source(
						txtName = droptable,
						wikiName = f"[[{droptable}]]"
					))
					cls.addToSource(RecipeRepo.getFromItemStr(drop.item, drop.quantity), Source(
						txtName = droptable,
						wikiName = f"[[{droptable}|Recipe from {droptable}]]"
					))
					continue
				cls.addToSource(drop.item, Source(
					txtName = droptable,
					wikiName = f"[[{droptable}]]"
				))

	@classmethod
	def addVendors(cls):
		for item, vendors in VendorRepo.items():
			for vendor in vendors.items:
				cls.addToSource(vendor.item, Source(
					txtName = vendor.vendor + " Vendor",
					wikiName = f"[[Vendors#{vendor.vendor}|{vendor.vendor} Vendors]]"
				))

	@classmethod
	def addPostOffice(cls):
		for postOffice, detail in PostOfficeRepo.items():
			for reward in detail.rewards:
				cls.addToSource(reward.item, Source(
					txtName = postOffice,
					wikiName = f"[[Post Office#{postOffice}|{postOffice}]]"
				))

	@classmethod
	def addRefinery(cls):
		for salt, _ in RefineryCostRepo.items():
			cls.addToSource(salt, Source(
				txtName = "Refinery",
				wikiName = "[[Construction#Refinery|Refinery]]"
			))

	@classmethod
	def addEnemyDroptables(cls):
		for enemy, drops in EnemyTableRepo.items():
			if enemy in Constants.ignoredEnemies:
				continue
			if not EnemyDetailsRepo.contains(enemy):
				continue
			wikiName = EnemyDetailsRepo.get(enemy).Name
			if "Chest" in wikiName:
				col, name = wikiName.split(" ", 1)
				wikiName = f"Colosseum/{col}#{name}|{col} {name}"
			for drop in drops.drops:
				if drop.item[:-1] == "SmithingRecipes":
					cls.addToRecipeFrom(RecipeRepo.getFromItemStr(drop.item, drop.quantity), Source(
						txtName = enemy,
						wikiName = f"[[{wikiName}]]"
					))
					cls.addToSource(RecipeRepo.getFromItemStr(drop.item, drop.quantity), Source(
						txtName = enemy,
						wikiName = f"[[{wikiName}|Recipe from {wikiName}]]"
					))
					continue
				cls.addToSource(drop.item, Source(
					txtName = enemy,
					wikiName = f"[[{wikiName}]]"
				))

	@classmethod
	def addRecipes(cls):
		for item, _ in RecipeRepo.items():
			cls.addToSource(item, Source(
				wikiName = "[[Smithing]]",
				txtName = "Smithing"
			))

	@classmethod
	def addToSource(cls, item: str, source: Source):
		if not cls.contains(item):
			cls.add(item, Sources())
		cls.get(item).sources.append(source)

	@classmethod
	def addToRecipeFrom(cls, item: str, source: Source):
		if not cls.contains(item):
			cls.add(item, Sources())
		cls.get(item).recipeFrom.append(source)

	@classmethod
	def addToQuestAss(cls, item: str, source: Source):
		if not cls.contains(item):
			cls.add(item, Sources())
		cls.get(item).questAss.append(source)
