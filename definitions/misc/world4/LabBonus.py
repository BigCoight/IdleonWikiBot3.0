from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer, Numeric


class LabBonus(IdleonModel):
	no: Integer
	x: Integer
	y: Integer
	range: Integer
	bonusOn: Numeric
	bonusOff: Numeric
	name: str
	description: str
