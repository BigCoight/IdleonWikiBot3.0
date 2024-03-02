from typing import Optional

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class Sigil(IdleonModel):
	name: str
	unlockCost: Integer
	boostCost: Integer
	unlockBonus: Numeric
	boostBonus: Numeric
	filler: str
	desc: str
	x1: Optional[Integer]
	x2: Optional[Integer]
