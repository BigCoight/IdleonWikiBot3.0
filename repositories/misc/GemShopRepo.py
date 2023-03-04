import string
from typing import List

from definitions.misc.GemShopItem import GemShopItem
from helpers.Constants import Constants
from helpers.HelperFunctions import getFrom4dArray, getFromSplit, replaceUnderscores, formatToSingleSpace
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository


class GemShopRepo(Repository[GemShopItem]):
	descOverrides = {
		"CardPack1": "Contains 3 cards from these sets: Blunder Hills, Easy Resources, & Bosses n Nightmares (15% chance).<br/>Rarties - Lvl 1: 50%, Lvl 2: 35%, Lvl 3: 15%.",
		"CardPack2": "Contains 4 cards from these sets: Yum-Yum Desert, Medium Resources, & Bosses n Nightmares (40% chance).<br/>Rarties - Lvl 1: 26%, Lvl 2: 30%, Lvl 3: 27%, Lvl 4: 17%.",
		"CardPack3": "Contains 4 cards from these sets: Frostbite Tundra, Hard Resources, & Bosses n Nightmares (At least 1).<br/>Rarties - Lvl 2: 30%, Lvl 3: 35%, Lvl 4: 35%.",
		"CardPack5": "Contains 4 cards from these sets: Hyperion Nebula, Hard Resources, & Bosses n Nightmares (At least 1).<br/>Rarties - Lvl 2: 30%, Lvl 3: 35%, Lvl 4: 35%.",
		"CardPack4": "Contains 3 cards from these sets: Dungeons, Dungeon Boss (35% Chance).<br/>Rarties - Lvl 1: 35%, ""Lvl 2: 29%, Lvl 3: 20%, Lvl 4: 16%.",
		"CardPack6": "Contains 4 cards from these sets: Smoulderin' Plateau, Hard Resources, & Bosses n Nightmares(At least ""1).<br/>Rarties - Lvl 2: 30%, Lvl 3: 35%, Lvl 4: 35%.",
	}

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ItemDetailRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def parse(cls, value) -> GemShopItem:
		return GemShopItem.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["GemShop"]

	@classmethod
	def generateRepo(cls) -> None:
		gemShopItems = getFrom4dArray(cls.getSection())[0]
		for n, parentSection in enumerate(gemShopItems):
			for m, childSection in enumerate(parentSection):
				for gemShopSlot in childSection:
					gemShop = getFromSplit(gemShopSlot)
					gemShop = [replaceUnderscores(x) for x in gemShop]
					if gemShop[0] in cls.descOverrides:
						gemShop[2] = cls.descOverrides[gemShop[0]]
					section = Constants.gemShopSections[n][m]
					itemName = ""
					if ItemDetailRepo.contains(gemShop[0]):
						itemName = ItemDetailRepo.getDisplayName(gemShop[0])
					toAdd = GemShopItem(
						section = section,
						name = gemShop[0],
						mtxName = string.capwords(gemShop[1]),
						itemDisplayName = itemName,
						desc = formatToSingleSpace(gemShop[2]),
						cost = gemShop[3],
						no = gemShop[4],
						maxPurchases = gemShop[5],
						qty = gemShop[6],
						costIncrement = gemShop[7]
					)
					cls.addList(toAdd)
					if gemShop[3] == "GemCostNum":
						continue
					cls.add(gemShop[0], toAdd)

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.get(name).mtxName
