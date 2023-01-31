import re
from typing import Dict, List

from mwparserfromhell import parse as mwparse
from pywikibot import Site, Page

from definitions.common.Note import Note
from definitions.questdef.NpcNote import NpcNote
from helpers.Constants import Constants
from helpers.HelperFunctions import formatStr, replaceUnderscores
from repositories.master.FileRepository import FileRepository


class NpcNoteRepo(FileRepository[NpcNote]):
	@classmethod
	def getCategory(cls) -> str:
		return "Npc"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> NpcNote:
		return NpcNote.parse_obj(value)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Quests", "Quests2"]

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		reNpcs = r'..\.addDialogueFor\("([a-zA-Z0-9_]*)", [^\s"]*\)'
		for n in range(len(cls.getSections())):
			questText = formatStr(cls.getSection(n), ["\n"])
			questData = re.split(reNpcs, questText)
			for i in range(1, len(questData), 2):
				npcName = replaceUnderscores(questData[i])
				npcName = Constants.nameConflicts.get(npcName, npcName)
				sources = cls.searchNotes(website, npcName)
				if not sources:
					continue
				cls.add(npcName, NpcNote(notes = sources.copy()))

	@classmethod
	def searchNotes(cls, website: Site, dispName: str) -> Dict[str, Note]:
		if dispName in ["", " "]: return {}
		res = {}
		text = Page(website, dispName).text
		replacedText = text.replace("\n", Constants.newLineRep)
		wikiCode = mwparse(replacedText)
		templates = wikiCode.filter_templates(recursive = False)
		for template in templates:
			if "name" not in template:
				continue
			if "notes" not in template:
				continue
			note = cls.getParsed(template, "notes")
			name = cls.getParsed(template, "name")
			res[name] = Note(note = note)
		return res

	@classmethod
	def getNote(cls, npc: str, qName: str) -> Note:
		if not cls.contains(npc):
			return Note(note = " ")
		npcNotes = cls.get(npc).notes
		if qName not in npcNotes:
			return Note(note = " ")
		return npcNotes[qName]
