from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer

class TaskDescription(IdleonModel):
	name: str
	description: str
	extraStr: str
	number1: Integer
	descLine2: str
	numbers: List[Integer]