from typing import List

from definitions.common.Component import Component
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class Chip(IdleonModel):
	name: str
	bonus: str
	description: str
	requirements: List[Component]
	bool1: bool
	stat: str
	baseVal: Numeric

