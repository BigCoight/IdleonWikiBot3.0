from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel


class NinjaItemType(IdleonEnum):
	Item = "Item"
	Weapon = "Weapon"
	Trinket = "Trinket"
	PristineCharm = "PristineCharm"
	Gemstone = "Gemstone"

	@staticmethod
	def fromInt(val: int):
		return [NinjaItemType.Item, NinjaItemType.Weapon, NinjaItemType.Trinket, NinjaItemType.PristineCharm,
		        NinjaItemType.Gemstone][val]


class BaseNinjaItem(IdleonModel):
	internalId: str
	itemTypeId: int
	itemType: NinjaItemType
	itemId: int
	name: str
