from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class CardSet(IdleonModel):
	bonus: str
	scaling: Numeric
	image: str