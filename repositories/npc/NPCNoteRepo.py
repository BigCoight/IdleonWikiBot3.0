import re
from typing import Dict, List

from pywikibot import Site, Page

from definitions.common.Note import Note
from definitions.questdef.NpcNote import NpcNote
from helpers.HelperFunctions import formatStr, replaceUnderscores
from repositories.master.FileRepository import FileRepository


class NpcNoteRepo(FileRepository[NpcNote]):

	@classmethod
	def parse(cls, value: Dict[str, any]) -> NpcNote:
		return NpcNote.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Quests"]

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		reNpcs = r'..\.addDialogueFor\("([a-zA-Z0-9_]*)", [^\s"]*\)'
		questText = formatStr(cls.getSection(), ["\n"])
		questData = re.split(reNpcs, questText)
		for i in range(1, len(questData), 2):
			npcName = replaceUnderscores(questData[i])
			cls.add(npcName, NpcNote(notes = []))
			sources = cls.searchSource(website, npcName)
			if not sources:
				continue
			for note in sources:
				cls.get(npcName).notes.append(Note(
					note = re.escape(note).replace('"', "'").replace("}}", ""),
				))

	@classmethod
	def searchSource(cls, website: Site, siteName: str) -> List[str]:
		if siteName not in ["", " "]:
			toSplit = "{{Quest/head}}"
			page = Page(website, siteName)
			splitText = page.text.split(toSplit)
			if len(splitText) > 1:
				searchText = page.text.split(toSplit)[1]
				notes = re.findall(r"\|notes=(.*)", searchText)
				return notes if notes else []
			return []
		return []
