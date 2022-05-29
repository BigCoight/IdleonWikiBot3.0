from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class DungTrait(IdleonModel):
	name: str


class DungSet(IdleonModel):
	rankReq: Numeric
	name: str
	traits: List[DungTrait]
