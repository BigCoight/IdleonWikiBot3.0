import re
from typing import List

from definitions.enemy.MapData import MapData
from helpers.Constants import Constants
from repositories.misc.MapNameRepo import MapNameRepo
from repositories.misc.MapPortalsRepo import MapPortalsRepo
from repositories.master.Repository import Repository


class MapDataRepo(Repository[MapData]):
	"""
	Requires: MapNameRepo
	"""

	@classmethod
	def initDependencies(cls) -> None:
		MapNameRepo.initialise(cls.codeReader)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["MapEnemies"]

	@classmethod
	def generateRepo(cls) -> None:
		mapEnemies = re.findall(r'"([ a-zA-Z0-_\'\n]*)"\.', cls.getSection())[0].split(" ")
		for n, v in enumerate(mapEnemies):
			worldIndex = n // 50
			if worldIndex > 3:
				continue
			if cls.contains(v):
				continue
			cls.add(v, MapData(
				area = MapNameRepo.get(n).name,
				world = Constants.worlds[worldIndex],
				id = MapNameRepo.get(n).id,
				portalRequirements = MapPortalsRepo.get(n).portalRequirements
			))
