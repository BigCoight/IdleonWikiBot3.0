from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric


class WeeklyTask(IdleonModel):
	desc: str
	reqFor50: Numeric
	requirement: str
	icon: str

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		return "{{WeeklyBoss/Req|"f"{self.icon}""}}"
