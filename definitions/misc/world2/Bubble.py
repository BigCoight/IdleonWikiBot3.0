from typing import List

from pydantic import validator

from definitions.common.Component import Component
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import replaceUnderscores


class Bubble(IdleonModel):
	cauldron: str
	x1: Numeric
	x2: Numeric
	func: str
	description: str
	requirements: List[Component]

	_removeUnderscores = validator("description", allow_reuse = True)(replaceUnderscores)
