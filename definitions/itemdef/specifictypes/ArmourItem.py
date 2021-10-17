from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.initialtypes.ItemTypes import ClassType
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from helpers.Constants import Constants
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import camelCaseSplitter


class ArmourItem(BaseItem):
	lvReqToCraft: Integer
	lvReqToEquip: Integer
	Class: ClassType
	Skill: str
	Weapon_Power: Integer
	Skill_Power: Integer
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
			miscUp1 = misc1,
			miscUp2 = misc2,
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
			"class": "Class",
			"level": "lvReqToEquip",
			"skill": "Skill",
			"weaponpower": "Weapon_Power",
			"skillpower": "Skill_Power",
			"str": "STR",
			"agi": "AGI",
			"wis": "WIS",
			"luck": "LUK",
			"misc": "miscUp1",
			"upgrade": "Upgrade_Slots_Left",
			"defence": "Defence",
		}
		return {**base, **extra}
