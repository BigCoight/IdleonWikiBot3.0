from typing import List, Dict, Union, Callable

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

	def getRequirements(self) -> str:
		return "".join(map(lambda task: task.writeWiki(False, False), self.possibleTasks))

	def intToWiki(self) -> Dict[str, Union[Callable, str]]:
		return {"name": "name",
		        "requirements": self.getRequirements,
		        "health": "health",
		        "healthmulti": "healthMult"
		        }

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{{WeeklyBoss"
		res += super().writeWiki()
		res += "}}"
		return res
