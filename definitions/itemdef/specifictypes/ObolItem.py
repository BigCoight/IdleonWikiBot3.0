from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.EquipItem import EquipItem
from definitions.itemdef.specifictypes.master.BaseItem import BaseItem
from helpers.Constants import Constants
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import camelCaseSplitter


class ObolItem(BaseItem):
	family: str
	rarity: str
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

	@classmethod
	def fromItemDetails(cls, item: EquipItem) -> BaseItem:
		misc1 = f"+{item.UQ1val} {item.UQ1txt.title()}"
		misc2 = f"+{item.UQ2val} {item.UQ2txt.title()}"
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
			miscUp1 = misc1,
			miscUp2 = misc2,
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
			"weaponpower": "Weapon_Power",
			"skillpower": "Skill_Power",
			"str": "STR",
			"agi": "AGI",
			"wis": "WIS",
			"luck": "LUK",
			"misc": "miscUp1",
			"defence": "Defence",
			"family": "family",
			"rarity": "rarity"
		}
		return {**base, **extra}
