import re
from typing import List

from definitions.misc.world6.ninjaitems.BaseNinjaItem import NinjaItemType, BaseNinjaItem
from definitions.misc.world6.ninjaitems.NinjaItem import NinjaItem
from definitions.misc.world6.ninjaitems.NinjaPristineCharm import NinjaPristineCharm
from definitions.misc.world6.ninjaitems.NinjaTrinket import NinjaTrinket
from definitions.misc.world6.ninjaitems.NinjaWeapon import NinjaWeapon
from helpers.HelperFunctions import getFromSplit, replaceUnderscores, strToArray
from repositories.master.Repository import Repository
from repositories.misc.world6.SummonEnemyBonusRepo import SummonEnemyBonusRepo


class NinjaItemRepo(Repository[BaseNinjaItem]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		SummonEnemyBonusRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Worlds/6"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["NinjaItems"]

	@classmethod
	def generateRepo(cls) -> None:
		lines = cls.getSection().split("\n")

		for line in lines:
			if "split" in line:
				result = re.findall(r'.\..\.(.+?) = (".+?"\.split\(" "\))\)', line)
				if not len(result) > 0:
					continue
				internalId, splitData = result[0]
				data = [replaceUnderscores(x) for x in getFromSplit(splitData)]
			else:
				result = re.findall(r".\..\.(.+?) = (\[.+?\])\)", line)
				if not len(result) > 0:
					continue
				internalId, listData = result[0]
				data = strToArray(listData, repU = True)

			ninjaItemType = NinjaItemType.fromInt(int(data[0]))
			if ninjaItemType == NinjaItemType.Item:
				toAdd = NinjaItem(
					internalId = internalId,
					itemTypeId = data[0],
					itemType = ninjaItemType,
					itemId = data[1],
					name = data[2],
					desc = data[3],
					filler = data[4]
				)
			elif ninjaItemType == NinjaItemType.Weapon:
				toAdd = NinjaWeapon(
					internalId = internalId,
					itemTypeId = data[0],
					itemType = ninjaItemType,
					itemId = data[1],
					name = data[2],
					x1 = data[3],
					x2 = data[4]
				)
			elif ninjaItemType == NinjaItemType.Trinket:
				toAdd = NinjaTrinket(
					internalId = internalId,
					itemTypeId = data[0],
					itemType = ninjaItemType,
					itemId = data[1],
					name = data[2],
					x1 = data[3],
					bonus = data[4],
					x3 = data[5],
				)
			elif ninjaItemType == NinjaItemType.PristineCharm:
				toAdd = NinjaPristineCharm(
					internalId = internalId,
					itemTypeId = data[0],
					itemType = ninjaItemType,
					itemId = data[1],
					name = data[2],
					x1 = data[3],
					desc = data[4],
					bonus = data[5],
				)
			else:
				toAdd = None
			cls.add(internalId, toAdd)
			cls.addList(toAdd)
