from definitions.component.ComponentBase import ComponentBase
from helpers.CustomTypes import Integer


class LiquidComponent(ComponentBase):
	liquidNo: str
	quantity: Integer

	def __str__(self) -> str:
		res = ""
		if self.quantity != -1:
			res += f"{self.quantity}x"
		res += "{{Liquid|"
		res += self.liquidNo
		return res + "}}"
