import re
from typing import List

from helpers.HelperFunctions import formatStr
from repositories.ListRepository import ListRepository
from repositories.Repository import Repository


class MapNameRepo(ListRepository[str]):

    @classmethod
    def getSections(cls) -> List[str]:
        return ["MapNames"]

    @ classmethod
    def generateRepo(cls) -> None:
        mapNames = re.findall(r'"([ a-zA-Z0-_\'\n]*)"\.', cls.getSection())[0].split(" ")
        for v in mapNames:
            cls.add(formatStr(v, replaceUnderscores = True))
