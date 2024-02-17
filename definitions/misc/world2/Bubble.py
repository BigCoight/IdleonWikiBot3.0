from typing import List

from pydantic import validator

from definitions.component.ComponentBase import ComponentBase
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric
from helpers.HelperFunctions import replaceUnderscores


class Bubble(IdleonModel):
	cauldron: str
	name: str
	x1: Numeric
	x2: Numeric
	func: str
	description: str
	requirements: List[ComponentBase]
	bonusKey: str

	_removeUnderscores = validator("description", allow_reuse = True)(replaceUnderscores)

	def compareKey(self) -> str:
		return self.name

	def useCompareKeyName(self) -> bool:
		return True


class Cauldron(IdleonModel):
	bubbles: List[Bubble]
