from typing import List

from definitions.common.Source import Source
from definitions.master.IdleonModel import IdleonModel


class Sources(IdleonModel):
	sources: List[Source] = []
	recipeFrom: List[Source] = []
	questAss: List[Source] = []

	def writeWiki(self, newLine = True, ignoreZero = True) -> str:
		def wikiSource(source: Source) -> str:
			return source.wikiName
		res = ""
		if self.questAss:
			res += "|quest=" + ", ".join(map(wikiSource, self.questAss))
			res += "\n"
		if self.sources:
			res += "|source=" + ", ".join(map(wikiSource, self.sources))
			res += "\n"
		return res
