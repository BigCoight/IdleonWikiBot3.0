from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class WeeklyTask(IdleonModel):
	desc: str
	reqFor50: Numeric
	requirement: str
	icon: str
