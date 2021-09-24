from pydantic import BaseModel


class FishingToolkit(BaseModel):
    name: str
    depth1: int
    depth2: int
    depth3: int
    depth4: int
    fishingExp: int
    fishingSpeed: int
    fishingPower: int
