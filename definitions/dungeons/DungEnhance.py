from typing import List

from pydantic import BaseModel

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class MiscUpgrade(IdleonModel):
	upgrade: str
	min: Integer
	max: Integer


class DungEnhance(IdleonModel):
	enhancements: List[MiscUpgrade]
