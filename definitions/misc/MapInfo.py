from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from typing import List

class MapInfo(IdleonModel):
	id: Integer
	portalRequirements: List[Integer]
