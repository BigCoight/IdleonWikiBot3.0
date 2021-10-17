from pydantic import BaseModel


class KeychainBonus(BaseModel):
	bonus: str
	lvl1: float
	lvl2: float
	lvl3: float
