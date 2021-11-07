import json
import os.path
from typing import TypeVar, Dict

from pydantic import BaseModel

from helpers.CodeReader import CodeReader
from helpers.JsonEncoder import CompactJSONEncoder
from repositories.master.Repository import Repository

T = TypeVar("T", bound = BaseModel)


class FileRepository(Repository[T]):
	override: bool

	@classmethod
	def initialise(cls, codeReader: CodeReader) -> None:
		cls.override = True
		cls.repository = {}
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
		with open(cls._getFileName(), mode = "w") as outfile:
			outfile.write(CompactJSONEncoder(indent = 4).encode(toEncode))

	@classmethod
	def shouldGetFromFile(cls) -> bool:
		if cls.override:
			return True
		if not os.path.isfile(cls._getFileName()):
			return False
		with open(cls._getFileName(), mode = "r") as infile:
			data = json.load(infile)
		if version := data.get("version"):
			if version == cls.codeReader.version:
				return True
		return False

	@classmethod
	def getFromFile(cls) -> None:
		with open(cls._getFileName(), mode = "r") as infile:
			data = json.load(infile)
		for key, value in data.items():
			if key == "version":
				continue
			cls.add(key, cls.parse(value))

	@classmethod
	def parse(cls, value: Dict[str, any]) -> T:
		raise NotImplementedError
