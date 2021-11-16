from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from definitions.itemdef.specifictypes.master.StatItem import StatItem
from helpers.Constants import Constants
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import camelCaseSplitter


class ObolItem(StatItem):
	family: str
	rarity: str
	Skill: str
	Skill_Power: Integer

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> BaseItem:
		skill = cls.isSkill(item)
		skillPower = 0
		weaponPower = 0
		rarity = item.displayName.split(" ")[0]
		family = cls.obolFamily(item)
		if skill:
			skillPower = item.Weapon_Power
		else:
			weaponPower = item.Weapon_Power
		return ObolItem(
			internalName = item.internalID,
			displayName = item.displayName,
			sellPrice = item.sellPrice,
			typeGen = item.typeGen,
			Type = item.Type,
			Skill = skill,
			rarity = rarity,
			Weapon_Power = weaponPower,
			Skill_Power = skillPower,
			family = family,
			STR = item.STR,
			AGI = item.AGI,
			WIS = item.WIS,
			LUK = item.LUK,
			Defence = item.Defence,
			miscUp1 = cls.getMisc1(item),
			miscUp2 = cls.getMisc2(item),
			lvReqToCraft = 0,
			lvReqToEquip = 0,
			Class = item.Class,
			Upgrade_Slots_Left = 0,
		)

	@classmethod
	def isSkill(cls, item: EquipItem) -> str:
		skill = camelCaseSplitter(item.internalID)[-1]
		if skill in Constants.skillNames:
			return skill
		return ""

	@classmethod
	def obolFamily(cls, item: EquipItem) -> str:
		intFamToExt = {
			"0": "STR",
			"1": "AGI",
			"2": "WIS",
			"3": "LUK",
			"Def": "Defence",
			"Luck": "Sixes",
			"Cons": "Construction",
			"A": "Bosses",
			"Kill": "Multikill",
			"EXP": "Experience",
		}
		splitName = camelCaseSplitter(item.internalID)[-1]
		if splitName[-1].isnumeric():
			fam = splitName[-1]
		else:
			fam = splitName
		return intFamToExt.get(fam, fam)

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		base = super().intToWiki()
		extra = {
			"skill": "Skill",
			"skillpower": "Skill_Power",
			"family": "family",
			"rarity": "rarity"
		}
		return {**base, **extra}
