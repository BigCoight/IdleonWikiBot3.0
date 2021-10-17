from pydantic import BaseModel, validator

from helpers.CustomTypes import Numeric, Integer
from helpers.HelperFunctions import replaceUnderscores


class Shrine(BaseModel):
	desc: str
	baseBonus: Numeric
	increment: Numeric
	misc: Integer

	_repU = validator("desc", pre = True, allow_reuse = True)(replaceUnderscores)
