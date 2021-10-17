from typing import List

from definitions.common.DropTypes import Drop
from definitions.master.CollectionModel import CollectionModel
from helpers.Constants import Constants


class DropTable(CollectionModel):
	drops: List[Drop]
	subTable: str

	def wikiWriterKey(self) -> str:
		res = ""
		for drop in self.drops:
			if drop.item == "COIN":
				continue
			res += self.writeDrop(drop) + Constants.newLine
		return res

	def writeDrop(self, drop: Drop) -> str:
		res = drop.wikiWriterKey()
		res += f"|tablename={self.subTable}|tabletype={self.rareMega()}"
		return res + "}}"

	def rareMega(self) -> str:
		if self.subTable[0] == "S":
			return "Mega"
		return "Rare"
