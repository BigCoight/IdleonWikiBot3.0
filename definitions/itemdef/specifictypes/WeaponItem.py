from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.StatItem import StatItem
from helpers.CustomTypes import Integer


class WeaponItem(StatItem):
	Speed: Integer
	Reach: Integer

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> BaseItem:
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
			miscUp1 = cls.getMisc1(item),
			miscUp2 = cls.getMisc2(item),
			Upgrade_Slots_Left = item.Upgrade_Slots_Left,
			Speed = item.Speed,
			Reach = item.Reach
		)

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {
			"speed": "Speed",
			"reach": "Reach",
		}
		return {**base, **extra}
