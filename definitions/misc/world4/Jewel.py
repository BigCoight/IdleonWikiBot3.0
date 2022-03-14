from typing import List

from definitions.common.Component import Component
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class Jewel(IdleonModel):
	x: Integer
	y: Integer
	range: Integer
	effect: str
	description: str
	requirements: List[Component]
	name: str
	x1: Numeric
