from pydantic import BaseModel, validator

from helpers.CustomTypes import Integer


class Critter(BaseModel):
	location: str
	baseExp: Integer
	baseShinyRate: float
	shiny: str
	effForBonus: Integer

	@validator("baseShinyRate", pre = True)
	def _floatPercentage(cls, v: str) -> float:
		return float(v)/100
