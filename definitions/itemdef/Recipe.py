from typing import List

from pydantic import BaseModel

from definitions.common.Component import Component


class Recipe(BaseModel):
    recipe: List[Component]
    levelReqToCraft: int
    expGiven: int
    no: int
    tab: str
