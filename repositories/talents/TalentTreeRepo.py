import re
import string
from typing import List

from definitions.talents.Build import BuildTalent, BuildTab, Build
from definitions.talents.TalentTree import TalentTree, Talent
from helpers.HelperFunctions import strToArray, replaceUnderscores, camelCaseToTitle, getFromSplit
from helpers.JsonEncoder import CompactJSONEncoder
from repositories.master.Repository import Repository
from repositories.talents.ActiveTalentRepo import ActiveTalentRepo

classTabs = {
	"Beginner": ["Beginner"],
	"Journeyman": ["Beginner", "Journeyman"],
	"Maestro": ["Beginner", "Journeyman", "Maestro"],
	"Virtuoso": [],
	"Infinilyte": [],
	"Warrior": ["Rage Basics", "Warrior"],
	"Barbarian": ["Rage Basics", "Warrior", "Barbarian"],
	"Squire": ["Rage Basics", "Warrior", "Squire"],
	"Blood_Berserker": ["Rage Basics", "Warrior", "Barbarian", "Blood Berserker"],
	"Death_Bringer": [],
	"Divine_Knight": ["Rage Basics", "Warrior", "Squire", "Divine Knight"],
	"Royal_Guardian": [],
	"Archer": ["Calm Basics", "Archer"],
	"Bowman": ["Calm Basics", "Archer", "Bowman"],
	"Hunter": ["Calm Basics", "Archer", "Hunter"],
	"Siege_Breaker": ["Calm Basics", "Archer", "Bowman", "Siege Breaker"],
	"Mayheim": [],
	"Wind_Walker": [],
	"Beast_Master": ["Calm Basics", "Archer", "Hunter", "Beast Master"],
	"Mage": ["Savvy Basics", "Mage"],
	"Shaman": ["Savvy Basics", "Mage", "Shaman"],
	"Wizard": ["Savvy Basics", "Mage", "Wizard"],
	"Elemental_Sorcerer": ["Savvy Basics", "Mage", "Wizard", "Elemental Sorcerer"],
	"Spiritual_Monk": [],
	"Bubonic_Conjuror": ["Savvy Basics", "Mage", "Shaman", "Bubonic Conjuror"],
	"Arcane_Cultist": [],
}


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
		talentNames = getFromSplit(cls.getSection(1))
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

	@classmethod
	def getClassTabs(cls, talentClass: str) -> List[BuildTab]:
		tabs = classTabs[talentClass]
		neededTabs = []
		for tab in tabs:
			currentTab = []
			for name, talent in cls.get(tab).talents.items():
				currentTab.append(BuildTalent(skillIndex = talent.skillIndex, level = 0, name = name, note = ""))
			neededTabs.append(BuildTab(name = tab, talents = currentTab.copy(), note = ""))
		return neededTabs.copy()

	@classmethod
	def exportTalentTemplates(cls) -> None:
		for talentClass in classTabs.keys():
			neededTabs = cls.getClassTabs(talentClass)
			build = Build(
				title = f"{replaceUnderscores(talentClass)} Build Template",
				notes = "",
				version = cls.codeReader.version,
				level = 0,
				tabs = neededTabs.copy(),
				idleonClass = talentClass)
			with open(cls._getPath("builds", "json", f"template_{talentClass}", noCat = True), 'w') as outfile:
				outfile.write(CompactJSONEncoder(indent = 4).encode(build.toDict()))
