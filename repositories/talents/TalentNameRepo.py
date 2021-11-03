import re

from definitions.talents.TalentName import TalentName
from helpers.HelperFunctions import replaceUnderscores
from repositories.master.ListRepository import ListRepository
from typing import List


class TalentNameRepo(ListRepository[TalentName]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TalentNames"]

	@classmethod
	def generateRepo(cls) -> None:
		reEverything = r'"([a-zA-Z0-9_ +{}\',.\-%!$:`?;\n\]\(\)]*)"\.'
		talentNames = re.findall(reEverything, cls.getSection())[0].split(" ")
		for n, talentName in enumerate(talentNames):
			cls.add(TalentName(
				name = replaceUnderscores(talentName).title(),
				id = n
			))
