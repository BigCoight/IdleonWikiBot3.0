from typing import Union

from pydantic import BaseModel

from helpers.CustomTypes import Numeric, Integer


class NpcHead(BaseModel):
	location: str
	world: str
	noQuest: Integer
	repeatable: str
	birthWeight: Union[float, Integer]
	starSign: str
	mothersMaidenName: str
	notes: str
