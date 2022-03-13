import re
from typing import List

from definitions.misc.MapName import MapName
from repositories.master.ListRepository import ListRepository


class MapNameRepo(ListRepository[MapName]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MapNames"]

	@classmethod
	def generateRepo(cls) -> None:
		mapNames = re.findall(r'"(.*?)"\.', cls.getSection())[0].split(" ")
		for n, v in enumerate(mapNames):
			cls.add(MapName(name = v, id = n))
