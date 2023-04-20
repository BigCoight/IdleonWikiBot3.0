import re
import string
from typing import Dict, Type, List

from definitions.itemdef.initialtypes.CommonItem import CommonItem
from definitions.itemdef.initialtypes.ConsumableItem import ConsumableItem
from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.itemdef.initialtypes.QuestItem import QuestItem
from helpers.Constants import Constants
from helpers.HelperFunctions import formatStr
from repositories.master.Repository import Repository


class ItemDetailRepo(Repository[CommonItem]):

    @classmethod
    def getCategory(cls) -> str:
        return "Item"

    @classmethod
    def parse(cls, value) -> CommonItem:
        return CommonItem.parse_obj(value)

    @classmethod
    def getSections(cls) -> List[str]:
        return [f"Items{i}" for i in range(Constants.numItemSections)]

    @classmethod
    def generateRepo(cls) -> None:

        itemTypes: Dict[str, Type[CommonItem]] = {
            'Item': CommonItem,
            'Quest': QuestItem,
            'Equip': EquipItem,
            'Consumable': ConsumableItem,
        }

        reNames = r'.\.addNew(.*?)\("(.*?)", .\)'
        reData = r'.\..\.(\S*?) = ?"?(.*?)"?\)'
        for j in range(len(cls.getSections())):
            itemText = formatStr(cls.getSection(j), ["\n", "  "])
            itemData = re.split(reNames, itemText)
            for i in range(0, len(itemData), 3):
                if data := re.findall(reData, itemData[i]):
                    itemName = itemData[i + 2]
                    itemType = itemData[i + 1]
                    item = {}
                    for atr, val in data:
                        item[atr] = formatStr(val, replaceUnderscores=True)
                    item["internalID"] = itemName
                    item["Type"] = string.capwords(item["Type"])
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
