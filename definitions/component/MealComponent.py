from definitions.component.ComponentBase import ComponentBase
from helpers.CustomTypes import Integer
from repositories.misc.world4.MealRepo import MealRepo


class MealComponent(ComponentBase):
	mealNo: str
	quantity: Integer

	def __str__(self) -> str:
		res = ""
		if self.quantity != -1:
			res += f"{self.quantity}x"

		name = MealRepo.getList(int(self.mealNo)).name
		res += "{{Icons"f"|{name}|text={name}""}}"
		return res
