from typing import List

from pydantic import BaseModel

from helpers.CustomTypes import Integer


class MiscUpgrade(BaseModel):
	upgrade: str
	min: Integer
	max: Integer


class DungEnhance(BaseModel):
	enhancements: List[MiscUpgrade]
