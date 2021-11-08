from typing import List

from definitions.misc.Constellation import Constellation
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository
from repositories.misc.MapNameRepo import MapNameRepo


class ConstellationsRepo(Repository[Constellation]):
	"""
	Dependent on: MapNameRepo
	"""

	@classmethod
	def initDependencies(cls):
		MapNameRepo.initialise(cls.codeReader)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Constellations"]

	@classmethod
	def generateRepo(cls) -> None:
		prefixes = ["A", "B", "C"]
		# StarQuests
		data = getFromSplitArray(cls.getSection())
		for n, const in enumerate(data):
			if const[0] == '':
				continue
			prefix = prefixes[n // 12]
			mapName = MapNameRepo.get(int(const[0])).name
			constName = f"{prefix}-{(n % 12) + 1}"
			finalData = [constName, mapName, *const[1:]]
			cls.add(constName, Constellation.fromList(finalData))
