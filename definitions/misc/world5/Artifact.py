from typing import Optional

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
	eldritchBonus: Optional[str] = None
	eldritchBonusQty: Optional[Numeric] = None
	sovereignBonus: Optional[str] = None
	sovereignBonusQty: Optional[Numeric] = None
