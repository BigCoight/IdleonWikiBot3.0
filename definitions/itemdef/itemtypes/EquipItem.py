from pydantic import validator

from definitions.itemdef.itemtypes.ItemTypes import ClassType
from helpers.HelperFunctions import scientificToInt
from definitions.itemdef.itemtypes.CommonItem import CommonItem


class EquipItem(CommonItem):
    """
    This dataclass contains all of the base details of the items that whose type
    is Equip
    """
    lvReqToEquip: int
    Class: ClassType
    Speed: int
    Reach: int
    Weapon_Power: int
    STR: int
    AGI: int
    WIS: int
    LUK: int
    Defence: int
    UQ1txt: str
    UQ1val: int
    UQ2txt: str
    UQ2val: int
    Upgrade_Slots_Left: int

    @validator('Defence', "lvReqToEquip", pre = True)
    def convertScientific(cls, v: str):
        return scientificToInt(v)

    @validator('Class', pre = True)
    def convertClass(cls, v: str):
        return ClassType(v.title())
