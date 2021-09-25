import re
from typing import List

from definitions.MapName import MapName
from helpers.HelperFunctions import formatStr
from repositories.ListRepository import ListRepository


class MapNameRepo(ListRepository[MapName]):

    @classmethod
    def getSections(cls) -> List[str]:
        return ["MapNames"]

    @ classmethod
    def generateRepo(cls) -> None:
        mapNames = re.findall(r'"([ a-zA-Z0-_\'\n]*)"\.', cls.getSection())[0].split(" ")
        for n, v in enumerate(mapNames):
            cls.add(MapName(name = v, id = n))
