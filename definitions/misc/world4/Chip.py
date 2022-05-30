from typing import List

from definitions.component.ComponentBase import ComponentBase
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class Chip(IdleonModel):
	name: str
	bonus: str
	description: str
	requirements: List[ComponentBase]
	bool1: bool
	stat: str
	baseVal: Numeric
