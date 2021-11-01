from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class SubTable(IdleonModel):
	name: str
	chance: float
	quantity: Numeric


class SubTables(IdleonModel):
	sources: List[SubTable]
