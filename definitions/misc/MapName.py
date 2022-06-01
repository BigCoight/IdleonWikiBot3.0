from pydantic import validator

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import replaceUnderscores


class MapName(IdleonModel):
	intName: str
	name: str
	id: Integer

	_repU = validator("name", pre = True, allow_reuse = True)(replaceUnderscores)
