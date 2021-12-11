from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class Constellation(IdleonModel):
	name: str
	area: str
	x: Integer
	y: Integer
	num1: Integer
	num2: Integer
	num3: Integer
	starChartPoints: Integer
	requirement: str
	type: Integer