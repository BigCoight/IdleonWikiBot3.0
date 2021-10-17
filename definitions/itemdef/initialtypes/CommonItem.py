from typing import Dict, Union, Callable

from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class CommonItem(IdleonModel):
	"""
	This dataclass contains all of the base details of the items
	"""

	internalID: str
	displayName: str
	sellPrice: Integer
	typeGen: TypeGen
	ID: Integer
	Type: str
	lvReqToCraft: Integer

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return
