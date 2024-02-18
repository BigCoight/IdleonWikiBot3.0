from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class JadeUpgrade(IdleonModel):
	name: str
	costA: Integer
	costB: int
	imageId: int
	filler1: str
	filler2: str
	bonus: str
