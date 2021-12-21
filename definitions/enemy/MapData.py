from typing import Dict, Union, Callable

from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from typing import List

class MapData(IdleonModel):
	area: str
	world: str
	id: Integer
	portalRequirements: List[Integer]
	
	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {"area": "area", "world": "world"}