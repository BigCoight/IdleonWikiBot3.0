from typing import Set

from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.itemdef.specifictypes.ACItem import ACItem
from definitions.itemdef.specifictypes.ArmourItem import ArmourItem
from definitions.itemdef.specifictypes.CardItem import CardItem
from definitions.itemdef.specifictypes.CarryBagItem import CarryBagItem
from definitions.itemdef.specifictypes.ChestItem import ChestItem
from definitions.itemdef.specifictypes.FishingTKItem import FishingTKItem
from definitions.itemdef.specifictypes.GoldenFoodItem import GoldenFoodItem
from definitions.itemdef.specifictypes.InvBagItem import InvBagItem
from definitions.itemdef.specifictypes.KeychainItem import KeychainItem
from definitions.itemdef.specifictypes.ObolItem import ObolItem
from definitions.itemdef.specifictypes.OreItem import OreItem
from definitions.itemdef.specifictypes.SkullItem import SkullItem
from definitions.itemdef.specifictypes.StampItem import StampItem
from definitions.itemdef.specifictypes.StatueItem import StatueItem
from definitions.itemdef.specifictypes.StoneItem import StoneItem
from definitions.itemdef.specifictypes.ToolItem import ToolItem
from definitions.itemdef.specifictypes.TrapBoxItem import TrapBoxItem
from definitions.itemdef.specifictypes.WeaponItem import WeaponItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from helpers.CodeReader import IdleonReader
from repositories.dungeons.KeychainBonusRepo import KeychainBonusRepo
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.item.CardDropChanceRepo import CardDropChanceRepo
from repositories.item.CardRepo import CardRepo
from repositories.item.FishingToolkitRepo import FishingToolkitRepo
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.StampDescriptionRepo import StampDescriptionRepo
from repositories.item.StatueRepo import StatueRepo
from repositories.item.TrapBoxRepo import TrapBoxRepo
from repositories.master.Repository import Repository
from repositories.misc.StorageOrderRepo import StorageOrderRepo


