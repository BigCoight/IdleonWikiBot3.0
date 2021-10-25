from pydantic import BaseModel

from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class Component(BaseModel):
	"""
	item: str
	quantity: int
	"""
	item: str
	quantity: Integer

	def __str__(self) -> str:
		res = f"{self.quantity}x" + "{{CraftReq|"
		res += ItemDetailRepo.getDisplayName(self.item)
		return res + "}}"
