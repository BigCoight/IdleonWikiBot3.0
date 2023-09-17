from typing import List

from definitions.master.IdleonModel import IdleonModel
from definitions.misc.weeklybosses.WeeklyTask import WeeklyTask
from helpers.CustomTypes import Integer, Numeric


class WeeklyBoss(IdleonModel):
	name: str
	possibleTasks: List[WeeklyTask]
	health: Integer
	healthMult: Numeric
	x: Integer
	y: Integer
	xOff: Integer
