from typing import Dict, Union, Callable, List

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.ToolItem import ToolItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.StatItem import StatItem
from definitions.master.IdleonModel import IdleonModel
from definitions.misc.world3.TrapBox import TrapBox
from helpers.Constants import Constants
from helpers.CustomTypes import Integer
from repositories.item.TrapBoxRepo import TrapBoxRepo


class TrapBoxItem(ToolItem):
	trapBoxData: TrapBox

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> BaseItem:
		skill = cls.isSkill(item)
		return TrapBoxItem(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			lvReqToCraft = item.lvReqToCraft,
			lvReqToEquip = item.lvReqToEquip,
			Class = item.Class,
			Skill = skill,
			Skill_Power = item.Weapon_Power,
			Weapon_Power = 0,
			Speed = item.Speed,
			STR = item.STR,
			AGI = item.AGI,
			WIS = item.WIS,
			LUK = item.LUK,
			Defence = item.Defence,
			miscUp1 = cls.getMisc1(item),
			miscUp2 = cls.getMisc2(item),
			Upgrade_Slots_Left = item.Upgrade_Slots_Left,
			trapBoxData = TrapBoxRepo.get(item.internalID)
		)

	def writeAfter(self) -> List[IdleonModel]:
		return [self.trapBoxData]