class SpecificItemRepo(Repository[BaseItem]):
	"""
	Dependent on: ItemDetailsRepo, RecipeRepo, CardRepo, EnemyDetailsRepo, StatueRepo, FishingToolkitRepo
	"""

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def initDependencies(cls, log = True):
		ItemDetailRepo.initialise(cls.codeReader, log)
		RecipeRepo.initialise(cls.codeReader, log)
		CardRepo.initialise(cls.codeReader, log)
		EnemyDetailsRepo.initialise(cls.codeReader, log)
		StatueRepo.initialise(cls.codeReader, log)
		FishingToolkitRepo.initialise(cls.codeReader, log)
		KeychainBonusRepo.initialise(cls.codeReader, log)
		StorageOrderRepo.initialise(cls.codeReader, log)
		StampDescriptionRepo.initialise(cls.codeReader, log)
		CardDropChanceRepo.initialise(cls.codeReader, log)
		TrapBoxRepo.initialise(cls.codeReader, log)

	@classmethod
	def generateRepo(cls) -> None:
		havntDone = set()
		for name, item in ItemDetailRepo.items():
			if item.typeGen in {TypeGen.dFish, TypeGen.dBugs, TypeGen.dCritters, TypeGen.dSouls, TypeGen.bCraft,
			                    TypeGen.dQuest, TypeGen.dCardPack, TypeGen.dTimeCandy, TypeGen.dCurrency}:
				cls.add(name, DescItem.fromItemDetails(item))
			elif item.typeGen in {TypeGen.bLog, TypeGen.bLeaf, TypeGen.bBar}:
				cls.add(name, BaseItem.fromItemDetails(item))
			elif item.typeGen in {TypeGen.aHelmet, TypeGen.aPants, TypeGen.aShoes, TypeGen.aShirt,
			                      TypeGen.aChatRingMTX, TypeGen.aTrophy, TypeGen.aPendant, TypeGen.aHelmetMTX,
			                      TypeGen.aRing, TypeGen.aCape, TypeGen.aNametag}:
				cls.add(name, ArmourItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aWeapon:
				cls.add(name, WeaponItem.fromItemDetails(item))
			elif item.typeGen in {TypeGen.aHatchet, TypeGen.aFishingRod, TypeGen.aBugNet, TypeGen.aPick,
			                      TypeGen.aDNAgun}:
				cls.add(name, ToolItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aTrap:
				cls.add(name, TrapBoxItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aSkull:
				cls.add(name, SkullItem.fromItemDetails(item))
			elif item.typeGen in {TypeGen.aObolCircle, TypeGen.aObolSquare, TypeGen.aObolSparkle, TypeGen.aObolHexagon}:
				cls.add(name, ObolItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aCarryBag:
				cls.add(name, CarryBagItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aStamp:
				cls.add(name, StampItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.bOre:
				cls.add(name, OreItem.fromItemDetails(item))
			elif item.typeGen in {TypeGen.cFood, TypeGen.cOil}:
				if item.Type == "Golden Food":
					cls.add(name, GoldenFoodItem.fromItemDetails(item))
				else:
					cls.add(name, ACItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.dCard:
				cls.add(name, CardItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aStorageChest:
				cls.add(name, ChestItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aInventoryBag:
				cls.add(name, InvBagItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.dStatueStone:
				cls.add(name, StatueItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.dFishToolkit:
				cls.add(name, FishingTKItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.dStone:
				cls.add(name, StoneItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aKeychain:
				cls.add(name, KeychainItem.fromItemDetails(item))
			else:
				havntDone.add(item.typeGen.value)
		if cls.log:
			print(havntDone)

	@classmethod
	def getDisplayName(cls, name: str) -> str:
		if item := cls.get(name):
			return item.displayName
		print(f"{name} not found in ItemRepo!!!")
		return ""

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.getDisplayName(name)

	@classmethod
	def compareVersions(cls, v1: IdleonReader, v2: IdleonReader, ignored: Set[str] = set(), useIgnore = True):
		return super().compareVersions(v1, v2, {"category", "internalName", "typeGen"})

	@classmethod
	def _ignore(cls, name: str, data: BaseItem) -> bool:
		if "Dung" in name:
			return True
		if name in {"EXP", "Blank", "LockedInvSpace", "COIN", "TalentBook1", "TalentBook2",
		            "TalentBook3", "TalentBook4", "TalentBook5", "SmithingRecipes1", "SmithingRecipes2",
		            "SmithingRecipes3", "SmithingRecipes4", "ExpSmith1", "Quest8", "EquipmentShirts8", "FoodHealth1d",
		            "FoodHealth2d", "FoodHealth3d", "PremiumGem", "Quest49", "Spice9"}:
			return True
		if name[:3] == "Gem":
			return True
		if data.displayName in {"Filler", "FILLER", "Blank"}:
			return True
		if data.Type in ["Dungeon Evaporate", "Spice", "Sail Treasure"]:
			return True
		return False

	@classmethod
	def _writeChangesWiki(cls, differences):
		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

		def item(v: str) -> str:
			return "{{patchnote/item|" + v + "}}\n"

		res = ""
		new = differences["new"]
		changes = differences["changes"]

		changesOrdered = {}
		for key in changes.keys():
			cType = cls.get(key).Type
			if cType not in changesOrdered:
				changesOrdered[cType] = []
			changesOrdered[cType].append(key)

		newOrdered = {}
		for key in new.keys():
			cType = cls.get(key).Type
			if cType not in newOrdered:
				newOrdered[cType] = []
			newOrdered[cType].append(key)

		res += "<div class=\"GenericFlex\"><div class=\"GenericChild\">\n"
		res += "==Changes==\n"
		for typ, keys in changesOrdered.items():
			res += head(typ)
			for change in keys:
				res += item(cls.getWikiName(change))
				res += cls._writeChangelog(changes[change])
			res += "|}\n\n"

		res += "</div><div class=\"GenericChild\">\n"
		res += "==New==\n"
		for typ, keys in newOrdered.items():
			res += head(typ)
			for change in keys:
				res += item(cls.getWikiName(change))
				res += cls._writeChangelog(new[change])
			res += "|}\n\n"

		res += "</div></div>"

		with open(cls._getPath("wikitext/_changes", "txt"), mode = 'w') as infile:
			infile.write(res)
