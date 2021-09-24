from pydantic import BaseModel, validator


class Critter(BaseModel):
	location: str
	baseExp: int
	baseShinyRate: float
	shiny: str
	effForBonus: int

	@validator("baseShinyRate", pre = True)
	def _floatPercentage(cls, v: str) -> float:
		return float(v)/100
