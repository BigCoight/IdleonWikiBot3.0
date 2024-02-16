from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class BonusMap(IdleonModel):
	id: Integer
	bonus: str
