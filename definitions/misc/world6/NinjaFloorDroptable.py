from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class NinjaFloorDrop(IdleonModel):
	ninjaItem: str
	chance: Numeric


class NinjaFloorDroptable(IdleonModel):
	drops: List[NinjaFloorDrop]
