from typing import List

from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class CourtCheckType(IdleonEnum):
	No = "no"
	CoinCheck = "coincheck"
	ChestCheck = "chestcheck"
	PopCheck = "popcheck"


class CaseOutcomeType(IdleonEnum):
	CourtCoins = "c"
	Popularity = "h"
	MentalHealth = "m"
	Chest = "r"
	Dismissals = "d"


class CaseOutcome(IdleonModel):
	category: CaseOutcomeType
	qty: Numeric


class CourtCase(IdleonModel):
	person: str
	desc: str
	approveOutcome: List[CaseOutcome]
	rejectOutcome: List[CaseOutcome]
	currencyScalePer5: List[CaseOutcomeType]
	coincheck: CourtCheckType
