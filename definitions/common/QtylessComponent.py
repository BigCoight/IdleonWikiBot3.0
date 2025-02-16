from definitions.master.IdleonModel import IdleonModel
from repositories.item.ItemDetailRepo import ItemDetailRepo


class QtylessComponent(IdleonModel):
	"""
	item: str
	quantity: int
	"""
	item: str

	def __str__(self) -> str:
		res = "{{ItemDisplay|"
		res += ItemDetailRepo.getDisplayName(self.item)
		return res + "}}"

	def shouldCompare(self) -> bool:
		return False
