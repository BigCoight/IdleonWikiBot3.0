import re
from typing import Dict

from mwparserfromhell import parse as mwparse
from pywikibot import Site, Page
from rich.progress import track

from definitions.itemdef.ItemSet import ItemSet
from helpers.Constants import Constants
from repositories.item.ItemDetailRepo import ItemDetailRepo
from repositories.master.FileRepository import FileRepository


class WikiSetRepo(FileRepository[ItemSet]):

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ItemDetailRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Item/Sources"

	@classmethod
	def parse(cls, value: Dict[str, any]) -> ItemSet:
		return ItemSet.parse_obj(value)

	@classmethod
	def generateRepo(cls) -> None:
		website = Site()
		items = ItemDetailRepo.items()
		for item, data in track(items, description = "Pulling set names..."):
			dispName = data.displayName
			note = cls.getNote(website, dispName)
			if note:
				cls.add(item, ItemSet(set = note))

	@classmethod
	def getNote(cls, website, dispName) -> str:
		text = Page(website, dispName).text
		replacedText = text.replace("\n", Constants.newLineRep)
		wikiCode = mwparse(replacedText)
		templates = wikiCode.filter_templates(recursive = False)
		selectedTemplate = None
		for template in templates:
			if "setname" not in template:
				continue
			selectedTemplate = template
			break
		if selectedTemplate is None:
			return ""
		note = cls.getParsed(selectedTemplate, "setname")
		if not note:
			return " "
		return re.escape(note)
