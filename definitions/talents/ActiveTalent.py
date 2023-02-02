from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class ActiveTalent(IdleonModel):
	name: str
	K: Numeric
	D: Numeric
	s: Numeric
	cooldown: Integer
	castTime: Numeric
	manaCost: Integer
	inputReq: Integer
	AFKrange: Integer
	AFKtype: str
	AFKactivity: Integer
