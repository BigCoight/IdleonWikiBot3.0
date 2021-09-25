from typing import Union

from pydantic import validator

from definitions.Validators import validateInteger
from definitions.itemdef.itemtypes.CommonItem import CommonItem
from definitions.itemdef.itemtypes.ItemTypes import ClassType, BagType


class EquipItem(CommonItem):
    """
    This dataclass contains all of the base details of the items that whose type
    is Equip
    """
    lvReqToEquip: int
    Class: Union[BagType,ClassType]
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

    _convertInts = validator("Defence", "lvReqToEquip", pre = True, allow_reuse = True)(validateInteger)

    @validator('Class', pre = True)
    def convertClass(cls, v: str):
        if v in BagType:
            return BagType(v)
        return ClassType(v.title())
