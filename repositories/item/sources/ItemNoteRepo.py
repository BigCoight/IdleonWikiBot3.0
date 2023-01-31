from typing import Dict

from pywikibot import Site
from rich.console import Console
from rich.progress import track

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
			note = cls.getNote(website, dispName)
			if note:
				cls.add(item, Note(note = note))
