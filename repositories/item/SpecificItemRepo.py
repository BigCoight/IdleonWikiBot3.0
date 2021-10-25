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
from definitions.itemdef.specifictypes.StampItem import StampItem
from definitions.itemdef.specifictypes.StatueItem import StatueItem
from definitions.itemdef.specifictypes.StoneItem import StoneItem
from definitions.itemdef.specifictypes.ToolItem import ToolItem
from definitions.itemdef.specifictypes.WeaponItem import WeaponItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from helpers.HelperFunctions import camelCaseToTitle
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.item.CardRepo import CardRepo
from repositories.item.FishingToolkitRepo import FishingToolkitRepo
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.RecipeRepo import RecipeRepo
from repositories.item.StatueRepo import StatueRepo
from repositories.master.Repository import Repository


class SpecificItemRepo(Repository[BaseItem]):
	"""
	Dependent on: ItemDetailsRepo, RecipeRepo, CardRepo, EnemyDetailsRepo, StatueRepo, FishingToolkitRepo
	"""

	@classmethod
	def initDependencies(cls):
		ItemDetailRepo.initialise(cls.codeReader)
		RecipeRepo.initialise(cls.codeReader)
		CardRepo.initialise(cls.codeReader)
		EnemyDetailsRepo.initialise(cls.codeReader)
		StatueRepo.initialise(cls.codeReader)
		FishingToolkitRepo.initialise(cls.codeReader)

	@classmethod
	def generateRepo(cls) -> None:
		cls.initDependencies()
		havntDone = set()
		for name, item in ItemDetailRepo.items():
			if item.typeGen in {TypeGen.dFish, TypeGen.dBugs, TypeGen.dCritters, TypeGen.dSouls, TypeGen.bCraft,
			                    TypeGen.dQuest, TypeGen.dCardPack, TypeGen.dTimeCandy, TypeGen.dCurrency}:
				cls.add(name, DescItem.fromItemDetails(item))
			elif item.typeGen in {TypeGen.bLog, TypeGen.bLeaf, TypeGen.bBar}:
				cls.add(name, BaseItem.fromItemDetails(item))
			elif item.typeGen in {TypeGen.aHelmet, TypeGen.aPants, TypeGen.aShoes, TypeGen.aShirt,
			                      TypeGen.aChatRingMTX, TypeGen.aTrophy, TypeGen.aPendant, TypeGen.aHelmetMTX,
			                      TypeGen.aRing}:
				cls.add(name, ArmourItem.fromItemDetails(item))
			elif item.typeGen == TypeGen.aWeapon:
				cls.add(name, WeaponItem.fromItemDetails(item))
			elif item.typeGen in {TypeGen.aHatchet, TypeGen.aFishingRod, TypeGen.aBugNet, TypeGen.aPick, TypeGen.aTrap,
			                      TypeGen.aSkull}:
				cls.add(name, ToolItem.fromItemDetails(item))
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
	def compareVersions(cls, v1: str, v2: str, ignored: Set[str] = set()):
		return super().compareVersions(v1, v2, {"category", "internalName", "typeGen"})

	@classmethod
	def _ignore(cls, name: str, data: BaseItem) -> bool:
		if "Dung" in name:
			return True
		if name in {"EXP", "Blank", "LockedInvSpace", "COIN", "TalentBook1", "TalentBook2",
		            "TalentBook3", "TalentBook4", "TalentBook5", "SmithingRecipes1", "SmithingRecipes2",
		            "SmithingRecipes3", "SmithingRecipes4", "ExpSmith1", "Quest8", "EquipmentShirts8"}:
			return True
		if name[:3] == "Gem":
			return True
		if data.displayName in {"Filler", "FILLER", "Blank"}:
			return True
		return False

	# Need to make this group by type
	@classmethod
	def writeChangesWiki(cls, differences):
		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

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
			for key in keys:
				res += cls._writeChangelogChange(key, changes[key])
			res += "|}\n\n"

		res += "</div><div class=\"GenericChild\">\n"
		res += "==New==\n"

		for typ, keys in newOrdered.items():
			res += head(typ)
			for key in keys:
				res += cls._writeChangelogNew(key, new[key])
			res += "|}\n\n"

		res += "</div></div>"

		with open(fr"./exported/wikitext/_changes/{cls.__name__}.txt", mode = 'w') as infile:
			infile.write(res)

	@classmethod
	def _writeChangelogNew(cls, item, change) -> str:
		def head(v: str) -> str:
			return "{{patchnote/item|" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + v + "}}\n"

		def patchnote(v: str, o, n) -> str:
			return "{{patchnote|" + f"{v}|{str(o)}|{str(n)}" + "}}\n"

		res = head(cls.getWikiName(item))
		for v, d in change.items():
			if isinstance(d, list):
				res += bold(camelCaseToTitle(v))
				for i, subC in enumerate(d):
					res += patchnote(str(i), " ", subC)
			elif isinstance(d, dict):
				res += bold(camelCaseToTitle(v))
				for atr, subC in d.items():
					res += patchnote(atr, " ", subC)
			else:
				if not d:
					continue
				res += patchnote(v, " ", d)
		return res

	@classmethod
	def _writeChangelogChange(cls, item, change) -> str:
		def head(v: str) -> str:
			return "{{patchnote/item|" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + v + "}}\n"

		def patchnote(v: str, o, n) -> str:
			return "{{patchnote|" + f"{v}|{str(o)}|{str(n)}" + "}}\n"

		res = head(cls.getWikiName(item))
		for v, d in change.items():
			if isinstance(d, tuple):
				o, n = d
				res += patchnote(v, o, n)
			elif isinstance(d, list):
				res += bold(camelCaseToTitle(v))
				for i, subC in enumerate(d):
					o, n = subC
					res += patchnote(str(i), o, n)
			elif isinstance(d, dict):
				res += bold(camelCaseToTitle(v))
				for atr, subC in d.items():
					o, n = subC
					res += patchnote(atr, o, n)
		return res
