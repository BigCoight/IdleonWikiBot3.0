from typing import List, Tuple, Union

from pydantic import BaseModel

from definitions.common.Component import Component


class Building(BaseModel):
	description: str
	bonus: str
	lvlUpReq: List[Component]
	maxLvl: int
	costIncrement: List[Union[int, float]]
	bonusInc: Union[int, float]
	misc: int

