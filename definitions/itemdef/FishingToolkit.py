from pydantic import BaseModel


class FishingToolkit(BaseModel):
    name: str
    depth1: int
    depth2: int
    depth3: int
    depth4: int
    fishExp: int
    fishSpeed: int
    fishPower: int
