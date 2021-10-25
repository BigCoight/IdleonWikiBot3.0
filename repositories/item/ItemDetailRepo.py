import re
from typing import Dict, Type, List

from definitions.itemdef.initialtypes.CommonItem import CommonItem
from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from helpers.HelperFunctions import formatStr
from repositories.master.Repository import Repository


class ItemDetailRepo(Repository[CommonItem]):

	@classmethod
	def parse(cls, value) -> CommonItem:
		return CommonItem.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Items", "Items2"]

	@classmethod
	def generateRepo(cls) -> None:

		itemTypes: Dict[str, Type[CommonItem]] = {
			'Item': CommonItem,
			'Quest': QuestItem,
			'Equip': EquipItem,
			'Consumable': ConsumableItem,
		}

		reNames = r'.\.addNew([a-zA-Z0-9_]*)\("([a-zA-Z0-9_]*)", ..?.?\);'
		reData = r'..\.setReserved\("([a-zA-Z0-9_]*)", ?"?([^\s"]*)"?\)'
		for i in range(len(cls.getSections())):
			itemText = formatStr(cls.getSection(i), ["\n", "  "])
			itemData = re.split(reNames, itemText)
			for i in range(0, len(itemData), 3):
				if data := re.findall(reData, itemData[i]):
					itemName = itemData[i + 2]
					itemType = itemData[i + 1]
					item = {}
					for atr, val in data:
						item[atr] = formatStr(val, replaceUnderscores = True)
					item["internalID"] = itemName
					item["Type"] = item["Type"].title()
					cls.add(itemName, itemTypes[itemType].parse_obj(item))

	@classmethod
	def isItemOfTypeGen(cls, item: str, typeGen: TypeGen) -> bool:
		if not cls.contains(item):
			return False
		return cls.get(item).typeGen == typeGen

	@classmethod
	def getDisplayName(cls, name: str) -> str:
		if item := cls.get(name):
			return item.displayName
		print(f"{name} not found in ItemRepo!!!")
		return ""

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return cls.getDisplayName(name)
