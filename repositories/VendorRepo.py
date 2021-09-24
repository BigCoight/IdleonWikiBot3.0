
from typing import Dict, Type, Union, List

from definitions.itemdef.CardData import CardData
from definitions.itemdef.Recipe import Recipe, Component
from definitions.itemdef.Vendors import Vendors, Vendor
from repositories.MapNameRepo import MapNameRepo
from repositories.Repository import Repository
from definitions.itemdef.itemtypes.CommonItem import CommonItem
from definitions.itemdef.itemtypes.QuestItem import QuestItem
from definitions.itemdef.itemtypes.EquipItem import EquipItem
from definitions.itemdef.itemtypes.ConsumableItem import ConsumeableItem
from helpers.HelperFunctions import formatStr, scientificToInt, wrap, strToArray, replaceUnderscores
import re


class VendorRepo(Repository[Vendors]):

    @classmethod
    def getSections(cls) -> List[str]:
        return ["ShopItems", "ShopQTY", "ShopLocations"]

    @ classmethod
    def generateRepo(cls) -> None:
        reElements = r'"([a-zA-Z0-_ ]*)"\.'
        shopItemData = cls.getSection(0)
        shopsItems = [x.split(" ") for x in re.findall(reElements, shopItemData)]
        shopQTYData = cls.getSection(1)
        shopsQTYSs = re.findall(reElements, shopQTYData)
        fixedShopQTY = []
        for shopQTYSs in shopsQTYSs:
            if " " not in shopQTYSs:
                fixedShopQTY.append(list(shopQTYSs))
            else:
                fixedShopQTY.append(shopQTYSs.split(" "))
        shopLocations = cls.getSection(2)
        shopsLocations = [MapNameRepo.get(int(x)) for x in re.findall(
            r"\[([a-zA-Z0-_ ,]*)]", shopLocations)[0].split(", ")]
        for i in range(len(shopsItems)):
            currentLocation = replaceUnderscores(shopsLocations[i])
            for j in range(len(shopsItems[i])):
                tempVendor = Vendor(vendor = currentLocation, quantity = fixedShopQTY[i][j], no = j)
                if current := cls.get(shopsItems[i][j]):
                    current.vendors.append(tempVendor)
                    continue
                cls.add(shopsItems[i][j], Vendors(vendors = [tempVendor]))



