import re
import string

from definitions.talents.TalentName import TalentName
from helpers.HelperFunctions import replaceUnderscores
from typing import List

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
		reEverything = r'"([a-zA-Z0-9_ +{}\',.\-%!$:`?;\n\]\(\)]*)"\.'
		talentNames = re.findall(reEverything, cls.getSection())[0].split(" ")
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
