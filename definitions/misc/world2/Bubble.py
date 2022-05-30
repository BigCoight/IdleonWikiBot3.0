from typing import List

from pydantic import validator

from definitions.component.ComponentBase import ComponentBase
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import replaceUnderscores


class Bubble(IdleonModel):
	cauldron: str
	x1: Numeric
	x2: Numeric
	func: str
	description: str
	requirements: List[ComponentBase]

	def sortKey(self) -> str:
		return self.cauldron

	_removeUnderscores = validator("description", allow_reuse = True)(replaceUnderscores)
