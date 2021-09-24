from pydantic import BaseModel, validator

from helpers.HelperFunctions import replaceUnderscores


class FishingToolkit(BaseModel):
    name: str
    depth1: int
    depth2: int
    depth3: int
    depth4: int
    fishingExp: int
    fishingSpeed: int
    fishingPower: int

    _replaceUnderscores = validator("name", allow_reuse = True)(replaceUnderscores)
