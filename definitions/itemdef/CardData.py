from typing import Union

from pydantic import BaseModel


class CardData(BaseModel):
    cardID: str
    category: str
    perTier: Union[int, float]
    effect: str
    bonus: Union[int, float]
    order: int
