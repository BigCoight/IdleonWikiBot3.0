from definitions.common.Source import Source
from definitions.itemdef.Sources import Sources
from repositories.master.Repository import Repository


class CustomSourceRepo(Repository[Sources]):
	"""
	Dependent On: DropTableRepo, EnemyDetailsRepo, PostOfficeRepo, GemShopRepo, EnemyTableRepo, ITemDetailRepo,
	RecipeRepo, RefineryCostRepo, VendorRepo, FlurboShopRepo
	"""

	@classmethod
	def excludeDefaults(cls) -> bool:
		return True

	@classmethod
	def generateRepo(cls) -> None:
		for item in ["EquipmentHats14", "EquipmentHats11", "EquipmentHats13", "EquipmentHats12"]:
			cls.addToSource(item, Source(
				wikiName = "Starter Hat",
				txtName = "Starter Hat"
			))

		for item in ["StampA23", "EquipmentHats21", "PremiumGem", "Timecandy1", "Timecandy2", "Timecandy3",
		             "Timecandy4", "Timecandy5", "Line6", "StoneZ1", "FoodPotYe1",
		             "FoodPotYe2", "FoodPotYe3", "StampC9", "Quest25",
		             "EquipmentStatues1", "EquipmentStatues2", "EquipmentStatues3", "EquipmentStatues4",
		             "EquipmentStatues5", "EquipmentStatues6", "EquipmentStatues7", "EquipmentStatues8"]:
			cls.addToSource(item, Source(
				wikiName = "[[Alchemy#Level up Gift|Level up Gift]]",
				txtName = "Level up Gift"
			))

		for item in ["Trophy9", "FoodPotYe3", "FoodPotYe2", "PremiumGem", "StoneA3b", "StoneW2", "StoneA2",
		             "StonePremLUK", "StoneHelm6", "StoneW6", "ExpBalloon1", "ExpBalloon2", "ExpBalloon3",
		             "ResetFrag", "Timecandy4", "Timecandy3", "Timecandy2", "Timecandy1"]:
			cls.addToSource(item, Source(
				wikiName = "[[Guild Giftbox]]",
				txtName = "Guild Giftbox"
			))

		for item in ["StampA1", "StampA2", "StampB1", "StampB2"]:
			cls.addToSource(item, Source(
				wikiName = "Start",
				txtName = "Start"
			))

		for item in ["ObolBronze0", "ObolBronze1", "ObolBronze2", "ObolBronze3", "ObolBronzeMining",
		             "ObolBronzeChoppin", "ObolBronzeDamage"]:
			cls.addToSource(item, Source(
				wikiName = "[[Alchemy#Liquid Shop|Mediocre Obols]]",
				txtName = "Mediocre Obols"
			))

		for item in ["ObolBronze0", "ObolBronze1", "ObolBronze2", "ObolBronze3", "ObolSilverDamage",
		             "ObolBronzeFishing",
		             "ObolBronzeCatching", "ObolSilverFishing",
		             "ObolSilverChoppin", "ObolSilverCatching", "ObolSilverMining", "ObolSilver0", "ObolSilver1",
		             "ObolSilver2", "ObolSilver3"]:
			cls.addToSource(item, Source(
				wikiName = "[[Alchemy#Liquid Shop|Decent Obols]]",
				txtName = "Decent Obols"
			))

		for item in ["ObolSilverDamage", "ObolBronze0", "ObolBronze1", "ObolBronze2", "ObolBronzeCons",
		             "ObolBronzeKill", "ObolBronzeDef",
		             "ObolBronzeTrapping", "ObolBronzeWorship",
		             "ObolSilverTrapping", "ObolSilverWorship", "ObolSilverCons", "ObolSilver0", "ObolSilver1",
		             "ObolSilver2", "ObolGold", "ObolGoldCard"]:
			cls.addToSource(item, Source(
				wikiName = "[[Alchemy#Liquid Shop|Grand Obols]]",
				txtName = "Grand Obols"
			))

		for item in ["StoneW1", "StoneA1", "StoneT1", "StoneHelm1", "StoneA1b"]:
			cls.addToSource(item, Source(
				wikiName = "[[Alchemy#Liquid Shop|Weak UPG Stone]]",
				txtName = "Weak UPG Stone"
			))

		for item in ["CritterCard1", "CritterCard2", "CritterCard3",
		             "CritterCard4", "CritterCard5", "CritterCard6", "CritterCard7"]:
			cls.addToSource(item, Source(
				wikiName = "[[Trapping]]",
				txtName = "Trapping"
			))

		for item in ["SoulCard1", "SoulCard2", "SoulCard3", "SoulCard4", "SoulCard5"]:
			cls.addToSource(item, Source(
				wikiName = "[[Worship]]",
				txtName = "Worship"
			))

		cls.addToSource("EquipmentRings15", Source(
			wikiName = "Has a 1/1M chance to drop from active kills if the Blue Hedgehog [[Star Signs|Starsign]] is equipped.",
			txtName = "Has a 1/1M chance to drop from active kills if the Blue Hedgehog is equipped."
		))

		cls.addToSource("Quest11", Source(
			wikiName = "[[Tiki Chief#Three Strikes, you're Out!|Three Strikes, you're Out!]]",
			txtName = "Tiki Chief: Three Strikes, you're Out!"
		))

		cls.addToSource("Quest26", Source(
			wikiName = "[[Alchemy#Level up Gift|Level up Gift (however this item has no use anymore)]]",
			txtName = "Level up Gift"
		))

		cls.addToSource("NPCtoken15", Source(
			wikiName = "[[TP Pete]]",
			txtName = "TP Pete"
		))

		cls.addToSource("NPCtoken10", Source(
			wikiName = "[[Krunk]]",
			txtName = "Krunk"
		))

		for item in ["BadgeG1", "BadgeG2", "BadgeG3", "NPCtoken1", "NPCtoken2", "NPCtoken3"]:
			cls.addToRecipeFrom(item, Source(
				wikiName = "[[Scripticus#Champion of the Grasslands|Champion of the Grasslands]]",
				txtName = "Scripticus: Champion of the Grasslands"
			))

		cls.addToRecipeFrom("Peanut", Source(
			wikiName = "[[Picnic Stowaway#Brunchin' with the Blobs|Brunchin' with the Blobs]]",
			txtName = "Brunchin' with the Blobs"
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
