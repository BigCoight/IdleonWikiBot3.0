from definitions.misc.TaskShopDesc import TaskShopDesc
from helpers.HelperFunctions import getFromSplitArray, replaceUnderscores
from typing import List

from repositories.master.Repository import Repository


class TaskShopDescRepo(Repository[TaskShopDesc]):
	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TaskShopDesc"]

	@classmethod
	def generateRepo(cls) -> None:
		sections = getFromSplitArray(cls.getSection())
		for n, section in enumerate(sections):
			cls.add(f"{n}", TaskShopDesc.fromList(section))
			cls.addList(TaskShopDesc.fromList(section))


