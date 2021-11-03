from pydantic import validator

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer
from helpers.HelperFunctions import replaceUnderscores


class Shrine(IdleonModel):
	desc: str
	baseBonus: Numeric
	increment: Numeric
	misc: Integer

	_repU = validator("desc", pre = True, allow_reuse = True)(replaceUnderscores)
