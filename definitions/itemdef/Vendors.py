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
			"vendor": "vendor",
			"stock": "quantity",
			"buyprice": "purchasePrice"
		}

	def __str__(self) -> str:
		res = f"{self.quantity}x " + "{{CraftReq|"
		res += ItemDetailRepo.getDisplayName(self.item) + "}}"
		return res


class ItemVendors(IdleonModel):
	vendors: List[Vendor]

	def writeWiki(self, newLine = True) -> str:
		res = "{{Vendoritem/head}}" + "\n"
		for vendor in self.vendors:
			res += "{{Vendoritem" + vendor.writeWiki(False) + "}}" + "\n"
		res += "|}"
		return res


class Vendors(IdleonModel):
	items: List[Vendor]
