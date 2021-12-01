import re
from typing import List

from definitions.misc.MapInfo import MapInfo
from repositories.master.ListRepository import ListRepository
from helpers.HelperFunctions import getFrom4dArray

class MapPortalsRepo(ListRepository[MapInfo]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MapPortals"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFrom4dArray(cls.getSection())
		for n, v in enumerate(data[0]):
			# Some maps only have one portal, and for some reason getFrom4dArray handles the array differently.
			# So if we have an array of values, it's a multi portal map
			print(v)
			if len(v) > 1:
				cls.add(MapInfo(id = n, portalRequirements = v[0]))
			# Else it's a map with only one portal, so just get that value directly
			else: 
				cls.add(MapInfo(id = n, portalRequirements = [v[0][0]]))
