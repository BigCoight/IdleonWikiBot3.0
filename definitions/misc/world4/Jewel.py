from typing import List

from definitions.component.ComponentBase import ComponentBase
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class Jewel(IdleonModel):
	x: Integer
	y: Integer
	range: Integer
	effect: str
	description: str
	requirements: List[ComponentBase]
	name: str
	bonusGiven: Numeric
