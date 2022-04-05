import string
from typing import Union

from pydantic import validator

from definitions.Validators import validateInteger
from definitions.itemdef.initialtypes.CommonItem import CommonItem
from definitions.itemdef.initialtypes.ItemTypes import ClassType, BagType
from helpers.CustomTypes import Integer


class EquipItem(CommonItem):
	"""
	This dataclass contains all of the base details of the items that whose type
	is Equip
	"""
	lvReqToEquip: Integer
	Class: Union[BagType, ClassType]
	Speed: Integer
	Reach: Integer
	Weapon_Power: Integer
	STR: Integer
	AGI: Integer
	WIS: Integer
	LUK: Integer
	Defence: Integer
	UQ1txt: str
	UQ1val: Integer
	UQ2txt: str
	UQ2val: Integer
	Upgrade_Slots_Left: Integer

	_convertInts = validator("Defence", "lvReqToEquip", pre = True, allow_reuse = True)(validateInteger)

	@validator('Class', pre = True)
	def convertClass(cls, v: str):
		if v in BagType:
			return BagType(v)
		return ClassType(string.capwords(v))
