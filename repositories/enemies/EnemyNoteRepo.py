import re
from concurrent.futures import ThreadPoolExecutor
from typing import Dict

from pywikibot import Site, Page
from rich.console import Console
from rich.progress import track, Progress

from definitions.common.Note import Note
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.FileRepository import FileRepository


class EnemyNoteRepo(FileRepository[Note]):

	@classmethod
	def getCategory(cls) -> str:
		return "Enemy"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> Note:
		return Note.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		items = EnemyDetailsRepo.items()

		for item, data in items:
			if EnemyDetailsRepo._ignore(item, data): continue
			dispName = data.Name
			sources = cls.searchSource(website, dispName)
			if not sources:
				continue
			cls.add(item, Note(
				note = re.escape(sources).replace('"', "'"),
			))


	@classmethod
	def searchSource(cls, website: Site, siteName: str) -> str:
		if siteName not in ["", " "]:
			toSplit = "|notes="
			page = Page(website, siteName)
			splitText = page.text.split(toSplit)
			if len(splitText) > 1:
				searchText = splitText[1]
				sources = searchText.split("}}\n")
				if len(sources) > 1:
					return sources[0]
				return searchText
		return ""
