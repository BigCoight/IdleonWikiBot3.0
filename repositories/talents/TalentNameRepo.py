import string
from typing import List

from definitions.talents.TalentName import TalentName
from helpers.HelperFunctions import replaceUnderscores, getFromSplit
from repositories.master.Repository import Repository


class TalentNameRepo(Repository[TalentName]):
	@classmethod
	def getCategory(cls) -> str:
		return "Talents"

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TalentNames"]

	@classmethod
	def generateRepo(cls) -> None:
		talentNames = getFromSplit(cls.getSection())
		for n, talentName in enumerate(talentNames):
			name = string.capwords(replaceUnderscores(talentName))
			cls.add(f"{n}", TalentName(
				name = name,
				id = n
			))
			cls.addList(TalentName(
				name = name,
				id = n
			))
