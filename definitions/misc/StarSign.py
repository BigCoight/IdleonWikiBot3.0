from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class StarSign(IdleonModel):
	name: str
	text: str
	x: Integer
	y: Integer
	prevReq: Integer
	cost: Integer

