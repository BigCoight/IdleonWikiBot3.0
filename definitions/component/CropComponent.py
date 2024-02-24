from definitions.component.ComponentBase import ComponentBase
from helpers.CustomTypes import Integer


class CropComponent(ComponentBase):
	cropId: str
	quantity: Integer

	def __str__(self) -> str:
		res = ""
		if self.quantity != -1:
			res += f"{self.quantity}x"
		res += "Crop "f"{self.cropId}"
		return res + ""
