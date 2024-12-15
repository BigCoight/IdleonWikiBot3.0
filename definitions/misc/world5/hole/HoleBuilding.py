from pydantic import validator

from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer


class SedimentType(IdleonEnum):
	Gravel = 0
	Goldust = 1
	Redstone = 2
	Mythril = 3
	Cobaltine = 4
	Bruntine = 5
	Freezium = 6
	Sweetium = 7
	RadCoral = 8
	HyperCoral = 9
	filler1 = 10
	filler2 = 11
	filler3 = 12


class HoleBuilding(IdleonModel):
	name: str
	squareImageType: Integer
	costType: SedimentType
	baseCost: Integer
	costCalcType: bool
	desc: str
	order: Integer

	@validator("costType", pre = True)
	def validate(cls, v):
		if isinstance(v, bool):
			return v
		if v == "1":
			return True
		return False
