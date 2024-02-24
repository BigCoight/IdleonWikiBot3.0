from definitions.component.ComponentBase import ComponentBase
from helpers.CustomTypes import Integer


class SailTreasureComponent(ComponentBase):
	sailTreasureNo: str
	quantity: Integer

	def __str__(self) -> str:
		res = ""
		if self.quantity != -1:
			res += f"{self.quantity}x"
		res += "{{Icons|Sailing Treasure"f" {self.sailTreasureNo}"
		res += " Sailing Treasure"f" {self.sailTreasureNo}"
		return res + "}}"
