from typing import List

from definitions.misc.MapName import MapName
from helpers.HelperFunctions import getFromSplit
from repositories.master.Repository import Repository


class MapNameRepo(Repository[MapName]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MapNames", "MapInternal"]

	@classmethod
	def generateRepo(cls) -> None:
		mapNames = getFromSplit(cls.getSection())
		mapIntName = getFromSplit(cls.getSection(1))
		for n, v in enumerate(mapNames):
			cls.add(mapIntName[n], MapName(intName = mapIntName[n], name = v, id = n))
			cls.addList(MapName(intName = mapIntName[n], name = v, id = n))
