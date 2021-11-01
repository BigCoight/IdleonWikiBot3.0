import re
from typing import Dict

from pywikibot import Site, Page

from definitions.common.Source import Source
from definitions.itemdef.Sources import Sources
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.item.sources.CustomSourceRepo import CustomSourceRepo
from repositories.item.sources.SourceRepo import SourceRepo
from repositories.master.FileRepository import FileRepository


class WikiSourceRepo(FileRepository[Sources]):

	@classmethod
	def parse(cls, value: Dict[str, any]) -> Sources:
		return Sources.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		for item, data in ItemDetailRepo.items():
			sPre = SourceRepo.contains(item) and not SourceRepo.get(item).questAss
			cPre = CustomSourceRepo.contains(item) and not CustomSourceRepo.get(item).questAss
			if (not SourceRepo.contains(item) and not CustomSourceRepo.contains(item)) or (sPre or cPre):
				dispName = data.displayName
				sources = cls.searchSource(website, dispName)
				for source in sources.split(','):
					if not source or "Start" in source:
						continue
					cls.addToSource(item, Source(
						wikiName = re.escape(source).replace('"', "'").replace("}}", ""),
						txtName = ""
					))
		temp = {}
		for item, sources in cls.items():
			for source in sources.sources:
				if source.wikiName not in temp:
					temp[source.wikiName] = []
				temp[source.wikiName].append(item)
		for source, items in temp.items():
			print(f"{source}\n{items}")

	@classmethod
	def searchSource(cls, website: Site, siteName: str) -> str:
		if siteName not in ["", " "]:
			toSplit = "|quest="
			page = Page(website, siteName)
			splitText = page.text.split(toSplit)
			if len(splitText) > 1:
				searchText = page.text.split(toSplit)[1]
				sources = searchText.split("\n")
				if len(sources) > 1:
					return sources[0]
				return searchText
		return ""

	@classmethod
	def addToSource(cls, item: str, source: Source):
		if not cls.contains(item):
			cls.add(item, Sources())
		cls.get(item).sources.append(source)
