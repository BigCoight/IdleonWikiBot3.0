from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class ActionType(IdleonEnum):
	Attack = "ATTACK"
	Buff = "BUFF"
	Misc = "MISC"


class WeeklyAction(IdleonModel):
	actionType: ActionType
	desc: str
	scaling: Numeric
	max: Numeric
	key: str
