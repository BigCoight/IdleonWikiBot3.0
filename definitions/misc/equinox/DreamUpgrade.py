from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class DreamUpgrade(IdleonModel):
	name: str
	upgrade: str
	x1: Integer
	x2: Integer
