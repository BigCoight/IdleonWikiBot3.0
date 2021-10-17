from typing import List, Dict, Union, Callable

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class Vendor(IdleonModel):
	vendor: str
	quantity: Integer
	no: Integer
	purchasePrice: Integer

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {
			"number": "no",
			"vendor": "vendor",
			"stock": "quantity",
			"buyprice": "purchasePrice"
		}


class Vendors(IdleonModel):
	vendors: List[Vendor]

	def writeWiki(self, newLine = True) -> str:
		res = "{{Vendoritem/head}}" + "\n"
		for vendor in self.vendors:
			res += "{{Vendoritem" + vendor.writeWiki(False) + "}}" + "\n"
		res += "|}"
		return res
