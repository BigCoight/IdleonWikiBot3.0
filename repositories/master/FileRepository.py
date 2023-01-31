import json
import os.path
import re
from abc import ABC
from typing import TypeVar, Dict

from mwparserfromhell import parse as mwparse
from pydantic import BaseModel
from pywikibot import Page

from helpers.CodeReader import CodeReader
from helpers.Constants import Constants
from helpers.JsonEncoder import CompactJSONEncoder
from repositories.master.Repository import Repository

T = TypeVar("T", bound = BaseModel)


class FileRepository(Repository[T], ABC):

	@classmethod
	def initialise(cls, codeReader: CodeReader, update: bool = False) -> None:
		cls.codeReader = codeReader
		cls.initDependencies(False)
		cls.update = update
		cls.repository = {}
		cls.listRepository = []
		cls.codeReader = codeReader
		cls.sections = cls.getSections()
		if cls.shouldGetFromFile():
			cls.getFromFile()
			return
		cls.generateRepo()
		cls._export()

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError

	@classmethod
	def _export(cls) -> None:
		toEncode = {key: val.dict() for key, val in cls.repository.items()}
		toEncode["version"] = cls.codeReader.version
		with open(cls._getPath("repo", "json"), mode = "w") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(toEncode))

	@classmethod
	def shouldGetFromFile(cls) -> bool:
		if not os.path.isfile(cls._getPath("repo", "json")):
			return False
		return not cls.update

	@classmethod
	def getFromFile(cls) -> None:
		with open(cls._getPath("repo", "json"), mode = "r") as infile:
			data = json.load(infile)
		for key, value in data.items():
			if key == "version":
				continue
			cls.add(key, cls.parse(value))

	@classmethod
	def parse(cls, value: Dict[str, any]) -> T:
		raise NotImplementedError

	@classmethod
	def getNote(cls, website, dispName) -> str:
		text = Page(website, dispName).text
		replacedText = text.replace("\n", Constants.newLineRep)
		wikiCode = mwparse(replacedText)
		templates = wikiCode.filter_templates(recursive = False)
		selectedTemplate = None
		for template in templates:
			if "notes" not in template:
				continue
			selectedTemplate = template
			break
		if selectedTemplate is None:
			return ""
		note = cls.getParsed(selectedTemplate, "notes")
		if not note:
			return " "
		return re.escape(note)

	@classmethod
	def getParsed(cls, tempalte, key) -> str:
		return str(tempalte.get(key).value).strip(Constants.newLineRep).strip()
