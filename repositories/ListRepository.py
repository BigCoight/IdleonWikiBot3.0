from typing import TypeVar, Generic, List, Optional

from helpers.CodeReader import CodeReader

T = TypeVar("T")


class ListRepository(Generic[T]):
    sections: List[str]
    codeReader: CodeReader
    repository: List[T] = []

    @ classmethod
    def initialise(cls, codeReader: CodeReader) -> None:
        cls.codeReader = codeReader
        cls.sections = cls.getSections()
        cls.generateRepo()

    @classmethod
    def getSections(cls) -> List[str]:
        raise NotImplementedError

    @ classmethod
    def generateRepo(cls) -> None:
        raise NotImplementedError

    @ classmethod
    def getSection(cls, index: int = 0) -> str:
        currentSection = cls.codeReader.getSection(cls.sections[index])
        assert currentSection is not None
        return currentSection

    @ classmethod
    def get(cls, i: int) -> Optional[T]:
        return cls.repository[i]

    @ classmethod
    def add(cls, value: T) -> None:
        cls.repository.append(value)
