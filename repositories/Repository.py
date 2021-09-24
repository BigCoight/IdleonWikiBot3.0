
from typing import Dict, Generic, Optional, TypeVar, List
from helpers.CodeReader import CodeReader
from abc import ABC

from pydantic import BaseModel

from helpers.JsonEncoder import CompactJSONEncoder

T = TypeVar("T", bound=BaseModel)


class Repository(Generic[T], ABC):
    sections: List[str]
    codeReader: CodeReader
    repository: Dict[str, T]

    @ classmethod
    def initialise(cls, codeReader: CodeReader) -> None:
        cls.repository = {}
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
    def get(cls, key: str) -> Optional[T]:
        return cls.repository.get(key)

    @ classmethod
    def add(cls, key: str, value: T) -> None:
        cls.repository[key] = value

    @classmethod
    def contains(cls, key: str) -> bool:
        return key in cls.repository

    @classmethod
    def export(cls) -> None:
        toEncode = {key: val.dict() for key, val in cls.repository.items()}
        name = cls.__name__
        print(name)
        with open(fr"./repositories/exported/{name}.json", mode = "w") as outfile:
            outfile.write(CompactJSONEncoder(indent = 4).encode(toEncode))
