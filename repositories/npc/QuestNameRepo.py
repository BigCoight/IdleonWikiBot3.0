import re
from typing import List

from definitions.questdef.QuestName import QuestName
from helpers.Constants import Constants
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository


class QuestNameRepo(Repository[QuestName]):
	@classmethod
	def getCategory(cls) -> str:
		return "Npc"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["QuestNames"]

	@classmethod
	def generateRepo(cls) -> None:
		reNames = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		questNames = re.findall(reNames, cls.getSection())
		for name, npc, diff, index in questNames:
			npc = replaceUnderscores(npc)
			npc = Constants.nameConflicts.get(npc, npc)
			if index == "f":
				continue
			cls.add(f"{npc}{index}", QuestName(
				name = replaceUnderscores(name),
				difficulty = diff[0]
			))
