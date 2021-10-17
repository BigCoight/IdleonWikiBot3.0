from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.initialtypes.ItemTypes import ClassType
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from helpers.CustomTypes import Integer


class WeaponItem(BaseItem):
	lvReqToCraft: Integer
	lvReqToEquip: Integer
	Class: ClassType
	Weapon_Power: Integer
	Speed: Integer
	Reach: Integer
	STR: Integer
	AGI: Integer
	WIS: Integer
	LUK: Integer
	Defence: Integer
	miscUp1: str
	miscUp2: str
	Upgrade_Slots_Left: Integer

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> BaseItem:
		misc1 = f"{item.UQ1val}{item.UQ1txt.title()}"
		misc2 = f"{item.UQ2val}{item.UQ2txt.title()}"
		return WeaponItem(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			lvReqToCraft = item.lvReqToCraft,
			lvReqToEquip = item.lvReqToEquip,
			Class = item.Class,
			Weapon_Power = item.Weapon_Power,
			STR = item.STR,
			AGI = item.AGI,
			WIS = item.WIS,
			LUK = item.LUK,
			Defence = item.Defence,
			miscUp1 = misc1,
			miscUp2 = misc2,
			Upgrade_Slots_Left = item.Upgrade_Slots_Left,
			Speed = item.Speed,
			Reach = item.Reach
		)

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {
			"class": "Class",
			"level": "lvReqToEquip",
			"speed": "Speed",
			"weaponpower": "Weapon_Power",
			"str": "STR",
			"agi": "AGI",
			"wis": "WIS",
			"luck": "LUK",
			"misc": "miscUp1",
			"reach": "Reach",
			"upgrade": "Upgrade_Slots_Left",
			"defence": "Defence",
		}
		return {**base, **extra}
