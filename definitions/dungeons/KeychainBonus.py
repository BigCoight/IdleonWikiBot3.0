from typing import List

from definitions.master.IdleonModel import IdleonModel


class KeychainBonus(IdleonModel):
	bonus: str
	lvl1: float
	lvl2: float
	lvl3: float

	def writeMisc(self) -> str:
		return f"+ [{self.lvl1:g},{self.lvl2:g},{self.lvl3:g}] {self.bonus}"

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		return f"|{self.bonus}||{self.lvl1:g}||{self.lvl2:g}||{self.lvl3:g}\n|-"


class KeychainBonuses(IdleonModel):
	bonuses: List[KeychainBonus]

	def writeMisc(self) -> str:
		return " OR ".join(map(lambda x: x.writeMisc(), self.bonuses))

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		return "\n".join(map(lambda x: x.writeWiki(), self.bonuses))
