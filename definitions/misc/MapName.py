from pydantic import BaseModel, validator

from helpers.CustomTypes import Integer
from helpers.HelperFunctions import replaceUnderscores


class MapName(BaseModel):
	name: str
	id: Integer

	_repU = validator("name", pre = True, allow_reuse = True)(replaceUnderscores)