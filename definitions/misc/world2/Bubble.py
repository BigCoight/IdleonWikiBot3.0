from typing import List, Union

from pydantic import validator

from definitions.common.Component import Component
from definitions.common.LiquidComponent import LiquidComponent
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import replaceUnderscores


class Bubble(IdleonModel):
	cauldron: str
	x1: Numeric
	x2: Numeric
	func: str
	description: str
	requirements: List[Union[Component, LiquidComponent]]

	_removeUnderscores = validator("description", allow_reuse = True)(replaceUnderscores)
