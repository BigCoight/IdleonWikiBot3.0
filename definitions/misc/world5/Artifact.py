from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class Artifact(IdleonModel):
	name: str
	baseBonus: int
	baseFindChance: int
	qtyBonus: int
	bonus: str
	ancientBonus: str
	ancientBonusQty: Numeric
