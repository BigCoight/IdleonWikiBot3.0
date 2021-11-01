import re
from typing import Dict

from pywikibot import Site, Page

from definitions.common.Note import Note
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.FileRepository import FileRepository


class ItemNoteRepo(FileRepository[Note]):

	@classmethod
	def parse(cls, value: Dict[str, any]) -> Note:
		return Note.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		for item, data in ItemDetailRepo.items():
			dispName = data.displayName
			sources = cls.searchSource(website, dispName)
			if not sources:
				continue
			cls.add(item, Note(
				note = re.escape(sources).replace('"', "'").replace("}}", ""),
			))

	@classmethod
	def searchSource(cls, website: Site, siteName: str) -> str:
		if siteName not in ["", " "]:
			toSplit = "|notes="
			page = Page(website, siteName)
			splitText = page.text.split(toSplit)
			if len(splitText) > 1:
				searchText = page.text.split(toSplit)[1]
				sources = searchText.split("\n")
				if len(sources) > 1:
					return sources[0]
				return searchText
		return ""
