from typing import List

from definitions.common.DropTypes import Drop
from definitions.master.CollectionModel import CollectionModel
from helpers.Constants import Constants


class EnemyTable(CollectionModel):
	drops: List[Drop]

	def wikiWriterKey(self) -> str:
		return Constants.newLine.join([drop.wikiWriterKey() + "}}" for drop in self.drops])
