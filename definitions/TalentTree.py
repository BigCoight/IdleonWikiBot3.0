from typing import List

from pydantic import BaseModel, validator

from helpers.CustomTypes import Numeric


class Talent(BaseModel):
	name: str
	description: str
	x1: Numeric
	x2: Numeric
	funcX: str
	y1: Numeric
	y2: Numeric
	funcY: str
	lvlUpText: str

	@validator("x1", "x2", "y1", "y2", pre = True)
	def funcValidator(cls, v: str):
		if v == "_":
			return -1
		return v


class TalentTree(BaseModel):
	talents: List[Talent]
