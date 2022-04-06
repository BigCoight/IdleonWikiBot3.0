from math import ceil
from typing import List

from definitions.master.IdleonModel import IdleonModel
from helpers.CustomTypes import Integer
from helpers.HelperFunctions import formatFloat
from repositories.item.ItemDetailRepo import ItemDetailRepo


class TrapBoxTime(IdleonModel):
	time: Integer
	qtyX: Integer
	expX: Integer
	shinyX: Integer

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		return "{{Traps/row|" + self.writeWikiSinge()

	def writeWikiSinge(self) -> str:
		dayform = self.time / 60 > 3600

		roundedTime = ceil((self.time/60)/60)*60
		res = f"|minutes={formatFloat(roundedTime)}|qty={self.qtyX}"
		if self.expX:
			res += f"|xp={self.expX}"
		else:
			res += f"|shiny={self.shinyX}"
		if dayform:
			res += "|dayform=yes"

		res += "}}\n"
		return res

	def shouldCompare(self) -> bool:
		return False

	def __str__(self) -> str:
		res = f"Time({self.time}) Qty({self.qtyX})"
		if self.expX:
			res += f" Exp({self.expX})"
		else:
			res += f" Shiny({self.shinyX})"
		return res


class TrapBox(IdleonModel):
	times: List[TrapBoxTime]

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = "{| class=\"wikitable mw-collapsible sortable\" id=\"Trap Efficiency\"\n|+Trap Data\n!Time\n!Qty "
		res += "Multi\n!XP Multi\n!Shiny Multi\n!Efficiency\n|-\n"
		res += "".join(map(lambda x: x.writeWiki(newLine, ignoreZero), self.times))
		res += "\n|}\n"

		return res

	def writeWikiSingle(self) -> str:
		res = self.times[0].writeWikiSinge()
		res += "".join(map(lambda x: x.writeWiki(), self.times[1:]))
		return res
