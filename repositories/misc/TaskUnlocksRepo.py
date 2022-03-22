from definitions.misc.TaskUnlocks import TaskUnlocks, TaskUnlock
from helpers.HelperFunctions import getFrom4dArray
from typing import List

from repositories.master.Repository import Repository


class TaskUnlocksRepo(Repository[TaskUnlocks]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TaskUnlocks"]

	@classmethod
	def generateRepo(cls) -> None:
		sections = getFrom4dArray(cls.getSection())
		for n, section in enumerate(sections):
			sectionUnlocks = TaskUnlocks(
				unlocks = []
			)
			for parts in section:
				partUnlocks = []
				for part in parts:
					if part[0] == "EquipmentHats1":
						return
					partUnlocks.append(TaskUnlock(
						item = part[0],
						tabNo = part[1],
						recipNo = part[2]
					))
				sectionUnlocks.unlocks.append(partUnlocks.copy())
			cls.add(f"{n}", sectionUnlocks.copy())
			cls.addList(sectionUnlocks.copy())
