from typing import List

from helpers.CustomTypes import Numeric
from definitions.master.IdleonModel import IdleonModel

class DungTrait(IdleonModel):
	name: str

class DungSet(IdleonModel):
	rankReq: Numeric
	name: str
	traits: List[DungTrait]