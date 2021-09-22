
from typing import Dict, Generic, Optional, TypeVar
from helpers.CodeReader import CodeReader

from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


class Repository(Generic[T]):
    section: str
    codeReader: CodeReader
    repository: Dict[str, T] = {}

    @ classmethod
    def initialise(cls, codeReader: CodeReader, section: str) -> None:
        cls.codeReader = codeReader
        cls.section = section
        cls.generateRepo()

    @ classmethod
    def generateRepo(cls) -> None:
        raise NotImplementedError

    @ classmethod
    def getSection(cls) -> str:
        currentSection = cls.codeReader.getSection(cls.section)
        assert currentSection is not None
        return currentSection

    @ classmethod
    def get(cls, key: str) -> Optional[T]:
        return cls.repository.get(key)

    @ classmethod
    def add(cls, key: str, value: T) -> None:
        cls.repository[key] = value
