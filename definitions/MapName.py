from pydantic import BaseModel, validator

from helpers.HelperFunctions import replaceUnderscores


class MapName(BaseModel):
	name: str
	id: int

	_repU = validator("name", pre = True, allow_reuse = True)(replaceUnderscores)