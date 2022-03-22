from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class Meal(IdleonModel):
	name: str
	cookingReq: Numeric
	bonusQty: Numeric
	bonusText: str
	description: str
	bonusKey: str
