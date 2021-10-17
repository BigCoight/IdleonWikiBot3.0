from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Numeric, Integer


class StatueData(IdleonModel):
	name: str
	effect: str
	dk: Integer
	bonus: Numeric

	def writeWiki(self, newLine = True) -> str:
		res = "{{Statuedata|"
		res += f"{self.bonus}|{self.effect}"
		res += "}}\n"
		return res
