from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.itemdef.specifictypes.ACItem import ACItem
from definitions.itemdef.specifictypes.ArmourItem import ArmourItem
from definitions.itemdef.specifictypes.CardItem import CardItem
from definitions.itemdef.specifictypes.CarryBagItem import CarryBagItem
from definitions.itemdef.specifictypes.ChestItem import ChestItem
from definitions.itemdef.specifictypes.FishingTKItem import FishingTKItem
from definitions.itemdef.specifictypes.GoldenFoodItem import GoldenFoodItem
from definitions.itemdef.specifictypes.InvBagItem import InvBagItem
from definitions.itemdef.specifictypes.ObolItem import ObolItem
from definitions.itemdef.specifictypes.OreItem import OreItem
from definitions.itemdef.specifictypes.StampItem import StampItem
from definitions.itemdef.specifictypes.StatueItem import StatueItem
from definitions.itemdef.specifictypes.StoneItem import StoneItem
from definitions.itemdef.specifictypes.ToolItem import ToolItem
from definitions.itemdef.specifictypes.WeaponItem import WeaponItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.DescItem import DescItem
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository


class SpecificItemRepo(Repository[BaseItem]):
	"""
	Dependent on: ItemDetailsRepo, RecipeRepo, CardRepo, EnemyDetailsRepo, StatueRepo, FishingToolkitRepo
	"""

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
			                      TypeGen.aRing, TypeGen.aKeychain}:
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
			else:
				havntDone.add(item.typeGen.value)
		print(havntDone)
