import difflib
import os.path
import re
from abc import ABC, abstractmethod
from copy import deepcopy
from enum import Enum
from typing import Dict, Generic, Optional, TypeVar, List, Set, Any

from pywikibot import Site, Page
from rich.progress import track

from definitions.master.IdleonEnum import IdleonEnum
from definitions.master.IdleonModel import IdleonModel
from helpers.CodeReader import CodeReader, IdleonReader
from helpers.ColourPrinter import printGreen, printRed, printYellow, printBlue, printPurple, console
from helpers.HelperFunctions import camelCaseToTitle, extractImportsClass
from helpers.JsonEncoder import CompactJSONEncoder

T = TypeVar("T", bound = IdleonModel)


class OldType(Enum):
	New = 0
	Changed = 1
	Old = 2


class Repository(Generic[T], ABC):
	sections: List[str]
	codeReader: CodeReader
	repository: Dict[str, T]
	listRepository: List[T]

	@classmethod
	def initialise(cls, codeReader: CodeReader, log: bool = True, export: bool = True) -> None:
		if cls.__dict__.get("codeReader"):
			if cls.codeReader.version == codeReader.version:
				return
		cls.log = log
		cls.repository = {}
		cls.listRepository = []
		cls.codeReader = codeReader
		cls.sections = cls.getSections()
		if cls.sections and not cls.getSection():
			printRed(f"Could not find {cls.__name__}'s Section")
			return None
		cls.initDependencies(log)
		cls.generateRepo()
		cls.generateTSRepo()
		if log:
			printGreen(f"Generated {cls.__name__}'s repo with {len(cls.repository)} Items")

		if export:
			cls._export()

	@classmethod
	def getSections(cls) -> List[str]:
		return []

	@classmethod
	def initDependencies(cls, log = True) -> None:
		pass

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
	def getList(cls, index: int) -> Optional[T]:
		return cls.listRepository[index]

	@classmethod
	def add(cls, key: str, value: T) -> None:
		cls.repository[key] = value

	@classmethod
	def addList(cls, value: T) -> None:
		cls.listRepository.append(value)

	@classmethod
	def lengthList(cls) -> int:
		return len(cls.listRepository)

	@classmethod
	def contains(cls, key: str) -> bool:
		return key in cls.repository

	@classmethod
	def items(cls):
		return cls.repository.items()

	@classmethod
	def itemsList(cls):
		return cls.listRepository

	@classmethod
	@abstractmethod
	def getCategory(cls) -> str:
		raise NotImplementedError

	@classmethod
	def getFilePath(cls) -> str:
		return f"{cls.getCategory()}/{cls.__name__}"

	@classmethod
	def _getPath(cls, location: str, fileExtension: str, nameOveride = "", noCat = False) -> str:
		"""

		Args:
			location: the base file location
			fileExtension: the extension of the file
			nameOveride: what to call the file, defaults to class name
			noCat: whether to include a category or not

		Returns:
			the created file path
		"""
		if noCat:
			path = fr"./exported/{location}/"
		else:
			path = fr"./exported/{location}/{cls.getCategory()}/"
		if not os.path.isdir(path):
			os.makedirs(path, exist_ok = True)
		if not nameOveride:
			return f"{path}{cls.__name__}.{fileExtension}"
		return f"{path}{nameOveride}.{fileExtension}"

	@classmethod
	def _export(cls) -> None:
		with open(cls._getPath("repo", "json"), mode = "w", encoding = "utf-8") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(cls.repository))
		if not cls.listRepository:
			return
		with open(cls._getPath("list", "json"), mode = "w", encoding = "utf-8") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(cls.listRepository))

	@classmethod
	def excludeDefaults(cls) -> bool:
		return True

	@classmethod
	def compareVersions(cls, v1: IdleonReader, v2: IdleonReader, ignored: Set[str] = set(), useIgnore = True,
	                    upload = False):
		"""

		Args:
		    upload:
		    upload:
		    useIgnore:
		    useIgnore: to use the classes ignore method when comparing
			v1: The version that is "Old"
			v2: The version that is "New"
			ignored: A set of attributes to ignore in the comparison

		Returns:
		"""

		changes = {}
		new = {}
		cr1 = v1.codeReader
		cr2 = v2.codeReader

		cls.initialise(cr1, False, False)
		repo1 = deepcopy(cls.repository)
		cls.initialise(cr2, False, False)
		repo2 = deepcopy(cls.repository)
		key1 = set(repo1.keys())
		key2 = set(repo2.keys())

		sameItems = key1.intersection(key2)
		newItems = key2 - key1
		for sameItem in sameItems:
			if cls._ignore(sameItem, repo2[sameItem]) and useIgnore:
				continue
			if repo1[sameItem].isFiller() and not repo2[sameItem].isFiller():
				newItems.add(sameItem)
				continue
			if modelChanges := repo1[sameItem].compare(repo2[sameItem], ignored):
				changes[sameItem] = modelChanges

		for newItem in newItems:
			if cls._ignore(newItem, repo2[newItem]) and useIgnore:
				continue
			if repo2[newItem].isFiller():
				continue
			current = repo2[newItem].toDict(ignored)
			if not any(current):
				continue
			new[newItem] = current

		out = {
			"new": new,
			"changes": changes
		}
		changeName = cls._getPath("changes", "json")
		with open(changeName, mode = "w", encoding = 'utf-8') as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(out))
		output = cls._writeChangesWiki(out)

		if len(new) == 0 and len(changes) == 0:
			return

		if upload:
			website = Site()
			cls._upload(website, cls._getChangelogPath(), output)

		printYellow(f"Compared {cls.__name__} with {len(new)} new items and {len(changes)} changes")

	@classmethod
	def _getChangelogPath(cls) -> str:
		repoName = cls.__name__.removesuffix("Repo")
		changeLogName = re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1 ', repoName)
		version = cls.codeReader.version
		return f"Changelog/{version}/{changeLogName}"

	@classmethod
	def _writeChangesWiki(cls, differences):

		def _writeChanges(diffs: Dict[str, any]) -> str:
			output = ""
			for item, change in diffs.items():
				output += head(cls.getWikiName(item))
				output += cls._writeChangelog(change).rstrip('\n')
				output += "\n|}\n\n"
			return output

		def _writeChangesSorted(diffs: Dict[str, any]) -> str:
			changesOrdered = {}
			for key in diffs.keys():
				cType = cls.get(key).sortKey()
				if cType not in changesOrdered:
					changesOrdered[cType] = []
				changesOrdered[cType].append(key)
			output = ""
			for typ, keys in changesOrdered.items():
				output += head(typ)
				for change in keys:
					output += bold(cls.getWikiName(change))
					output += cls._writeChangelog(diffs[change], 1)
				output += "|}\n\n"
			return output

		def writeChanges(diffs: Dict[str, any]) -> str:
			if not diffs:
				return ""
			firstKey = list(diffs.keys())[0]
			if cls.get(firstKey).sortKey():
				return _writeChangesSorted(diffs)
			return _writeChanges(diffs)

		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + f"{v}|0" + "}}\n"

		res = ""
		new = differences["new"]
		changes = differences["changes"]
		res += "<div class=\"GenericFlex\"><div class=\"GenericChild\">\n"
		res += "==Changes==\n"
		res += writeChanges(changes)

		res += "</div><div class=\"GenericChild\">\n"
		res += "==New==\n"

		res += writeChanges(new)

		res += "</div></div>"

		with open(cls._getPath("wikitext/_changes", "txt"), mode = 'w', encoding = 'utf-8') as infile:
			infile.write(res)

		return res

	@classmethod
	def _writeChangelog(cls, changes, indent = 0):
		def bold(v: str) -> str:
			return "{{patchnote/bold|" + f"{camelCaseToTitle(v)}|{indent}" + "}}\n"

		def patchnote(v: str, o, n) -> str:
			if not o:
				o = " "
			return "{{patchnote|" + f"{camelCaseToTitle(v)}|{str(o)}|{str(n)}|{indent}" + "}}\n"

		def aux(atr, val):

			if isinstance(val, tuple):
				return patchnote(atr, val[0], val[1])
			if isinstance(val, dict):
				res = bold(atr)
				res += cls._writeChangelog(val, indent + 1)
				return res
			if isinstance(val, list):
				res = bold(atr)
				newChanges = {f"{n}": v for n, v in enumerate(val)}
				res += cls._writeChangelog(newChanges, indent + 1)
				return res
			if not isinstance(val, IdleonModel) and val in {0, "0", "00"}:
				return ""
			return patchnote(atr, " ", val)

		return "".join([aux(atr, val) for atr, val in changes.items()])

	@classmethod
	def exportWikiSingle(cls) -> None:
		"""

		Exports the entire repo into one file

		"""
		res = cls._extractWikiSingle()

		with open(cls._getPath(f"wikitext/{cls.__name__}", "txt", noCat = True), mode = 'w') as outfile:
			outfile.write(res)

	@classmethod
	def _extractWikiSingle(cls) -> str:
		res = ""
		for _, data in cls.items():
			res += data.writeWiki() + '\n'
		return res

	@classmethod
	def exportWikiMult(cls) -> None:
		"""

		Exports the entire repo into multiple files

		"""
		for name, data in cls.items():
			path = cls._getPath(f"wikitext/{cls.__name__}", "txt", nameOveride = cls.getWikiName(name), noCat = True)
			with open(path, mode = 'w') as outfile:
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
	def _getOldData(cls, item: str, data: Any):
		return data.writeWiki()

	@classmethod
	def _createOldDir(cls):
		if not os.path.exists(cls._oldLocation()):
			os.mkdir(cls._oldLocation())

	@classmethod
	def _isOld(cls, name: str, data: Any) -> OldType:
		def onlyDelta(x: str) -> bool:
			return x.startswith("+") or x.startswith("-")

		if not os.path.isfile(f"{cls._oldLocation()}/{name}.txt"):
			printPurple(f'{OldType.New.name}:  {cls.getWikiName(name)}')
			return OldType.New
		with open(f"{cls._oldLocation()}/{name}.txt", mode = 'r') as infile:
			wiki = cls._getOldData(name, data)
			old = infile.read()
			if wiki == old:
				return OldType.Old
			printBlue(f'{OldType.Changed.name}:  {cls.getWikiName(name)}')
			print("\n".join(filter(onlyDelta, difflib.ndiff(old.splitlines(), wiki.splitlines()))))
			print("")
			return OldType.Changed

	@classmethod
	def _writeOld(cls, name: str, data: Any) -> None:
		with open(f"{cls._oldLocation()}/{name}.txt", mode = 'w') as outfile:
			outfile.write(cls._getOldData(name, data))

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
		wikiPage.save("Coights API 3.0", botflag = True)

	@classmethod
	def upload(cls, debug: bool) -> None:
		debugNum = 0
		cls._createOldDir()
		website = Site()
		for name, data in track(cls.items(), description = f"Uploading {cls.__name__}", console = console):
			if cls._ignore(name, data):
				continue
			if (oldStatus := cls._isOld(name, data)) == OldType.Old:
				continue
			if debug:
				debugNum += 1
				continue
			cls._upload(website, cls.getWikiName(name), data.writeWiki())
			cls._writeOld(name, data)

		if debug:
			printYellow(f"{cls.__name__} has {debugNum} changes")

	@classmethod
	def _manualOld(cls):
		cls._createOldDir()
		for name, data in cls.items():
			cls._writeOld(name, data)

	@classmethod
	def getFirstKey(cls) -> str:
		return list(cls.repository.keys())[0]

	@classmethod
	def getFirstElement(cls) -> T:
		return cls.get(cls.getFirstKey())

	@classmethod
	def generateTSRepo(cls):
		def all_subclasses(cls):
			return set(cls.__subclasses__()).union(
				[s for c in cls.__subclasses__() for s in all_subclasses(c)])

		for subclass in all_subclasses(IdleonModel):
			tsRepr = subclass.toTsInterface()
			name = subclass.__name__[0].lower() + subclass.__name__[1:] + "Model"
			path = cls._getPath("ts/model", "ts", noCat = True, nameOveride = name)
			with open(path, "w") as infile:
				infile.write(tsRepr)

		for enum in all_subclasses(IdleonEnum):
			name = enum.__name__[0].lower() + enum.__name__[1:] + "Enum"
			path = cls._getPath("ts/enum", "ts", noCat = True, nameOveride = name)
			tsEnum = f"export enum {enum.__name__}Enum ""{\n"
			out = []
			for e in enum:
				out.append(f"    {e.name} = \"{e.name}\"")
			tsEnum += ",\n".join(out)
			tsEnum += "\n}\n"
			with open(path, "w") as infile:
				infile.write(tsEnum)

		path = cls._getPath("ts/data", "ts", noCat = True)
		tsData = ""
		imports = set()

		if not cls.listRepository:
			tsData += cls.getFirstElement().toTsClass(False)
			className = cls.getFirstElement().getHighestClass().__name__
			imports.add(f"{className}Model")
			tsData += "\n\n\n\n"
			tsData += f"export const init{cls.__name__} = () => ""{\n    return [    \n"
			for n, (atr, val) in enumerate(cls.items()):
				tsObj, toImport = val.toTs()
				[imports.add(x) for x in toImport]
				tsData += f"        new {className}Base(\"{atr}\", {tsObj})"
				if n != len(cls.items()) - 1:
					tsData += ",\n"
			tsData += "    \n]\n}\n"
		else:
			tsData += cls.getList(0).toTsClass(True)
			className = cls.getFirstElement().getHighestClass().__name__
			imports.add(f"{className}Model")
			tsData += "\n\n\n\n"
			tsData += f"export const init{cls.__name__} = () => ""{\n    return [    \n"
			for n, val in enumerate(cls.listRepository):
				tsObj, toImport = val.toTs()
				[imports.add(x) for x in toImport]
				tsData += f"        new {className}Base({n}, {tsObj})"
				if n != len(cls.listRepository) - 1:
					tsData += ",\n"
			tsData += "    \n]\n}\n"
		tsData = extractImportsClass(imports) + tsData
		with open(path, "w", encoding = "utf-8") as infile:
			infile.write(tsData)
