from pydantic import BaseModel

from helpers.CustomTypes import Numeric


class StatueData(BaseModel):
    name: str
    effect: str
    dk: int
    bonus: Numeric
