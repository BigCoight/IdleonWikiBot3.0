import re

from definitions.questdef.QuestName import QuestName
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.Repository import Repository
from typing import List


class QuestNameRepo(Repository[QuestName]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["QuestNames"]

	@classmethod
	def generateRepo(cls) -> None:
		reNames = r'\["([^ ]*)", "([^ ]*)", "([^ ]*)", "([^ ]*)"\],'
		questNames = re.findall(reNames, cls.getSection())
		for name, npc, diff, index in questNames:
			npc = replaceUnderscores(npc)
			if index == "f":
				continue
			cls.add(f"{npc}{index}", QuestName(
				name = replaceUnderscores(name),
				difficulty = diff[0]
			))
