from pydantic import BaseModel


class StatueData(BaseModel):
    name: str
    effect: str
    _: int
    bonus: int
