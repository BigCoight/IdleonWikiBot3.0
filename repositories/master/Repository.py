import os.path
from abc import ABC
from copy import deepcopy
from typing import Dict, Generic, Optional, TypeVar, List

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
		cls.generateRepo()
		cls.export()

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
	def getFileName(cls) -> str:
		return fr"./exported/repo/{cls.__name__}.json"

	@classmethod
	def export(cls) -> None:
		with open(cls.getFileName(), mode = "w") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(cls.repository))

	@classmethod
	def excludeDefaults(cls) -> bool:
		return True

	@classmethod
	def compareVersions(cls, v1: str, v2: str):
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
			modelChanges = repo1[sameItem].compare(repo2[sameItem])
			if modelChanges:
				changes[sameItem] = modelChanges

		for newItem in newItems:
			new[newItem] = repo2[newItem].dict()

		out = {
			"new": new,
			"changes": changes

		}

		changeName = fr"./exported/changes/{cls.__name__}.json"

		with open(changeName, mode = "w") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(out))

	@classmethod
	def wikitextLocation(cls):
		return fr"./exported/wikitext/{cls.__name__}"

	@classmethod
	def createDirectory(cls):
		if not os.path.exists(cls.wikitextLocation()):
			os.mkdir(cls.wikitextLocation())

	@classmethod
	def exportWikiSingle(cls):
		cls.createDirectory()
		res = ""
		for _, data in cls.items():
			res += data.writeWiki() + '\n'

		with open(f"{cls.wikitextLocation()}/{cls.__name__}.txt", mode = 'w') as outfile:
			outfile.write(res)

	@classmethod
	def exportWikiMult(cls):
		cls.createDirectory()
		for name, data in cls.items():
			with open(f"{cls.wikitextLocation()}/{cls.getWikiName(name, data)}.txt", mode = 'w') as outfile:
				outfile.write(data.writeWiki())

	@classmethod
	def getWikiName(cls, name: str, data: T) -> str:
		return name
