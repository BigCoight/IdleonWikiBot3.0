from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class Bribe(IdleonModel):
	name: str
	desc: str
	cost: Integer
	type: str
	intName: str
	amount: Integer
