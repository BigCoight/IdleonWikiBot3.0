from typing import Dict

from pywikibot import Site
from rich.progress import track

from definitions.common.Note import Note
from repositories.enemies.EnemyDetailsRepo import EnemyDetailsRepo
from repositories.master.FileRepository import FileRepository


class EnemyNoteRepo(FileRepository[Note]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		EnemyDetailsRepo.initialise(cls.codeReader, log)

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
		for item, data in track(items, "Getting enemy Notes..."):
			if EnemyDetailsRepo._ignore(item, data): continue
			dispName = data.Name
			note = cls.getNote(website, dispName)
			if note:
				cls.add(item, Note(note = note))
