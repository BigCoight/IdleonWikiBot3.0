from typing import TypeVar, Generic, List, Optional

from pydantic import BaseModel

from helpers.CodeReader import CodeReader
from helpers.JsonEncoder import CompactJSONEncoder

T = TypeVar("T", bound = BaseModel)


class ListRepository(Generic[T]):
    sections: List[str]
    codeReader: CodeReader
    repository: List[T]

    @ classmethod
    def initialise(cls, codeReader: CodeReader) -> None:
        cls.repository = []
        cls.codeReader = codeReader
        cls.sections = cls.getSections()
        cls.generateRepo()
        cls.export()

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

    @classmethod
    def export(cls) -> None:
        toEncode = [val.dict() for val in cls.repository]
        name = cls.__name__
        with open(fr"./repositories/exported/{name}.json", mode = "w") as outfile:
            outfile.write(CompactJSONEncoder(indent = 4).encode(toEncode))

