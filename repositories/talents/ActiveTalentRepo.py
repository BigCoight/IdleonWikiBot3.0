import re

from definitions.talents.ActiveTalent import ActiveTalent
from definitions.talents.TalentName import TalentName
from helpers.HelperFunctions import replaceUnderscores, formatStr
from repositories.master.ListRepository import ListRepository
from typing import List

from repositories.master.Repository import Repository


class ActiveTalentRepo(Repository[ActiveTalent]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["ActiveSkill"]

	@classmethod
	def generateRepo(cls) -> None:
		# Active skill information
		activeData = cls.getSection()
		activeDataSplit = re.split(
			r'..\.addAtkMoveDef\("([a-zA-Z0-9_ +{}\',.\-%!$:`?;\n\]\(\)]*)"', activeData)[1:]
		reData = r'([\w]*): ([\w."\-]*)'
		for i in range(0, len(activeDataSplit) - 1, 2):
			activeDict = {}
			activeDetails = re.findall(reData, activeDataSplit[i + 1])
			for atr, val in activeDetails:
				activeDict[atr] = formatStr(val, ['"'])
			cls.add(replaceUnderscores(activeDataSplit[i]).title(), ActiveTalent.parse_obj(activeDict))
