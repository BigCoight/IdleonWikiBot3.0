from pydantic import BaseModel

from helpers.CustomTypes import Numeric


class Prayer(BaseModel):
	id: int
	bonus: str
	curse: str
	x1: Numeric
	x2: Numeric
	soul: str
	mult: int
	unlockZone: str
	unlockWave: int


