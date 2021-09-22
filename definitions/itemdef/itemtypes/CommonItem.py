from helpers.HelperFunctions import scientificToInt
from pydantic import BaseModel
from pydantic.class_validators import validator
from definitions.itemdef.itemtypes.ItemTypes import TypeGen


class CommonItem(BaseModel):
    ''' 
    This dataclass contains all of the base details of the items
    '''
    internalID: str
    displayName: str
    sellPrice: int
    typeGen: TypeGen
    ID: int
    Type: str
    lvReqToCraft: int

    @validator("lvReqToCraft", "ID", pre=True)
    def validateLvReq(cls, v: str) -> int:
        if not v.isnumeric():
            return -1
        return scientificToInt(v)
