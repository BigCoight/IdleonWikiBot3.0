from typing import List

from definitions.common.DropTypes import Drop
from definitions.master.IdleonModel import IdleonModel
from helpers.Constants import Constants


class EnemyTable(IdleonModel):
	drops: List[Drop]

	def wikiWriterKey(self) -> str:
		return Constants.newLine.join([drop.writeWiki() + "}}" for drop in self.drops])
