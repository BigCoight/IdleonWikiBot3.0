from typing import Dict, Union, Callable

from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel


class MapData(IdleonModel):
	area: str
	world: str

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {"area": "area", "world": "world"}