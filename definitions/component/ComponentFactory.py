from typing import Union

from definitions.component.Component import Component
from definitions.component.ComponentBase import ComponentBase
from definitions.component.CropComponent import CropComponent
from definitions.component.JadeComponent import JadeComponent
from definitions.component.LiquidComponent import LiquidComponent
from definitions.component.MealComponent import MealComponent
from definitions.component.SailTeasureComponent import SailTreasureComponent
from definitions.component.SpiceComponent import SpiceComponent
from definitions.component.SummonComponent import SummonComponent
from helpers.CustomTypes import Integer


class ComponentFactory:
	# itemName -> ["Type", "id"]
	# Check _customBlock_removeitems = function
	hardCodedComponents = {
		"W6item0": ["Jade", ""],
		"W6item1": ["Crop", "3"],
		"W6item2": ["Crop", "60"],
		"W6item3": ["Crop", "46"],
		"W6item4": ["Crop", "72"],
		"W6item5": ["Crop", "99"],
		"W6item6": ["Summon", "0"],
		"W6item7": ["Summon", "0"],
		"W6item8": ["Summon", "0"],
		"W6item9": ["Summon", "0"],
		"W6item10": ["Summon", "0"],
	}

	@classmethod
	def getComponent(cls, part: str, quantity: Union[Integer, str]) -> ComponentBase:
		if part in cls.hardCodedComponents:
			typ, num = cls.hardCodedComponents[part]
			if typ == "Jade":
				return JadeComponent(quantity = quantity)
			if typ == "Crop":
				return CropComponent(cropId = num, quantity = quantity)
			if typ == "Summon":
				return SummonComponent(summonId = num, quantity = quantity)
		if part[0:6] == "Liquid":
			return LiquidComponent(liquidNo = part[6:], quantity = quantity)
		if part[0:5] == "Spice":
			return SpiceComponent(spiceNo = part[5:], quantity = quantity)
		if part[0:4] == "Meal":
			return MealComponent(mealNo = part[4:], quantity = quantity)
		if part[0:6] == "SailTr":
			return SailTreasureComponent(sailTreasureNo = part[6:], quantity = quantity)
		return Component(item = part, quantity = quantity)
