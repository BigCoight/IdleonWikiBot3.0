from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class LabBonus(IdleonModel):
	no: Integer
	x: Integer
	y: Integer
	range: Integer
	x2: Numeric
	x3: Numeric
	name: str
	description: str
