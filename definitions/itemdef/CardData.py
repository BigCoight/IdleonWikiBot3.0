from pydantic import BaseModel, validator

from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import replaceUnderscores


class CardData(BaseModel):
    cardID: str
    category: str
    perTier: Numeric
    effect: str
    bonus: Numeric
    order: int

    @validator("effect", pre = True)
    def repU(cls, v: str) -> str:
        return replaceUnderscores(v)