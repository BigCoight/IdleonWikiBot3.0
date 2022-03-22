from definitions.misc.TaskDescription import TaskDescription
from helpers.HelperFunctions import getFromSplitArray
from typing import List

from repositories.master.Repository import Repository


class TaskDescriptionRepo(Repository[TaskDescription]):

	@classmethod
	def getCategory(cls) -> str:
		return "Misc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TaskDescriptions"]

	@classmethod
	def generateRepo(cls) -> None:
		# Don't remove underscores during split, as we have sentences with spaces in between.
		sections = getFromSplitArray(cls.getSection(), False)
		for section in sections:
			# Detect if this is a daily task, if so handle a bit differently
			if (section[2].isnumeric()):
				name = section[0].replace("_", " ")
				toAdd = TaskDescription(
					name = name,
					description = section[1].replace("_", " "),
					extraStr = "",
					number1 = section[2],
					descLine2 = section[3].replace("_", " "),
					numbers = section[4:]
				)
				cls.add(name, toAdd)
				cls.addList(toAdd)
			else:
				name = section[0].replace("_", " ")
				toAdd = TaskDescription(
					name = section[0].replace("_", " "),
					description = section[1].replace("_", " "),
					extraStr = section[2].replace("_", " "),
					number1 = section[3],
					descLine2 = section[4].replace("_", " "),
					numbers = section[5:]
				)
				cls.add(name, toAdd)
				cls.addList(toAdd)
				