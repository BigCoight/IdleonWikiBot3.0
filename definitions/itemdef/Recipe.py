from typing import List
from pydantic import BaseModel


class _Component(BaseModel):
    name: str
    amount: int


class Recipe(BaseModel):
    recipe: List[_Component]
    levelReqToCraft: int
    expGiven: int
    no: int
    tab: str
