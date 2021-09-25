from pydantic import BaseModel, validator

from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import replaceUnderscores


class Shrine(BaseModel):
	desc: str
	baseBonus: Numeric
	increment: Numeric
	misc: int

	_repU = validator("desc", pre = True, allow_reuse = True)(replaceUnderscores)
