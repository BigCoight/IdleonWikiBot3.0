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
			sources = cls.searchNotes(website, npcName)
			if not sources:
				continue
			cls.add(npcName, NpcNote(notes = sources.copy()))

	@classmethod
	def searchNotes(cls, website: Site, siteName: str) -> Dict[str, Note]:
		if siteName in ["", " "]:
			return {}
		toSplit = "{{Quest/head}}"
		res = {}
		page = Page(website, siteName)
		splitText = page.text.split(toSplit)
		if not len(splitText) > 1:
			return {}
		searchText = page.text.split(toSplit)[1]
		justQuests = searchText.split("{{dialogue/head}}")[0]
		quests = justQuests.split("\n}}")
		for quest in quests:
			matches = re.findall(r"\|name=(.*)|notes=(.*)", quest)
			if not len(matches) == 2:
				continue
			res[matches[0][0]] = Note(note = matches[1][1])
		return res

	@classmethod
	def getNote(cls, npc: str, qName: str) -> Note:
		if not cls.contains(npc):
			return Note(note = " ")
		npcNotes = cls.get(npc).notes
		if qName not in npcNotes:
			return Note(note = " ")
		return npcNotes[qName]
