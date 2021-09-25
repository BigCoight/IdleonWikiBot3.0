import re

from definitions.TalentTree import TalentTree, Talent
from helpers.HelperFunctions import strToArray, formatStr, replaceUnderscores
from repositories.Repository import Repository
from typing import List


class TalentTreeRepo(Repository[TalentTree]):

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TalentOrder", "TalentNames", "TalentData", "ClassNames", "ActiveSkill"]

	@classmethod
	def generateRepo(cls) -> None:
		reEverything = r'"([a-zA-Z0-9_ +{}\',.\-%!$:`?;\n\]\(\)]*)"\.'
		talentOrder = [int(x) for x in strToArray(cls.getSection(0)) if x]
		talentNames = re.findall(reEverything, cls.getSection(1))[0].split(" ")
		reTalentDesc = r'\[\["(.*)"\], "(.*)"\.split\(" "\), \["(.*)"\], \["(.*)"\]\]'
		talentDescriptions = [" ".join(x).split(" ") for x in re.findall(reTalentDesc, cls.getSection(2))]
		classNames = re.findall(reEverything, cls.getSection(3))[0].split(" ")[1:]
		specialTalents = []
		for n, i in enumerate([41, 42, 43, 44, 45], 1):
			specialTalents.append(f"Special Talent {n}")

		# Active skill information
		activeDict = {}
		activeData = cls.getSection(4)
		activeDataSplit = re.split(
			r'..\.addAtkMoveDef\("([a-zA-Z0-9_ +{}\',.\-%!$:`?;\n\]\(\)]*)"', activeData)[1:]
		reData = r'([\w]*): ([\w."\-]*)'
		for i in range(0, len(activeDataSplit) - 1, 2):
			activeDict[activeDataSplit[i]] = {}
			activeDetails = re.findall(reData, activeDataSplit[i + 1])
			for atr, val in activeDetails:
				activeDict[activeDataSplit[i]][atr] = formatStr(val, ['"'])

		def doTalents(arr, off, mod):
			for n, name in enumerate(arr):
				if name == "_":
					continue
				talents = TalentTree(talents = [])
				for i in range(mod):
					skillI = int(talentOrder[off + n * mod + i])
					talentName, talentDesc = talentNames[skillI], talentDescriptions[skillI]
					if talentName == "_" or talentDesc[0] == "_":
						continue
					print(talentDesc)
					talents.talents.append(Talent(
						name = replaceUnderscores(talentName).title(),
						description = replaceUnderscores(talentDesc[0]),
						x1 = talentDesc[1],
						x2 = talentDesc[2],
						funcX = talentDesc[3],
						y1 = talentDesc[4],
						y2 = talentDesc[5],
						funcY = talentDesc[6],
						lvlUpText = replaceUnderscores(talentDesc[7]).title()
					))
				cls.add(replaceUnderscores(name).title(), talents)

		doTalents(classNames[:41], 0, 15)
		doTalents(specialTalents, 615, 13)
