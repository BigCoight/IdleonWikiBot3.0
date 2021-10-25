from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.StatItem import StatItem
from helpers.Constants import Constants
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import camelCaseSplitter


class ArmourItem(StatItem):
	Skill: str
	Skill_Power: Integer

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> BaseItem:
		skill = cls.isSkill(item)
		skillPower = 0
		weaponPower = 0
		if skill:
			skillPower = item.Weapon_Power
		else:
			weaponPower = item.Weapon_Power
		return ArmourItem(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			lvReqToCraft = item.lvReqToCraft,
			lvReqToEquip = item.lvReqToEquip,
			Class = item.Class,
			Skill = skill,
			Weapon_Power = weaponPower,
			Skill_Power = skillPower,
			STR = item.STR,
			AGI = item.AGI,
			WIS = item.WIS,
			LUK = item.LUK,
			Defence = item.Defence,
			miscUp1 = cls.getMisc1(item),
			miscUp2 = cls.getMisc2(item),
			Upgrade_Slots_Left = item.Upgrade_Slots_Left)

	@classmethod
	def isSkill(cls, item: EquipItem) -> str:
		skill = camelCaseSplitter(item.internalID)[-1]
		if skill in Constants.skillNames:
			return skill
		return ""

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {
			"skill": "Skill",
			"skillpower": "Skill_Power",
		}
		return {**base, **extra}
