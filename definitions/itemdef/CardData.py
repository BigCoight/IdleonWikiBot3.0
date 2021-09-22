from pydantic import BaseModel


class CardData(BaseModel):
    category: str
    perTier: int
    effect: str
    bonus: int
    order: int
    title: str
