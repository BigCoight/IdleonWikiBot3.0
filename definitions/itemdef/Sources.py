from typing import List

from definitions.common.Source import Source
from definitions.master.IdleonModel import IdleonModel
from helpers.HelperFunctions import wikiSource


class Sources(IdleonModel):
	sources: List[Source] = []
	recipeFrom: List[Source] = []
	questAss: List[Source] = []

	def writeWiki(self, newLine = True) -> str:
		res = ""
		if self.questAss:
			res += "|quest=" + ", ".join(map(wikiSource, self.questAss))
			res += "\n"
		if self.sources:
			res += "|source=" + ", ".join(map(wikiSource, self.sources))
			res += "\n"
		return res
