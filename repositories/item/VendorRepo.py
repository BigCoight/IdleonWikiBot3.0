import re
from typing import List

from definitions.itemdef.Vendors import Vendors, Vendor, ItemVendors
from helpers.HelperFunctions import replaceUnderscores
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.Repository import Repository
from repositories.misc.MapNameRepo import MapNameRepo


class VendorRepo(Repository[Vendors]):
	"""
	Dependent on ItemDetailsRepo
	"""

	@classmethod
	def getCategory(cls) -> str:
		return "Item"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		MapNameRepo.initialise(cls.codeReader, log)
		ItemDetailRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ShopItems", "ShopQTY", "ShopLocations"]

	@classmethod
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
		shopsLocations = [MapNameRepo.getList(int(x)).name for x in re.findall(
			r"\[([a-zA-Z0-_ ,]*)]", shopLocations)[0].split(", ")]
		for i in range(len(shopsItems)):
			currentLocation = replaceUnderscores(shopsLocations[i])
			for j in range(len(shopsItems[i])):
				tempVendor = Vendor(
					vendor = currentLocation,
					item = shopsItems[i][j],
					quantity = fixedShopQTY[i][j],
					no = j + 1,
					purchasePrice = ItemDetailRepo.get(shopsItems[i][j]).sellPrice * 4)
				if current := cls.get(currentLocation):
					current.items.append(tempVendor)
					continue
				cls.add(currentLocation, Vendors(items = [tempVendor]))

	@classmethod
	def getVendorFromItem(cls, item: str) -> ItemVendors:
		res = ItemVendors(vendors = [])
		for _, items in cls.items():
			for slot in items.items:
				if slot.item == item:
					res.vendors.append(slot)
		return res if res.vendors else None
