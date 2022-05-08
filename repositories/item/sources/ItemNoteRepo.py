import re
from concurrent.futures import ThreadPoolExecutor
from typing import Dict

from pywikibot import Site, Page
from rich.console import Console
from rich.progress import track, Progress

from definitions.common.Note import Note
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.FileRepository import FileRepository


class ItemNoteRepo(FileRepository[Note]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ItemDetailRepo.initialise(cls.codeReader, log)


	@classmethod
	def getCategory(cls) -> str:
		return "Item/Sources"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> Note:
		return Note.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		items = ItemDetailRepo.items()
		for item, data in track(items, description = "Pulling notes...", console = Console(color_system = None)):
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
