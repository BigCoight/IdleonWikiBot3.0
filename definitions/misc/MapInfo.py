from pydantic import BaseModel

from helpers.CustomTypes import Integer
from typing import List

class MapInfo(BaseModel):
	id: Integer
	portalRequirements: List[Integer]
