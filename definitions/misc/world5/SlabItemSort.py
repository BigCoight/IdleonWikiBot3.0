from definitions.common.QtylessComponent import QtylessComponent
from definitions.master.IdleonModel import IdleonModel


class SlabItemSort(IdleonModel):
	item: QtylessComponent
	order: int

	def sortKey(self) -> str:
		return "Order"
