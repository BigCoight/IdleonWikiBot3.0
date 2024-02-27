from definitions.component.ComponentBase import ComponentBase
from helpers.CustomTypes import Integer


class SummonComponent(ComponentBase):
	summonId: str
	quantity: Integer

	def __str__(self) -> str:
		res = ""
		if self.quantity != -1:
			res += f"{self.quantity}x"
		res += "Soul "f"{self.summonId}"
		return res + ""
