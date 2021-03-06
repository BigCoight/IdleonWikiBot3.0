from definitions.itemdef.initialtypes.CommonItem import CommonItem
from helpers.CustomTypes import Integer


class ConsumableItem(CommonItem):
	'''
	This dataclass contails all of the base details of the items that whos type is
	Consumeable
	'''
	desc_line1: str
	desc_line2: str
	desc_line3: str
	desc_line4: str
	desc_line5: str
	desc_line6: str
	desc_line7: str
	desc_line8: str
	Effect: str
	Trigger: str
	Amount: Integer
	Cooldown: Integer
