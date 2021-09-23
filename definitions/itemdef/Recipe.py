from typing import List
from pydantic import BaseModel


class Component(BaseModel):
    item: str
    quantity: int


class Recipe(BaseModel):
    recipe: List[Component]
    levelReqToCraft: int
    expGiven: int
    no: int
    tab: str
