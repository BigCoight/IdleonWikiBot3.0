from typing import List

from pydantic import BaseModel, validator

from definitions.common.Component import Component
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import replaceUnderscores


class Bubble(BaseModel):
	cauldron: str
	x1: Numeric
	x2: Numeric
	func: str
	description: str
	requirements: List[Component]

	_removeUnderscores = validator("description", allow_reuse = True)(replaceUnderscores)

