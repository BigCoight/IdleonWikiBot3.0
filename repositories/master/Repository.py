import os.path
from abc import ABC
from copy import deepcopy
from typing import Dict, Generic, Optional, TypeVar, List, Set

from pywikibot import Site, Page

from definitions.master.IdleonModel import IdleonModel
from helpers.CodeReader import CodeReader, IdelonReader
from helpers.JsonEncoder import CompactJSONEncoder

T = TypeVar("T", bound = IdleonModel)


class Repository(Generic[T], ABC):
	sections: List[str]
	codeReader: CodeReader
	repository: Dict[str, T]

	@classmethod
	def initialise(cls, codeReader: CodeReader) -> None:
		cls.repository = {}
		cls.codeReader = codeReader
		cls.sections = cls.getSections()
		if cls.sections and not cls.getSection():
			return None
		cls.generateRepo()
		cls._export()

	@classmethod
	def getSections(cls) -> List[str]:
		return []

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError

	@classmethod
	def getSection(cls, index: int = 0) -> str:
		currentSection = cls.codeReader.getSection(cls.sections[index])
		assert currentSection is not None
		return currentSection

	@classmethod
	def get(cls, key: str) -> Optional[T]:
		return cls.repository.get(key)

	@classmethod
	def add(cls, key: str, value: T) -> None:
		cls.repository[key] = value

	@classmethod
	def contains(cls, key: str) -> bool:
		return key in cls.repository

	@classmethod
	def items(cls):
		return cls.repository.items()

	@classmethod
	def _getFileName(cls) -> str:
		return fr"./exported/repo/{cls.__name__}.json"

	@classmethod
	def _export(cls) -> None:
		with open(cls._getFileName(), mode = "w") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(cls.repository))

	@classmethod
	def excludeDefaults(cls) -> bool:
		return True

	@classmethod
	def compareVersions(cls, v1: str, v2: str, ignored: Set[str] = set()):

		changes = {}
		new = {}
		cr1 = IdelonReader(v1).codeReader
		cr2 = IdelonReader(v2).codeReader

		cls.initialise(cr1)
		repo1 = deepcopy(cls.repository)
		cls.initialise(cr2)
		repo2 = deepcopy(cls.repository)
		key1 = set(repo1.keys())
		key2 = set(repo2.keys())

		sameItems = key1.intersection(key2)
		newItems = key2 - key1
		for sameItem in sameItems:
			modelChanges = repo1[sameItem].compare(repo2[sameItem], ignored)
			if modelChanges:
				changes[sameItem] = modelChanges

		for newItem in newItems:
			new[newItem] = repo2[newItem].dict(exclude = set(ignored))

		out = {
			"new": new,
			"changes": changes
		}

		changeName = fr"./exported/changes/{cls.__name__}.json"

		with open(changeName, mode = "w") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(out))

		cls.writeChangesWiki(out)

	@classmethod
	def writeChangesWiki(cls, differences):
		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + v + "}}\n"

		def patchnote(v: str, o, n) -> str:
			return "{{patchnote|" + f"{v}|{str(o)}|{str(n)}" + "}}\n"

		res = ""
		new = differences["new"]
		changes = differences["changes"]
		res += "__NOTOC__<div class=\"GenericFlex\"><div class=\"GenericChild\">\n"
		res += "==Changes==\n"
		for item, change in changes.items():
			res += head(cls.getWikiName(item))
			for v, d in change.items():
				if isinstance(d, tuple):
					o, n = d
					res += patchnote(v, o, n)
				elif isinstance(d, list):
					res += bold(v)
					for i, subC in enumerate(d):
						o, n = subC
						res += patchnote(str(i), o, n)
					res += "|-\n|\n"
			res += '|}\n'

		with open(fr"./exported/wikitext/_changes/{cls.__name__}.txt", mode = 'w') as infile:
			infile.write(res)

	@classmethod
	def _wikitextLocation(cls):
		return fr"./exported/wikitext/{cls.__name__}"

	@classmethod
	def _createWikiTextDir(cls):
		if not os.path.exists(cls._wikitextLocation()):
			os.mkdir(cls._wikitextLocation())

	@classmethod
	def exportWikiSingle(cls) -> None:
		cls._createWikiTextDir()
		res = cls._extractWikiSingle()

		with open(f"{cls._wikitextLocation()}/{cls.__name__}.txt", mode = 'w') as outfile:
			outfile.write(res)

	@classmethod
	def _extractWikiSingle(cls) -> str:
		res = ""
		for _, data in cls.items():
			res += data.writeWiki() + '\n'
		return res

	@classmethod
	def exportWikiMult(cls) -> None:
		cls._createWikiTextDir()
		for name, data in cls.items():
			with open(f"{cls._wikitextLocation()}/{cls.getWikiName(name)}.txt", mode = 'w') as outfile:
				outfile.write(cls._extractWikiMult(data))

	@classmethod
	def _extractWikiMult(cls, data: T) -> str:
		return data.writeWiki()

	@classmethod
	def getWikiName(cls, name: str) -> str:
		return name

	@classmethod
	def _oldLocation(cls):
		return fr"./exported/old/{cls.__name__}"

	@classmethod
	def _createOldDir(cls):
		if not os.path.exists(cls._oldLocation()):
			os.mkdir(cls._oldLocation())

	@classmethod
	def _isOld(cls, name: str, data: T) -> bool:
		if not os.path.isfile(f"{cls._oldLocation()}/{name}.txt"):
			return False
		with open(f"{cls._oldLocation()}/{name}.txt", mode = 'r') as infile:
			wiki = data.writeWiki()
			old = infile.read()
			if wiki == old:
				return True
			# print("".join(difflib.ndiff(wiki.splitlines(), old.splitlines())))
			return False

	@classmethod
	def _writeOld(cls, name: str, data: T) -> None:
		with open(f"{cls._oldLocation()}/{name}.txt", mode = 'w') as outfile:
			outfile.write(data.writeWiki())

	@classmethod
	def _ignore(cls, name: str, data: T) -> bool:
		"""
		override this to add predicates if certain data should be left of the wiki. Return true for
		things that need to be ignored

		Args:
			name: key
			data: data

		Returns:
			If the data should be uploaded

		"""
		return False

	@classmethod
	def _upload(cls, website: Site, name: str, data: str) -> None:

		wikiPage = Page(website, name)
		wikiPage.text = data
		wikiPage.save("Coights API 3.0")

	@classmethod
	def upload(cls) -> None:
		cls._createOldDir()
		website = Site()
		for name, data in cls.items():
			if cls._ignore(name, data):
				continue
			if cls._isOld(name, data):
				continue
			print(f'New  {cls.getWikiName(name)}')
			cls._upload(website, cls.getWikiName(name), data.writeWiki())
			cls._writeOld(name, data)

	@classmethod
	def _manualOld(cls):
		cls._createOldDir()
		for name, data in cls.items():
			cls._writeOld(name, data)
