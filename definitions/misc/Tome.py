from typing import Optional

from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class TomeScaling(IdleonEnum):
	decay = "0"
	decayLog = "1"
	linearToMax = "2"
	inverseDecay = "3"


class Tome(IdleonModel):
	name: str
	keyQty: Integer
	scalingType: TomeScaling
	totalVal: Integer
	decimalDisplay: Optional[Integer]
	desc: Optional[str]
