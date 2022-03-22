from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class LiquidComponent(IdleonModel):
	"""
	item: str
	quantity: int
	"""
	liquidNo: str
	quantity: Integer

	def __str__(self) -> str:
		res = ""
		if self.quantity != -1:
			res += f"{self.quantity}x" \
			       f""
		res += "{{Liquid|"
		res += self.liquidNo
		return res + "}}"

	def shouldCompare(self) -> bool:
		return False
