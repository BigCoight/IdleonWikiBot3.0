from typing import Protocol


class Definition(Protocol):

    def convertSection(self, section):
        raise NotImplementedError
