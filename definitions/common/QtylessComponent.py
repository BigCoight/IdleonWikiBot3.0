from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class QtylessComponent(IdleonModel):
	"""
	item: str
	quantity: int
	"""
	item: str

	def __str__(self) -> str:
		res = "{{CraftReq|"
		res += ItemDetailRepo.getDisplayName(self.item)
		return res + "}}"

	def shouldCompare(self) -> bool:
		return False
