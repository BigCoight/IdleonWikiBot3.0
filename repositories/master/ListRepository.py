import os
from typing import TypeVar, Generic, List, Optional

from pydantic import BaseModel

from helpers.CodeReader import CodeReader
from helpers.JsonEncoder import CompactJSONEncoder

T = TypeVar("T", bound = BaseModel)


class ListRepository(Generic[T]):
	sections: List[str]
	codeReader: CodeReader
	repository: List[T]

	@classmethod
	def initialise(cls, codeReader: CodeReader) -> None:
		cls.repository = []
		cls.codeReader = codeReader
		cls.sections = cls.getSections()
		if cls.sections and not cls.getSection():
			print(f"Could not find {cls.__name__}'s Section")
			return None
		cls.generateRepo()
		print(f"Generated {cls.__name__}'s repo with {len(cls.repository)} Items")
		cls.export()

	@classmethod
	def getSections(cls) -> List[str]:
		raise NotImplementedError

	@classmethod
	def generateRepo(cls) -> None:
		raise NotImplementedError

	@classmethod
	def getSection(cls, index: int = 0) -> str:
		currentSection = cls.codeReader.getSection(cls.sections[index])
		assert currentSection is not None
		return currentSection

	@classmethod
	def getFileName(cls) -> str:
		return fr"./exported/repo/{cls.__name__}.json"

	@classmethod
	def get(cls, i: int) -> Optional[T]:
		return cls.repository[i]

	@classmethod
	def add(cls, value: T) -> None:
		cls.repository.append(value)

	@classmethod
	def export(cls) -> None:
		with open(cls.getFileName(), mode = "w") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(cls.repository))

	@classmethod
	def items(cls):
		yield from cls.repository

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
		for data in cls.items():
			res += data.writeWiki() + '\n'

		with open(f"{cls.wikitextLocation()}/{cls.__name__}.txt", mode = 'w') as outfile:
			outfile.write(res)
