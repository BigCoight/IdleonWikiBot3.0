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
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def initDependencies(cls, log = True):
		MapNameRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["Constellations"]

	@classmethod
	def generateRepo(cls) -> None:
		prefixes = ["A", "B", "C"]
		# StarQuests
		data = getFromSplitArray(cls.getSection())
		fillterCount = 1  # used to handle multiple constellsations with the same name.
		for n, const in enumerate(data):
			if const[0] == '':
				tooAdd = Constellation(
					name = f"Filler",
					area = "",
					x = 0,
					y = 0,
					num1 = 0,
					num2 = 0,
					num3 = 0,
					starChartPoints = 0,
					requirement = "",
					type = 0,
				)
				cls.add(f"Filler{fillterCount}", tooAdd)
				cls.addList(tooAdd)
				fillterCount += 1
				continue

			# If map id < 50, it's world 1
			if int(const[0]) < 50:
				prefix = "A"
				number = 1 + n
			# If map id > 50 but < 100, world 2
			elif int(const[0]) < 100:
				prefix = "B"
				number = 1 + n - 12
			# If map id > 100 but < 150, world 3
			elif int(const[0]) < 150:
				prefix = "C"
				number = 1 + n - 23
			elif int(const[0]) < 150:
				prefix = "C"
				number = 1 + n - 23
			# If map id > 150 but < 200, world 4
			elif int(const[0]) < 200:
				prefix = "D"
				number = 1 + n - 34
			# else world 4
			else:
				prefix = "E"
				number = 1 + n - 44
			mapName = MapNameRepo.getList(int(const[0])).name
			constName = f"{prefix}-{number}"
			finalData = [constName, mapName, *const[1:]]
			cls.add(constName, Constellation.fromList(finalData))
			cls.addList(Constellation.fromList(finalData))
