from typing import List, Union

from definitions.itemdef.initialtypes.ItemTypes import TypeGen
from definitions.master.IdleonModel import IdleonModel


class Use(IdleonModel):
	repoSource: str
	key: str
	name: str
	amount: Union[int, str]
	type: str


class Uses(IdleonModel):
	uses: List[Use]
	typeGen: TypeGen
	type: str
