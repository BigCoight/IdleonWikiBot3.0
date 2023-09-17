from typing import List

from definitions.misc.weeklybosses.WeeklyBoss import WeeklyBoss
from helpers.HelperFunctions import getFromSplitArray
from repositories.master.Repository import Repository
from repositories.misc.weeklyboss.WeeklyTaskRepo import WeeklyTaskRepo


class WeeklyBossRepo(Repository[WeeklyBoss]):
	@classmethod
	def initDependencies(cls, log = True) -> None:
		WeeklyTaskRepo.initialise(cls.codeReader, log)

	@classmethod
	def getCategory(cls) -> str:
		return "Misc/WeeklyTask"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["WeeklyBoss"]

	@classmethod
	def generateRepo(cls) -> None:
		data = getFromSplitArray(cls.getSection())
		for n, boss in enumerate(data):
			tasks = [int(boss[x]) for x in range(1, 4)]
			possibleTasks = list(map(WeeklyTaskRepo.getList, tasks))
			print(possibleTasks)
			toAdd = WeeklyBoss(
				name = boss[0],
				possibleTasks = possibleTasks,
				health = boss[4],
				healthMult = boss[5],
				x = boss[6],
				y = boss[7],
				xOff = boss[8],
			)
			cls.add(boss[0], toAdd)
			cls.addList(toAdd)
