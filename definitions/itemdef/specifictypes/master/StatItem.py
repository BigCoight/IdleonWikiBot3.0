from __future__ import annotations

from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.initialtypes.ItemTypes import ClassType
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from helpers.CustomTypes import Integer


class StatItem(BaseItem):
	lvReqToCraft: Integer
	lvReqToEquip: Integer
	Class: ClassType
	Weapon_Power: Integer
	STR: Integer
	AGI: Integer
	WIS: Integer
	LUK: Integer
	Defence: Integer
	miscUp1: str
	miscUp2: str
	Upgrade_Slots_Left: Integer

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> StatItem:
		return StatItem(
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
			miscUp1 = cls.getMisc1(item),
			miscUp2 = cls.getMisc2(item),
			Upgrade_Slots_Left = item.Upgrade_Slots_Left,
		)

	@classmethod
	def getMisc1(cls, item: EquipItem):
		return f"{item.UQ1val}{item.UQ1txt.title()}"

	@classmethod
	def getMisc2(cls, item: EquipItem):
		return f"{item.UQ2val}{item.UQ2txt.title()}"

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {
			"class": "Class",
			"level": "lvReqToEquip",
			"weaponpower": "Weapon_Power",
			"str": "STR",
			"agi": "AGI",
			"wis": "WIS",
			"luck": "LUK",
			"misc": "miscUp1",
			"misc2": "miscUp2",
			"upgrade": "Upgrade_Slots_Left",
			"defence": "Defence",
		}
		return {**base, **extra}
