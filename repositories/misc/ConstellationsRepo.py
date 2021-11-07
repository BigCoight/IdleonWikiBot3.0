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
		prefix = 'A'
		emptyCount = 0
		perWorldCounter = 1
		for n, constellation in enumerate(data):
			prefIndex = n // 12
			# # Count the empty rows and skip them
			if constellation[0] == '':
				continue
			# 	continue
			#
			# # After 2 empty rows, world 2 constellations start
			# if emptyCount == 2 and prefix != 'B':
			# 	prefix = 'B'
			# 	perWorldCounter = 1
			# # After 3 more empty rows, world 3 constellations will start (future proofing)
			# elif emptyCount == 5 and prefix != 'C':
			# 	prefix = 'C'
			# 	perWorldCounter = 1
			prefix = prefixes[prefIndex]

			mapName = MapNameRepo.get(int(constellation[0])).name
			finalData = [f"{prefix}-{(n % 12) + 1}", mapName, *constellation[1:]]
			cls.add(f"{prefix}-{(n % 12) + 1}", Constellation.fromList(finalData))
			perWorldCounter += 1
