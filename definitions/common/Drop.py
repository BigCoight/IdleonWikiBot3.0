from pydantic import BaseModel

from helpers.CustomTypes import Numeric


class Drop(BaseModel):
	"""
		item: str
		quantity: int
		chance: float
		questLink: str
	"""
	item: str
	quantity: Numeric
	chance: float
	questLink: str
