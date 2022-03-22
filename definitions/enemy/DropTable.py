from typing import List

from definitions.common.DropTypes import Drop
from definitions.master.CollectionModel import CollectionModel
from definitions.master.IdleonModel import IdleonModel
from helpers.Constants import Constants


class DropTable(IdleonModel):
	drops: List[Drop]
	subTable: str

	def writeHeader(self) -> str:
		res = "__NOCACHE__\n"
		res += "{{#cargo_query:tables=DropTables\n"
		res += " |fields=CONCAT(\"[[\", DropSourceEntity, \"]]\")=DropSourceEntity\n"
		res += " |where=TableName HOLDS \"{{PAGENAME}}\" AND DropSourceEntity NOT LIKE \"{{PAGENAME}}\"\n"
		res += " |group by=DropTables.DropSourceEntity\n"
		res += " |order by=`DropSourceEntity` ASC\n"
		res += " |default=\n"
		res += f" |intro=This is a {self.rareMegaTable()} Droptable for:\n"
		res += " |outro=To see monster specific droprates, visit the specified source page.\n"
		res += " |limit=100\n"
		res += " |offset=0\n"
		res += " |format=ul\n"
		res += " |columns=1\n"
		res += "}}\n"
		return res

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		res = self.writeHeader() + "{{DropTable/head}}\n"
		for drop in self.drops:
			if drop.item == "COIN":
				continue
			res += self.writeDrop(drop) + "\n"
		return res

	def writeDrop(self, drop: Drop) -> str:
		res = drop.writeWiki()
		if drop.hasDropTableExtra():
			res += f"|tablename={self.subTable}|tabletype={self.rareMega()}"
		return res + "}}"

	def rareMega(self) -> str:
		if self.subTable[0] == "S":
			return "Mega"
		return "Rare"

	def rareMegaTable(self) -> str:
		if self.subTable[0] == "S":
			return "Mega Rare"
		return "Rare"
