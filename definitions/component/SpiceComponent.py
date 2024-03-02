from definitions.component.ComponentBase import ComponentBase
from helpers.Constants import Constants
from helpers.CustomTypes import Integer


class SpiceComponent(ComponentBase):
	spiceNo: str
	quantity: Integer

	def __str__(self) -> str:
		res = ""
		if self.quantity != -1:
			res += f"{self.quantity}x"

		name = Constants.territoryNiceNames[int(self.spiceNo)] + " Spice"
		res += "{{Icons"f"|{name}|text={name}""}}"
		return res
