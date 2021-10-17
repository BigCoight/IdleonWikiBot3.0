from definitions.TaskUnlocks import TaskUnlocks, TaskUnlock
from helpers.HelperFunctions import getFrom4dArray
from repositories.master.ListRepository import ListRepository
from typing import List


class TaskUnlocksRepo(ListRepository[TaskUnlocks]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TaskUnlocks"]

	@classmethod
	def generateRepo(cls) -> None:
		sections = getFrom4dArray(cls.getSection())
		for section in sections:
			sectionUnlocks = TaskUnlocks(
				unlocks = []
			)
			for parts in section:
				partUnlocks = []
				for part in parts:
					if part[0] == "EquipmentHats1":
						return
					partUnlocks.append(TaskUnlock(
						item =part[0],
						tabNo =part[1],
						recipNo =part[2]
					))
				sectionUnlocks.unlocks.append(partUnlocks.copy())
			cls.add(sectionUnlocks.copy())



