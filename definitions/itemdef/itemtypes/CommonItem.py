from definitions.Validators import validateInteger
from helpers.HelperFunctions import scientificToInt
from pydantic import BaseModel
from pydantic.class_validators import validator
from definitions.itemdef.itemtypes.ItemTypes import TypeGen


class CommonItem(BaseModel):
    """
    This dataclass contains all of the base details of the items
    """
    internalID: str
    displayName: str
    sellPrice: int
    typeGen: TypeGen
    ID: int
    Type: str
    lvReqToCraft: int

    _convertInts = validator("lvReqToCraft", "ID", "sellPrice", pre = True, allow_reuse = True)(validateInteger)
