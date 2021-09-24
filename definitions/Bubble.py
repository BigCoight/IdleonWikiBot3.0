from typing import Union, List

from pydantic import BaseModel, validator

from definitions.common.Component import Component
from helpers.HelperFunctions import replaceUnderscores


class Bubble(BaseModel):
	cauldron: str
	x1: Union[int, float]
	x2: Union[int, float]
	func: str
	description: str
	requirements: List[Component]

	_removeUnderscores = validator("description", allow_reuse = True)(replaceUnderscores)

