from typing import List, Dict, Union, Callable

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class Vendor(IdleonModel):
	vendor: str
	item: str
	quantity: Integer
	no: Integer
	purchasePrice: Integer

	def shouldCompare(self) -> bool:
		return False

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"number": "no",
			"item": self.getItemDisplayName,
			"vendor": "vendor",
			"stock": "quantity",
			"buyprice": "purchasePrice",

		}

	def getItemDisplayName(self) -> str:
		return ItemDetailRepo.getDisplayName(self.item)

	def __str__(self) -> str:
		res = f"{self.quantity}x " + "{{CraftReq|"
		res += self.getItemDisplayName() + "}}"
		return res


class ItemVendors(IdleonModel):
	vendors: List[Vendor]

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{Vendoritem/head}}" + "\n"
		for vendor in self.vendors:
			res += "{{Vendoritem" + vendor.writeWiki(False) + "}}" + "\n"
		res += "|}"
		return res


class Vendors(IdleonModel):
	area: str
	items: List[Vendor]

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{Vendoritem/head"f"|{self.area} Shop""}}" + "\n"
		for vendor in self.items:
			res += "{{Vendoritem" + vendor.writeWiki(False) + "}}" + "\n"
		res += "|}"
		return res
