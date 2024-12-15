from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class LampWish(IdleonModel):
	name: str
	x1: Numeric
	x2: Numeric
	x3: Numeric
	desc: str
