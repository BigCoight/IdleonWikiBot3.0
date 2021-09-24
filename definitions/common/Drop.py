from pydantic import BaseModel


class Drop(BaseModel):
	"""
		item: str
		quantity: int
		chance: float
		questLink: str
	"""
	item: str
	quantity: int
	chance: float
	questLink: str
