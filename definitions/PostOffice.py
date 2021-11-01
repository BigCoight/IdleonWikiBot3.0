from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer
from repositories.item.ItemDetailRepo import ItemDetailRepo


class Part(IdleonModel):
	item: str
	base: Integer
	increment: Numeric

	def shouldCompare(self) -> bool:
		return False

	def __str__(self) -> str:
		res = f"{self.base}x"
		res += "{{CraftReq|" + ItemDetailRepo.getDisplayName(self.item) + "}} "
		res += f"inc: {self.increment}"
		return res


class PostOffice(IdleonModel):
	orders: List[Part]
	coinRewards: List[Integer]
	rewards: List[Part]
