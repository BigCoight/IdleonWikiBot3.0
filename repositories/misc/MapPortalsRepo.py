import re
from typing import List

from definitions.misc.MapInfo import MapInfo
from helpers.HelperFunctions import getFrom4dArray
from repositories.master.Repository import Repository


class MapPortalsRepo(Repository[MapInfo]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MapPortals"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFrom4dArray(cls.getSection())
		for n, v in enumerate(data[0]):
			# Some maps only have one portal, and for some reason getFrom4dArray handles the array differently.
			# So if we have an array of values, it's a multi portal map
			if len(v) > 1:
				cls.add(f"{n}", MapInfo(id = n, portalRequirements = v[0]))
				cls.addList(MapInfo(id = n, portalRequirements = v[0]))
			# Else it's a map with only one portal, so just get that value directly
			else: 
				cls.add(f"{n}", MapInfo(id = n, portalRequirements = [v[0][0]]))
				cls.addList(MapInfo(id = n, portalRequirements = [v[0][0]]))
