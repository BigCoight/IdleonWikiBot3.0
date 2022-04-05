import re
import string
from typing import List

from definitions.talents.TalentTree import TalentTree, Talent
from helpers.HelperFunctions import strToArray, formatStr, replaceUnderscores, camelCaseToTitle
from repositories.master.Repository import Repository
from repositories.talents.ActiveTalentRepo import ActiveTalentRepo


class TalentTreeRepo(Repository[TalentTree]):
	@classmethod
	def getCategory(cls) -> str:
		return "Talents"

	@classmethod
	def initDependencies(cls, log = True) -> None:
		ActiveTalentRepo.initialise(cls.codeReader, log)

	@classmethod
	def getSections(cls) -> List[str]:
		return ["TalentOrder", "TalentNames", "TalentData", "ClassNames"]

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
					fTalentName = string.capwords(replaceUnderscores(talentName))
					talents.talents[fTalentName] = (Talent(
						name = fTalentName,
						description = replaceUnderscores(talentDesc[0]),
						x1 = talentDesc[1],
						x2 = talentDesc[2],
						funcX = talentDesc[3],
						y1 = talentDesc[4],
						y2 = talentDesc[5],
						funcY = talentDesc[6],
						lvlUpText = replaceUnderscores(talentDesc[7]).title(),
						skillIndex = skillI,
						activeData = ActiveTalentRepo.get(fTalentName)
					))
				cls.add(string.capwords(replaceUnderscores(name)), talents)

		doTalents(classNames[:41], 0, 15)
		doTalents(specialTalents, 615, 13)

	@classmethod
	def _writeChangelogChange(cls, item, change) -> str:
		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + v + "}}\n"

		def patchnote(v: str, o, n) -> str:
			return "{{patchnote|" + f"{v}|{str(o)}|{str(n)}" + "}}\n"

		def italic(v: str) -> str:
			return "{{patchnote/italic|" + v + "}}\n"

		res = head(cls.getWikiName(item))
		for v, d in change.items():
			if isinstance(d, tuple):
				o, n = d
				res += patchnote(v, o, n)
			elif isinstance(d, list):
				res += bold(camelCaseToTitle(v))
				for i, subC in enumerate(d):
					o, n = subC
					res += patchnote(str(i), o, n)
			elif isinstance(d, dict):
				for quest, subC in d.items():
					res += bold(camelCaseToTitle(quest))
					for atr, val in subC.items():
						if isinstance(val, dict):
							res += italic(atr)
							for innerAtr, innerVal in val.items():
								o, n = innerVal
								res += patchnote(innerAtr, o, n)
							continue
						o, n = val
						res += patchnote(atr, o, n)

		res += '|}\n'
		return res

	@classmethod
	def _writeChangelogNew(cls, item, change) -> str:
		def head(v: str) -> str:
			return "{{patchnote/head|changed=" + v + "}}\n"

		def bold(v: str) -> str:
			return "{{patchnote/bold|" + v + "}}\n"

		def italic(v: str) -> str:
			return "{{patchnote/italic|" + v + "}}\n"

		def patchnote(v: str, o, n) -> str:
			return "{{patchnote|" + f"{v}|{str(o)}|{str(n)}" + "}}\n"

		res = head(cls.getWikiName(item))
		for v, d in change.items():
			if isinstance(d, list):
				res += bold(camelCaseToTitle(v))
				for i, subC in enumerate(d):
					res += patchnote(str(i), " ", subC)
			elif isinstance(d, dict):
				for quest, subC in d.items():
					res += bold(camelCaseToTitle(quest))
					for atr, val in subC.items():
						if isinstance(val, list):
							res += italic(camelCaseToTitle(atr))
							for n, subV in enumerate(val):
								res += patchnote(str(n), " ", subV)
							continue
						res += patchnote(atr, " ", val)
			else:
				if not d:
					continue
				res += patchnote(v, " ", d)
		res += '|}\n'
		return res
