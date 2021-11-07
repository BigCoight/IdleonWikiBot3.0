from typing import List
from definitions.misc.Constellation import Constellation
from definitions.misc.MapName import MapName
from repositories.misc.MapNameRepo import MapNameRepo
from helpers.HelperFunctions import getFromArrayArray, getFromSplit, getFromSplitArray
from repositories.master.Repository import Repository


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
		# StarQuests
		data = getFromSplitArray(cls.getSection())
		prefix = 'A'
		emptyCount = 0
		perWorldCounter = 1
		for constellation in data:
			# Count the empty rows and skip them
			if constellation[0] == '':
				emptyCount += 1
				continue

			# After 2 empty rows, world 2 constellations start
			if emptyCount == 2 and prefix != 'B':
				prefix = 'B'
				perWorldCounter = 1
			# After 3 more empty rows, world 3 constellations will start (future proofing)
			elif emptyCount == 5 and prefix != 'C':
				prefix = 'C'
				perWorldCounter = 1

			mapName = MapNameRepo.get(int(constellation[0])).name
			finalData = [ f"{prefix}-{perWorldCounter}", mapName, *constellation[1:] ]
			cls.add(f"{prefix}-{perWorldCounter}", Constellation.fromList(finalData))
			perWorldCounter += 1		
