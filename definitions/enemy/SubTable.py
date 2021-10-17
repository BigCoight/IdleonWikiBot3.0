from typing import List

from pydantic import BaseModel

from helpers.CustomTypes import Integer


class SubTable(BaseModel):
	name: str
	chance: float
	quantity: Integer


class SubTables(BaseModel):
	rare: List[SubTable]
	mega: List[SubTable]
