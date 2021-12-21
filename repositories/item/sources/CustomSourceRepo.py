from definitions.common.Source import Source
from definitions.itemdef.Sources import Sources
from repositories.master.Repository import Repository


class CustomSourceRepo(Repository[Sources]):

	@classmethod
	def excludeDefaults(cls) -> bool:
		return True

	@classmethod
	def generateRepo(cls) -> None:
		for item in ["Quest50", "CardsY11", "CardsY12", "StoneWeb", "StoneT1eb", "StoneAeB"]:
			cls.addToSource(item, Source(
				wikiName = "[[Summer Cooler]]",
				txtName = "Summer Cooler"
			))

		for item in ["CardsY14", "StoneT1e", "StoneHelm1b", "CardsY1", "CardsY2", "Pearl4", "FoodEvent8",
		             "FoodEvent7", "FoodEvent6", "FoodEvent1"]:
			cls.addToSource(item, Source(
				wikiName = "[[2021 Giftmas Box]]",
				txtName = "2021 Giftmas Box"
			))

		for item in ["CardsY2", "CardsY0", "CardsY1", "FoodEvent2", "FoodEvent1", "FoodEvent3",
		             "FoodEvent4"]:
			cls.addToSource(item, Source(
				wikiName = "[[Choco Box]]",
				txtName = "Choco Box"
			))

		for item in ["CardsX0", "CardsX1", "CardsX2", "CardsX3", "CardsX4", "CardsX5",
					 "CardsX15", "CardsX14"]:
			cls.addToSource(item, Source(
				wikiName = "[[Dungeons#Grandfrog's Gazebo|Grandfrog's Gazebo]]",
				txtName = "Dungeons: Grandfrog's Gazebo"
			))

		for item in ["CardsX6", "CardsX7", "CardsX8", "CardsX9", "CardsX10", "CardsX11",
		             "CardsX12", "CardsX13", "CardsX16", "Quest51", "PalmTreeD", "Quest53", "Quest54", "Quest55"]:
			cls.addToSource(item, Source(
				wikiName = "[[Dungeons#Crypt of Snakenhotep|Crypt of Snakenhotep]]",
				txtName = "Dungeons: Crypt of Snakenhotep"
			))

		for item in ["CardsX17", "CardsX18", "CardsX19", "CardsX20", "Tree7D", "PlatD", "Fish1D", "Fish3D", "Cashb", "Dung3Ice"]:
			cls.addToSource(item, Source(
				wikiName = "[[Dungeons#Igloo's Basement|Igloo's Basement]]",
				txtName = "Dungeons: Igloo's Basement"
			))

		cls.addToQuestAss("Quest52", Source(
			wikiName = "[[Bill Brr#Coin Shenanigans|Coin Shenanigans]]",
			txtName = "Bill Brr: Coin Shenanigans"
		))

		cls.addToQuestAss("Quest63", Source(
			wikiName = "[[Shuvelle#Diggy Hole!|Diggy Hole!]]", 
			txtName = "Shuvelle: Diggy Hole!",
		))

		sourceDict = {
			"Giftmas Event": 'EquipmentHats42',
			"Valenslimes Day Event": 'EquipmentHats51',
			"Steam Launch Event": 'EquipmentHats55',
			"Easter Event": 'EquipmentHats56',
			"Summer Break Event": 'EquipmentHats63',
			"Summer Bundle Gem Offer": 'Trophy14'
		}

		for source, item in sourceDict.items():
			cls.addToSource(item, Source(
				wikiName = source,
				txtName = source
			))

		for item in ['ObolPinkChoppin', 'ObolSilverPop', 'ObolGoldPop', 'ObolSilverKill', 'ObolPlatinumTrapping',
		             'ObolPinkTrapping', 'ObolPlatinumCons', 'ObolPinkCons', 'ObolPlatinumWorship', 'ObolPinkWorship']:
			cls.addToSource(item, Source(
				wikiName = "Obol Combining",
				txtName = "Obol Combining"
			))

		for item in ['EquipmentRingsChat8', 'InvBag22', 'InvBag23', 'InvBag24', 'InvBag25', 'InvBag26',
		             'InvStorage32', 'InvStorage33', 'InvStorage34', 'InvStorage35', 'InvStorage36', 'InvStorage37',
		             'InvStorage38', 'InvStorage39', 'InvStorage40', 'InvStorage41', 'InvStorage42', 'EquipmentHats31',
		             'EquipmentHats32', 'EquipmentHats33', 'EquipmentHats34', 'EquipmentHats36', 'EquipmentHats40',
		             'EquipmentHats37', 'EquipmentHats45', 'EquipmentHats57', 'EquipmentHats62']:
			cls.addToSource(item, Source(
				wikiName = "[[Gem Shop]]",
				txtName = "Gem Shop"
			))

		for item in ['BallJoePickle', 'StampC4', 'Gfoodcoupon', 'ItemsCoupon1', 'ItemsCoupon2', 'EquipmentHats65',
		             'StampC5', 'StampC8']:
			cls.addToSource(item, Source(
				wikiName = "[[Arcade]]",
				txtName = "Arcade"
			))

		for item in ['ObolGold0', 'ObolGold1', 'ObolGold2', 'ObolGoldDamage', 'ObolGoldMoney', 'ObolGoldMining',
		             'ObolGoldChoppin', 'ObolGoldFishing', 'ObolGoldCatching', 'ObolGoldLuck', 'ObolGoldKill',
		             'ObolGoldEXP', 'ObolSilverCard', 'ObolSilverDef', 'ObolGoldDef']:
			cls.addToSource(item, Source(
				wikiName = "[[Gem Shop#Quality Obol Stack|Quality Obol Stack]]",
				txtName = "Gem Shop: Quality Obol Stack"
			))

		for item in ['ObolGold0', 'ObolGold1', 'ObolGold2', 'ObolGoldDamage', 'ObolGoldMoney', 'ObolGoldMining',
		             'ObolGoldChoppin', 'ObolGoldFishing', 'ObolGoldCatching', 'ObolGoldLuck', 'ObolGoldKill',
		             'ObolGoldEXP', 'ObolGoldDef', 'ObolPlatinum0', 'ObolPlatinum1', 'ObolPlatinum2',
		             'ObolPlatinum3', 'ObolPink0', 'ObolPink1', 'ObolPink2', 'ObolPink3', 'ObolPlatinumDamage',
		             'ObolPinkDamage', 'ObolPlatinumMining', 'ObolPinkMining', 'ObolPlatinumChoppin',
		             'ObolPlatinumFishing', 'ObolPinkFishing', 'ObolPlatinumCatching', 'ObolPinkCatching',
		             'ObolPlatinumLuck', 'ObolPinkLuck', 'ObolPlatinumPop', 'ObolPinkPop', 'ObolPlatinumKill',
		             'ObolPinkKill', 'ObolPlatinumEXP', 'ObolPinkEXP', 'ObolPlatinumCard', 'ObolPinkCard',
		             'ObolPlatinumDef', 'ObolPinkDef', 'ObolGoldTrapping', 'ObolGoldCons', 'ObolGoldWorship']:
			cls.addToSource(item, Source(
				wikiName = "[[Gem Shop#Marvelous Obol Stack|Marvelous Obol Stack]]",
				txtName = "Gem Shop: Marvelous Obol Stack"
			))

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
				txtName = "Alchemy: Level up Gift"
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
				txtName = "Alchemy: Mediocre Obols"
			))

		for item in ["ObolBronze0", "ObolBronze1", "ObolBronze2", "ObolBronze3", "ObolSilverDamage",
		             "ObolBronzeFishing",
		             "ObolBronzeCatching", "ObolSilverFishing",
		             "ObolSilverChoppin", "ObolSilverCatching", "ObolSilverMining", "ObolSilver0", "ObolSilver1",
		             "ObolSilver2", "ObolSilver3"]:
			cls.addToSource(item, Source(
				wikiName = "[[Alchemy#Liquid Shop|Decent Obols]]",
				txtName = "Alchemy: Decent Obols"
			))

		for item in ["ObolSilverDamage", "ObolBronze0", "ObolBronze1", "ObolBronze2", "ObolBronzeCons",
		             "ObolBronzeKill", "ObolBronzeDef",
		             "ObolBronzeTrapping", "ObolBronzeWorship",
		             "ObolSilverTrapping", "ObolSilverWorship", "ObolSilverCons", "ObolSilver0", "ObolSilver1",
		             "ObolSilver2", "ObolGold", "ObolGoldCard"]:
			cls.addToSource(item, Source(
				wikiName = "[[Alchemy#Liquid Shop|Grand Obols]]",
				txtName = "Alchemy: Grand Obols"
			))

		for item in ["StoneW1", "StoneA1", "StoneT1", "StoneHelm1", "StoneA1b"]:
			cls.addToSource(item, Source(
				wikiName = "[[Alchemy#Liquid Shop|Weak UPG Stone]]",
				txtName = "Alchemy: Weak UPG Stone"
			))

		for item in ['Pearl3', 'Pearl2', 'Pearl1']:
			cls.addToSource(item, Source(
				wikiName = "[[Beach Oyster]]",
				txtName = "Beach Oyster"
			))

		for item in ['StoneT1e', 'StoneHelm1b']:
			cls.addToSource(item, Source(
				wikiName = "[[Giftmas Box]]",
				txtName = "Giftmas Box"
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

		cls.addToSource("EquipmentHats69", Source(
			wikiName = "[[Gem Shop|Limited time bundle]]",
			txtName = "Gem Shop: Limited time bundle"
		))

		cls.addToSource("Trophy8", Source(
			wikiName = "The only way to obtain this is when the [[Gem Shop|Lava Supporter Pack]] is available, "
			           "or from contests (discord, twitch, twitter)",
			txtName = "The only way to obtain this is when the Lava Supporter Pack is available, "
			          "or from contests (discord, twitch, twitter)"
		))

		cls.addToSource("Quest11", Source(
			wikiName = "[[Tiki Chief#Three Strikes, you're Out!|Three Strikes, you're Out!]]",
			txtName = "Tiki Chief: Three Strikes, you're Out!"
		))

		cls.addToSource("Quest26", Source(
			wikiName = "[[Alchemy#Level up Gift|Level up Gift (however this item has no use anymore)]]",
			txtName = "Alchemy: Level up Gift"
		))

		cls.addToSource("NPCtoken15", Source(
			wikiName = "[[TP Pete]]",
			txtName = "TP Pete"
		))

		cls.addToSource("Quest56", Source(
			wikiName = "[[King Doot]]",
			txtName = "King Doot"
		))

		cls.addToSource("NPCtoken10", Source(
			wikiName = "[[Krunk]]",
			txtName = "Krunk"
		))

		cls.addToSource("Quest2", Source(
			wikiName = "[[Glumlee#Literally Burning your Money|Literally Burning your Money]]",
			txtName = "Glumlee: Literally Burning your Money"
		))

		cls.addToSource("Quest38", Source(
			wikiName = "[[Alchemy#Level up Gift|Level up Gift]]",
			txtName = "Alchemy: Level up Gift"
		))

		cls.addToSource("Quest47", Source(
			wikiName = "[[Cactolyte#Peanut De-Aging|Peanut De-Aging]]",
			txtName = "Cactolyte: Peanut De-Aging"
		))

		cls.addToSource("PureWater2", Source(
			wikiName = "[[Alchemy#Liquid Shop|Alchemy Liquid Shop]]",
			txtName = "Alchemy: Liquid Shop"
		))

		cls.addToSource("Trophy5", Source(
			wikiName = "[[Special Talents#Special Talent Book Sources|Roll Da Dice]]",
			txtName = "Roll Da Dice"
		))

		cls.addToSource("Trophy12", Source(
			wikiName = "Catch the Megalodon in the [[Fishing]] minigame",
			txtName = "Catch the Megalodon in the Fishing minigame"
		))

		cls.addToSource("Mayo", Source(
			wikiName = "Dug at the end of the 'Treasure Hunt 1' quest from [[Walupiggy]]",
			txtName = "Dug at the end of the 'Treasure Hunt 1' quest from Walupiggy"
		))

		cls.addToSource("Trash", Source(
			wikiName = "Dug at the end of the 'Treasure Hunt 2' quest from [[Walupiggy]]",
			txtName = "Dug at the end of the 'Treasure Hunt 2' quest from Walupiggy"
		))

		cls.addToSource("Trash2", Source(
			wikiName = "Dug at the end of the 'Treasure Hunt 3' quest from [[Walupiggy]]",
			txtName = "Dug at the end of the 'Treasure Hunt 3' quest from Walupiggy"
		))

		for item in ["BadgeG1", "BadgeG2", "BadgeG3", "NPCtoken1", "NPCtoken2", "NPCtoken3"]:
			cls.addToRecipeFrom(item, Source(
				wikiName = "[[Scripticus#Champion of the Grasslands|Champion of the Grasslands]]",
				txtName = "Scripticus: Champion of the Grasslands"
			))

		for item in ['BadgeD1', 'BadgeD2', 'BadgeD3', 'NPCtoken28', 'NPCtoken29', 'NPCtoken30']:
			cls.addToRecipeFrom(item, Source(
				wikiName = "[[Cowbo_Jones#The_New_Sheriff|The New Sheriff]]",
				txtName = "Cowbo Jones: The New Sheriff"
			))

		for item in ['EquipmentHats52', 'EquipmentShirts26', 'EquipmentPants20', 'EquipmentShoes21',
		             'EquipmentRings16']:
			cls.addToRecipeFrom(item, Source(
				wikiName = "[[Tasks/Yum_Yum_Desert#Merit_Shop|Yum Yum Desert Merit Shop]]",
				txtName = "Yum Yum Desert Merit Shop"
			))

		for item in ['EquipmentHats22', 'EquipmentShirts18', 'EquipmentPants17', 'EquipmentShoes20',
		             'EquipmentPendant17']:
			cls.addToRecipeFrom(item, Source(
				wikiName = "[[Tasks/Blunder_Hills#Merit_Shop|Blunder Hills Merit Shop]]",
				txtName = "Blunder Hills Merit Shop"
			))

		cls.addToSource("Quest45", Source(
			wikiName = "[[Mimic|Active Mimics (1/100)]]",
			txtName = "Active Mimics (1/100)"
		))

		cls.addToRecipeFrom("Peanut", Source(
			wikiName = "[[Picnic Stowaway#Brunchin' with the Blobs|Brunchin' with the Blobs]]",
			txtName = "Picnic Stowaway: Brunchin' with the Blobs"
		))

		cls.addToRecipeFrom("EquipmentShoes15", Source(
			wikiName = "[[Colosseum#Dewdrop_Silver_Chest|W1 Colosseum first silver chest]]",
			txtName = "Colosseum: W1 Colosseum first silver chest"
		))

		cls.addToQuestAss("Quest2", Source(
			wikiName = "[[Scripticus#Certified Swinger, of Pickaxes of course!|Certified Swinger, of Pickaxes of course!]]",
			txtName = "Scripticus: Certified Swinger, of Pickaxes of course!"
		))

		cls.addToQuestAss("Quest10", Source(
			wikiName = "[[Picnic Stowaway#Afternoon Tea in a Jiffy|Afternoon Tea in a Jiffy]]",
			txtName = "Picnic Stowaway: Afternoon Tea in a Jiffy"
		))

		cls.addToQuestAss("Quest11", Source(
			wikiName = "[[Tiki Chief#Three Strikes, you're Out!|Three Strikes, you're Out!]]",
			txtName = "Tiki Chief: Three Strikes, you're Out!"
		))

		cls.addToQuestAss("Quest47", Source(
			wikiName = "[[Cactolyte#Peanut De-Aging|Peanut De-Aging]]",
			txtName = "Cactolyte: Peanut De-Aging"
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
