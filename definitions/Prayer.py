from pydantic import BaseModel

from helpers.CustomTypes import Numeric, Integer


class Prayer(BaseModel):
	id: Integer
	bonus: str
	curse: str
	x1: Numeric
	x2: Numeric
	soul: str
	mult: Integer
	unlockZone: str
	unlockWave: Integer


