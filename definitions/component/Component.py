from definitions.component.ComponentBase import ComponentBase
from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class Component(ComponentBase):
	item: str
	quantity: Integer

	def compareKey(self) -> str:
		return self.item

	def __str__(self) -> str:
		res = ""
		if self.quantity != -1:
			res += f"{self.quantity}x"
		res += "{{CraftReq|"
		res += ItemDetailRepo.getDisplayName(self.item)
		return res + "}}"

	def shouldCompare(self) -> bool:
		return False
