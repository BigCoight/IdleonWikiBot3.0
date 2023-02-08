from typing import List

from definitions.common.QtylessComponent import QtylessComponent
from definitions.component.Component import Component
from definitions.itemdef.Uses import Uses, Use
from definitions.itemdef.specifictypes.StampItem import StampItem
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.SpecificItemRepo import SpecificItemRepo
from repositories.master.Repository import Repository
from repositories.misc.world2.BubbleRepo import BubbleRepo
from repositories.misc.world2.PostOfficeRepo import PostOfficeRepo
from repositories.misc.world3.BuildingRepo import BuildingRepo
from repositories.misc.world3.PrayerRepo import PrayerRepo
from repositories.misc.world3.SaltLickRepo import SaltLickRepo
from repositories.npc.NpcRepo import NpcRepo


class UsesRepo(Repository[Uses]):

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def getSections(cls) -> List[str]:
		return []

	@classmethod
	def initDependencies(cls, log = True) -> None:
		RecipeRepo.initialise(cls.codeReader, False)
		BubbleRepo.initialise(cls.codeReader, False)
		SpecificItemRepo.initialise(cls.codeReader, False)
		NpcRepo.initialise(cls.codeReader, False)
		BuildingRepo.initialise(cls.codeReader, False)
		PrayerRepo.initialise(cls.codeReader, False)
		SaltLickRepo.initialise(cls.codeReader, False)
		PostOfficeRepo.initialise(cls.codeReader, False)

	@classmethod
	def generateRepo(cls) -> None:
		# Recipes
		for item, recipe in RecipeRepo.items():
			for component in recipe.recipe:
				cls.addToUses(component.item, Use(
					repoSource = "RecipeRepo",
					key = item,
					name = f"{RecipeRepo.getWikiName(item)} Recipe",
					amount = component.quantity,
					type = "recipe"))
			for component in recipe.detailedRecipe.detRecipeTotals:
				cls.addToUses(component.item, Use(
					repoSource = "RecipeRepo",
					key = item,
					name = f"{RecipeRepo.getWikiName(item)} Detailed Recipe",
					amount = component.quantity,
					type = "detRecipe"))

		# Bubbles
		for bubName, bubble in BubbleRepo.items():
			bubType = "vial" if bubble.cauldron == "Vials" else "bubble"
			name = "" if bubble.cauldron == "Vials" else " Bubble"
			for component in bubble.requirements:
				if isinstance(component, (Component, QtylessComponent)):
					cls.addToUses(component.item, Use(
						repoSource = "BubbleRepo",
						key = f"{bubble.cauldron}@{bubName}",
						name = f"{bubble.cauldron}: {bubble.name}{name}",
						amount = "Lots",
						type = bubType))

		for item, stamp in SpecificItemRepo.items():
			if isinstance(stamp, StampItem):
				cls.addToUses(stamp.stampData.material.item, Use(
					repoSource = "ItemRepo",
					key = item,
					name = f"{SpecificItemRepo.getWikiName(item)} Material",
					amount = "Lots",
					type = "stamp"))

		for npc, data in NpcRepo.items():
			for questName, questData in data.quests.items():
				for component in questData.getRequirements():
					if isinstance(component, (Component, QtylessComponent)):
						cls.addToUses(component.item, Use(
							repoSource = "NpcRepo",
							key = f"{npc}@{questName}",
							name = f"{questName} Requirements",
							amount = component.quantity,
							type = "quest"))

		for building, data in BuildingRepo.items():
			for component in data.lvlUpReq:
				if isinstance(component, (Component, QtylessComponent)):
					cls.addToUses(component.item, Use(
						repoSource = "BuildingRepo",
						key = f"{building}",
						name = f"{building} Requirements",
						amount = "Lots",
						type = "building"))

		for prayer, data in PrayerRepo.items():
			cls.addToUses(data.soul, Use(
				repoSource = "PrayerRepo",
				key = f"{prayer}",
				name = f"{prayer} Requirements",
				amount = "Lots",
				type = "prayer"))

		for n, (salt, data) in enumerate(SaltLickRepo.items()):
			cls.addToUses(data.item, Use(
				repoSource = "SaltLickRepo",
				key = f"{n}",
				name = f"Salt Lick {n} Requirements",
				amount = "Lots",
				type = "saltLick"))

		for poBox, data in PostOfficeRepo.items():
			for part in data.orders:
				cls.addToUses(part.item, Use(
					repoSource = "PostOfficeRepo",
					key = f"{poBox}",
					name = f"{poBox} Order",
					amount = "Lots",
					type = "poBox"))

	@classmethod
	def addToUses(cls, item: str, use: Use):
		if not SpecificItemRepo.contains(item):
			return
		if not cls.contains(item):
			cls.add(item, Uses(
				uses = [use],
				typeGen = SpecificItemRepo.get(item).typeGen,
				type = SpecificItemRepo.get(item).Type
			))
			return
		cls.get(item).uses.append(use)
