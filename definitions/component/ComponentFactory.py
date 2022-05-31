from typing import Union

from definitions.component.Component import Component
from definitions.component.ComponentBase import ComponentBase
from definitions.component.LiquidComponent import LiquidComponent
from definitions.component.MealComponent import MealComponent
from definitions.component.SpiceComponent import SpiceComponent
from helpers.CustomTypes import Integer


class ComponentFactory:
	@classmethod
	def getComponent(cls, part: str, quantity: Union[Integer, str]) -> ComponentBase:
		if part[0:6] == "Liquid":
			return LiquidComponent(liquidNo = part[6:], quantity = quantity)
		if part[0:5] == "Spice":
			return SpiceComponent(spiceNo = part[5:], quantity = quantity)
		if part[0:4] == "Meal":
			return MealComponent(mealNo = part[4:], quantity = quantity)
		return Component(item = part, quantity = quantity)
